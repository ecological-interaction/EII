# EII — Ecological Indicator Inventory

**Status:** Living reference · Stage A (inventory)  
**Source document version:** 0.1.0  
**Created:** 2026-10-10  
**Project:** Ecological Indicator Inventory (EII) — independent of EIRKB, designed for later interoperability  
**Scope:** Landscape, GIS/remote sensing, point clouds, soil, microbiomes, ecological processes, and socio-ecological context.


**Consolidated document version:** 0.5.0 · Local review draft · 21 October 2026  
**Work in Progress — Academic Research Resource**  
Jonathan Minchin · Ecological Interaction · [ORCID 0000-0001-8152-1796](https://orcid.org/0000-0001-8152-1796).

**Edition note:** The original v0.1.0 scientific wording, five-column table format and 120 indicator rows are preserved, together with all 115 later indicator rows. This edition reorganises the 235 records into EII Domain Taxonomy v1.0.0 (D01–D15), using the established machine-record assignments. Historical A–P presentation groups are retained in the migration crosswalk in EII_Machine_Reference.md. The original source-version/date fields refer to the source edition; ID prefixes do not replace domain membership.

The complete definitions, measurements, formulas, interpretation limits, supporting indicators, classifications, scientific references and candidate source routes remain in [EII_Machine_Reference.md](EII_Machine_Reference.md). Original wording is retained as historical wording where later source editions qualify it; it is not newly validated. Historical proposals for EIRKB mapping below remain source-edition proposals and are outside current EII interoperability scope. Future IoT and bioinformatics routes remain unassigned. DRM v1.0.0 is the intended methodology; conformance remains unverified.

## 1. Purpose and boundaries

EII is a **parallel, standalone inventory** of ecological variables, indicators, indices, and inferences. It consolidates the earlier GIS/remote-sensing and bioinformatics discussions into one growing, human-readable Markdown reference. It is **not yet** a validated indicator standard, a database, or an EIRKB module. Scientific verification, bibliographic enrichment, and database implementation belong to later stages.

**Important distinction:** The previously discussed **21 TRAILS4SOIL items are regenerative management practices**, not 21 verified ecological indicators. Their mappings below are exploratory, not an official programme indicator framework.

### Reading key

- **M** = directly measurable variable; **D** = derived indicator/index; **P** = proxy; **I** = inference / modelled property; **C** = contextual or pressure variable.
- **GIS** = GIS / remote sensing; **PC** = photogrammetry / point cloud / LiDAR; **BIO** = DNA/RNA microbiome / bioinformatics; **LAB** = laboratory; **FIELD** = field monitoring; **MODEL** = modelling.
- These labels describe *common* uses, not exclusive or definitive categories. A property may be measured or inferred by different methods.
- **IDs are stable**: add new records without renumbering old ones. Gaps are permitted. IDs are local to EII; later database interoperability should use namespaced IDs such as `EII:VEG-001`.

## Domain Index

**Classification reference:** EII Domain Taxonomy v1.0.0. Domain codes are stable identifiers, independent of display order. Each indicator appears once under its primary domain; secondary relationships and the previous A–P grouping crosswalk are retained in the machine reference.

| Domain | Scope | Records |
|---|---|---:|
| D01 | [Atmosphere and climate](#d01) | 14 |
| D02 | [Hydrology](#d02) | 21 |
| D03 | [Soil physics](#d03) | 14 |
| D04 | [Soil chemistry](#d04) | 12 |
| D05 | [Soil biology](#d05) | 19 |
| D06 | [Biodiversity](#d06) | 15 |
| D07 | [Vegetation](#d07) | 28 |
| D08 | [Ecological interactions](#d08) | 15 |
| D09 | [Biogeochemical cycles](#d09) | 20 |
| D10 | [Landscape ecology](#d10) | 16 |
| D11 | [Ecosystem functioning](#d11) | 9 |
| D12 | [Ecological resilience](#d12) | 13 |
| D13 | [Agricultural ecology](#d13) | 15 |
| D14 | [Human–ecological systems](#d14) | 13 |
| D15 | [Planetary and regional boundaries](#d15) | 11 |

## 2. Consolidated indicator register — Stage A

<a id="d01"></a>

### D01 — Atmosphere and climate

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| TER-004 | Solar radiation / insolation | I | GIS, MODEL | Thermal exposure and species suitability. |
| HYD-003 | Land Surface Temperature (LST) | D/M | GIS | Surface heating and moisture / vegetation stress context. |
| DIS-006 | Air temperature / precipitation | M | FIELD, GIS | Climate baseline and anomalies. |
| DIS-007 | Drought index / aridity | D/I | GIS, MODEL | Water stress and future suitability. |
| DIS-008 | Heatwave / frost frequency | D | FIELD, GIS, MODEL | Climate extremes and crop risk. |
| ATM-001 | Air temperature | M | FIELD | Shows local heat and cold conditions. Nearby shade, exposure and sensor placement affect readings. |
| ATM-002 | Precipitation amount/intensity | M | FIELD | Shows water arriving as rain or snow and how quickly it falls. One gauge may not represent a whole watershed. |
| ATM-003 | Relative humidity/vapour-pressure deficit | M/D | FIELD | Helps assess how strongly the air can draw water from plants. This does not show how dry the soil is. |
| ATM-004 | Photosynthetically active radiation | M | FIELD | Shows light available for photosynthesis. The amount plants absorb and use also depends on the canopy and plant condition. |
| ATM-005 | Wind speed/direction | M | FIELD | Helps assess exposure, drying and possible spread of fire or airborne material. Shelter and measurement height affect readings. |
| ATM-006 | Atmospheric CO₂ concentration | M | FIELD | Shows carbon dioxide in the air. Local concentration changes do not directly measure carbon uptake or release by an ecosystem. |
| ATM-007 | Ozone exposure | M/D/C | FIELD | Helps assess ozone exposure that could harm plants. Actual damage depends on plant type, timing and ozone uptake. |
| ATM-008 | PM₂.₅/PM₁₀ concentration | M/C | FIELD | Shows the amount of fine airborne particles. Particle mass alone does not identify their chemicals or where they came from. |
| ATM-009 | Snow cover/snow water equivalent | M/D | GIS, FIELD | Helps assess snow-covered area and stored meltwater. Snow cover alone does not show how much water the snow contains. |

<a id="d02"></a>

### D02 — Hydrology

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| TER-005 | Topographic wetness index | D/P | GIS | Potential moisture accumulation, not measured wetness. |
| TER-006 | Flow accumulation / drainage pathways | D/I | GIS, PC | Runoff routing and catchment connectivity. |
| HYD-001 | Surface / root-zone soil moisture | M/I | FIELD, GIS, MODEL | Water availability and drought exposure. |
| HYD-006 | Stream discharge / river flow | M | FIELD | Water availability, flooding, ecological flow. |
| HYD-007 | Groundwater level / recharge | M/I | FIELD, MODEL | Aquifer condition and water balance. |
| HYD-008 | Flood extent / frequency | D/I | GIS, MODEL, FIELD | Exposure and wetland dynamics. |
| HYD-009 | Water turbidity / suspended sediment | M | FIELD, LAB, GIS | Erosion and water quality. |
| HYD-010 | Water nutrient concentrations | M | LAB, FIELD | Eutrophication / runoff pressure. |
| HYD-011 | Water conductivity / salinity / pH | M | FIELD, LAB | Water quality and ecological constraints. |
| HYD-012 | Evapotranspiration | M/I | GIS, FIELD, MODEL | Water demand and ecosystem flux. |
| HYD-013 | Dissolved oxygen | M | FIELD | Helps assess whether water contains enough oxygen for aquatic life. Levels can vary with temperature, flow and time of day. |
| HYD-014 | Water chlorophyll-a | M/P | GIS, FIELD | Helps estimate the amount of microscopic algae in water. Pigment levels and cloudiness can affect the estimate. |
| HYD-015 | Water temperature | M | GIS, FIELD | Shows thermal conditions for aquatic life. Surface temperature may not represent deeper water. |
| HYD-016 | Surface-water occurrence/hydroperiod | D | GIS, FIELD | Shows how often or how long surface water is present. Missed observations and hidden soil saturation can affect the result. |
| HYD-017 | Environmental-flow deficit | D/C | FIELD | Helps identify flows below a locally defined ecological need. The threshold must fit the river and its species. |
| HYD-018 | Water nutrient load | D/M | FIELD | Shows how much nutrient is carried by water. Storms can carry large amounts that occasional samples miss. |
| HYD-019 | Faecal indicator bacteria | M/P | FIELD, LAB, BIO | Helps screen for faecal contamination. Indicator bacteria do not identify every pathogen or guarantee that water is safe. |
| HYD-020 | Water contaminant residues | M/C | FIELD, LAB | Shows named chemical residues in water. Their effects depend on concentration, exposure time, mixtures and organisms. |
| HYD-021 | Water transparency/Secchi depth | M/P | FIELD | Shows how clear water is. Algae, sediment and dissolved colour can all reduce clarity. |
| HYD-022 | Ocean carbonate chemistry | M/D | GIS, FIELD, LAB | Helps understand ocean acidity and conditions for shell-forming organisms. One pH reading does not describe the full chemical balance. |
| DIS-011 | SAR-derived inundation / surface change | D/P | GIS | Flooding and land-surface change in cloudy conditions. |

<a id="d03"></a>

### D03 — Soil physics

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| TER-007 | Surface roughness | D | PC, GIS | Erosion, habitat and terrain structure. |
| TER-009 | Erosion rills / gullies / sediment pathways | M/D | PC, GIS, FIELD | Soil loss and intervention prioritisation. |
| HYD-004 | Infiltration rate | M | FIELD | Runoff versus soil water entry. |
| HYD-005 | Soil water-holding capacity | M/I | LAB, FIELD, MODEL | Water retention / crop resilience. |
| SOI-001 | Soil texture | M | LAB, FIELD | Water retention and substrate characteristics. |
| SOI-002 | Bulk density / compaction | M | FIELD, LAB | Rooting constraints and soil structure. |
| SOI-003 | Soil aggregate stability | M | FIELD, LAB | Erosion resistance and soil structure. |
| SOI-004 | Soil porosity | M/D | FIELD, LAB | Aeration, infiltration and rooting. |
| SOI-011 | Soil temperature | M | FIELD | Biological activity and stress. |
| SOI-012 | Erosion rate / soil loss | M/I | FIELD, GIS, MODEL | Soil conservation. |
| SOI-014 | Coarse fragments/soil depth | M | FIELD | Shows soil depth and the amount of stones. Both affect rooting space, water storage and carbon-stock estimates. |
| SOI-015 | Saturated hydraulic conductivity | M | FIELD | Shows how easily water moves through saturated soil. Small samples may miss channels that carry water quickly in the field. |
| SOI-016 | Soil matric potential | M | FIELD | Shows how tightly soil holds water. Salt content also affects how easily plants can take it up. |
| SOI-017 | Macropore abundance/connectivity | M/D | FIELD | Shows large soil pores and how they connect. Their presence alone does not measure actual water or nutrient movement. |

<a id="d04"></a>

### D04 — Soil chemistry

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| SOI-005 | Soil organic carbon stock / concentration | M/D | LAB, FIELD, MODEL | Carbon storage and soil condition; distinguish stock vs %. |
| SOI-006 | Soil pH | M | FIELD, LAB | Nutrient availability and microbial habitat. |
| SOI-007 | Electrical conductivity / soil salinity | M | FIELD, LAB | Salinity stress. |
| SOI-008 | Available nitrogen / phosphorus / potassium | M | LAB | Nutrient supply / fertilisation context. |
| SOI-009 | Cation exchange capacity | M | LAB | Nutrient retention potential. |
| SOI-013 | Soil contamination / heavy metals | M | LAB | Pollution pressure and food safety. |
| SOI-018 | Total soil nitrogen/C:N ratio | M/D | FIELD, LAB | Helps compare total nitrogen and the balance of carbon to nitrogen. This does not directly measure nutrients available to plants. |
| SOI-019 | Exchangeable sodium percentage/SAR | D/C | FIELD, LAB | Helps screen for sodium levels that may damage soil structure. Salt content and soil minerals also matter. |
| SOI-020 | Soil inorganic carbon | M/D | FIELD, LAB | Shows carbon stored in soil minerals such as carbonates. More carbonate does not automatically mean more carbon removed from the atmosphere. |
| SOI-021 | Labile/particulate/mineral-associated organic carbon | M | FIELD, LAB | Helps compare different soil organic-carbon fractions. The fractions do not give an exact lifetime for stored carbon. |
| SOI-022 | Bioavailable contaminant fraction | M/P | FIELD, LAB | Helps estimate the fraction of a pollutant organisms might absorb. Laboratory extraction is an approximation that needs checking for the organism concerned. |
| SOI-023 | Soil redox potential | M/P | FIELD, LAB | Helps assess whether soil conditions favour oxygen-dependent or oxygen-poor processes. Small areas within the soil may differ. |

<a id="d05"></a>

### D05 — Soil biology

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| SOI-010 | Soil respiration / CO₂ efflux | M | FIELD, LAB | Biological activity; not alone a soil-health score. |
| MIC-001 | Bacterial community composition | D | BIO | Taxonomic community structure and turnover. |
| MIC-002 | Archaeal community composition | D | BIO | Archaeal community structure and functional context. |
| MIC-003 | Fungal community composition | D | BIO | Decomposer, mutualist and pathogen context. |
| MIC-004 | Protist community composition | D | BIO | Microbial food-web and predation context. |
| MIC-005 | Microbial alpha diversity | D | BIO | Within-sample richness/evenness; method-dependent. |
| MIC-006 | Microbial beta diversity | D | BIO | Community differentiation across sites/times. |
| MIC-007 | Microbial biomass carbon / nitrogen | M | LAB | Living microbial biomass pool. |
| MIC-008 | Fungal:bacterial abundance ratio | D/P | BIO, LAB | Broad community balance; strongly method-dependent. |
| MIC-019 | Extracellular enzyme activity | M | LAB | Specific substrate-processing activity. |
| MIC-020 | Community turnover along land-use gradients | D | BIO, GIS | Effects of management, soil type and disturbance. |
| MIC-021 | Spatial microbial community similarity / connectivity | D/I | BIO, GIS | Biogeographic patterns; similarity ≠ dispersal proof. |
| MIC-022 | Metatranscriptomic expression of functional genes | M/D/I | BIO | Active gene expression at sampling time; not direct process rate. |
| MIC-025 | Absolute microbial load | M/D | FIELD, LAB, BIO | Helps estimate microbial numbers rather than just relative shares. Recovery and gene copies per cell affect some methods. |
| MIC-026 | Soil fauna abundance/biomass | M | FIELD, LAB | Shows the number or mass of soil animals. Their roles depend on which groups are present, not just the total. |
| MIC-027 | Nematode trophic composition | D | FIELD, LAB, BIO | Helps describe the feeding groups of soil nematodes. Sampling and identification affect the picture of the soil food web. |
| MIC-028 | Metaproteomic functional profile | D/P | FIELD, LAB, BIO | Shows proteins detected in a microbial sample. Protein detection alone does not measure how quickly a process is running. |
| MIC-029 | Metabolomic profile | M/D | FIELD, LAB, BIO | Shows chemicals present in a biological sample. Their amounts reflect both production and use, not just one process rate. |
| MIC-030 | Microbial carbon-use efficiency | D/M | FIELD, LAB, BIO | Helps estimate how microbes divide carbon between growth and respiration. Results depend on the test conditions and substrate used. |

<a id="d06"></a>

### D06 — Biodiversity

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| BIO-001 | Species richness | D | FIELD, BIO, GIS | Number of detected taxa in defined sampling design. |
| BIO-002 | Species abundance / occupancy | M/I | FIELD, BIO, MODEL | Population status and distribution. |
| BIO-003 | Shannon / Simpson diversity | D | FIELD, BIO | Richness/evenness summary. |
| BIO-004 | Functional diversity | D | FIELD, BIO | Trait and ecological role diversity. |
| BIO-005 | Habitat area / quality | D/I | GIS, FIELD | Conservation condition. |
| BIO-010 | Invasive species presence / spread | M/D | FIELD, GIS, BIO | Ecological risk and management priorities. |
| BIO-011 | Indicator / threatened species occurrence | M | FIELD, BIO | Conservation planning. |
| BIO-012 | Acoustic biodiversity / soundscape indices | D/P | FIELD | Biological activity proxy; validate against taxa. |
| BIO-014 | Environmental-DNA taxon detection | M/D | BIO | Helps detect organisms from DNA left in water, soil or other samples. DNA may travel or remain after an organism has gone. |
| BIO-015 | Genetic diversity/population differentiation | D | BIO | Shows genetic variation within and between populations. Past population changes and sampling can also explain genetic differences. |
| BIO-016 | Population growth/recruitment/survival | M/I | BIO, MODEL | Helps track population growth, new individuals and survival. Movement and missed detections must also be considered. |
| BIO-017 | Community-weighted traits | D | BIO | Shows the typical traits of the organisms present, weighted by abundance. Missing trait data can bias the result. |
| BIO-018 | Freshwater macroinvertebrate composition | M/D | BIO | Helps assess aquatic communities and river condition. Habitat, season and the sampling method affect interpretation. |
| BIO-019 | Live coral cover/bleaching prevalence | M | GIS | Shows living coral cover or how common bleaching is. Habitat maps alone cannot establish either measure. |
| BIO-020 | Mangrove extent/condition | D/M | GIS | Shows mangrove extent and measured condition. Stable area does not necessarily mean unchanged health or function. |

<a id="d07"></a>

### D07 — Vegetation

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
| VEG-018 | Fraction of absorbed PAR | M/I | GIS, FIELD, MODEL | Shows the share of useful light vegetation absorbs. Absorbing light does not mean all of it becomes plant growth. |
| VEG-019 | Solar-induced chlorophyll fluorescence | D/P | FIELD | Can help study how vegetation responds during photosynthesis. The signal cannot be converted to carbon uptake without a suitable model. |
| VEG-020 | Leaf water potential/stomatal conductance | M | FIELD | Helps assess plant water status and control of water loss. Time of day, weather and plant type affect the response. |
| VEG-021 | Plant mortality/recruitment | M | GIS, FIELD | Shows plant deaths and new establishment. Seedlings may not survive to become mature plants. |
| VEG-022 | Root biomass/depth distribution | M | FIELD | Shows root mass and how deep roots occur. Root mass alone does not measure nutrient or water uptake. |
| TER-010 | Tree height | M/D | PC, FIELD | Stand development, biomass proxy. |
| TER-011 | Canopy volume | D | PC | Tree structure and productivity / biomass proxy. |
| TER-012 | Canopy gaps / crown cover | D | PC, GIS | Regeneration, light availability, habitat structure. |
| TER-013 | Vertical vegetation complexity | D | PC | Habitat layering and fuel structure. |
| HYD-002 | Normalised Difference Moisture Index (NDMI) | D/P | GIS | Vegetation canopy moisture proxy; index definitions vary. |
| DIS-012 | Hyperspectral material / vegetation trait signatures | D/P | GIS | Fine spectral differentiation; ground truth required. |

<a id="d08"></a>

### D08 — Ecological interactions

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| MIC-014 | Mycorrhizal community / colonisation | M/D/I | BIO, FIELD, LAB | Root symbiosis and nutrient exchange context. |
| MIC-015 | Rhizosphere-associated community structure | D | BIO | Plant–microbe relationships. |
| MIC-016 | Potential plant pathogens / beneficial taxa | I | BIO, LAB | Risk or beneficial associations; confirm function. |
| BIO-008 | Pollinator abundance / visitation | M | FIELD | Pollination activity / crop support. |
| BIO-009 | Predation / natural pest-control rate | M | FIELD | Biological control process. |
| BIO-013 | Food-web / interaction network structure | D/I | FIELD, BIO, MODEL | Ecological relationships; sampling bias matters. |
| INT-001 | Pollen deposition/pollen limitation | M | FIELD, LAB | Helps assess pollen delivery and whether extra pollen improves reproduction. Water and nutrient shortages can also limit seed production. |
| INT-002 | Fruit/seed set | M/D | FIELD, LAB | Shows how many flowers produce fruits or seeds. Pollination, weather, nutrition and damage all affect the result. |
| INT-003 | Herbivory rate | M | FIELD, LAB | Shows plant tissue eaten or damaged by herbivores. Existing damage may not reflect the current feeding rate. |
| INT-004 | Competition effect | D/M | FIELD, LAB | Tests whether neighbours reduce a plant's growth or reproduction. Finding species together does not prove competition. |
| INT-005 | Facilitation effect | D/M | FIELD, LAB | Tests whether one organism helps another grow or survive. The benefit can change with conditions and life stage. |
| INT-006 | Mycorrhizal nutrient transfer | M | FIELD, LAB, BIO | Tests nutrient transfer associated with root fungi. Fungal presence alone does not prove transfer or benefit to the plant. |
| INT-007 | Seed dispersal/removal | M | FIELD, LAB, BIO | Shows how seeds move or disappear. Removed seeds may be eaten rather than dispersed successfully. |
| INT-008 | Diet/trophic-link evidence | M/D | FIELD, LAB, BIO | Helps identify feeding relationships. DNA and isotope evidence need careful interpretation to estimate dietary contributions. |
| INT-009 | Disease suppression in bioassays | M | FIELD, LAB, BIO | Tests whether a soil or microbial treatment reduces disease. A successful laboratory test does not guarantee the same field result. |

<a id="d09"></a>

### D09 — Biogeochemical cycles

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| MIC-009 | Carbon-degradation gene/pathway potential | I | BIO | Potential decomposition capabilities, not measured flux. |
| MIC-010 | Nitrogen-fixation genetic potential | I | BIO | Presence/abundance of nitrogen fixation markers. |
| MIC-011 | Nitrification genetic potential | I | BIO | Potential ammonia oxidation / nitrification pathways. |
| MIC-012 | Denitrification genetic potential | I | BIO | Potential nitrate reduction pathways; not measured emissions. |
| MIC-013 | Phosphorus solubilisation / acquisition potential | I | BIO | Genetic potential for P mobilisation / uptake. |
| MIC-018 | Pollutant degradation gene potential | I | BIO | Potential biodegradation pathways. |
| MIC-023 | Nitrogen mineralisation / nitrification rate | M | LAB, FIELD | Actual process rate for comparison with genetic potential. |
| MIC-024 | Decomposition / litter mass-loss rate | M | FIELD, LAB | Realised ecosystem process rate. |
| FUN-002 | Carbon sequestration / stock change | D/I | LAB, FIELD, GIS, MODEL | Carbon dynamics; distinguish pools and fluxes. |
| FUN-003 | Nutrient retention / leaching | M/I | FIELD, LAB, MODEL | Pollution mitigation and nutrient cycling. |
| CYC-001 | Net ecosystem CO₂ exchange | M/D | FIELD, LAB | Shows net carbon dioxide exchange between an ecosystem and air. Harvests and other carbon movements are needed for a full carbon balance. |
| CYC-002 | N₂O flux | M | FIELD, LAB | Shows nitrous oxide released or taken up. Short-lived emission bursts can be missed by occasional measurements. |
| CYC-003 | Methane flux | M | FIELD, LAB | Shows net methane exchange. Production, consumption and gas movement all contribute to the measured result. |
| CYC-004 | Biological nitrogen-fixation rate | M | FIELD, LAB, BIO | Measures nitrogen added through biological fixation. Scaling a small test to a field introduces uncertainty. |
| CYC-005 | Denitrification rate | M | FIELD, LAB | Measures conversion of nitrate into nitrogen gases. Nitrous oxide alone does not show the whole process. |
| CYC-006 | Phosphorus mineralisation rate | M | FIELD, LAB | Measures release of inorganic phosphorus from organic material. Binding to soil and microbial uptake can affect the net result. |
| CYC-007 | Nitrogen/phosphorus balance | D/M | FIELD, LAB | Shows whether recorded nutrient inputs exceed outputs. Missing losses or inputs can distort the balance. |
| CYC-008 | Nutrient resorption efficiency | D/M | FIELD, LAB | Shows how much nutrient plants recover before leaves fall. Leaf mass changes and sampling time affect the estimate. |
| CYC-009 | Measured contaminant transformation | M | FIELD, LAB | Tests whether a pollutant is transformed. Disappearance alone may mean storage or movement, and breakdown products may still be harmful. |
| CYC-010 | Dissolved organic carbon export | D/M | FIELD, LAB | Shows carbon carried away in dissolved form by water. Concentration alone does not show the total amount exported. |

<a id="d10"></a>

### D10 — Landscape ecology

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| TER-001 | Elevation / digital terrain model | M/D | GIS, PC | Terrain reference for spatial analyses. |
| TER-002 | Slope gradient | D | GIS, PC | Erosion, access, land-use suitability. |
| TER-003 | Aspect / slope orientation | D | GIS, PC | Radiation, exposure, microclimate and planting. |
| TER-008 | Terrace geometry / terrace-wall condition | M/D | PC, GIS, FIELD | Historic terrace conservation and restoration. |
| TER-014 | Surface / canopy change between surveys | D | PC, GIS | Erosion, growth, disturbance or restoration monitoring. |
| BIO-006 | Landscape fragmentation / patch size | D | GIS | Habitat continuity and edge exposure. |
| BIO-007 | Habitat connectivity / corridor suitability | D/I | GIS, MODEL | Potential movement and dispersal pathways. |
| DIS-004 | Land-cover / land-use class | D/C | GIS, FIELD | Habitat and management context. |
| DIS-005 | Land-cover transition rate | D | GIS | Abandonment, urbanisation, reforestation. |
| FUN-008 | Field-margin / hedgerow length and condition | D | GIS, FIELD | Habitat, erosion control and landscape structure. |
| LAN-001 | Edge density/core habitat area | D | GIS | Shows habitat edges and remaining interior areas. Effects depend on the species and the distance at which edges matter. |
| LAN-002 | Landscape composition/diversity | D | GIS | Shows the mix of land or habitat types. A varied landscape does not automatically contain more species or work better ecologically. |
| LAN-003 | Riparian buffer extent/continuity | D | GIS, PC | Shows the width and continuity of vegetation beside water. Width alone does not prove effective nutrient filtering or flood protection. |
| LAN-004 | Barrier density/permeability | D/I/C | GIS, PC, MODEL | Shows obstacles to movement and how passable they may be. The same barrier can affect different species differently. |
| LAN-005 | Burned/converted area by habitat | D/C | GIS | Shows how much of each habitat has burned or changed use. Errors in habitat and event maps affect the totals. |
| LAN-006 | Topographic position/terrain curvature | D/C | GIS, PC | Helps describe ridges, hollows and curved slopes. Terrain shape suggests conditions but does not directly measure soil properties. |

<a id="d11"></a>

### D11 — Ecosystem functioning

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| FUN-001 | Primary productivity (GPP/NPP) | M/I | GIS, FIELD, MODEL | Ecosystem carbon uptake and biomass production. |
| FUN-012 | Composite soil-health index | D | LAB, FIELD, BIO | Multimetric condition assessment; specify exact framework. |
| FUN-013 | Ecosystem condition / integrity index | D/I | GIS, FIELD, MODEL | Multi-indicator ecological condition. |
| FUN-015 | Net ecosystem metabolism | D/M | FIELD | Shows the balance between ecosystem production and respiration. Water movement and gas exchange must be included in aquatic estimates. |
| FUN-016 | Trophic transfer efficiency | D/M | BIO | Helps estimate how much production passes between feeding levels. The ratio of standing biomass is not the same as energy-transfer efficiency. |
| FUN-017 | Ecosystem multifunctionality | D | FIELD | Combines evidence about several ecosystem functions. The selected functions and scoring method affect the result. |
| FUN-018 | Water purification/removal efficiency | D/M | FIELD | Shows how much of a named pollutant a system removes. Dilution or temporary storage should not be counted as permanent removal. |
| FUN-019 | Thermal regulation effect | D/M | GIS | Helps assess cooling associated with vegetation or habitat. Comparable weather and control locations are needed to isolate the effect. |
| FUN-020 | Soil-function deficit profile | D | FIELD | Shows which soil functions fall below chosen references. Different functions may show different strengths and weaknesses. |

<a id="d12"></a>

### D12 — Ecological resilience

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| MIC-017 | Drought / salinity stress-response gene potential | I | BIO | Community adaptation potential, not proven resilience. |
| DIS-001 | Normalised Burn Ratio (NBR) | D/P | GIS | Burn severity / disturbance mapping with calibration. |
| DIS-002 | Fire fuel load / vertical continuity | M/I | PC, GIS, FIELD | Wildfire behaviour potential. |
| DIS-003 | Fire occurrence / recurrence | D | GIS, FIELD | Disturbance history. |
| DIS-009 | Soil/vegetation recovery after disturbance | D/I | GIS, FIELD | Resilience and restoration tracking. |
| DIS-010 | Future climate exposure / suitability | I | MODEL, GIS | Scenario-based long-term planning. |
| RES-001 | Disturbance resistance | D | GIS | Shows how much a measured property changes during disturbance. Resistance may differ between species, soils and functions. |
| RES-002 | Recovery rate/time | D/I | GIS, MODEL | Shows how quickly a measured property returns towards a reference. The chosen baseline and survey timing affect recovery estimates. |
| RES-003 | Temporal variability/stability | D | GIS | Shows how much a property varies over time. A consistently degraded system can also have low variability. |
| RES-004 | Response diversity/asynchrony | D | BIO | Shows whether species respond differently over time. Different responses may help buffer change, but this needs actual time-series evidence. |
| RES-005 | Post-fire compositional/function recovery | D | GIS, BIO | Tracks species and functions after fire. Green cover can return before the original community or functions recover. |
| RES-006 | Early-warning time-series signals | D/I | FIELD | Flags patterns that might precede a major change. Noise and changing external conditions can produce false warnings. |
| RES-007 | Scenario sensitivity/model uncertainty | D/I | MODEL | Shows how predictions change with scenarios and assumptions. The tested models may not cover every source of uncertainty. |

<a id="d13"></a>

### D13 — Agricultural ecology

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| FUN-004 | Crop yield / yield stability | M/D | FIELD | Production and climate resilience. |
| FUN-005 | Groundcover persistence | D | GIS, FIELD | Soil protection through the year. |
| FUN-006 | Grazing pressure / stocking intensity | M/C | FIELD, GIS | Vegetation and soil management pressure. |
| FUN-007 | Irrigation / fertiliser / pesticide input | M/C | FIELD | Management pressure and resource efficiency. |
| AGR-001 | Agronomic nitrogen-use efficiency | D | FIELD | Helps compare crop output or response per nitrogen input. The chosen efficiency measure does not directly show nitrogen losses. |
| AGR-002 | Crop water productivity | D | FIELD | Shows crop output per amount of water supplied or used. Higher farm efficiency does not necessarily mean less basin-wide water consumption. |
| AGR-003 | Pesticide hazard/risk indicator | D/I/C | FIELD, MODEL | Helps screen pesticide hazards or modelled risks. Applied mass alone does not describe toxicity or actual exposure. |
| AGR-004 | Pest population/crop damage | M/C | FIELD | Shows pest numbers or crop damage. Trap counts do not directly tell us the likely yield loss. |
| AGR-005 | Crop disease incidence/severity | M/C | FIELD, BIO | Shows how common or severe crop disease is. Similar symptoms can have non-disease causes, so diagnosis matters. |
| AGR-006 | Crop/rotation diversity | D/C | FIELD | Shows the variety of crops and rotations. Diversity alone does not prove better yields, resilience or lower input use. |
| AGR-007 | Land equivalent ratio | D | FIELD | Compares land productivity of mixed crops with separate crops. The comparison needs suitable reference yields and comparable inputs. |
| AGR-008 | Harvest nutrient removal | D/M | FIELD | Shows nutrients removed in harvests. Other nutrient inputs and losses are needed for the whole farm balance. |
| AGR-009 | Forage utilisation/feed dependence | D/C | FIELD | Helps assess forage use and reliance on imported feed. Trampling, waste and impacts outside the farm also matter. |
| AGR-010 | Tillage/traffic disturbance intensity | M/C | FIELD | Shows recorded disturbance from machinery or tillage. Actual effects need soil measurements, not just counts of operations. |
| AGR-011 | Farm nutrient/energy balance | D | FIELD | Shows farm nutrient and energy inputs and outputs. Missing imports, losses and differences in products can change the comparison. |

<a id="d14"></a>

### D14 — Human–ecological systems

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| TER-015 | Built structures and landscape geometry | M/C | PC, GIS | Human occupation, material and intervention context. |
| FUN-009 | Human settlement / roads / infrastructure | C | GIS, PC | Accessibility, fragmentation and design context. |
| FUN-010 | Material / biomass availability | M/I | GIS, FIELD, MODEL | Potential local production and circular resource flows. |
| FUN-011 | Ecological footprint / resource demand | D/I | MODEL | Socio-ecological pressure at defined system boundary. |
| HUM-001 | Impervious surface fraction | D/C | GIS, MODEL | Shows how much ground is sealed. Runoff also depends on drainage connections and whether some built surfaces let water through. |
| HUM-002 | Land-use intensity | M/D/C | GIS, MODEL | Helps compare the intensity of recorded land use. Land-use names alone do not show the level of pressure. |
| HUM-003 | Material-flow account/circularity | D/C | MODEL | Shows material use and recycling. A high recycled share does not necessarily mean low overall resource demand. |
| HUM-004 | Energy demand/return | M/D/C | MODEL | Shows energy demand or energy returned for the investment. Energy sources and the services produced affect fair comparisons. |
| HUM-005 | Water withdrawal/consumption | M/D/C | MODEL | Shows water taken from sources and water not returned. Withdrawal and consumption have different effects on water availability. |
| HUM-006 | Lifecycle greenhouse-gas intensity | D/I/C | MODEL | Helps compare climate emissions per product or service. Results depend on which lifecycle stages and emissions are included. |
| HUM-007 | Artificial light at night | M/C | MODEL | Shows artificial light exposure at night. Satellite brightness may differ from the light experienced by organisms. |
| HUM-008 | Anthropogenic noise exposure | M/C | MODEL | Shows exposure to human-made noise. Different species hear different frequencies and may respond differently. |
| HUM-009 | Resource import dependence | D/C | MODEL | Shows reliance on resources from outside an area. Import dependence alone does not establish environmental sustainability. |

<a id="d15"></a>

### D15 — Planetary and regional boundaries

| EII ID | Variable / indicator | Kind | Main approaches | Typical interpretation / use |
|---|---|---|---|---|
| FUN-014 | Planetary / regional boundary exceedance | D/I | MODEL | System-level sustainability constraints; scale dependent. |
| PB-001 | Atmospheric CO₂/radiative forcing control variables | M/I/C | MODEL | Helps compare global climate pressures with a stated framework. Local carbon dioxide readings are not a global boundary measure. |
| PB-002 | Biosphere genetic/functional integrity controls | I/C | MODEL | Helps assess large-scale loss of biodiversity and ecosystem function. Local species counts cannot represent the whole global picture. |
| PB-003 | Biogeochemical N/P control variables | D/I/C | MODEL | Helps assess large-scale human changes to nitrogen and phosphorus flows. A farm nutrient surplus is a different measure. |
| PB-004 | Freshwater blue/green change controls | D/I/C | GIS, MODEL | Helps assess large-scale changes in river flows and soil moisture. Water withdrawals and drought indices measure different things. |
| PB-005 | Land-system change control variables | D/C | GIS, MODEL | Helps assess changes in forest or biome extent. Tree cover alone does not show native forest condition. |
| PB-006 | Stratospheric ozone | M/D | MODEL | Helps assess the ozone layer's protection. Ozone near the ground is a different environmental issue. |
| PB-007 | Novel-entity releases/assessment coverage | D/C | MODEL | Helps track releases of new chemicals and how well they are assessed. No single safe concentration applies to all substances. |
| PB-008 | Ocean acidification control variable | D/C | GIS, MODEL | Helps assess ocean chemistry affecting shell formation. Local pH alone cannot establish the global boundary measure. |
| PB-009 | Atmospheric aerosol loading control variable | D/C | MODEL | Helps assess large-scale airborne particle effects. Particle mass and their effect on sunlight are different measures. |
| PB-010 | Regional ecological threshold departure | D/I | MODEL | Shows departure from a locally justified ecological threshold. Global thresholds cannot be transferred automatically to a region. |

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

**Historical material only:** This pasted crosswalk is retained verbatim for preservation. It is excluded from the active EII indicator inventory and does not establish current interoperability or verified programme indicators.

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

## 9. Scientific domain classification — consolidated edition

Each indicator has one home domain. This index preserves the expanded 15-domain classification without duplicating indicator records.

| Domain | Scope | Indicator ranges | Records |
|---|---|---|---:|
| D01 | Atmosphere and climate | TER-004, HYD-003, DIS-006–008, ATM-001–009 | 14 |
| D02 | Hydrology | TER-005–006, HYD-001, HYD-006–022, DIS-011 | 21 |
| D03 | Soil physics | TER-007, TER-009, HYD-004–005, SOI-001–004, SOI-011–012, SOI-014–017 | 14 |
| D04 | Soil chemistry | SOI-005–009, SOI-013, SOI-018–023 | 12 |
| D05 | Soil biology | SOI-010, MIC-001–008, MIC-019–022, MIC-025–030 | 19 |
| D06 | Biodiversity | BIO-001–005, BIO-010–012, BIO-014–020 | 15 |
| D07 | Vegetation | VEG-001–022, TER-010–013, HYD-002, DIS-012 | 28 |
| D08 | Ecological interactions | MIC-014–016, BIO-008–009, BIO-013, INT-001–009 | 15 |
| D09 | Biogeochemical cycles | MIC-009–013, MIC-018, MIC-023–024, FUN-002–003, CYC-001–010 | 20 |
| D10 | Landscape ecology | TER-001–003, TER-008, TER-014, BIO-006–007, DIS-004–005, FUN-008, LAN-001–006 | 16 |
| D11 | Ecosystem functioning | FUN-001, FUN-012–013, FUN-015–020 | 9 |
| D12 | Ecological resilience | MIC-017, DIS-001–003, DIS-009–010, RES-001–007 | 13 |
| D13 | Agricultural ecology | FUN-004–007, AGR-001–011 | 15 |
| D14 | Human–ecological systems | TER-015, FUN-009–011, HUM-001–009 | 13 |
| D15 | Planetary and regional boundaries | FUN-014, PB-001–010 | 11 |

## 10. Scientific references — consolidated edition

These references support the stated definitions or framework connections. Specialist entries without an individual protocol citation remain working definitions. Specific inference limits are retained beside each indicator. Framework-defined thresholds require a stated version and regional justification.

| Key | Primary / authoritative reference | Documentary scope |
|---|---|---|
| R01 | [USGS — Landsat Enhanced Vegetation Index](https://www.usgs.gov/landsat-missions/landsat-enhanced-vegetation-index) | Standard EVI formula and band/scaling context; documentary check, not local validation. Relevant entries: Enhanced vegetation index (EVI). |
| R02 | [USGS — Landsat Normalized Burn Ratio](https://www.usgs.gov/landsat-missions/landsat-normalized-burn-ratio) | NBR formula and product context; not universal severity thresholds. Relevant entries: Burn ratio (NBR). |
| R03 | [FAO — SOC stock calculation sub-protocol, Annex 4](https://www.fao.org/fileadmin/user_upload/GSP/MRV/GSP_MRV_Protocol_A4_EN_002.pdf) | SOC stock inputs and compatible density/coarse-fragment basis. Relevant entries: Soil organic carbon. |
| R04 | [EMBL-EBI — MGnify](https://www.ebi.ac.uk/about/teams/microbiome-informatics/mgnify/) | Taxonomic and functional-potential outputs, versioned pipelines; no project dataset accession bound. Relevant entries: Bacterial community, Archaeal community, Fungal community, Protist community, Carbon-breakdown genes, Microbial gene expression. |
| R05 | [Vandeputte et al. (2017) — Quantitative microbiome profiling](https://www.nature.com/articles/nature24460) | Primary study on relative versus quantitative abundance; gut study supports the compositional measurement caution, not soil-specific effect claims. Relevant entries: Bacterial community, Fungal:bacterial ratio, Microbial numbers. |
| R06 | [GEO BON — EBV strategy v2](https://geobon.org/downloads/governance-documents/Essential_Biodiversity_Variable_Strategy_v2.pdf) | Biodiversity observation framework; no claim that EII entries are certified EBVs. Relevant entries: Domain 6. |
| R07 | [WMO/GCOS — About Essential Climate Variables](https://gcos.wmo.int/site/global-climate-observing-system-gcos/essential-climate-variables/about-essential-climate-variables) | Climate observation framework; no one-to-one ECV crosswalk established. Relevant entries: Domain 1. |
| R08 | [UN — SEEA Ecosystem Accounting](https://seea.un.org/en/methodology/ecosystem-accounting) | Extent/condition/function accounting framework; EII composites remain locally specified. Relevant entries: Domain 11. |
| R09 | [Richardson et al. (2023) — Earth beyond six of nine planetary boundaries](https://doi.org/10.1126/sciadv.adh2458) | Historical framework reference for control-variable families; not a current boundary-status assessment or a local allocation method. Relevant entries: Domain 15. |
| R11 | [USGS — Normalized Difference Moisture Index](https://www.usgs.gov/landsat-missions/normalized-difference-moisture-index) | NIR/SWIR vegetation-moisture contrast and product context. Relevant entries: Canopy moisture index (NDMI). |
| R12 | [USGS — Scaling Landsat Collection 2 Level 2 Data](https://www.usgs.gov/software/scaling-landsat-collection-2-level-2-data) | Reflectance scaling before vegetation-index calculation and thermal conversion. Relevant entries: Vegetation greenness (NDVI). |
| R10 | [USGS — Dissolved Oxygen and Water](https://www.usgs.gov/water-science-school/science/dissolved-oxygen-and-water) | Dissolved oxygen as a water-quality variable and ecological context. Relevant entries: Dissolved oxygen. |


### Consolidated edition history

- **0.5.0 — 2026-10-21:** Reorganised all 235 unchanged scientific rows under D01–D15 and added the linked Domain Index. Adopted EII Domain Taxonomy v1.0.0; preserved existing primary/secondary assignments and A–P migration provenance in the machine reference. Scientific descriptions, source-edition material and references are unchanged. DRM v1.0.0 conformance remains unverified.
- **0.4.0 — 2026-10-19:** Preserved the supplied v0.1.0 presentation and all original indicator rows; added 115 later indicators for 235 unique records; retained the 15-domain classification and later scientific references. The pasted programme crosswalk is historical material only.
