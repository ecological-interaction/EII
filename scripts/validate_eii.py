"""Read-only preservation checks for the EII JSON authority and curated views.

No generation/synchronisation of scientific tables. The embedded transcription is
immutable migration evidence, not a second editable authority. Python 3 stdlib;
installed jsonschema/cffconvert may additionally validate their standard schemas.
"""
from pathlib import Path
import collections
import hashlib
import html
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
FENCES = re.compile(r'^```json\n(.*?)^```[ \t]*$', re.M | re.S)


def digest(value):
    return hashlib.sha256(value).hexdigest()


def text_without_fences(text):
    return re.sub(r'^```[^\n]*\n.*?^```[ \t]*$', '', text, flags=re.M | re.S)


def slug(text):
    text = html.unescape(re.sub(r'<[^>]+>', '', text)).replace('`', '')
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[-\s]+', '-', re.sub(r'[^\w\s-]', '', text)).strip('-')


def anchors(text):
    text = text_without_fences(text)
    result = set(re.findall(r'<a id="([^"]+)"', text))
    headings = set()
    for title in re.findall(r'^#{1,6} (.+)$', text, re.M):
        base = slug(title); value = base; i = 0
        while value in headings:
            i += 1; value = base + '_' + str(i)
        headings.add(value)
    return result | headings


def section(text, start, end=None):
    return text[text.index(start):text.index(end) if end else len(text)]


def indicator_rows(text):
    return re.findall(r'^\| ([A-Z]{2,3}-\d{3}) \|.*$', text, re.M)


def row_lines(text):
    return [line for line in text.splitlines() if re.match(r'^\| [A-Z]{2,3}-\d{3} \|', line)]


def validate():
    data = json.loads((ROOT / 'EII_Machine_Reference.json').read_text())
    cross = json.loads((ROOT / 'EII_Preservation_Crosswalk.json').read_text())
    snapshot = data['source_transcription']['markdown']
    assert digest(snapshot.encode()) == data['source_transcription']['sha256'] == cross['baseline_files']['EII_Machine_Reference.md']
    old = [json.loads(m[1]) for m in FENCES.finditer(snapshot)]
    assert len(old) == 237
    original = [obj for obj in old if 'id' in obj]
    records = data['indicators']
    assert records == original, 'An original indicator field, value, type or order changed'
    assert data['metadata']['previous_machine_manifest'] == old[0]
    assert data['classification_migration'] == old[0]['classification_migration']
    assert data['source_context'] == old[-1]['source_context']
    assert data['domains'] == old[0]['domains']
    ids = [obj['id'] for obj in records]
    assert len(ids) == len(set(ids)) == 235
    assert set(data['classification_migration']['crosswalk'][i]['eii_id'] for i in range(235)) == set(ids)
    for obj in records:
        fingerprint = digest(json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode())
        assert fingerprint == cross['record_objects_sha256'][obj['id']]
    assert [d['id'] for d in data['domains']] == [f'D{i:02}' for i in range(1, 16)]
    counts = collections.Counter(obj['domain'] for obj in records)
    assert counts == {d['id']: d['record_count'] for d in data['domains']}
    support = [(obj['id'], target) for obj in records for target in obj['support']]
    assert len(support) == 724 and all(target in ids for _, target in support)
    assert sum(len(obj['related_domains']) for obj in records) == 72
    # All extracted historical registries/templates retain original values and source editions.
    extracted = []
    for key, value in data['source_context'].items():
        if isinstance(value, str):
            for i, m in enumerate(FENCES.finditer(value)):
                extracted.append((key, i, json.loads(m[1])))
    assert [(x['source_context_key'], x['json_block'], x['value']) for x in data['extracted_historical_structures']] == extracted
    assert data['source_routes'][0]['registry'] == extracted[0][2]['source_routes']
    assert data['source_routes'][1]['registry'] == extracted[-1][2]['source_routes']
    assert data['scientific_references']['records'] == extracted[-1][2]['scientific_references']
    assert [(x['source_context_key'], x['json_block'], x['value']) for x in data['observation_schema']] == [x for x in extracted if 'observation_id' in x[2]]
    # Exact five-column rows remain in source order in both reading views.
    readme = (ROOT / 'README.md').read_text()
    scientific = (ROOT / 'EII_Scientific_Reference_Register.md').read_text()
    assert row_lines(readme) == row_lines(scientific) and len(row_lines(readme)) == 235
    assert {'EII:' + value for value in indicator_rows(readme)} == set(ids)
    # Baseline table fingerprints ensure README/Scientific Register cannot drift together unnoticed.
    for name, fingerprint in cross['presentation_fingerprints'].items():
        assert digest(section(readme, *fingerprint['readme_section']).encode()) == fingerprint['sha256'], name
    assert digest('\n'.join(row_lines(readme)).encode()) == cross['indicator_rows_sha256']
    current_domain = None; assignments = {}
    for line in scientific.splitlines():
        if re.match(r'^### D\d\d —', line): current_domain = line.split()[1]
        match = re.match(r'^\| ([A-Z]{2,3}-\d{3}) \|', line)
        if match and len(assignments) < 235: assignments['EII:' + match[1]] = current_domain
    assert assignments == {x['id']: x['domain'] for x in records}
    scientific_anchors = anchors(scientific)
    assert all(x['id'].split(':')[1].lower() in scientific_anchors for x in records)
    # Canonical and display text must both appear independently; no replacement by concise tables.
    for obj in records:
        for key in ['definition', 'direct', 'inference', 'display_label', 'display_measurement', 'display_inference']:
            assert obj[key] in scientific, (obj['id'], key)
    remote = (ROOT / 'EII - Remote Sensing.md').read_text()
    remote_ids = re.findall(r'<a id="([a-z]{2,3}-\d{3})"', remote)
    assert len(remote_ids) == len(set(remote_ids)) == 91
    assert set('EII:' + value.upper() for value in remote_ids) <= set(ids)
    restored_remote = remote.replace('**Document version:** 0.1.1 · 26 October 2026<br/>', '**Document version:** 0.1.0 · 21 October 2026  ').replace('](EII_Scientific_Reference_Register.md#', '](EII_Machine_Reference.md#').replace('](https://github.com/ecological-interaction/GISDS/blob/main/GISDS.md)', '](../GISDS/GISDS.md)')
    assert digest(restored_remote.encode()) == cross['baseline_files']['EII - Remote Sensing.md']
    current_domain = None
    for line in remote.splitlines():
        match = re.match(r'^## (D\d\d) —', line)
        if match: current_domain = match[1]
        match = re.search(r'<a id="([a-z]{2,3}-\d{3})"', line)
        if match: assert assignments['EII:' + match[1].upper()] == current_domain
    pointer = (ROOT / 'EII_Machine_Reference.md').read_text()
    assert not FENCES.search(pointer)
    assert set(re.findall(r'<a id="([^"]+)"', snapshot)) <= anchors(pointer)
    # Resolve working Markdown links, excluding fenced historical code/data.
    checked = 0
    anchor_cache = {}
    for document in ROOT.glob('*.md'):
        for target in re.findall(r'\]\(([^\s)]+)\)', text_without_fences(document.read_text())):
            url = urlsplit(target)
            if url.scheme or url.netloc: continue
            dest = (document.parent / unquote(url.path)).resolve() if url.path else document
            assert dest.is_file(), (document.name, target, 'missing file')
            if url.fragment and dest.suffix == '.md':
                if dest not in anchor_cache:
                    anchor_cache[dest] = anchors(dest.read_text())
                assert unquote(url.fragment) in anchor_cache[dest], (document.name, target, 'missing anchor')
            checked += 1
    # All fifteen scientific names remain; domain codes and counts are absent from rendered labels.
    source = (ROOT / 'assets/diagrams/eii_overview.mmd').read_text()
    labels = dict(re.findall(r'^\s*(?:subgraph\s+)?(\w+)\["([^"\n]+)"\]', source, re.M))
    for domain in data['domains']:
        assert labels[domain['id']].replace('<br/>', ' ') == domain['label']
    with tempfile.TemporaryDirectory(prefix='eii-diagram-check-') as directory:
        directory = Path(directory)
        for name in ['render_eii_overview.py', 'eii_overview.mmd']:
            shutil.copyfile(ROOT / 'assets/diagrams' / name, directory / name)
        subprocess.run([sys.executable, '-B', str(directory / 'render_eii_overview.py')], check=True)
        svg = (directory / 'eii_overview.svg').read_bytes()
        subprocess.run([sys.executable, '-B', str(directory / 'render_eii_overview.py')], check=True)
        assert svg == (directory / 'eii_overview.svg').read_bytes() == (ROOT / 'assets/diagrams/eii_overview.svg').read_bytes()
    import xml.etree.ElementTree as ET
    svg_root = ET.fromstring(svg)
    assert svg_root.attrib['viewBox'].startswith('0 0 1200 ')
    assert svg_root.attrib['role'] == 'img' and svg_root.attrib['aria-labelledby'] == 'title description'
    assert digest((ROOT / 'assets/diagrams/eii_overview.mmd').read_bytes()).encode() in svg
    assert svg_root.find('{http://www.w3.org/2000/svg}title').text
    assert svg_root.find('{http://www.w3.org/2000/svg}desc').text
    assert 'View full-size diagram' in readme and '![EII' in readme
    # Attribution and absence of invented release fields.
    cff = (ROOT / 'CITATION.cff').read_text()
    for item in ['cff-version: 1.2.0', 'family-names: Minchin', 'given-names: Jonathan', 'affiliation: Ecological Interaction', 'https://orcid.org/0000-0001-8152-1796', 'https://github.com/ecological-interaction/EII']:
        assert item in cff, item
    assert not re.search(r'^(version|date-released|doi|license):', cff, re.M)
    optional = {}
    if importlib.util.find_spec('jsonschema'):
        import jsonschema
        schema = json.loads((ROOT / 'EII_Machine_Reference.schema.json').read_text())
        jsonschema.Draft202012Validator.check_schema(schema)
        jsonschema.Draft202012Validator(schema).validate(data)
        optional['json_schema'] = 'PASS'
    else: optional['json_schema'] = 'not installed; stdlib preservation checks passed'
    if importlib.util.find_spec('cffconvert'):
        from cffconvert import Citation
        Citation(cff).validate()
        optional['cff_schema'] = 'PASS'
    else: optional['cff_schema'] = 'not installed; attribution/field checks passed'
    return {'status':'PASS', 'indicators':len(ids), 'domains':len(counts), 'secondary_domains':72, 'supporting_relationships':len(support), 'remote_sensing_records':91, 'original_json_blocks':len(old), 'historical_structures':len(extracted), 'local_links_and_anchors':checked, 'diagram':'reproduced twice byte-for-byte; accessible SVG metadata present', **optional}


if __name__ == '__main__':
    print(json.dumps(validate(), indent=2))
