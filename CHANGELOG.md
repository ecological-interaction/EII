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
