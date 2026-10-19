# Changelog

Meaningful changes to research content, indicator registers, database structure,
classifications, publication interfaces and documentation are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Research-resource releases are separate from document, register and schema versions.

## [Unreleased]

### Added

- CFF 1.2.0 citation metadata naming Jonathan Minchin, Ecological Interaction and ORCID 0000-0001-8152-1796.
- Work-in-progress academic research status and links to the existing human-readable register and remote-sensing subset.
- This development changelog.

### Changed

- Removed ChatGPT-specific preparation notes and an internal project identifier from README.md and EII.md.
- Shortened the internal generated-inventory provenance path to `inventory.json`, retaining its original SHA-256 checksum. This historical source artifact is not included in the repository.

- Prepared document version 0.3.0: EII.md is now the compact four-column catalogue; EII_Reference_Register.md is the authoritative sequence of structured JSON records; README.md is the project entry point.
- Preserved existing record fields, full earlier inventory text, prior table rows, contextual material, source registries and scientific references in the complete register. Recovered the original 120 indicator rows from the initial Git commit without reintroducing its excluded programme crosswalk.
- Referenced DRM v1.0.0 as the intended methodology, explicitly marking conformance unverified because the specification was unavailable.

Existing scientific record fields, identifiers, classifications, scientific references, observation
schemas and source hashes are unchanged. The remote-sensing subset is unchanged.
No website integration, release tag or publication is included in this preparation.

## Development provenance

These are Git history entries, not published releases:

- 12 October 2026: `d617d7ab9e8da27e0adb6e66d185f3fea0404ca4` established the independent EII repository, authored by Jonathan Minchin.
- 19 October 2026: `45a1e5200e739a65a4fae96d0bd1b9a8d78186bf` updated the research inventory and README and added the human-readable Reference Register and remote-sensing subset, authored by Jonathan Minchin.

The inventory identifies itself as v0.2.0 and the register pair as v0.2.1, dated
13 October 2026. These document versions do not establish Git release tags.
No public release version or release date is assigned here.
