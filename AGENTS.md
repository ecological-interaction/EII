# EII repository instructions

Read README.md, EII_Research_Protocol.md and CHANGELOG.md before research or architecture edits. This independent EII repository retains its own scientific scope; do not impose its structure on neighbours.

## Authority and preservation

- EII_Machine_Reference.json is authoritative for structured records. Scientific Register and README tables are manually maintained human-readable presentations. Remote Sensing is a separately curated analytical view. Do not implement automatic generation or synchronisation without approval.
- Preserve all 235 issued EII identifiers, fields, canonical/display distinctions, historical fields, empty/null/absent states, 15 D01–D15 domains, 72 secondary-domain relations, variants and 724 directed supporting relationships. Supporting indicators are not calculation dependencies.
- JSON source_context, source_transcription, prior manifests and the preservation crosswalk are immutable migration evidence, not current editable authorities. Historical paths/hashes, editions, assertions and bibliography qualifiers retain their source meaning.
- EII_Machine_Reference.md is only an anchor-preserving compatibility pointer. Do not restore a competing full corpus there. Legacy source snapshots/workbooks are evidence, not current authorities.
- Preserve exact five-column scientific wording and row order. Classifications, definitions and source-status distinctions require explicit research review; do not reinterpret earlier wording as new verified definitions.
- Trails4Soil is a historical provisional management-practice crosswalk excluded from active indicators. Cross-domain examples are exploratory, not validated causal assertions.
- GISDS routes remain candidates. Do not assign OSDS IDs or unresolved IoT/bioinformatics namespaces, infer dataset bindings, verification histories, reviewers or lifecycle events. Observational Systems is an empty placeholder until separately researched.
- Current DRM terminology is Database Reference Methodology, developing conventions. Historical Database Research Methodology v1.0.0 claims remain labelled source-edition history; no approved conformance is established.
- Document versions, record schema, taxonomy, serialization schema and resource releases are independent. Do not invent a release, DOI or licence. Preserve Jonathan Minchin, Ecological Interaction and ORCID in CFF metadata.

## Validation and diagrams

Run `python3 scripts/validate_eii.py`. It checks original objects and historical evidence, exact tables, domains, supporting targets, Remote Sensing parity, local links/anchors, source hashes, citation metadata and reproducible SVG output. Installed jsonschema / cffconvert dependencies may additionally check their standard schemas. Validation is read-only; temporary renderer runs remain outside the repository.

Edit labels/layout/palette in assets/diagrams/eii_overview.mmd and regenerate with `python3 assets/diagrams/render_eii_overview.py`. Render twice and compare bytes. Preserve 1200-pixel width, title/description/viewBox, source checksum, accessible alternative text and full-size links. Never edit generated SVG labels independently. The renderer is purpose-specific; candidate/proposed relationships do not establish observation bindings or an operational federation.

## Boundaries

Source repository retains authority; website publication is a separate approved pinned view. Keep preview artifacts/dependencies and temporary baselines outside this repository. Do not stage, commit, push, configure Git, edit website publication manifests or deploy without explicit authorisation. Preserve unrelated work.
