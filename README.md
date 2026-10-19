# EII — Ecological Indicator Inventory

**Work in Progress — Academic Research Resource**

Jonathan Minchin · Ecological Interaction · [ORCID 0000-0001-8152-1796](https://orcid.org/0000-0001-8152-1796).

EII is a higher-level reference for scientific and technological ecological indicators. Contributing catalogues describe observations, datasets, technologies or methods; EII describes measurements, qualified inferences and interpretive relationships. It is an exploratory research resource, not a validated monitoring standard.

## Start here

- [EII.md](EII.md): compact human-readable catalogue, 235 indicators in 15 domains.
- [EII_Reference_Register.md](EII_Reference_Register.md): authoritative full-length structured records, source registries, scientific references, classifications, observation schemas and historical context.
- [Remote-sensing subset](EII%20-%20Remote%20Sensing.md): existing focused reading view, unchanged by this revision.
- [CITATION.cff](CITATION.cff): academic attribution.
- [CHANGELOG.md](CHANGELOG.md): development and publication preparation.

## Maintaining the files

Edit the complete register first, then update the catalogue from the same stable IDs and fields. The catalogue uses `display_label`, `direct` and `display_inference`; it is a presentation of the register, not an independent scientific inventory. The remote-sensing subset is a separately curated view and must be reviewed explicitly when its underlying records change. There is no automatic synchronization or database service.

Register records use fenced JSON inside Markdown. Existing fields and full descriptions are retained, with additive historical preservation fields. Do not recycle IDs, flatten family variants or treat supporting indicators as calculation inputs. Validate unique IDs, domain counts, source/reference keys, supporting relationships and presentation parity after edits. Historical source hashes describe reviewed editions, not current file contents.

The register references DRM v1.0.0 as the intended methodology. Its specification was unavailable; conformance remains unverified. No new SQL database or invented external identifiers are introduced. GISDS routes remain candidate sources, AMRKB links remain technical context, and future IoT/bioinformatics bindings remain unassigned. Trails4Soil practice crosswalks and PBCKA/EIRKB interoperability remain excluded.

The proposed website reading entry point is `EII.md`, with the complete register as its detailed reference. Website integration, licensing and publication require separate review.
