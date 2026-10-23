# Project instructions

Ecological Indicator Inventory. Read README.md, EII_Scientific_Reference_Register.md and EII_Machine_Reference.md. Preserve stable indicator IDs and distinguish exploratory inventory entries from verified standards.

- This directory is an independent Git repository within the ecological-information umbrella.
- Keep work within this project unless cross-project changes are explicitly requested.
- Preserve research content and provenance. Keep version information inside documents and use stable filenames.
- Prepare interoperability through explicit identifiers, references and relationships; do not merge the projects' scopes.
- Do not push to GitHub or configure a remote unless the user requests it.

- Use EII Domain Taxonomy v1.0.0 (D01–D15), with one primary domain and preserved secondary-domain relationships. Keep scientific tables in their existing five-column format and preserve their wording. Record classification changes in the machine migration crosswalk and keep the remote-sensing subset aligned.

## Overview diagram maintenance

- Keep the editable labels, relationships, palette and fixed layout in `assets/diagrams/eii_overview.mmd`; regenerate with `python3 assets/diagrams/render_eii_overview.py`. The renderer supports this diagram's Mermaid subset only and requires no third-party packages.
- Maintain source and SVG together. Regenerate twice and compare output bytes; retain SVG title, description, viewBox, source checksum and README alternative text/full-size link. Never edit SVG labels independently.
- Treat the illustration as a documented overview, not a new classification, implemented service or claim of scientific validation. Preserve all records, codes and original documentation.
- Use repository-relative asset paths. Pinned-source website publication must separately approve, allowlist and checksum the SVG; do not run the renderer during website builds or advance publication pins as part of diagram maintenance.
