# Changelog

## Local restructuring — 26 October 2026 (unreleased)

- Converted all 237 original JSON blocks into a single UTF-8 JSON document, preserving all 235 indicator objects field-for-field, the complete original manifest, classification migration, source context and original machine Markdown as immutable migration evidence. Historical registries, bibliography and observation templates are exposed with edition/status labels.
- Shortened README and copied the existing Reading Key, Domain Index, 235 five-column rows and platform table without scientific edits. Added inline GitHub reading links and the citation/version footer.
- Added complete canonical/display scientific details, source-edition scientific supplements and a labelled historical Trails4Soil appendix to the Scientific Register. Methods/governance moved to the Research Protocol; administrative history moved here. The old machine Markdown becomes an anchor-preserving compatibility pointer.
- Remote Sensing retains all 91 records; only full-register link destinations, the GISDS catalogue link (same source document, GitHub URL replacing a sibling-filesystem path) and document version changed. Added an empty Observational Systems placeholder with no records or bindings.
- Refined the editable overview diagram: unchanged scientific domain names, no domain codes/counts in the taxonomy panel, candidate GISDS/OSDS sources distinguished from scientific presentation, and developing DRM conventions explicitly qualified.
- Updated repository guidance and CFF attribution. No scientific revalidation, new classifications, source bindings, OSDS IDs, resource release, DOI or licence.

## Document and schema versions

README 0.2.0 (first explicit compact presentation version); Scientific Register 0.5.0 → 0.6.0; Machine document 0.3.1 → JSON 0.4.0; Remote Sensing 0.1.0 → 0.1.1 (links only); separate Research Protocol 0.1.0. EII Domain Taxonomy v1.0.0 and the existing record schema remain independent. JSON serialization schema `eii.machine-reference/0.1-draft` is not approved DRM conformance or a resource release.

## Preservation and file mappings

The [preservation crosswalk](EII_Preservation_Crosswalk.json) records baseline file hashes, every relocated section and original indicator-object fingerprints. The JSON `source_transcription` preserves the complete 0.3.1 machine Markdown; `source_context` and the original manifest remain unchanged historical evidence. Old machine indicator fragments now link to the Scientific Register, with original IDs retained. Historical EII.md / EII_Reference_Register.md roles map to the Scientific Register; historical paths/hashes inside evidence remain source-edition provenance. No automatic synchronisation is implemented.

## Unresolved research and provenance

Historical Trails4Soil mappings and unspecific model-input language remain provisional and excluded from active indicators. Conversation-derived source labels, unresolved reference ranges, unbound source routes, missing historical inventory.json and the unavailable detailed DRM specification remain unresolved. Current and superseded definitions are not merged or newly verified.

## Earlier administrative history (preserved)

# Changelog

Meaningful changes to research content, indicator registers, database structure,
classifications, publication interfaces and documentation are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Research-resource releases are separate from document, register and schema versions.

## [Unreleased]

### Added

- Academic publication review notes covering verified source access, register differences, outstanding historical-provenance decisions and proposed reading/source-file routes. The research registers are unchanged by this review.
- Explicit distinction between public access and reuse permission in the README and citation abstract; no licence has been selected.

- 21 October 2026: EII Domain Taxonomy v1.0.0 as the shared classification reference, a linked Scientific Reference Register Domain Index and the complete 235-ID A–P → D01–D15 migration crosswalk in the machine manifest.
- CFF 1.2.0 citation metadata naming Jonathan Minchin, Ecological Interaction and ORCID 0000-0001-8152-1796.
- Work-in-progress academic research status and links to the existing human-readable register and remote-sensing subset.
- This development changelog.

### Changed

- Aligned README terminology with the umbrella's Database Reference Methodology introduction, while retaining unverified conformance and leaving the protected methodology, identifiers and classifications unchanged.
- Recorded a future scope review for the 21 historical Trails4Soil practice mappings, their referenced indicator IDs and unresolved model-input wording; no scientific scope revision is implemented.
- Documented remaining internal development-source labels, historical provenance paths and register locations for explicit later review. Publication-facing development history retains neutral research wording; scholarly reference keys and factual chronology are preserved.

- 21 October 2026: Scientific Reference Register 0.5.0 reorganises all 235 original five-column rows under D01–D15 without changing descriptions; Machine Reference 0.3.1 retains all fields/values and existing domain relationships; Remote Sensing declares its first explicit version 0.1.0 with 91 unchanged scientific rows and aligned domain references.
- Corrected current file roles and stale links in the reference documents, README and maintenance instructions. Historical manifests, source paths/hashes, earlier descriptions and excluded historical material remain preserved. DRM v1.0.0 conformance remains unverified.
- Removed platform-specific preparation notes and an internal project identifier from the earlier README.md and EII.md source editions.
- Shortened the internal generated-inventory provenance path to `inventory.json`, retaining its original SHA-256 checksum. This historical source artifact is not included in the repository.

- At document version 0.3.0, EII.md became the compact four-column catalogue, EII_Reference_Register.md held the authoritative structured records, and README.md became the project entry point. These are historical filenames and roles, superseded by the versions listed below.
- Preserved existing record fields, full earlier inventory text, prior table rows, contextual material, source registries and scientific references in the complete register. Recovered the original 120 indicator rows from the initial Git commit without reintroducing its excluded programme crosswalk.
- Referenced DRM v1.0.0 as the intended methodology, explicitly marking conformance unverified because the specification was unavailable.

Existing scientific record fields, identifiers, classifications, scientific references, observation
schemas and source hashes are unchanged. The remote-sensing scientific content and scope are unchanged; its classification references, links and document metadata are updated.
No website integration, release tag or publication is included in this preparation.

## Development provenance

These are Git history entries, not published releases:

- 12 October 2026: `d617d7ab9e8da27e0adb6e66d185f3fea0404ca4` established the independent EII repository, authored by Jonathan Minchin.
- 19 October 2026: `45a1e5200e739a65a4fae96d0bd1b9a8d78186bf` updated the research inventory and README and added the human-readable Reference Register and remote-sensing subset, authored by Jonathan Minchin.
- 19 October 2026: `9f547399d91257ae9c82131a878f7ffc44c8a2f7` restructured the scientific and machine reference registers, authored by Jonathan Minchin.
- 19 October 2026: `40d26a6903a9908036cdf06fb94d3432e2c17ae1` expanded the Scientific Reference Register using the original v0.1.0 format, authored by Jonathan Minchin.
- 21 October 2026: `fb3705660178d2efd948863d362b236cd8d1d540` aligned the registers with EII Domain Taxonomy v1.0.0, authored by Jonathan Minchin.

Historical source editions identify the inventory as v0.2.0 and the register pair as v0.2.1, dated
13 October 2026. The current document versions are Scientific Reference Register 0.5.0, Machine Reference 0.3.1 and Remote Sensing 0.1.0, independently dated 21 October 2026; they share EII Domain Taxonomy v1.0.0. These document versions do not establish Git release tags.
No public release version or release date is assigned here.


## Relocated source-edition administrative sections



### Former README — Repository and publication status

**Historical README edition; current authorities are defined in the Research Protocol.**

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



### Former README — Proposed academic reading interface

**Historical README edition; current authorities are defined in the Research Protocol.**

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


### Scientific Register — 8. Editorial rules and roadmap

### Version history

- **0.1.0 — 2026-10-10:** Initial EII Markdown inventory. Merged GIS, point-cloud, bioinformatics and ecological-indicator discussion lists; added provisional TRAILS4SOIL practices crosswalk, stable local IDs and future interoperability schema.



### Scientific Register — consolidated edition history

### Consolidated edition history

- **0.5.0 — 2026-10-21:** Reorganised all 235 unchanged scientific rows under D01–D15 and added the linked Domain Index. Adopted EII Domain Taxonomy v1.0.0; preserved existing primary/secondary assignments and A–P migration provenance in the machine reference. Scientific descriptions, source-edition material and references are unchanged. DRM v1.0.0 conformance remains unverified.
- **0.4.0 — 2026-10-19:** Preserved the supplied v0.1.0 presentation and all original indicator rows; added 115 later indicators for 235 unique records; retained the 15-domain classification and later scientific references. The pasted programme crosswalk is historical material only.


### Source context: machine_readme_v0_2_1 — Versions and changes

**Historical source edition `machine_readme_v0_2_1`; original research status and qualifications retained.**

## Versions and changes

**Pair version:** 0.2.1. **Scientific inventory baseline:** extended EII v0.2.0. **Created:** 13 October 2026.

- EII v0.1.0 provided 120 stable IDs and labels across eight compilation groups.
- EII v0.2.0 expanded this to 235 records in the agreed 15 domains, adding operational definitions, units/formulas, qualified inferences, support links, classifications and candidate source routes.
- The v0.2.1 presentation converted these entries to human-readable tables without changing the inventory's scientific content.
- This new two-file register uses the complete extended v0.2.0 record set and the table presentation. Administrative sections, editorial roadmap, provenance hashes, technical variants and machine data are moved here. The human file retains scientific limitations, since those are essential to interpreting the indicators.
- Pair v0.2.0 simplifies the main register to five columns: indicator, measurement/source, beginner inference, supporting indicator names and concise sources. Visible EII IDs, coded kind/method columns, indicator definitions and dagger markers are removed from the main reading view. Stable IDs, canonical labels, rigorous definitions and detailed inferences remain in the machine snapshot; names link through stable anchors. Both deliverables remain Markdown.

### Reference display update — pair v0.2.1

Each indicator now displays its short stable reference beside its existing beginner-facing name, for example **MIC-005 — Microbial diversity within a sample**. The same references are restored in the left columns of the classification and indicator-family tables. The human names, measurements, inferences, supporting links and source pointers remain unchanged.

The register still has five main columns: no separate ID or coded kind/method column is added. Main-table first-column reference/name text and last-column Sources text use HTML `<small>`; the middle columns retain the normal text size. Bold reference/name text uses `<strong>` inside `<small>`. Markdown has no native per-column font-size control, so visual sizing depends on the renderer supporting these HTML tags; readers that strip them still retain the references and content.

`display_reference` stores the short ID. `display_reference_label` stores the combined short ID/name. `display_column_sizes` records the presentation intent. The preserved `id`, canonical label/definition/measurement/inference fields, beginner display fields, classifications, source routes and all other record metadata remain intact. The manifest stores the previous presentation state in `presentation_history` and the current display rule in `presentation`.

For future edits, add or preserve the short reference in the left cell, keep its stable anchor unchanged, and retain the smaller first/last-column wrappers. An indicator name change must update `display_label` and `display_reference_label`; an identity change requires an explicit stable-ID decision, not a cosmetic rename. Refresh the human hash after saving.

The files use stable names; future versions belong inside this README rather than new filename suffixes. The human register contains no version history, implementation schema, raw JSON registry, workflow, audit hashes or file-system provenance.



### Source context: machine_readme_v0_2_1 — Current pair validation

**Historical source edition `machine_readme_v0_2_1`; original research status and qualifications retained.**

## Current pair validation

235 human main-table rows match 235 JSON records by stable anchors; beginner display names, acquisition sources and inferences match their snapshot fields; all 120 legacy IDs/labels are preserved; all 15 domains are represented; support and navigation links resolve; source/ref keys resolve; the human file contains no JSON blocks or administrative sections. GISDS/AMRKB references remain candidates/context rather than invented observed provenance.

Future updates must rerun these checks and record changed counts here rather than assuming this saved validation applies indefinitely.


### Machine document 0.3.1 version history

## Version history

- **0.3.1 — 2026-10-21:** Adopted EII Domain Taxonomy v1.0.0 as the explicit shared classification reference; added the 235-ID A–P migration crosswalk and per-record taxonomy reference. Preserved all existing record fields/values and historical content, corrected current file-role metadata and the scientific-register link, and retained the prior manifest/introduction. No primary or secondary domain assignments changed.
- **0.3.0 — 2026-10-19:** Authoritative structured register with 235 indicators, full scientific/display fields, source registries and additive historical preservation fields. Earlier edition details remain in the source context.



## Section destination crosswalk

| Source document / context | Original section | Destination |
|---|---|---|
| README.md | Introduction | EII_Research_Protocol.md |
| README.md | Start here | EII_Research_Protocol.md |
| README.md | Maintaining the files | EII_Research_Protocol.md |
| README.md | Domain taxonomy and document versions | EII_Research_Protocol.md |
| README.md | Repository and publication status | CHANGELOG.md |
| README.md | Register comparison and publication review | EII_Research_Protocol.md |
| README.md | Proposed academic reading interface | CHANGELOG.md |
| EII_Scientific_Reference_Register.md | Introduction | EII_Research_Protocol.md |
| EII_Scientific_Reference_Register.md | 1. Purpose and boundaries | EII_Research_Protocol.md; Scientific Register#reading-key |
| EII_Scientific_Reference_Register.md | Domain Index | EII_Scientific_Reference_Register.md |
| EII_Scientific_Reference_Register.md | 2. Consolidated indicator register — Stage A | EII_Scientific_Reference_Register.md |
| EII_Scientific_Reference_Register.md | 3. Observation platforms and information products | EII_Scientific_Reference_Register.md |
| EII_Scientific_Reference_Register.md | 4. TRAILS4SOIL regenerative practices: exploratory indicator crosswalk | EII_Scientific_Reference_Register.md#historical-research-appendix-trails4soil |
| EII_Scientific_Reference_Register.md | 5. Cross-domain questions and example indicator combinations | EII_Scientific_Reference_Register.md |
| EII_Scientific_Reference_Register.md | 6. Proposed record schema for later interoperability | EII_Research_Protocol.md |
| EII_Scientific_Reference_Register.md | 7. Source and verification register (starter) | EII_Scientific_Reference_Register.md |
| EII_Scientific_Reference_Register.md | 8. Editorial rules and roadmap | EII_Research_Protocol.md; CHANGELOG.md |
| EII_Scientific_Reference_Register.md | 9. Scientific domain classification — consolidated edition | EII_Scientific_Reference_Register.md |
| EII_Scientific_Reference_Register.md | 10. Scientific references — consolidated edition | EII_Scientific_Reference_Register.md |
| EII_Machine_Reference.md:source_context.inventory_v0_2_0_introduction | Introduction | EII_Research_Protocol.md |
| EII_Machine_Reference.md:source_context.inventory_v0_2_0_introduction | Purpose and reviewed source baseline | EII_Research_Protocol.md |
| EII_Machine_Reference.md:source_context.inventory_v0_2_0_introduction | Reading and interpretation rules | EII_Research_Protocol.md |
| EII_Machine_Reference.md:source_context.inventory_v0_2_0_introduction | Domain index | EII_Research_Protocol.md |
| EII_Machine_Reference.md:source_context.inventory_v0_2_0_appendices | Appendix A — Source routes and interoperable observation schema | EII_Research_Protocol.md |
| EII_Machine_Reference.md:source_context.inventory_v0_2_0_appendices | Appendix B — Scientific reference and verification register | EII_Scientific_Reference_Register.md |
| EII_Machine_Reference.md:source_context.inventory_v0_2_0_appendices | Appendix C — Cross-domain interpretation examples | EII_Scientific_Reference_Register.md |
| EII_Machine_Reference.md:source_context.inventory_v0_2_0_appendices | Maintenance, validation and next review | EII_Research_Protocol.md |
| EII_Machine_Reference.md:source_context.register_v0_2_1_introduction | Introduction | EII_Research_Protocol.md |
| EII_Machine_Reference.md:source_context.register_v0_2_1_introduction | Reading the tables | EII_Research_Protocol.md |
| EII_Machine_Reference.md:source_context.register_v0_2_1_supplementary_sections | Classifications | EII_Scientific_Reference_Register.md |
| EII_Machine_Reference.md:source_context.register_v0_2_1_supplementary_sections | Observation methods and information products | EII_Scientific_Reference_Register.md |
| EII_Machine_Reference.md:source_context.register_v0_2_1_supplementary_sections | Source register | EII_Scientific_Reference_Register.md |
| EII_Machine_Reference.md:source_context.register_v0_2_1_supplementary_sections | Scientific references | EII_Scientific_Reference_Register.md |
| EII_Machine_Reference.md:source_context.register_v0_2_1_supplementary_sections | Indicator families and distinct quantities | EII_Scientific_Reference_Register.md |
| EII_Machine_Reference.md:source_context.register_v0_2_1_supplementary_sections | Cross-domain questions | EII_Scientific_Reference_Register.md |
| EII_Machine_Reference.md:source_context.machine_readme_v0_2_1 | Introduction | EII_Research_Protocol.md |
| EII_Machine_Reference.md:source_context.machine_readme_v0_2_1 | Two maintained files | EII_Research_Protocol.md |
| EII_Machine_Reference.md:source_context.machine_readme_v0_2_1 | Versions and changes | CHANGELOG.md |
| EII_Machine_Reference.md:source_context.machine_readme_v0_2_1 | Update workflow | EII_Research_Protocol.md |
| EII_Machine_Reference.md:source_context.machine_readme_v0_2_1 | Scope and scientific review state | EII_Research_Protocol.md |
| EII_Machine_Reference.md:source_context.machine_readme_v0_2_1 | Identifier and field contract | EII_Research_Protocol.md |
| EII_Machine_Reference.md:source_context.machine_readme_v0_2_1 | Interoperability and unresolved routes | EII_Research_Protocol.md |
| EII_Machine_Reference.md:source_context.machine_readme_v0_2_1 | Observation binding template | EII_Research_Protocol.md |
| EII_Machine_Reference.md:source_context.machine_readme_v0_2_1 | Manifest and source-route registry | EII_Research_Protocol.md |
| EII_Machine_Reference.md:source_context.machine_readme_v0_2_1 | Complete synchronized record snapshot | EII_Research_Protocol.md |
| EII_Machine_Reference.md:source_context.machine_readme_v0_2_1 | Current pair validation | CHANGELOG.md |
| EII_Machine_Reference.md:source_context.classification_migration_v1_0_0 | previous_scientific_introduction | EII_Machine_Reference.json#source_context; Research Protocol |
| EII_Machine_Reference.md:source_context.classification_migration_v1_0_0 | previous_machine_introduction | EII_Machine_Reference.json#source_context; Research Protocol |
| EII_Machine_Reference.md:source_context.classification_migration_v1_0_0 | prior_machine_document_version | EII_Machine_Reference.json#source_context; Research Protocol |
| EII_Machine_Reference.md:source_context.classification_migration_v1_0_0 | previous_scientific_presentation_headings | EII_Machine_Reference.json#source_context; Research Protocol |
| EII - Remote Sensing.md | complete document | EII - Remote Sensing.md |


## Relocated historical version history

### Version history

- **0.2.0 — 13 October 2026:** Expanded the 120-record baseline into the 15-domain master register; retained every original ID and preferred label; added working definitions, observed inputs, units, qualified inferences, supporting-ID links and four-level classifications. Removed the excluded programme crosswalk and excluded interoperability dependencies. Added candidate GISDS source routes, scope-only AMRKB context, unresolved future channels, variant discipline, provenance hashes and schema validation.
- **0.1.0 — 10 October 2026:** Original consolidated inventory; retained as the reviewed provenance baseline, including sections intentionally removed from this edition.
