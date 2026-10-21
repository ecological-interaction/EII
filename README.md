# EII — Ecological Indicator Inventory

**Work in Progress — Academic Research Resource**

Jonathan Minchin · Ecological Interaction · [ORCID 0000-0001-8152-1796](https://orcid.org/0000-0001-8152-1796).

EII is a higher-level reference for scientific and technological ecological indicators. Contributing catalogues describe observations, datasets, technologies or methods; EII describes measurements, qualified inferences and interpretive relationships. It is an exploratory research resource, not a validated monitoring standard.

## Start here

- [Scientific Reference Register](EII_Scientific_Reference_Register.md): concise human-readable five-column catalogue, 235 indicators in the 15 scientific domains.
- [Machine Reference](EII_Machine_Reference.md): authoritative full-length structured records, source registries, scientific references, classifications, observation schemas, historical context and the domain-migration crosswalk.
- [Remote-sensing subset](EII%20-%20Remote%20Sensing.md): independently curated satellite/drone reading view with 91 indicators; aligned to the same domain taxonomy.
- [CITATION.cff](CITATION.cff): academic attribution.
- [CHANGELOG.md](CHANGELOG.md): development and publication preparation.

## Maintaining the files

Maintain EII_Machine_Reference.md as the complete scientific record and EII_Scientific_Reference_Register.md as its concise five-column scientific presentation. Preserve the scientific table wording and identifiers during classification-only edits; do not replace the original scientific descriptions with display text. Full canonical/display descriptions remain in the machine records; the presentation is not an independent indicator inventory. The remote-sensing subset is a separately curated view and must be reviewed explicitly when its underlying records change. There is no automatic synchronization or database service.

Register records use fenced JSON inside Markdown. Existing fields and full descriptions are retained, with additive historical preservation fields. Do not recycle IDs, flatten family variants or treat supporting indicators as calculation inputs. Validate unique IDs, domain counts, source/reference keys, supporting relationships and presentation parity after edits. Historical source hashes describe reviewed editions, not current file contents.

The publication-facing methodology name is Database Reference Methodology (DRM), following the Ecological Information umbrella. The protected registers retain their historical methodology name and v1.0.0 reference. The umbrella currently supplies an introduction under development, not an approved detailed specification; conformance remains unverified. No new SQL database or invented external identifiers are introduced. GISDS routes remain candidate sources, AMRKB links remain technical context, and future IoT/bioinformatics bindings remain unassigned. Trails4Soil practice crosswalks are outside the active indicator scope but remain in the historical scientific register pending review. PBCKA/EIRKB interoperability remains outside the current scope.

The proposed website reading entry point is `EII_Scientific_Reference_Register.md`, with `EII_Machine_Reference.md` as its detailed structured reference. The previous EII.md / EII_Reference_Register.md names are historical file roles. Website integration, licensing and publication require separate review.

## Domain taxonomy and document versions

All three reference documents use **EII Domain Taxonomy v1.0.0** (D01–D15). Domain codes are stable and independent of sorting or ID prefixes. Each indicator has one primary domain; existing secondary domains remain in machine-record `related_domains`. The machine manifest preserves the 235-ID crosswalk from the scientific register's former A–P presentation groups. Historical source editions and file-role descriptions are retained as history, not current instructions.

| Document | Independent document version | Records |
|---|---|---:|
| Scientific Reference Register | 0.5.0 — 21 October 2026 | 235 |
| Machine Reference | 0.3.1 — 21 October 2026 | 235 |
| Remote Sensing | 0.1.0 — 21 October 2026 | 91 |

Document versions, EII Domain Taxonomy v1.0.0, the existing record schema and DRM v1.0.0 are independent references. No resource-release version is assigned by this migration. Database Reference Methodology compatibility is not certified: the available umbrella introduction is not a detailed specification.

## Repository and publication status

The source repository is [ecological-interaction/EII](https://github.com/ecological-interaction/EII).
Anonymous Git access was verified on 21 October 2026. The current local and
remote `main` commit is `fb3705660178d2efd948863d362b236cd8d1d540`.
This records the audited baseline, not a new release or publication date.
The website routes discussed below are proposals; EII is not integrated into
the central website by this preparation.

No licence has been selected for this repository or its research documentation.
Public accessibility does not itself grant permission to reuse, redistribute
or adapt the material. Citation metadata provides attribution information,
not a licence. Referenced third-party works and datasets retain their own
licences, access conditions and attribution requirements.

## Register comparison and publication review

The Scientific Reference Register and Machine Reference each contain 235 unique
indicator IDs with matching canonical names, acquisition-method fields and
primary assignments across D01–D15. The 91-indicator remote-sensing subset uses
matching primary assignments. The documents serve different purposes and
must not be treated as identical representations: the scientific catalogue
retains 120 earlier interpretation statements and 115 later display
inferences, while machine records preserve fuller canonical definitions,
measurements, inferences, classifications and relationships.

The Scientific Reference Register still contains internal discussion-derived
source labels and a historical Trails4Soil practice crosswalk explicitly
excluded from the active indicator inventory. Its historical proposals for
EIRKB mapping are also outside current interoperability scope. The Machine
Reference retains historical source paths, previous file roles, schemas and
provenance text. Those are archival evidence, not current paths or implemented
capabilities. Both registers are preserved unchanged; neutralising or separating
historical source material requires a specific research/publication decision.
The existing reference ranges, scientific wording and classifications are not
silently reconciled by this review.

### Database Reference Methodology alignment

This README uses **Database Reference Methodology (DRM)**, matching the
Information umbrella's `DRM/README.md`, which was read directly for this review.
This is terminology alignment only. The registers retain their historical
methodology wording and v1.0.0 reference, without any change to research methods,
classifications or version claims.

EII currently defines its own D01–D15 taxonomy, stable indicator IDs, record and
observation schemas, family variants, directed supporting-indicator relations,
source-route adapters and migration provenance. The umbrella introduction
sets out broader aims for portable classifications, shared identifiers and
explicit mappings, conceptual relationships and cross-database analytical
frameworks while preserving each database's own authority. It does not define
or validate EII's specific fields, relation vocabulary, mappings or schemas.

A federation-wide review must establish how EII's identifiers and classification
mappings relate to shared conventions, how candidate sources become evidenced
dataset bindings, and how analytical relations preserve evidence status and
project-specific exclusions. The historical v1.0.0 reference must also be
reconciled with the umbrella's unversioned introduction. No conflict is silently
resolved, and no methodological conformance is certified by this edit.

### Historical scope review: Trails4Soil

The historical material remains in the current Scientific Reference Register
pending a future scope revision. Its introduction (line 22), Section 4
(lines 416–443, 21 provisional practice rows), Section 7 source entry
`FRAME-T4S` (line 498), and v0.1.0 history (line 513) require review together.
These are historical management-practice mappings, not 21 additional measured
indicators. Their retention does not complete a scope revision or establish
programme verification. No indicator has been removed, reclassified, merged or
relocated.

The 21 rows reference the existing indicator families below; ranges expand
only for audit identification and do not introduce or renumber records:

- BIO-001, BIO-004, BIO-005, BIO-007, BIO-008, BIO-009.
- DIS-010.
- FUN-003, FUN-004, FUN-005, FUN-006, FUN-007, FUN-008, FUN-013.
- HYD-001.
- MIC-001, MIC-002, MIC-003, MIC-004, MIC-005, MIC-006, MIC-007, MIC-008, MIC-009, MIC-010, MIC-011, MIC-012, MIC-013, MIC-014, MIC-015, MIC-016, MIC-019, MIC-020, MIC-021, MIC-023, MIC-024.
- SOI-002, SOI-003, SOI-005, SOI-008, SOI-010, SOI-011, SOI-012.
- TER-013.
- VEG-001, VEG-012, VEG-017.

Row 21 also uses the unspecific phrase “MIC profiles as optional model input”.
It cannot be assigned a precise indicator ID without a research decision.
Review it rather than inferring an identifier. The machine register's statements
excluding the crosswalk from active scope remain intact.

### Historical provenance requiring research review

The Scientific Reference Register Section 7 retains four internal development
source labels at lines 488–491. They are not scholarly bibliographic identifiers;
they require an explicit provenance mapping or neutral-wording revision in a
future authorised register edit. Its introductory wording (lines 20 and 22),
Section 4 provenance (line 420), Section 7 introduction (line 484), and v0.1.0
history (line 513) likewise remain unchanged. `FRAME-T4S` is a provisional
programme-source label, not a verified scholarly citation, and is preserved.
Scholarly/local reference keys such as R01–R12, provider IDs RS001–RS025,
indicator IDs and DOI/URL references must not be mistaken for internal
conversation metadata.

The Machine Reference's historical `source_context` retains the named earlier
scope source at line 19107 (`inventory_v0_2_0_introduction`) and local source paths
at lines 19108 and 19111 (`inventory_v0_2_0_appendices` and
`machine_readme_v0_2_1`). Those paths and source hashes are historical provenance,
not current access routes. The generic `inventory.json` derivation artifact is
not present locally; its identity cannot be reconstructed from its filename
alone. Historical source editions, checksums and all protected bytes remain
preserved for a future review. Line references identify this audited edition
and may change in later revisions.

## Proposed academic reading interface

- `/information/EII/`: the Scientific Reference Register, preserving its
  established tables, ranges, wording and reference links.
- `/information/EII/research-guide/`: this README, explaining scope, versions,
  attribution, interpretation and limitations.
- `/information/EII/machine-reference/`: a short access page linking to the
  exact approved `EII_Machine_Reference.md` source on GitHub and its raw-file
  representation. The complete register remains authoritative; Markdown JSON
  fences must be parsed as documented, not treated as a standalone JSON file.

A full webpage rendering of the approximately 1 MB machine register is
optional, rather than required for the first publication. Its 237 JSON blocks
include the manifest, 235 indicator records and historical context; a source
link avoids turning this material into an unwieldy reading page. The existing
remote-sensing subset can remain available through the source repository
until separately approved for website publication.

Any later integration should use an approved full commit SHA and checksums,
with source-relative links mapped explicitly and citation/changelog links
pointing to that same version. No independently maintained research copies,
new database implementation or hosted observation datasets are introduced.
