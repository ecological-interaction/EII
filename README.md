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

The register references DRM v1.0.0 as the intended methodology. Its specification was unavailable; conformance remains unverified. No new SQL database or invented external identifiers are introduced. GISDS routes remain candidate sources, AMRKB links remain technical context, and future IoT/bioinformatics bindings remain unassigned. Trails4Soil practice crosswalks and PBCKA/EIRKB interoperability remain excluded.

The proposed website reading entry point is `EII_Scientific_Reference_Register.md`, with `EII_Machine_Reference.md` as its detailed structured reference. The previous EII.md / EII_Reference_Register.md names are historical file roles. Website integration, licensing and publication require separate review.

## Domain taxonomy and document versions

All three reference documents use **EII Domain Taxonomy v1.0.0** (D01–D15). Domain codes are stable and independent of sorting or ID prefixes. Each indicator has one primary domain; existing secondary domains remain in machine-record `related_domains`. The machine manifest preserves the 235-ID crosswalk from the scientific register's former A–P presentation groups. Historical source editions and file-role descriptions are retained as history, not current instructions.

| Document | Independent document version | Records |
|---|---|---:|
| Scientific Reference Register | 0.5.0 — 21 October 2026 | 235 |
| Machine Reference | 0.3.1 — 21 October 2026 | 235 |
| Remote Sensing | 0.1.0 — 21 October 2026 | 91 |

Document versions, EII Domain Taxonomy v1.0.0, the existing record schema and DRM v1.0.0 are independent references. No resource-release version is assigned by this migration. DRM compatibility is not certified because its authoritative specification is unavailable.
