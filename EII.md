# EII — Ecological Indicator Inventory

**Status:** Living reference · Stage A (inventory)  
**Document version:** 0.1.0  
**Created:** 2026-10-10  
**Project:** Ecological Indicator Inventory (EII) — independent of EIRKB, designed for later interoperability  
**Scope:** Landscape, GIS/remote sensing, point clouds, soil, microbiomes, ecological processes, and socio-ecological context.

## 1. Purpose and boundaries

EII is a **parallel, standalone inventory** of ecological variables, indicators, indices, and inferences. It consolidates the earlier GIS/remote-sensing and bioinformatics discussions into one growing, human-readable Markdown reference. It is **not yet** a validated indicator standard, a database, or an EIRKB module. Scientific verification, bibliographic enrichment, and database implementation belong to later stages.

**Important distinction:** The previously discussed **21 TRAILS4SOIL items are regenerative management practices**, not 21 verified ecological indicators. Their mappings below are exploratory, not an official programme indicator framework.

### Reading key

- **M** = directly measurable variable; **D** = derived indicator/index; **P** = proxy; **I** = inference / modelled property; **C** = contextual or pressure variable.
- **GIS** = GIS / remote sensing; **PC** = photogrammetry / point cloud / LiDAR; **BIO** = DNA/RNA microbiome / bioinformatics; **LAB** = laboratory; **FIELD** = field monitoring; **MODEL** = modelling.
- These labels describe *common* uses, not exclusive or definitive categories. A property may be measured or inferred by different methods.
- **IDs are stable**: add new records without renumbering old ones. Gaps are permitted. IDs are local to EII; later database interoperability should use namespaced IDs such as `EII:VEG-001`.

## 2. Consolidated indicator register — Stage A

### A. Vegetation, photosynthesis and plant condition

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| VEG-001 | Normalised Difference Vegetation Index (NDVI) | D/P | GIS | Photosynthetically active green vegetation proxy; compare seasonal vigour. |
| VEG-002 | Green Normalised Difference Vegetation Index (GNDVI) | D/P | GIS | Canopy greenness / chlorophyll-related variation. |
| VEG-003 | Normalised Difference Red Edge Index (NDRE) | D/P | GIS | Chlorophyll and canopy physiology proxy. |
| VEG-004 | Soil Adjusted Vegetation Index (SAVI) | D/P | GIS | Vegetation signal where soil background is exposed. |
| VEG-005 | Enhanced Vegetation Index (EVI) | D/P | GIS | Vegetation greenness with background/atmospheric corrections. |
| VEG-006 | Green–Red Vegetation Index (GRVI) | D/P | GIS | RGB green-versus-red contrast; visible greenness. |
| VEG-007 | Excess Green (ExG) | D/P | GIS | RGB vegetation segmentation / green cover. |
| VEG-008 | Visible Atmospherically Resistant Index (VARI) | D/P | GIS | Visible-band greenness under variable atmospheric conditions. |
| VEG-009 | Green Leaf Index (GLI) | D/P | GIS | RGB green foliage prominence. |
| VEG-010 | Red–Green–Blue Vegetation Index (RGBVI) | D/P | GIS | RGB vegetation contrast / cover mapping. |
| VEG-011 | Leaf Area Index (LAI) | M/I | GIS, FIELD, MODEL | Leaf surface area and canopy development. |
| VEG-012 | Fractional vegetation / ground cover | M/D | GIS, PC, FIELD | Bare-soil protection, habitat and erosion context. |
| VEG-013 | Canopy chlorophyll content | M/I | GIS, FIELD, LAB | Nutrient / physiological condition, with calibration. |
| VEG-014 | Above-ground biomass | M/I | PC, GIS, FIELD, MODEL | Productivity, carbon and fuel loading. |
| VEG-015 | Plant water stress / canopy temperature anomaly | D/I | GIS, FIELD, MODEL | Irrigation, drought and heat response. |
| VEG-016 | Phenology / green-up / senescence dates | D | GIS, FIELD | Seasonal shifts, climate responses. |
| VEG-017 | Species / cultivar composition | M/C | FIELD, GIS, BIO | Community identity and agroecological selection. |

### B. Land surface, terrain and three-dimensional structure

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| TER-001 | Elevation / digital terrain model | M/D | GIS, PC | Terrain reference for spatial analyses. |
| TER-002 | Slope gradient | D | GIS, PC | Erosion, access, land-use suitability. |
| TER-003 | Aspect / slope orientation | D | GIS, PC | Radiation, exposure, microclimate and planting. |
| TER-004 | Solar radiation / insolation | I | GIS, MODEL | Thermal exposure and species suitability. |
| TER-005 | Topographic wetness index | D/P | GIS | Potential moisture accumulation, not measured wetness. |
| TER-006 | Flow accumulation / drainage pathways | D/I | GIS, PC | Runoff routing and catchment connectivity. |
| TER-007 | Surface roughness | D | PC, GIS | Erosion, habitat and terrain structure. |
| TER-008 | Terrace geometry / terrace-wall condition | M/D | PC, GIS, FIELD | Historic terrace conservation and restoration. |
| TER-009 | Erosion rills / gullies / sediment pathways | M/D | PC, GIS, FIELD | Soil loss and intervention prioritisation. |
| TER-010 | Tree height | M/D | PC, FIELD | Stand development, biomass proxy. |
| TER-011 | Canopy volume | D | PC | Tree structure and productivity / biomass proxy. |
| TER-012 | Canopy gaps / crown cover | D | PC, GIS | Regeneration, light availability, habitat structure. |
| TER-013 | Vertical vegetation complexity | D | PC | Habitat layering and fuel structure. |
| TER-014 | Surface / canopy change between surveys | D | PC, GIS | Erosion, growth, disturbance or restoration monitoring. |
| TER-015 | Built structures and landscape geometry | M/C | PC, GIS | Human occupation, material and intervention context. |

### C. Water, hydrology and thermal environment

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| HYD-001 | Surface / root-zone soil moisture | M/I | FIELD, GIS, MODEL | Water availability and drought exposure. |
| HYD-002 | Normalised Difference Moisture Index (NDMI) | D/P | GIS | Vegetation canopy moisture proxy; index definitions vary. |
| HYD-003 | Land Surface Temperature (LST) | D/M | GIS | Surface heating and moisture / vegetation stress context. |
| HYD-004 | Infiltration rate | M | FIELD | Runoff versus soil water entry. |
| HYD-005 | Soil water-holding capacity | M/I | LAB, FIELD, MODEL | Water retention / crop resilience. |
| HYD-006 | Stream discharge / river flow | M | FIELD | Water availability, flooding, ecological flow. |
| HYD-007 | Groundwater level / recharge | M/I | FIELD, MODEL | Aquifer condition and water balance. |
| HYD-008 | Flood extent / frequency | D/I | GIS, MODEL, FIELD | Exposure and wetland dynamics. |
| HYD-009 | Water turbidity / suspended sediment | M | FIELD, LAB, GIS | Erosion and water quality. |
| HYD-010 | Water nutrient concentrations | M | LAB, FIELD | Eutrophication / runoff pressure. |
| HYD-011 | Water conductivity / salinity / pH | M | FIELD, LAB | Water quality and ecological constraints. |
| HYD-012 | Evapotranspiration | M/I | GIS, FIELD, MODEL | Water demand and ecosystem flux. |

### D. Soil physical and chemical condition

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| SOI-001 | Soil texture | M | LAB, FIELD | Water retention and substrate characteristics. |
| SOI-002 | Bulk density / compaction | M | FIELD, LAB | Rooting constraints and soil structure. |
| SOI-003 | Soil aggregate stability | M | FIELD, LAB | Erosion resistance and soil structure. |
| SOI-004 | Soil porosity | M/D | FIELD, LAB | Aeration, infiltration and rooting. |
| SOI-005 | Soil organic carbon stock / concentration | M/D | LAB, FIELD, MODEL | Carbon storage and soil condition; distinguish stock vs %. |
| SOI-006 | Soil pH | M | FIELD, LAB | Nutrient availability and microbial habitat. |
| SOI-007 | Electrical conductivity / soil salinity | M | FIELD, LAB | Salinity stress. |
| SOI-008 | Available nitrogen / phosphorus / potassium | M | LAB | Nutrient supply / fertilisation context. |
| SOI-009 | Cation exchange capacity | M | LAB | Nutrient retention potential. |
| SOI-010 | Soil respiration / CO₂ efflux | M | FIELD, LAB | Biological activity; not alone a soil-health score. |
| SOI-011 | Soil temperature | M | FIELD | Biological activity and stress. |
| SOI-012 | Erosion rate / soil loss | M/I | FIELD, GIS, MODEL | Soil conservation. |
| SOI-013 | Soil contamination / heavy metals | M | LAB | Pollution pressure and food safety. |

### E. Microbiomes, genetics and soil biological processes

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| MIC-001 | Bacterial community composition | D | BIO | Taxonomic community structure and turnover. |
| MIC-002 | Archaeal community composition | D | BIO | Archaeal community structure and functional context. |
| MIC-003 | Fungal community composition | D | BIO | Decomposer, mutualist and pathogen context. |
| MIC-004 | Protist community composition | D | BIO | Microbial food-web and predation context. |
| MIC-005 | Microbial alpha diversity | D | BIO | Within-sample richness/evenness; method-dependent. |
| MIC-006 | Microbial beta diversity | D | BIO | Community differentiation across sites/times. |
| MIC-007 | Microbial biomass carbon / nitrogen | M | LAB | Living microbial biomass pool. |
| MIC-008 | Fungal:bacterial abundance ratio | D/P | BIO, LAB | Broad community balance; strongly method-dependent. |
| MIC-009 | Carbon-degradation gene/pathway potential | I | BIO | Potential decomposition capabilities, not measured flux. |
| MIC-010 | Nitrogen-fixation genetic potential | I | BIO | Presence/abundance of nitrogen fixation markers. |
| MIC-011 | Nitrification genetic potential | I | BIO | Potential ammonia oxidation / nitrification pathways. |
| MIC-012 | Denitrification genetic potential | I | BIO | Potential nitrate reduction pathways; not measured emissions. |
| MIC-013 | Phosphorus solubilisation / acquisition potential | I | BIO | Genetic potential for P mobilisation / uptake. |
| MIC-014 | Mycorrhizal community / colonisation | M/D/I | BIO, FIELD, LAB | Root symbiosis and nutrient exchange context. |
| MIC-015 | Rhizosphere-associated community structure | D | BIO | Plant–microbe relationships. |
| MIC-016 | Potential plant pathogens / beneficial taxa | I | BIO, LAB | Risk or beneficial associations; confirm function. |
| MIC-017 | Drought / salinity stress-response gene potential | I | BIO | Community adaptation potential, not proven resilience. |
| MIC-018 | Pollutant degradation gene potential | I | BIO | Potential biodegradation pathways. |
| MIC-019 | Extracellular enzyme activity | M | LAB | Specific substrate-processing activity. |
| MIC-020 | Community turnover along land-use gradients | D | BIO, GIS | Effects of management, soil type and disturbance. |
| MIC-021 | Spatial microbial community similarity / connectivity | D/I | BIO, GIS | Biogeographic patterns; similarity ≠ dispersal proof. |
| MIC-022 | Metatranscriptomic expression of functional genes | M/D/I | BIO | Active gene expression at sampling time; not direct process rate. |
| MIC-023 | Nitrogen mineralisation / nitrification rate | M | LAB, FIELD | Actual process rate for comparison with genetic potential. |
| MIC-024 | Decomposition / litter mass-loss rate | M | FIELD, LAB | Realised ecosystem process rate. |

### F. Biodiversity, habitat and ecological interactions

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| BIO-001 | Species richness | D | FIELD, BIO, GIS | Number of detected taxa in defined sampling design. |
| BIO-002 | Species abundance / occupancy | M/I | FIELD, BIO, MODEL | Population status and distribution. |
| BIO-003 | Shannon / Simpson diversity | D | FIELD, BIO | Richness/evenness summary. |
| BIO-004 | Functional diversity | D | FIELD, BIO | Trait and ecological role diversity. |
| BIO-005 | Habitat area / quality | D/I | GIS, FIELD | Conservation condition. |
| BIO-006 | Landscape fragmentation / patch size | D | GIS | Habitat continuity and edge exposure. |
| BIO-007 | Habitat connectivity / corridor suitability | D/I | GIS, MODEL | Potential movement and dispersal pathways. |
| BIO-008 | Pollinator abundance / visitation | M | FIELD | Pollination activity / crop support. |
| BIO-009 | Predation / natural pest-control rate | M | FIELD | Biological control process. |
| BIO-010 | Invasive species presence / spread | M/D | FIELD, GIS, BIO | Ecological risk and management priorities. |
| BIO-011 | Indicator / threatened species occurrence | M | FIELD, BIO | Conservation planning. |
| BIO-012 | Acoustic biodiversity / soundscape indices | D/P | FIELD | Biological activity proxy; validate against taxa. |
| BIO-013 | Food-web / interaction network structure | D/I | FIELD, BIO, MODEL | Ecological relationships; sampling bias matters. |

### G. Disturbance, climate and landscape change

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| DIS-001 | Normalised Burn Ratio (NBR) | D/P | GIS | Burn severity / disturbance mapping with calibration. |
| DIS-002 | Fire fuel load / vertical continuity | M/I | PC, GIS, FIELD | Wildfire behaviour potential. |
| DIS-003 | Fire occurrence / recurrence | D | GIS, FIELD | Disturbance history. |
| DIS-004 | Land-cover / land-use class | D/C | GIS, FIELD | Habitat and management context. |
| DIS-005 | Land-cover transition rate | D | GIS | Abandonment, urbanisation, reforestation. |
| DIS-006 | Air temperature / precipitation | M | FIELD, GIS | Climate baseline and anomalies. |
| DIS-007 | Drought index / aridity | D/I | GIS, MODEL | Water stress and future suitability. |
| DIS-008 | Heatwave / frost frequency | D | FIELD, GIS, MODEL | Climate extremes and crop risk. |
| DIS-009 | Soil/vegetation recovery after disturbance | D/I | GIS, FIELD | Resilience and restoration tracking. |
| DIS-010 | Future climate exposure / suitability | I | MODEL, GIS | Scenario-based long-term planning. |
| DIS-011 | SAR-derived inundation / surface change | D/P | GIS | Flooding and land-surface change in cloudy conditions. |
| DIS-012 | Hyperspectral material / vegetation trait signatures | D/P | GIS | Fine spectral differentiation; ground truth required. |

### H. Ecosystem functioning, agriculture and human context

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| FUN-001 | Primary productivity (GPP/NPP) | M/I | GIS, FIELD, MODEL | Ecosystem carbon uptake and biomass production. |
| FUN-002 | Carbon sequestration / stock change | D/I | LAB, FIELD, GIS, MODEL | Carbon dynamics; distinguish pools and fluxes. |
| FUN-003 | Nutrient retention / leaching | M/I | FIELD, LAB, MODEL | Pollution mitigation and nutrient cycling. |
| FUN-004 | Crop yield / yield stability | M/D | FIELD | Production and climate resilience. |
| FUN-005 | Groundcover persistence | D | GIS, FIELD | Soil protection through the year. |
| FUN-006 | Grazing pressure / stocking intensity | M/C | FIELD, GIS | Vegetation and soil management pressure. |
| FUN-007 | Irrigation / fertiliser / pesticide input | M/C | FIELD | Management pressure and resource efficiency. |
| FUN-008 | Field-margin / hedgerow length and condition | D | GIS, FIELD | Habitat, erosion control and landscape structure. |
| FUN-009 | Human settlement / roads / infrastructure | C | GIS, PC | Accessibility, fragmentation and design context. |
| FUN-010 | Material / biomass availability | M/I | GIS, FIELD, MODEL | Potential local production and circular resource flows. |
| FUN-011 | Ecological footprint / resource demand | D/I | MODEL | Socio-ecological pressure at defined system boundary. |
| FUN-012 | Composite soil-health index | D | LAB, FIELD, BIO | Multimetric condition assessment; specify exact framework. |
| FUN-013 | Ecosystem condition / integrity index | D/I | GIS, FIELD, MODEL | Multi-indicator ecological condition. |
| FUN-014 | Planetary / regional boundary exceedance | D/I | MODEL | System-level sustainability constraints; scale dependent. |

## 3. Observation platforms and information products

This section records **methods and source data, not additional indicators**.

| Method / platform | Primary outputs | Typical linked EII groups |
|---|---|---|
| RGB drone / ground camera | Red, green, blue reflectance/intensity; orthomosaics | VEG, TER, DIS |
| Multispectral camera | Red, green, red-edge, NIR bands | VEG, HYD |
| Thermal imaging | Radiometric surface temperature | HYD, VEG, DIS |
| Hyperspectral sensing | Dense spectral signatures | DIS, VEG, SOI |
| Satellite SAR | Radar backscatter / interferometric products | HYD, DIS, TER |
| LiDAR / structure-from-motion | Point clouds, DSM/DTM, geometry | TER, DIS, VEG |
| Weather / hydrology stations | Temperature, precipitation, flow, humidity | HYD, DIS |
| Soil sensors / laboratory | Moisture, pH, nutrients, carbon, density | SOI, HYD |
| Amplicon sequencing (16S/ITS/18S) | Taxonomic marker reads | MIC, BIO |
| Shotgun metagenomics | Community DNA, gene/pathway profiles | MIC |
| Metatranscriptomics | Community RNA / expressed genes | MIC |
| Enzyme assays / process measurements | Activity and flux rates | MIC, SOI, FUN |
| Field ecology / acoustic surveys | Species observations, interactions, recordings | BIO |
| Historical maps / cadastral records | Past land use, terraces, occupation | TER, DIS, FUN |

## 4. TRAILS4SOIL regenerative practices: exploratory indicator crosswalk

**Provenance note:** The following 21 practice categories were recalled from the earlier bioinformatics discussion; exact official naming and programme scope **require verification**. These are **management practices**, not a canonical set of 21 measured indicators. Crosswalks are hypotheses for study design, not validated causal links.

| # | Practice category (provisional wording) | Candidate EII indicators | Potential microbiome contribution |
|---|---|---|---|
| 1 | Groundcovers | VEG-012, FUN-005, SOI-005 | MIC-001–006, MIC-020 |
| 2 | Cover crops | VEG-017, SOI-008, FUN-005 | MIC-010, MIC-013, MIC-015 |
| 3 | Mulching | HYD-001, SOI-005, SOI-011 | MIC-009, MIC-019, MIC-024 |
| 4 | Organic amendments | SOI-005, SOI-008, SOI-010 | MIC-007, MIC-009, MIC-019 |
| 5 | Minimum tillage | SOI-002, SOI-003, SOI-005 | MIC-003, MIC-008, MIC-014 |
| 6 | Permanent cover | VEG-012, FUN-005, SOI-012 | MIC-005, MIC-020 |
| 7 | Planting green | VEG-012, SOI-008, HYD-001 | MIC-015, MIC-020 |
| 8 | Mechanical groundcover control | VEG-012, SOI-002, FUN-005 | MIC-020 |
| 9 | Intercropping | VEG-017, BIO-004, FUN-004 | MIC-005, MIC-014, MIC-015 |
| 10 | Crop-rotation diversity | VEG-017, SOI-008, FUN-004 | MIC-005, MIC-006, MIC-020 |
| 11 | Nutrient strategies | SOI-008, FUN-003 | MIC-010–013, MIC-023 |
| 12 | Weed control | VEG-012, VEG-017, FUN-007 | MIC-020 |
| 13 | Plant protection | BIO-009, FUN-007 | MIC-016 |
| 14 | Field margins / buffers | FUN-008, BIO-005, BIO-008 | MIC-020, MIC-021 |
| 15 | Biodiversity structures | BIO-001, BIO-005, BIO-007 | MIC-005, MIC-021 |
| 16 | Forest curtains / shelterbelts | TER-013, BIO-005, FUN-008 | MIC-003, MIC-014 |
| 17 | Grazing | FUN-006, SOI-002, VEG-012 | MIC-001–008, MIC-020 |
| 18 | Animal-feed rotations | FUN-004, FUN-006, VEG-017 | MIC-010, MIC-020 |
| 19 | Permanent grassland | VEG-012, SOI-005, BIO-004 | MIC-003, MIC-014, MIC-020 |
| 20 | Precision farming | HYD-001, SOI-008, VEG-001 | MIC-020 as spatial validation layer |
| 21 | Modelling / digital twins / remote sensing | DIS-010, FUN-013, VEG-001 | MIC profiles as optional model input |

## 5. Cross-domain questions and example indicator combinations

| Research question | Combined indicator families | Main caution |
|---|---|---|
| Where are drought-resilient tree guilds suitable? | TER-003/004, HYD-001/005, SOI-001/006, DIS-007/010, VEG-017 | Suitability requires species traits and scenario validation. |
| Which terraces are most vulnerable to erosion? | TER-002/008/009, VEG-012, HYD-004, SOI-003, DIS-006 | Terrain indices alone cannot establish actual erosion rate. |
| Does reduced tillage improve soil functioning? | SOI-003/005/010, MIC-003/008/019/023/024 | Use controls, repeat samples and actual process measurements. |
| Which areas offer pollinator habitat? | BIO-008, BIO-005/007, FUN-008, VEG-016/017 | Floral resources and seasonal continuity matter. |
| Where is wildfire risk concentrated? | DIS-002/003/007, TER-002/003, TER-013, VEG-014 | Hazard, exposure and vulnerability are distinct. |
| Can DNA identify active nitrogen cycling? | MIC-010/011/012/022/023, SOI-008, HYD-001 | DNA potential ≠ RNA expression ≠ realised flux. |
| How has abandonment altered the landscape? | DIS-004/005, TER-008/014, VEG-012/016, FUN-009 | Historical map georeferencing uncertainty. |

## 6. Proposed record schema for later interoperability

EII stays in Markdown for now. Each record could later be normalised into CSV/SQLite/JSON-LD with these fields:

| Field | Purpose |
|---|---|
| `eii_id` | Stable namespaced identifier (`EII:MIC-010`) |
| `preferred_label` / `aliases` | Human-readable name and synonyms |
| `entity_kind` | Variable, index, proxy, inference, contextual factor |
| `domain` / `related_domains` | Primary and secondary categories |
| `definition` | Operational definition and limitations |
| `unit` / `formula` | Unit and computation where applicable |
| `observed_property` | What the measurement actually records |
| `methods` / `platforms` | Sampling, instruments, processing pipelines |
| `spatial_scale` / `temporal_scale` | Resolution and applicable time horizon |
| `data_requirements` | Input bands, samples, reference datasets |
| `uncertainty` / `validation` | Error sources and ground-truth requirements |
| `reference_ids` | Bibliographic cross-references; later EIRKB mapping |
| `dataset_ids` / `place_ids` | External dataset and geospatial references |
| `related_eii_ids` | Dependencies, derived products and links |
| `provenance` / `review_status` | Source and evidence status |

**Interoperability principle:** Do not duplicate the EIRKB bibliographic catalogue. Later use explicit mappings from `EII:*` to EIRKB reference identifiers, Zotero keys/DOIs, and GIS-compatible dataset/feature IDs. No live EIRKB link is implied at this stage.

## 7. Source and verification register (starter)

The inventory consolidates **previous conversation-derived working lists**. They are not independently validated against every source in this edition.

| Source ID | Source / framework | Relevance | Status |
|---|---|---|---|
| CONV-GIS-20261007 | GIS and Remote Sensing Scope discussion | Spectral indices, terrain, land cover, ecology, human occupation | Consolidated; check technical definitions |
| CONV-PC-20261007 | Point Cloud from Aerial Scan discussion | 3D structure, terraces, canopy, erosion, repeat surveys | Consolidated; check technical definitions |
| CONV-BIO-20261010 | Bioinformatics Overview discussion | Microbial taxa, functions, stress, soil process inference | Consolidated; check against primary literature |
| CONV-EII-20261010 | Ecological Indicators Compilation discussion | 15-domain scope and measurement/inference distinction | Consolidated |
| FRAME-EBV | Essential Biodiversity Variables | Candidate biodiversity classification crosswalk | To research |
| FRAME-ECV | Essential Climate Variables | Candidate climate classification crosswalk | To research |
| FRAME-EOV | Essential Ocean Variables | Candidate aquatic/ocean classification crosswalk | To research |
| FRAME-SEEA | UN System of Environmental-Economic Accounting — Ecosystem Accounting | Ecosystem extent, condition and services | To research |
| FRAME-SOIL | EU soil monitoring / soil health frameworks | Soil condition metrics | To research |
| FRAME-PB | Planetary Boundaries framework | Regional/global pressure and boundary metrics | To research |
| FRAME-T4S | TRAILS4SOIL programme | Verify practice taxonomy and official indicator lists | **Unverified** |

## 8. Editorial rules and roadmap

1. **Stage A — Inventory (current):** Expand coverage, de-duplicate synonyms, separate indicators from methods, pressures and practices; retain stable IDs.
2. **Stage B — Scientific definitions:** Add formulas, units, sampling protocols, scale, reference standards, DOI/Zotero references, validation and evidence grading.
3. **Stage C — Relationships and inference:** Link observation → measurement → index → ecological process → interpretation, marking inferential confidence.
4. **Stage D — Place-based applications:** Add location-specific applicability, GIS layers, climate analogues and intervention use cases.

### Known gaps for subsequent Stage A expansions

Freshwater ecology and aquatic eDNA; marine/coastal indicators; soil fauna and nematodes; animal behaviour and movement; ecosystem services; atmospheric pollutants; geochemistry and geological substrates; disease ecology; socio-ecological governance; environmental justice; explicit biogeochemical fluxes; conservation status; ecological network metrics; regional and planetary boundaries; cross-scale temporal indicators.

### Version history

- **0.1.0 — 2026-10-10:** Initial EII Markdown inventory. Merged GIS, point-cloud, bioinformatics and ecological-indicator discussion lists; added provisional TRAILS4SOIL practices crosswalk, stable local IDs and future interoperability schema.
