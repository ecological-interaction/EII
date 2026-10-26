# EII — Ecological Indicator Inventory

**Scientific Register document version:** 0.6.0 · Work in Progress — Academic Research Resource. Jonathan Minchin · Ecological Interaction · [ORCID](https://orcid.org/0000-0001-8152-1796). [Citation](CITATION.cff).

[Reading Key](#reading-key) · [Domain Index](#domain-index) · [Canonical and display details](#canonical-and-display-details) · [Historical supplements](#historical-scientific-supplements) · [Research Protocol](EII_Research_Protocol.md).

## Reading Key

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




## Canonical and display details

These current structured-record definitions remain separate from the concise five-column presentation and the labelled earlier source editions below. Supporting indicators are interpretive relationships, not calculation inputs. No new verification is implied.

<a id="veg-001"></a>

### EII:VEG-001 — Normalised Difference Vegetation Index (NDVI)

**Definition:** NDVI is the normalised contrast between near-infrared and red reflectance.

**Direct observations / derivation:** (NIR-red)/(NIR+red), dimensionless, from masked surface-reflectance bands.

**Inference and limits:** Supports comparison of green vegetation and seasonal vigour; saturation, soil background and species prevent diagnosis of health or biomass alone.

**Display label:** Vegetation greenness (NDVI)

**Display measurement:** Satellite or multispectral drone imagery. (NIR-red)/(NIR+red), dimensionless, from masked surface-reflectance bands.

**Display interpretation:** Helps compare how green vegetation is and how it changes through the seasons. Greenness alone does not prove plant health.

**Measurement origin:** Satellite or multispectral drone imagery

**Supporting indicators:** [EII:VEG-011](#veg-011); [EII:VEG-012](#veg-012); [EII:VEG-013](#veg-013); [EII:HYD-001](#hyd-001)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["opt"]`

**Scientific reference keys:** `["R12"]`

**Display source keys:** RS001, RS002

**Research status:** curated_working_definition

**Review scope:** specific_documentary_aspects_only

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-001","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["opt"],"refs":["R12"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** NDVI is the normalised contrast between near-infrared and red reflectance.
- **Direct observations / derivation:** (NIR-red)/(NIR+red), dimensionless, from masked surface-reflectance bands.
- **Inference and limits:** Supports comparison of green vegetation and seasonal vigour; saturation, soil background and species prevent diagnosis of health or biomass alone.
- **Supporting indicators:** [EII:VEG-011](#veg-011), [EII:VEG-012](#veg-012), [EII:VEG-013](#veg-013), [EII:HYD-001](#hyd-001).

<a id="veg-002"></a>

### EII:VEG-002 — Green Normalised Difference Vegetation Index (GNDVI)

**Definition:** GNDVI substitutes green for red in a normalised vegetation contrast.

**Direct observations / derivation:** (NIR-green)/(NIR+green), dimensionless reflectance ratio.

**Inference and limits:** Can track chlorophyll-related variation after crop-specific calibration; canopy structure and illumination confound interpretation.

**Display label:** Green vegetation index (GNDVI)

**Display measurement:** Satellite or multispectral drone imagery. (NIR-green)/(NIR+green), dimensionless reflectance ratio.

**Display interpretation:** Can help track changes in leaf pigments. Plant type and the amount of leaf cover also affect the result.

**Measurement origin:** Satellite or multispectral drone imagery

**Supporting indicators:** [EII:VEG-013](#veg-013); [EII:VEG-011](#veg-011); [EII:SOI-008](#soi-008)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["opt"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS001, RS002

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-002","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["opt"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** GNDVI substitutes green for red in a normalised vegetation contrast.
- **Direct observations / derivation:** (NIR-green)/(NIR+green), dimensionless reflectance ratio.
- **Inference and limits:** Can track chlorophyll-related variation after crop-specific calibration; canopy structure and illumination confound interpretation.
- **Supporting indicators:** [EII:VEG-013](#veg-013), [EII:VEG-011](#veg-011), [EII:SOI-008](#soi-008).

<a id="veg-003"></a>

### EII:VEG-003 — Normalised Difference Red Edge Index (NDRE)

**Definition:** NDRE contrasts near-infrared with red-edge reflectance.

**Direct observations / derivation:** (NIR-rededge)/(NIR+rededge), dimensionless; record exact band wavelengths.

**Inference and limits:** Supports chlorophyll-related canopy comparisons; sensor band choice, leaf area and species affect response.

**Display label:** Red-edge vegetation index (NDRE)

**Display measurement:** Satellite or multispectral drone imagery. (NIR-rededge)/(NIR+rededge), dimensionless; record exact band wavelengths.

**Display interpretation:** Can help compare leaf pigment levels in a canopy. Different sensors and plant types need careful comparison.

**Measurement origin:** Satellite or multispectral drone imagery

**Supporting indicators:** [EII:VEG-013](#veg-013); [EII:VEG-011](#veg-011); [EII:VEG-017](#veg-017)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["rededge"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS001

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-003","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["rededge"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** NDRE contrasts near-infrared with red-edge reflectance.
- **Direct observations / derivation:** (NIR-rededge)/(NIR+rededge), dimensionless; record exact band wavelengths.
- **Inference and limits:** Supports chlorophyll-related canopy comparisons; sensor band choice, leaf area and species affect response.
- **Supporting indicators:** [EII:VEG-013](#veg-013), [EII:VEG-011](#veg-011), [EII:VEG-017](#veg-017).

<a id="veg-004"></a>

### EII:VEG-004 — Soil Adjusted Vegetation Index (SAVI)

**Definition:** SAVI adjusts a red–NIR vegetation contrast for soil background.

**Direct observations / derivation:** (1+L)(NIR-red)/(NIR+red+L), dimensionless; declare L and reflectance scaling.

**Inference and limits:** Improves comparison where vegetation is sparse; adjustment does not remove all soil or atmospheric effects.

**Display label:** Soil-adjusted vegetation index (SAVI)

**Display measurement:** Satellite or multispectral drone imagery. (1+L)(NIR-red)/(NIR+red+L), dimensionless; declare L and reflectance scaling.

**Display interpretation:** Helps identify vegetation where bare soil is visible. Soil colour can still affect the result.

**Measurement origin:** Satellite or multispectral drone imagery

**Supporting indicators:** [EII:VEG-012](#veg-012); [EII:VEG-001](#veg-001); [EII:SOI-001](#soi-001)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["opt"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS001, RS002

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-004","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["opt"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** SAVI adjusts a red–NIR vegetation contrast for soil background.
- **Direct observations / derivation:** (1+L)(NIR-red)/(NIR+red+L), dimensionless; declare L and reflectance scaling.
- **Inference and limits:** Improves comparison where vegetation is sparse; adjustment does not remove all soil or atmospheric effects.
- **Supporting indicators:** [EII:VEG-012](#veg-012), [EII:VEG-001](#veg-001), [EII:SOI-001](#soi-001).

<a id="veg-005"></a>

### EII:VEG-005 — Enhanced Vegetation Index (EVI)

**Definition:** EVI uses red, blue and NIR bands with background and atmospheric resistance terms.

**Direct observations / derivation:** 2.5(NIR-red)/(NIR+6red-7.5blue+1), dimensionless, for the standard three-band form.

**Inference and limits:** Supports greenness comparisons in dense vegetation; cloud, aerosols and processing still matter.

**Display label:** Enhanced vegetation index (EVI)

**Display measurement:** Satellite or multispectral drone imagery. 2.5(NIR-red)/(NIR+6red-7.5blue+1), dimensionless, for the standard three-band form.

**Display interpretation:** Helps compare vegetation greenness, including dense canopies. Clouds and image processing can still affect it.

**Measurement origin:** Satellite or multispectral drone imagery

**Supporting indicators:** [EII:VEG-001](#veg-001); [EII:VEG-011](#veg-011); [EII:VEG-012](#veg-012)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["opt"]`

**Scientific reference keys:** `["R01"]`

**Display source keys:** RS001, RS002

**Research status:** curated_working_definition

**Review scope:** specific_documentary_aspects_only

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-005","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["opt"],"refs":["R01"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** EVI uses red, blue and NIR bands with background and atmospheric resistance terms.
- **Direct observations / derivation:** 2.5(NIR-red)/(NIR+6red-7.5blue+1), dimensionless, for the standard three-band form.
- **Inference and limits:** Supports greenness comparisons in dense vegetation; cloud, aerosols and processing still matter.
- **Supporting indicators:** [EII:VEG-001](#veg-001), [EII:VEG-011](#veg-011), [EII:VEG-012](#veg-012).

<a id="veg-006"></a>

### EII:VEG-006 — Green–Red Vegetation Index (GRVI)

**Definition:** GRVI is the normalised green–red contrast.

**Direct observations / derivation:** (green-red)/(green+red), dimensionless; calibrated RGB preferred.

**Inference and limits:** Indicates visible greenness, not photosynthesis directly; shade and camera colour processing confound comparisons.

**Display label:** Green–red vegetation index (GRVI)

**Display measurement:** Drone or ground-camera photographs. (green-red)/(green+red), dimensionless; calibrated RGB preferred.

**Display interpretation:** Helps identify green vegetation in colour images. Shadows and camera settings can change the result.

**Measurement origin:** Drone or ground-camera photographs

**Supporting indicators:** [EII:VEG-012](#veg-012); [EII:VEG-013](#veg-013); [EII:VEG-001](#veg-001)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["rgb"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-006","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["rgb"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** GRVI is the normalised green–red contrast.
- **Direct observations / derivation:** (green-red)/(green+red), dimensionless; calibrated RGB preferred.
- **Inference and limits:** Indicates visible greenness, not photosynthesis directly; shade and camera colour processing confound comparisons.
- **Supporting indicators:** [EII:VEG-012](#veg-012), [EII:VEG-013](#veg-013), [EII:VEG-001](#veg-001).

<a id="veg-007"></a>

### EII:VEG-007 — Excess Green (ExG)

**Definition:** ExG enhances green relative to red and blue for vegetation segmentation.

**Direct observations / derivation:** 2g-r-b using normalised RGB channels, dimensionless; record normalisation and threshold.

**Inference and limits:** Supports green-cover segmentation; threshold accuracy depends on illumination and background.

**Display label:** Excess green (ExG)

**Display measurement:** Drone or ground-camera photographs. 2g-r-b using normalised RGB channels, dimensionless; record normalisation and threshold.

**Display interpretation:** Helps separate green plants from their background in photographs. Lighting affects how well this works.

**Measurement origin:** Drone or ground-camera photographs

**Supporting indicators:** [EII:VEG-012](#veg-012); [EII:VEG-006](#veg-006); [EII:VEG-017](#veg-017)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["rgb"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-007","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["rgb"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** ExG enhances green relative to red and blue for vegetation segmentation.
- **Direct observations / derivation:** 2g-r-b using normalised RGB channels, dimensionless; record normalisation and threshold.
- **Inference and limits:** Supports green-cover segmentation; threshold accuracy depends on illumination and background.
- **Supporting indicators:** [EII:VEG-012](#veg-012), [EII:VEG-006](#veg-006), [EII:VEG-017](#veg-017).

<a id="veg-008"></a>

### EII:VEG-008 — Visible Atmospherically Resistant Index (VARI)

**Definition:** VARI uses a visible-band contrast with a blue-band correction.

**Direct observations / derivation:** (green-red)/(green+red-blue), dimensionless; mask near-zero denominators.

**Inference and limits:** Supports visible green-cover comparisons; atmospheric resistance is limited and does not guarantee radiometric comparability.

**Display label:** Visible vegetation index (VARI)

**Display measurement:** Drone or ground-camera photographs. (green-red)/(green+red-blue), dimensionless; mask near-zero denominators.

**Display interpretation:** Helps estimate green cover from colour images. Different light and atmospheric conditions can still affect it.

**Measurement origin:** Drone or ground-camera photographs

**Supporting indicators:** [EII:VEG-012](#veg-012); [EII:VEG-006](#veg-006); [EII:VEG-001](#veg-001)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["rgb"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-008","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["rgb"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** VARI uses a visible-band contrast with a blue-band correction.
- **Direct observations / derivation:** (green-red)/(green+red-blue), dimensionless; mask near-zero denominators.
- **Inference and limits:** Supports visible green-cover comparisons; atmospheric resistance is limited and does not guarantee radiometric comparability.
- **Supporting indicators:** [EII:VEG-012](#veg-012), [EII:VEG-006](#veg-006), [EII:VEG-001](#veg-001).

<a id="veg-009"></a>

### EII:VEG-009 — Green Leaf Index (GLI)

**Definition:** GLI enhances green relative to the other visible channels.

**Direct observations / derivation:** (2green-red-blue)/(2green+red+blue), dimensionless.

**Inference and limits:** Supports foliage segmentation; camera calibration and shadow determine accuracy.

**Display label:** Green leaf index (GLI)

**Display measurement:** Drone or ground-camera photographs. (2green-red-blue)/(2green+red+blue), dimensionless.

**Display interpretation:** Helps identify green leaves in photographs. Shadows and camera calibration matter.

**Measurement origin:** Drone or ground-camera photographs

**Supporting indicators:** [EII:VEG-012](#veg-012); [EII:VEG-007](#veg-007); [EII:VEG-017](#veg-017)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["rgb"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-009","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["rgb"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** GLI enhances green relative to the other visible channels.
- **Direct observations / derivation:** (2green-red-blue)/(2green+red+blue), dimensionless.
- **Inference and limits:** Supports foliage segmentation; camera calibration and shadow determine accuracy.
- **Supporting indicators:** [EII:VEG-012](#veg-012), [EII:VEG-007](#veg-007), [EII:VEG-017](#veg-017).

<a id="veg-010"></a>

### EII:VEG-010 — Red–Green–Blue Vegetation Index (RGBVI)

**Definition:** RGBVI contrasts squared green against red–blue products.

**Direct observations / derivation:** (green²-red×blue)/(green²+red×blue), dimensionless; record channel treatment.

**Inference and limits:** Can distinguish vegetation from backgrounds; not a direct chlorophyll or productivity measurement.

**Display label:** RGB vegetation index (RGBVI)

**Display measurement:** Drone or ground-camera photographs. (green²-red×blue)/(green²+red×blue), dimensionless; record channel treatment.

**Display interpretation:** Helps distinguish vegetation from other surfaces in colour images. It does not directly measure plant growth or leaf pigments.

**Measurement origin:** Drone or ground-camera photographs

**Supporting indicators:** [EII:VEG-012](#veg-012); [EII:VEG-013](#veg-013); [EII:VEG-001](#veg-001)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["rgb"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-010","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["rgb"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** RGBVI contrasts squared green against red–blue products.
- **Direct observations / derivation:** (green²-red×blue)/(green²+red×blue), dimensionless; record channel treatment.
- **Inference and limits:** Can distinguish vegetation from backgrounds; not a direct chlorophyll or productivity measurement.
- **Supporting indicators:** [EII:VEG-012](#veg-012), [EII:VEG-013](#veg-013), [EII:VEG-001](#veg-001).

<a id="veg-011"></a>

### EII:VEG-011 — Leaf Area Index (LAI)

**Definition:** LAI is leaf area per unit ground area, with convention declared.

**Direct observations / derivation:** Leaf area and ground area, m²/m²; destructive sampling, optical gap inversion or calibrated remote estimation.

**Inference and limits:** Represents canopy development and potential light interception; clumping and woody material bias optical estimates.

**Display label:** Leaf Area Index (LAI)

**Display measurement:** Field leaf measurements or calibrated satellite estimates. Leaf area and ground area, m²/m²; destructive sampling, optical gap inversion or calibrated remote estimation.

**Display interpretation:** Shows how much leaf area a canopy has, helping us understand light interception. Overlapping leaves can make estimates less accurate.

**Measurement origin:** Field leaf measurements or calibrated satellite estimates

**Supporting indicators:** [EII:VEG-012](#veg-012); [EII:TER-013](#ter-013); [EII:VEG-014](#veg-014)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["veg"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS001, RS002

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-011","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","modelled"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["veg"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** LAI is leaf area per unit ground area, with convention declared.
- **Direct observations / derivation:** Leaf area and ground area, m²/m²; destructive sampling, optical gap inversion or calibrated remote estimation.
- **Inference and limits:** Represents canopy development and potential light interception; clumping and woody material bias optical estimates.
- **Supporting indicators:** [EII:VEG-012](#veg-012), [EII:TER-013](#ter-013), [EII:VEG-014](#veg-014).

<a id="veg-012"></a>

### EII:VEG-012 — Fractional vegetation / ground cover

**Definition:** Fractional cover is the proportion of a defined surface occupied by vegetation.

**Direct observations / derivation:** Point-intercept counts or classified pixels, fraction or %; distinguish green, total, ground and crown cover.

**Inference and limits:** Supports assessment of soil exposure and habitat structure; equal cover need not imply equal biomass or diversity.

**Display label:** Vegetation cover

**Display measurement:** Field observations, drone images or satellite maps. Point-intercept counts or classified pixels, fraction or %; distinguish green, total, ground and crown cover.

**Display interpretation:** Shows how much ground vegetation covers. This helps assess exposed soil, but cover alone does not reveal plant diversity or biomass.

**Measurement origin:** Field observations, drone images or satellite maps

**Supporting indicators:** [EII:VEG-017](#veg-017); [EII:SOI-012](#soi-012); [EII:FUN-005](#fun-005)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["observed", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["veg"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS001, RS002

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-012","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["observed","derived"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["veg"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fractional cover is the proportion of a defined surface occupied by vegetation.
- **Direct observations / derivation:** Point-intercept counts or classified pixels, fraction or %; distinguish green, total, ground and crown cover.
- **Inference and limits:** Supports assessment of soil exposure and habitat structure; equal cover need not imply equal biomass or diversity.
- **Supporting indicators:** [EII:VEG-017](#veg-017), [EII:SOI-012](#soi-012), [EII:FUN-005](#fun-005).

<a id="veg-013"></a>

### EII:VEG-013 — Canopy chlorophyll content

**Definition:** Canopy chlorophyll content describes chlorophyll quantity on a declared leaf or ground-area basis.

**Direct observations / derivation:** Pigment extraction, calibrated chlorophyll meters or spectral inversion, mg/m²; meter units require calibration.

**Inference and limits:** Supports assessment of pigment status; nutrient limitation, age, stress and species can produce similar changes.

**Display label:** Chlorophyll content

**Display measurement:** Leaf laboratory tests, field meters or calibrated imagery. Pigment extraction, calibrated chlorophyll meters or spectral inversion, mg/m²; meter units require calibration.

**Display interpretation:** Helps assess the amount of green pigment in leaves. Differences can reflect nutrition, stress, leaf age or plant type.

**Measurement origin:** Leaf laboratory tests, field meters or calibrated imagery

**Supporting indicators:** [EII:VEG-011](#veg-011); [EII:SOI-008](#soi-008); [EII:VEG-015](#veg-015)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["veg"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS001, RS002

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-013","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","modelled"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["veg"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Canopy chlorophyll content describes chlorophyll quantity on a declared leaf or ground-area basis.
- **Direct observations / derivation:** Pigment extraction, calibrated chlorophyll meters or spectral inversion, mg/m²; meter units require calibration.
- **Inference and limits:** Supports assessment of pigment status; nutrient limitation, age, stress and species can produce similar changes.
- **Supporting indicators:** [EII:VEG-011](#veg-011), [EII:SOI-008](#soi-008), [EII:VEG-015](#veg-015).

<a id="veg-014"></a>

### EII:VEG-014 — Above-ground biomass

**Definition:** Above-ground biomass is dry living plant mass above the soil surface.

**Direct observations / derivation:** Harvest dry mass, kg/m² or Mg/ha; inventories and LiDAR require validated allometry.

**Inference and limits:** Supports carbon-pool and fuel estimates; water content, dead biomass and allometric uncertainty must be separated.

**Display label:** Above-ground biomass

**Display measurement:** Field harvests and tree surveys, with calibrated LiDAR or imagery. Harvest dry mass, kg/m² or Mg/ha; inventories and LiDAR require validated allometry.

**Display interpretation:** Shows how much plant material is present above ground. Carbon and fire-fuel estimates need information about plant type and dry mass.

**Measurement origin:** Field harvests and tree surveys, with calibrated LiDAR or imagery

**Supporting indicators:** [EII:TER-010](#ter-010); [EII:TER-011](#ter-011); [EII:VEG-017](#veg-017); [EII:DIS-002](#dis-002)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["veg"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS001, RS002

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-014","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","modelled"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["veg"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Above-ground biomass is dry living plant mass above the soil surface.
- **Direct observations / derivation:** Harvest dry mass, kg/m² or Mg/ha; inventories and LiDAR require validated allometry.
- **Inference and limits:** Supports carbon-pool and fuel estimates; water content, dead biomass and allometric uncertainty must be separated.
- **Supporting indicators:** [EII:TER-010](#ter-010), [EII:TER-011](#ter-011), [EII:VEG-017](#veg-017), [EII:DIS-002](#dis-002).

<a id="veg-015"></a>

### EII:VEG-015 — Plant water stress / canopy temperature anomaly

**Definition:** Canopy temperature anomaly compares canopy temperature with air or a reference canopy.

**Direct observations / derivation:** Thermal radiance converted to temperature and reference temperature, °C difference; stress indices require stated wet/dry baselines.

**Inference and limits:** May indicate reduced transpiration or heat exposure; radiation, wind and architecture also affect temperature.

**Display label:** Plant water stress and canopy temperature

**Display measurement:** Thermal satellite or camera images with weather sensors. Thermal radiance converted to temperature and reference temperature, °C difference; stress indices require stated wet/dry baselines.

**Display interpretation:** A warmer canopy can be a sign of reduced cooling through water loss. Sunlight and wind can also change canopy temperature.

**Measurement origin:** Thermal satellite or camera images with weather sensors

**Supporting indicators:** [EII:HYD-001](#hyd-001); [EII:HYD-012](#hyd-012); [EII:ATM-003](#atm-003); [EII:ATM-005](#atm-005)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["canopy_temperature_anomaly", "validated_water_stress_index"]`

**Record type:** family

**Candidate source routes:** `["thermal", "iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS002; IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-015","domain":"D07","related_domains":[],"record_type":"family","variants":["canopy_temperature_anomaly","validated_water_stress_index"],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["thermal","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Canopy temperature anomaly compares canopy temperature with air or a reference canopy.
- **Direct observations / derivation:** Thermal radiance converted to temperature and reference temperature, °C difference; stress indices require stated wet/dry baselines.
- **Inference and limits:** May indicate reduced transpiration or heat exposure; radiation, wind and architecture also affect temperature.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:HYD-012](#hyd-012), [EII:ATM-003](#atm-003), [EII:ATM-005](#atm-005).

<a id="veg-016"></a>

### EII:VEG-016 — Phenology / green-up / senescence dates

**Definition:** Phenological dates locate seasonal events such as green-up and senescence.

**Direct observations / derivation:** Repeated observations or fitted vegetation-index curves, day-of-year and duration in days; declare event threshold.

**Inference and limits:** Reveals seasonal shifts; cloud gaps, mixed vegetation and crop calendars can mimic climatic responses.

**Display label:** Seasonal plant timing

**Display measurement:** Repeated field observations or satellite images. Repeated observations or fitted vegetation-index curves, day-of-year and duration in days; declare event threshold.

**Display interpretation:** Shows when plants start growing or lose their leaves. Changes may reflect weather, plant type or farming schedules.

**Measurement origin:** Repeated field observations or satellite images

**Supporting indicators:** [EII:VEG-001](#veg-001); [EII:DIS-006](#dis-006); [EII:VEG-017](#veg-017)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["observed", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["green_up_date", "senescence_date", "season_duration"]`

**Record type:** family

**Candidate source routes:** `["veg"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS001, RS002

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-016","domain":"D07","related_domains":[],"record_type":"family","variants":["green_up_date","senescence_date","season_duration"],"secondary":["observed","derived"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["veg"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Phenological dates locate seasonal events such as green-up and senescence.
- **Direct observations / derivation:** Repeated observations or fitted vegetation-index curves, day-of-year and duration in days; declare event threshold.
- **Inference and limits:** Reveals seasonal shifts; cloud gaps, mixed vegetation and crop calendars can mimic climatic responses.
- **Supporting indicators:** [EII:VEG-001](#veg-001), [EII:DIS-006](#dis-006), [EII:VEG-017](#veg-017).

<a id="veg-017"></a>

### EII:VEG-017 — Species / cultivar composition

**Definition:** Species/cultivar composition records plant identity and relative representation.

**Direct observations / derivation:** Botanical counts, cover estimates or validated molecular assignments, taxa and proportions.

**Inference and limits:** Supports community and crop comparisons; remote classes rarely resolve cultivars without validation.

**Display label:** Plant species and crop varieties

**Display measurement:** Field plant surveys, crop records or validated DNA tests. Botanical counts, cover estimates or validated molecular assignments, taxa and proportions.

**Display interpretation:** Shows which plants or crop varieties are present. This helps interpret differences in habitat, growth and resource needs.

**Measurement origin:** Field plant surveys, crop records or validated DNA tests

**Supporting indicators:** [EII:BIO-001](#bio-001); [EII:BIO-004](#bio-004); [EII:VEG-016](#veg-016)

**Primary domain:** D07

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["observed", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["species_composition", "cultivar_composition"]`

**Record type:** family

**Candidate source routes:** `["veg", "bio", "amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS001, RS002; Bioinformatics (future); AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-017","domain":"D07","related_domains":["D13"],"record_type":"family","variants":["species_composition","cultivar_composition"],"secondary":["observed","derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["veg","bio","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Species/cultivar composition records plant identity and relative representation.
- **Direct observations / derivation:** Botanical counts, cover estimates or validated molecular assignments, taxa and proportions.
- **Inference and limits:** Supports community and crop comparisons; remote classes rarely resolve cultivars without validation.
- **Supporting indicators:** [EII:BIO-001](#bio-001), [EII:BIO-004](#bio-004), [EII:VEG-016](#veg-016).

<a id="ter-001"></a>

### EII:TER-001 — Elevation / digital terrain model

**Definition:** Elevation/DTM represents ground-surface height relative to a vertical datum.

**Direct observations / derivation:** Survey or ground-classified LiDAR heights, m; declare datum, grid size and ground classification.

**Inference and limits:** Provides terrain context; a surface model containing canopy/buildings is not a ground model.

**Display label:** Ground elevation

**Display measurement:** Field surveys, LiDAR or photogrammetric terrain/canopy models. Survey or ground-classified LiDAR heights, m; declare datum, grid size and ground classification.

**Display interpretation:** Provides the ground heights needed to understand terrain. Heights of trees and buildings must be separated from the ground.

**Measurement origin:** Field surveys, LiDAR or photogrammetric terrain/canopy models

**Supporting indicators:** [EII:TER-002](#ter-002); [EII:TER-003](#ter-003); [EII:TER-014](#ter-014)

**Primary domain:** D10

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["landscape", "watershed", "region"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["terrain"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:TER-001","domain":"D10","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["state"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Elevation/DTM represents ground-surface height relative to a vertical datum.
- **Direct observations / derivation:** Survey or ground-classified LiDAR heights, m; declare datum, grid size and ground classification.
- **Inference and limits:** Provides terrain context; a surface model containing canopy/buildings is not a ground model.
- **Supporting indicators:** [EII:TER-002](#ter-002), [EII:TER-003](#ter-003), [EII:TER-014](#ter-014).

<a id="ter-002"></a>

### EII:TER-002 — Slope gradient

**Definition:** Slope is the local rate of elevation change.

**Direct observations / derivation:** DTM derivatives, degrees or %; record neighbourhood and grid resolution.

**Inference and limits:** Indicates gravitational runoff/erosion context; does not measure realised erosion.

**Display label:** Slope gradient

**Display measurement:** Field surveys, LiDAR or photogrammetric terrain/canopy models. DTM derivatives, degrees or %; record neighbourhood and grid resolution.

**Display interpretation:** Shows how steep the ground is. Steeper ground may favour runoff, but slope alone does not measure soil loss.

**Measurement origin:** Field surveys, LiDAR or photogrammetric terrain/canopy models

**Supporting indicators:** [EII:SOI-012](#soi-012); [EII:TER-009](#ter-009); [EII:VEG-012](#veg-012)

**Primary domain:** D10

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "context"]`

**Spatial/temporal dimensions:** `{"spatial": ["landscape", "watershed", "region"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["context"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["terrain"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:TER-002","domain":"D10","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","context"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["context"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Slope is the local rate of elevation change.
- **Direct observations / derivation:** DTM derivatives, degrees or %; record neighbourhood and grid resolution.
- **Inference and limits:** Indicates gravitational runoff/erosion context; does not measure realised erosion.
- **Supporting indicators:** [EII:SOI-012](#soi-012), [EII:TER-009](#ter-009), [EII:VEG-012](#veg-012).

<a id="ter-003"></a>

### EII:TER-003 — Aspect / slope orientation

**Definition:** Aspect is the compass direction of maximum downslope gradient.

**Direct observations / derivation:** DTM orientation, degrees clockwise from north; undefined on flat terrain.

**Inference and limits:** Supports radiation and exposure interpretation; local shading modifies actual microclimate.

**Display label:** Slope direction

**Display measurement:** Field surveys, LiDAR or photogrammetric terrain/canopy models. DTM orientation, degrees clockwise from north; undefined on flat terrain.

**Display interpretation:** Shows which direction a slope faces. This helps explain sunlight and exposure, although nearby shade also matters.

**Measurement origin:** Field surveys, LiDAR or photogrammetric terrain/canopy models

**Supporting indicators:** [EII:TER-004](#ter-004); [EII:HYD-001](#hyd-001); [EII:DIS-006](#dis-006)

**Primary domain:** D10

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "context"]`

**Spatial/temporal dimensions:** `{"spatial": ["landscape", "watershed", "region"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["context"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["terrain"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:TER-003","domain":"D10","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","context"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["context"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Aspect is the compass direction of maximum downslope gradient.
- **Direct observations / derivation:** DTM orientation, degrees clockwise from north; undefined on flat terrain.
- **Inference and limits:** Supports radiation and exposure interpretation; local shading modifies actual microclimate.
- **Supporting indicators:** [EII:TER-004](#ter-004), [EII:HYD-001](#hyd-001), [EII:DIS-006](#dis-006).

<a id="ter-004"></a>

### EII:TER-004 — Solar radiation / insolation

**Definition:** Insolation is incoming solar energy at a surface over a specified interval.

**Direct observations / derivation:** Radiometer measurements or terrain/atmosphere radiation models, W/m² or MJ/m²/day.

**Inference and limits:** Supports energy-balance and microclimate assessment; potential terrain radiation differs from actual cloud-affected radiation.

**Display label:** Solar radiation

**Display measurement:** Field radiation sensors or terrain-based radiation models. Radiometer measurements or terrain/atmosphere radiation models, W/m² or MJ/m²/day.

**Display interpretation:** Helps explain how much solar energy reaches a place. Estimates based only on terrain do not account fully for clouds.

**Measurement origin:** Field radiation sensors or terrain-based radiation models

**Supporting indicators:** [EII:TER-003](#ter-003); [EII:ATM-004](#atm-004); [EII:HYD-012](#hyd-012)

**Primary domain:** D01

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "landscape", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["terrain", "iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021; IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:TER-004","domain":"D01","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","modelled"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["terrain","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Insolation is incoming solar energy at a surface over a specified interval.
- **Direct observations / derivation:** Radiometer measurements or terrain/atmosphere radiation models, W/m² or MJ/m²/day.
- **Inference and limits:** Supports energy-balance and microclimate assessment; potential terrain radiation differs from actual cloud-affected radiation.
- **Supporting indicators:** [EII:TER-003](#ter-003), [EII:ATM-004](#atm-004), [EII:HYD-012](#hyd-012).

<a id="ter-005"></a>

### EII:TER-005 — Topographic wetness index

**Definition:** Topographic wetness index expresses terrain-driven accumulation potential.

**Direct observations / derivation:** ln(a/tan β), where a is specific contributing area and β slope; dimensionless with declared algorithm.

**Inference and limits:** Suggests relative topographic saturation propensity; not measured water content and unreliable without hydrological validation.

**Display label:** Topographic wetness index

**Display measurement:** Field surveys, LiDAR or photogrammetric terrain/canopy models. ln(a/tan β), where a is specific contributing area and β slope; dimensionless with declared algorithm.

**Display interpretation:** Suggests where water may collect because of terrain. It does not measure actual soil moisture.

**Measurement origin:** Field surveys, LiDAR or photogrammetric terrain/canopy models

**Supporting indicators:** [EII:HYD-001](#hyd-001); [EII:TER-006](#ter-006); [EII:SOI-001](#soi-001)

**Primary domain:** D02

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "watershed", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["terrain"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:TER-005","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Topographic wetness index expresses terrain-driven accumulation potential.
- **Direct observations / derivation:** ln(a/tan β), where a is specific contributing area and β slope; dimensionless with declared algorithm.
- **Inference and limits:** Suggests relative topographic saturation propensity; not measured water content and unreliable without hydrological validation.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:TER-006](#ter-006), [EII:SOI-001](#soi-001).

<a id="ter-006"></a>

### EII:TER-006 — Flow accumulation / drainage pathways

**Definition:** Flow accumulation/drainage pathways describe terrain-routed contributing area.

**Direct observations / derivation:** Hydrologically conditioned DTM and routing algorithm, cells or m²; declare sink handling.

**Inference and limits:** Suggests runoff pathways; engineered drainage, infiltration and subsurface flow can alter routes.

**Display label:** Runoff pathways

**Display measurement:** Field surveys, LiDAR or photogrammetric terrain/canopy models. Hydrologically conditioned DTM and routing algorithm, cells or m²; declare sink handling.

**Display interpretation:** Suggests where runoff may flow. Drains, soil absorption and underground water can change the actual route.

**Measurement origin:** Field surveys, LiDAR or photogrammetric terrain/canopy models

**Supporting indicators:** [EII:HYD-006](#hyd-006); [EII:HYD-008](#hyd-008); [EII:TER-009](#ter-009)

**Primary domain:** D02

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "watershed", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["terrain"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:TER-006","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","modelled"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Flow accumulation/drainage pathways describe terrain-routed contributing area.
- **Direct observations / derivation:** Hydrologically conditioned DTM and routing algorithm, cells or m²; declare sink handling.
- **Inference and limits:** Suggests runoff pathways; engineered drainage, infiltration and subsurface flow can alter routes.
- **Supporting indicators:** [EII:HYD-006](#hyd-006), [EII:HYD-008](#hyd-008), [EII:TER-009](#ter-009).

<a id="ter-007"></a>

### EII:TER-007 — Surface roughness

**Definition:** Surface roughness quantifies elevation variation over a stated support area.

**Direct observations / derivation:** Survey heights and declared RMS, standard deviation or rugosity metric, m or ratio.

**Inference and limits:** Supports runoff, seedbed and habitat interpretation; metric and measurement scale determine meaning.

**Display label:** Surface roughness

**Display measurement:** Field surveys, LiDAR or photogrammetric terrain/canopy models. Survey heights and declared RMS, standard deviation or rugosity metric, m or ratio.

**Display interpretation:** Shows how uneven the soil surface is. This can affect runoff and habitats, depending on the size of the features measured.

**Measurement origin:** Field surveys, LiDAR or photogrammetric terrain/canopy models

**Supporting indicators:** [EII:HYD-004](#hyd-004); [EII:SOI-003](#soi-003); [EII:TER-002](#ter-002)

**Primary domain:** D03

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["terrain", "amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021; AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:TER-007","domain":"D03","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["terrain","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Surface roughness quantifies elevation variation over a stated support area.
- **Direct observations / derivation:** Survey heights and declared RMS, standard deviation or rugosity metric, m or ratio.
- **Inference and limits:** Supports runoff, seedbed and habitat interpretation; metric and measurement scale determine meaning.
- **Supporting indicators:** [EII:HYD-004](#hyd-004), [EII:SOI-003](#soi-003), [EII:TER-002](#ter-002).

<a id="ter-008"></a>

### EII:TER-008 — Terrace geometry / terrace-wall condition

**Definition:** Terrace geometry/wall condition describes measured dimensions and damage.

**Direct observations / derivation:** Surveyed terrace width, wall height, slope and damage frequency, m and %; retain component fields.

**Inference and limits:** Supports stability and maintenance assessment; structural safety requires site investigation.

**Display label:** Terrace shape and wall condition

**Display measurement:** Field surveys, LiDAR or photogrammetric terrain/canopy models. Surveyed terrace width, wall height, slope and damage frequency, m and %; retain component fields.

**Display interpretation:** Helps identify terraces that need maintenance. Measurements and visible damage alone do not establish structural safety.

**Measurement origin:** Field surveys, LiDAR or photogrammetric terrain/canopy models

**Supporting indicators:** [EII:TER-009](#ter-009); [EII:TER-002](#ter-002); [EII:HYD-006](#hyd-006)

**Primary domain:** D10

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "context"]`

**Spatial/temporal dimensions:** `{"spatial": ["landscape", "watershed", "region"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["context"]`

**Family / variant distinctions:** `["terrace_geometry", "wall_condition"]`

**Record type:** family

**Candidate source routes:** `["terrain", "amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021; AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:TER-008","domain":"D10","related_domains":["D13"],"record_type":"family","variants":["terrace_geometry","wall_condition"],"secondary":["measured","context"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["context"],"routes":["terrain","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Terrace geometry/wall condition describes measured dimensions and damage.
- **Direct observations / derivation:** Surveyed terrace width, wall height, slope and damage frequency, m and %; retain component fields.
- **Inference and limits:** Supports stability and maintenance assessment; structural safety requires site investigation.
- **Supporting indicators:** [EII:TER-009](#ter-009), [EII:TER-002](#ter-002), [EII:HYD-006](#hyd-006).

<a id="ter-009"></a>

### EII:TER-009 — Erosion rills / gullies / sediment pathways

**Definition:** Rill/gully geometry records concentrated erosion features and sediment routes.

**Direct observations / derivation:** Mapped lengths, depths, areas or volumes, m, m² or m³, from repeat surveys.

**Inference and limits:** Provides evidence of erosion morphology; a single feature map does not establish an annual mass-loss rate.

**Display label:** Erosion channels

**Display measurement:** Field surveys, LiDAR or photogrammetric terrain/canopy models. Mapped lengths, depths, areas or volumes, m, m² or m³, from repeat surveys.

**Display interpretation:** Shows where concentrated erosion has formed channels. A single survey cannot tell us the annual amount of soil lost.

**Measurement origin:** Field surveys, LiDAR or photogrammetric terrain/canopy models

**Supporting indicators:** [EII:SOI-012](#soi-012); [EII:TER-014](#ter-014); [EII:HYD-009](#hyd-009)

**Primary domain:** D03

**Secondary domains:** `[]`

**Classification dimensions:** `["observed", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["terrain"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:TER-009","domain":"D03","related_domains":[],"record_type":"indicator","variants":[],"secondary":["observed","derived"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Rill/gully geometry records concentrated erosion features and sediment routes.
- **Direct observations / derivation:** Mapped lengths, depths, areas or volumes, m, m² or m³, from repeat surveys.
- **Inference and limits:** Provides evidence of erosion morphology; a single feature map does not establish an annual mass-loss rate.
- **Supporting indicators:** [EII:SOI-012](#soi-012), [EII:TER-014](#ter-014), [EII:HYD-009](#hyd-009).

<a id="ter-010"></a>

### EII:TER-010 — Tree height

**Definition:** Tree height is vertical distance from ground to tree top.

**Direct observations / derivation:** Field range measurements or canopy-minus-ground heights, m.

**Inference and limits:** Supports stand development and biomass estimation; occlusion and ground errors propagate.

**Display label:** Tree height

**Display measurement:** Field surveys, LiDAR or photogrammetric terrain/canopy models. Field range measurements or canopy-minus-ground heights, m.

**Display interpretation:** Shows tree size and stand development. Estimating biomass also requires information about species and tree shape.

**Measurement origin:** Field surveys, LiDAR or photogrammetric terrain/canopy models

**Supporting indicators:** [EII:VEG-014](#veg-014); [EII:TER-011](#ter-011); [EII:VEG-017](#veg-017)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot"], "temporal": ["event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["terrain"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:TER-010","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["organism","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Tree height is vertical distance from ground to tree top.
- **Direct observations / derivation:** Field range measurements or canopy-minus-ground heights, m.
- **Inference and limits:** Supports stand development and biomass estimation; occlusion and ground errors propagate.
- **Supporting indicators:** [EII:VEG-014](#veg-014), [EII:TER-011](#ter-011), [EII:VEG-017](#veg-017).

<a id="ter-011"></a>

### EII:TER-011 — Canopy volume

**Definition:** Canopy volume is a defined three-dimensional crown envelope.

**Direct observations / derivation:** Point-cloud crown segmentation and volume algorithm, m³; declare convex hull/voxel method.

**Inference and limits:** Supports crown architecture comparison; envelope volume is not woody mass or leaf area.

**Display label:** Canopy volume

**Display measurement:** Field surveys, LiDAR or photogrammetric terrain/canopy models. Point-cloud crown segmentation and volume algorithm, m³; declare convex hull/voxel method.

**Display interpretation:** Shows the space occupied by a tree crown. This is not the same as the mass of wood or the area of leaves.

**Measurement origin:** Field surveys, LiDAR or photogrammetric terrain/canopy models

**Supporting indicators:** [EII:TER-010](#ter-010); [EII:VEG-014](#veg-014); [EII:VEG-011](#veg-011)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot"], "temporal": ["event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["terrain"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:TER-011","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Canopy volume is a defined three-dimensional crown envelope.
- **Direct observations / derivation:** Point-cloud crown segmentation and volume algorithm, m³; declare convex hull/voxel method.
- **Inference and limits:** Supports crown architecture comparison; envelope volume is not woody mass or leaf area.
- **Supporting indicators:** [EII:TER-010](#ter-010), [EII:VEG-014](#veg-014), [EII:VEG-011](#veg-011).

<a id="ter-012"></a>

### EII:TER-012 — Canopy gaps / crown cover

**Definition:** Canopy gaps/crown cover quantify projected crowns and openings.

**Direct observations / derivation:** Mapped crown/gap area divided by plot area, %, with minimum gap definition.

**Inference and limits:** Supports light and regeneration interpretation; projected cover differs from leaf area and understory cover.

**Display label:** Canopy gaps and crown cover

**Display measurement:** Field surveys, LiDAR or photogrammetric terrain/canopy models. Mapped crown/gap area divided by plot area, %, with minimum gap definition.

**Display interpretation:** Shows openings and crown cover in a canopy. This helps assess light and regeneration, but does not describe all vegetation layers.

**Measurement origin:** Field surveys, LiDAR or photogrammetric terrain/canopy models

**Supporting indicators:** [EII:VEG-011](#veg-011); [EII:TER-013](#ter-013); [EII:BIO-005](#bio-005)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["gap_fraction", "crown_cover"]`

**Record type:** family

**Candidate source routes:** `["terrain", "veg"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021, RS004, RS001, RS002

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:TER-012","domain":"D07","related_domains":[],"record_type":"family","variants":["gap_fraction","crown_cover"],"secondary":["derived"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["terrain","veg"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Canopy gaps/crown cover quantify projected crowns and openings.
- **Direct observations / derivation:** Mapped crown/gap area divided by plot area, %, with minimum gap definition.
- **Inference and limits:** Supports light and regeneration interpretation; projected cover differs from leaf area and understory cover.
- **Supporting indicators:** [EII:VEG-011](#veg-011), [EII:TER-013](#ter-013), [EII:BIO-005](#bio-005).

<a id="ter-013"></a>

### EII:TER-013 — Vertical vegetation complexity

**Definition:** Vertical vegetation complexity describes vegetation distribution through height strata.

**Direct observations / derivation:** Height-bin returns, foliage profiles or stated structural diversity index, proportions or index.

**Inference and limits:** Supports habitat and vertical fuel interpretation; LiDAR sampling and sensor geometry affect profiles.

**Display label:** Vegetation layers

**Display measurement:** Field surveys, LiDAR or photogrammetric terrain/canopy models. Height-bin returns, foliage profiles or stated structural diversity index, proportions or index.

**Display interpretation:** Shows how vegetation is arranged at different heights. This helps assess habitat layers and the paths fire might follow.

**Measurement origin:** Field surveys, LiDAR or photogrammetric terrain/canopy models

**Supporting indicators:** [EII:TER-010](#ter-010); [EII:DIS-002](#dis-002); [EII:BIO-004](#bio-004)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["terrain"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:TER-013","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Vertical vegetation complexity describes vegetation distribution through height strata.
- **Direct observations / derivation:** Height-bin returns, foliage profiles or stated structural diversity index, proportions or index.
- **Inference and limits:** Supports habitat and vertical fuel interpretation; LiDAR sampling and sensor geometry affect profiles.
- **Supporting indicators:** [EII:TER-010](#ter-010), [EII:DIS-002](#dis-002), [EII:BIO-004](#bio-004).

<a id="ter-014"></a>

### EII:TER-014 — Surface / canopy change between surveys

**Definition:** Repeat surface/canopy change is the difference between co-registered surveys.

**Direct observations / derivation:** Height or volume differences, m or m³, with a spatial level-of-detection threshold.

**Inference and limits:** Can indicate growth, erosion or deposition; season, registration and occlusion can mimic change.

**Display label:** Ground and canopy change

**Display measurement:** Field surveys, LiDAR or photogrammetric terrain/canopy models. Height or volume differences, m or m³, with a spatial level-of-detection threshold.

**Display interpretation:** Shows changes in ground or canopy height between surveys. Alignment errors and seasonal differences can look like real change.

**Measurement origin:** Field surveys, LiDAR or photogrammetric terrain/canopy models

**Supporting indicators:** [EII:TER-001](#ter-001); [EII:TER-009](#ter-009); [EII:VEG-014](#veg-014)

**Primary domain:** D10

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["landscape", "watershed", "region"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["ground_height_change", "canopy_height_change", "volume_change"]`

**Record type:** family

**Candidate source routes:** `["terrain"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:TER-014","domain":"D10","related_domains":[],"record_type":"family","variants":["ground_height_change","canopy_height_change","volume_change"],"secondary":["derived"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["state"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Repeat surface/canopy change is the difference between co-registered surveys.
- **Direct observations / derivation:** Height or volume differences, m or m³, with a spatial level-of-detection threshold.
- **Inference and limits:** Can indicate growth, erosion or deposition; season, registration and occlusion can mimic change.
- **Supporting indicators:** [EII:TER-001](#ter-001), [EII:TER-009](#ter-009), [EII:VEG-014](#veg-014).

<a id="ter-015"></a>

### EII:TER-015 — Built structures and landscape geometry

**Definition:** Built geometry describes physical structures and engineered landscape features.

**Direct observations / derivation:** Surveyed footprints, dimensions and volumes, m² and m³; classify feature type.

**Inference and limits:** Provides land occupation/material context; geometry alone does not reveal resource consumption or social meaning.

**Display label:** Built-feature geometry

**Display measurement:** Field surveys, LiDAR or photogrammetric terrain/canopy models. Surveyed footprints, dimensions and volumes, m² and m³; classify feature type.

**Display interpretation:** Shows the size and position of built features. Their shape alone does not tell us how much energy or material people use.

**Measurement origin:** Field surveys, LiDAR or photogrammetric terrain/canopy models

**Supporting indicators:** [EII:FUN-009](#fun-009); [EII:HUM-001](#hum-001); [EII:DIS-004](#dis-004)

**Primary domain:** D14

**Secondary domains:** `[]`

**Classification dimensions:** `["observed", "context"]`

**Spatial/temporal dimensions:** `{"spatial": ["farm", "watershed", "region"], "temporal": ["year"]}`

**Ecological purpose:** `["context"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["terrain", "settlement"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021, RS019

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:TER-015","domain":"D14","related_domains":[],"record_type":"indicator","variants":[],"secondary":["observed","context"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["context"],"routes":["terrain","settlement"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Built geometry describes physical structures and engineered landscape features.
- **Direct observations / derivation:** Surveyed footprints, dimensions and volumes, m² and m³; classify feature type.
- **Inference and limits:** Provides land occupation/material context; geometry alone does not reveal resource consumption or social meaning.
- **Supporting indicators:** [EII:FUN-009](#fun-009), [EII:HUM-001](#hum-001), [EII:DIS-004](#dis-004).

<a id="hyd-001"></a>

### EII:HYD-001 — Surface / root-zone soil moisture

**Definition:** Soil moisture is water held in a defined soil layer.

**Direct observations / derivation:** Gravimetric mass ratio or calibrated volumetric sensors, g/g or m³/m³; satellite retrievals estimate different depth/support.

**Inference and limits:** Supports water-availability assessment; rooting depth, texture and matric potential govern plant access.

**Display label:** Soil moisture

**Display measurement:** Soil sensors, weighed soil samples or calibrated satellite/model estimates. Gravimetric mass ratio or calibrated volumetric sensors, g/g or m³/m³; satellite retrievals estimate different depth/support.

**Display interpretation:** Helps assess water available in soil. Plants' access also depends on soil type, root depth and how tightly water is held.

**Measurement origin:** Soil sensors, weighed soil samples or calibrated satellite/model estimates

**Supporting indicators:** [EII:HYD-005](#hyd-005); [EII:SOI-001](#soi-001); [EII:SOI-011](#soi-011)

**Primary domain:** D02

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "watershed", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["surface_moisture", "root_zone_moisture"]`

**Record type:** family

**Candidate source routes:** `["iot", "drought"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS015; IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-001","domain":"D02","related_domains":[],"record_type":"family","variants":["surface_moisture","root_zone_moisture"],"secondary":["measured","modelled"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot","drought"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Soil moisture is water held in a defined soil layer.
- **Direct observations / derivation:** Gravimetric mass ratio or calibrated volumetric sensors, g/g or m³/m³; satellite retrievals estimate different depth/support.
- **Inference and limits:** Supports water-availability assessment; rooting depth, texture and matric potential govern plant access.
- **Supporting indicators:** [EII:HYD-005](#hyd-005), [EII:SOI-001](#soi-001), [EII:SOI-011](#soi-011).

<a id="hyd-002"></a>

### EII:HYD-002 — Normalised Difference Moisture Index (NDMI)

**Definition:** NDMI contrasts near-infrared with shortwave-infrared reflectance.

**Direct observations / derivation:** (NIR-SWIR1)/(NIR+SWIR1), dimensionless; declare wavelengths and alias conventions.

**Inference and limits:** Supports canopy moisture comparisons; leaf area, soil exposure and species confound water-status inference.

**Display label:** Canopy moisture index (NDMI)

**Display measurement:** Satellite or multispectral drone imagery. (NIR-SWIR1)/(NIR+SWIR1), dimensionless; declare wavelengths and alias conventions.

**Display interpretation:** Can indicate changes in canopy moisture. Plant type, leaf cover and exposed soil also affect the signal.

**Measurement origin:** Satellite or multispectral drone imagery

**Supporting indicators:** [EII:HYD-001](#hyd-001); [EII:VEG-011](#veg-011); [EII:VEG-015](#veg-015)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["opt"]`

**Scientific reference keys:** `["R11"]`

**Display source keys:** RS001, RS002

**Research status:** curated_working_definition

**Review scope:** specific_documentary_aspects_only

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-002","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["opt"],"refs":["R11"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** NDMI contrasts near-infrared with shortwave-infrared reflectance.
- **Direct observations / derivation:** (NIR-SWIR1)/(NIR+SWIR1), dimensionless; declare wavelengths and alias conventions.
- **Inference and limits:** Supports canopy moisture comparisons; leaf area, soil exposure and species confound water-status inference.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:VEG-011](#veg-011), [EII:VEG-015](#veg-015).

<a id="hyd-003"></a>

### EII:HYD-003 — Land Surface Temperature (LST)

**Definition:** LST is radiometric temperature of the observed land surface.

**Direct observations / derivation:** Thermal radiance corrected for atmosphere and emissivity, K or °C; record acquisition time.

**Inference and limits:** Supports surface-energy and heat-exposure analysis; it is neither air temperature nor uniquely a water-stress signal.

**Display label:** Land surface temperature

**Display measurement:** Thermal satellite imagery or field thermal cameras. Thermal radiance corrected for atmosphere and emissivity, K or °C; record acquisition time.

**Display interpretation:** Shows how warm the land surface is. It differs from air temperature and cannot identify water stress on its own.

**Measurement origin:** Thermal satellite imagery or field thermal cameras

**Supporting indicators:** [EII:DIS-006](#dis-006); [EII:VEG-012](#veg-012); [EII:HYD-012](#hyd-012)

**Primary domain:** D01

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "landscape", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["thermal"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS002

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-003","domain":"D01","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["thermal"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** LST is radiometric temperature of the observed land surface.
- **Direct observations / derivation:** Thermal radiance corrected for atmosphere and emissivity, K or °C; record acquisition time.
- **Inference and limits:** Supports surface-energy and heat-exposure analysis; it is neither air temperature nor uniquely a water-stress signal.
- **Supporting indicators:** [EII:DIS-006](#dis-006), [EII:VEG-012](#veg-012), [EII:HYD-012](#hyd-012).

<a id="hyd-004"></a>

### EII:HYD-004 — Infiltration rate

**Definition:** Infiltration rate is water entry through the soil surface under stated conditions.

**Direct observations / derivation:** Infiltrometer volume/time/area, mm/h; distinguish initial, steady and saturated regimes.

**Inference and limits:** Supports runoff susceptibility assessment; antecedent moisture and imposed head affect results.

**Display label:** Infiltration rate

**Display measurement:** Field infiltration tests. Infiltrometer volume/time/area, mm/h; distinguish initial, steady and saturated regimes.

**Display interpretation:** Shows how quickly water enters soil. The result depends on the test and how wet the soil was beforehand.

**Measurement origin:** Field infiltration tests

**Supporting indicators:** [EII:SOI-003](#soi-003); [EII:SOI-002](#soi-002); [EII:HYD-001](#hyd-001)

**Primary domain:** D03

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["event", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-004","domain":"D03","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Infiltration rate is water entry through the soil surface under stated conditions.
- **Direct observations / derivation:** Infiltrometer volume/time/area, mm/h; distinguish initial, steady and saturated regimes.
- **Inference and limits:** Supports runoff susceptibility assessment; antecedent moisture and imposed head affect results.
- **Supporting indicators:** [EII:SOI-003](#soi-003), [EII:SOI-002](#soi-002), [EII:HYD-001](#hyd-001).

<a id="hyd-005"></a>

### EII:HYD-005 — Soil water-holding capacity

**Definition:** Water-holding capacity describes a stated soil retention quantity.

**Direct observations / derivation:** Water retained at declared matric potentials; available water often θfield-capacity−θwilting, m³/m³ or mm over depth.

**Inference and limits:** Supports storage and rooting-zone drought assessment; conventional potentials are method-dependent and crop access varies.

**Display label:** Soil water storage

**Display measurement:** Soil samples tested in a laboratory. Water retained at declared matric potentials; available water often θfield-capacity−θwilting, m³/m³ or mm over depth.

**Display interpretation:** Helps estimate how much water soil can store for plants. Root depth and the chosen laboratory test affect the estimate.

**Measurement origin:** Soil samples tested in a laboratory

**Supporting indicators:** [EII:SOI-001](#soi-001); [EII:SOI-002](#soi-002); [EII:HYD-001](#hyd-001)

**Primary domain:** D03

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["water_retention_at_potential", "plant_available_water_capacity"]`

**Record type:** family

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-005","domain":"D03","related_domains":["D13"],"record_type":"family","variants":["water_retention_at_potential","plant_available_water_capacity"],"secondary":["measured","derived"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Water-holding capacity describes a stated soil retention quantity.
- **Direct observations / derivation:** Water retained at declared matric potentials; available water often θfield-capacity−θwilting, m³/m³ or mm over depth.
- **Inference and limits:** Supports storage and rooting-zone drought assessment; conventional potentials are method-dependent and crop access varies.
- **Supporting indicators:** [EII:SOI-001](#soi-001), [EII:SOI-002](#soi-002), [EII:HYD-001](#hyd-001).

<a id="hyd-006"></a>

### EII:HYD-006 — Stream discharge / river flow

**Definition:** Discharge is water volume crossing a channel section per time.

**Direct observations / derivation:** Velocity–area gauging or calibrated stage–discharge relation, m³/s.

**Inference and limits:** Supports flow availability and flood assessment; rating extrapolation, backwater and channel change affect estimates.

**Display label:** River flow

**Display measurement:** River gauges and field flow measurements. Velocity–area gauging or calibrated stage–discharge relation, m³/s.

**Display interpretation:** Shows how much water moves through a stream. This helps assess water supply and flooding, but measurement accuracy varies with flow conditions.

**Measurement origin:** River gauges and field flow measurements

**Supporting indicators:** [EII:HYD-008](#hyd-008); [EII:HYD-009](#hyd-009); [EII:DIS-006](#dis-006)

**Primary domain:** D02

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "watershed", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot", "water"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS013; IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-006","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot","water"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Discharge is water volume crossing a channel section per time.
- **Direct observations / derivation:** Velocity–area gauging or calibrated stage–discharge relation, m³/s.
- **Inference and limits:** Supports flow availability and flood assessment; rating extrapolation, backwater and channel change affect estimates.
- **Supporting indicators:** [EII:HYD-008](#hyd-008), [EII:HYD-009](#hyd-009), [EII:DIS-006](#dis-006).

<a id="hyd-007"></a>

### EII:HYD-007 — Groundwater level / recharge

**Definition:** Groundwater level and recharge are distinct aquifer state and flux quantities.

**Direct observations / derivation:** Well water level, m relative to datum; recharge estimated with water-balance, tracer or hydraulic methods, mm/year.

**Inference and limits:** Level change does not equal recharge; pumping, storage coefficients and lateral flow must be resolved.

**Display label:** Groundwater level and recharge

**Display measurement:** Well sensors and aquifer recharge models. Well water level, m relative to datum; recharge estimated with water-balance, tracer or hydraulic methods, mm/year.

**Display interpretation:** Shows changes in groundwater level or estimates water entering an aquifer. Pumping and underground flows must also be considered.

**Measurement origin:** Well sensors and aquifer recharge models

**Supporting indicators:** [EII:HYD-006](#hyd-006); [EII:HYD-001](#hyd-001); [EII:DIS-006](#dis-006)

**Primary domain:** D02

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "watershed", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["groundwater_level", "recharge_rate"]`

**Record type:** family

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-007","domain":"D02","related_domains":[],"record_type":"family","variants":["groundwater_level","recharge_rate"],"secondary":["measured","modelled"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Groundwater level and recharge are distinct aquifer state and flux quantities.
- **Direct observations / derivation:** Well water level, m relative to datum; recharge estimated with water-balance, tracer or hydraulic methods, mm/year.
- **Inference and limits:** Level change does not equal recharge; pumping, storage coefficients and lateral flow must be resolved.
- **Supporting indicators:** [EII:HYD-006](#hyd-006), [EII:HYD-001](#hyd-001), [EII:DIS-006](#dis-006).

<a id="hyd-008"></a>

### EII:HYD-008 — Flood extent / frequency

**Definition:** Flood extent/frequency describe inundated area and repeated occurrence.

**Direct observations / derivation:** Validated event masks, km²; event counts or statistical recurrence, events/year or years.

**Inference and limits:** Supports exposure and wetland-dynamics assessment; observed history does not alone provide a future return period.

**Display label:** Flood area and frequency

**Display measurement:** Satellite flood maps, field records or flood models. Validated event masks, km²; event counts or statistical recurrence, events/year or years.

**Display interpretation:** Shows where and how often flooding was recorded. Past observations alone do not predict the timing of the next flood.

**Measurement origin:** Satellite flood maps, field records or flood models

**Supporting indicators:** [EII:HYD-006](#hyd-006); [EII:TER-001](#ter-001); [EII:DIS-011](#dis-011)

**Primary domain:** D02

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "watershed", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["inundated_extent", "observed_event_frequency", "modelled_return_period"]`

**Record type:** family

**Candidate source routes:** `["flood", "water"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS014, RS013

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-008","domain":"D02","related_domains":[],"record_type":"family","variants":["inundated_extent","observed_event_frequency","modelled_return_period"],"secondary":["derived","modelled"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["flood","water"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Flood extent/frequency describe inundated area and repeated occurrence.
- **Direct observations / derivation:** Validated event masks, km²; event counts or statistical recurrence, events/year or years.
- **Inference and limits:** Supports exposure and wetland-dynamics assessment; observed history does not alone provide a future return period.
- **Supporting indicators:** [EII:HYD-006](#hyd-006), [EII:TER-001](#ter-001), [EII:DIS-011](#dis-011).

<a id="hyd-009"></a>

### EII:HYD-009 — Water turbidity / suspended sediment

**Definition:** Turbidity and suspended sediment are separate optical and mass metrics.

**Direct observations / derivation:** Nephelometer response, FNU/NTU; filtered dry sediment mass, mg/L; convert only with local calibration.

**Inference and limits:** Supports sediment-transport interpretation; particle size, colour and organic matter affect optical response.

**Display label:** Water cloudiness and suspended sediment

**Display measurement:** Water sensors and laboratory sediment tests. Nephelometer response, FNU/NTU; filtered dry sediment mass, mg/L; convert only with local calibration.

**Display interpretation:** Helps assess cloudiness and sediment in water. Cloudiness cannot be converted to sediment mass without local testing.

**Measurement origin:** Water sensors and laboratory sediment tests

**Supporting indicators:** [EII:HYD-006](#hyd-006); [EII:SOI-012](#soi-012); [EII:HYD-010](#hyd-010)

**Primary domain:** D02

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "watershed", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["turbidity", "suspended_sediment_concentration"]`

**Record type:** family

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-009","domain":"D02","related_domains":[],"record_type":"family","variants":["turbidity","suspended_sediment_concentration"],"secondary":["measured","proxy"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Turbidity and suspended sediment are separate optical and mass metrics.
- **Direct observations / derivation:** Nephelometer response, FNU/NTU; filtered dry sediment mass, mg/L; convert only with local calibration.
- **Inference and limits:** Supports sediment-transport interpretation; particle size, colour and organic matter affect optical response.
- **Supporting indicators:** [EII:HYD-006](#hyd-006), [EII:SOI-012](#soi-012), [EII:HYD-010](#hyd-010).

<a id="hyd-010"></a>

### EII:HYD-010 — Water nutrient concentrations

**Definition:** Water nutrients are concentrations of specified nutrient forms.

**Direct observations / derivation:** Laboratory/sensor nitrate, ammonium, phosphate or total N/P, mg N/L or mg P/L; specify filtration and method.

**Inference and limits:** Supports enrichment assessment; concentration is not load, source attribution or biological response.

**Display label:** Water nutrient concentrations

**Display measurement:** Water samples tested in a laboratory or suitable sensors. Laboratory/sensor nitrate, ammonium, phosphate or total N/P, mg N/L or mg P/L; specify filtration and method.

**Display interpretation:** Shows nutrient levels in water and possible enrichment. The amount carried downstream also depends on water flow.

**Measurement origin:** Water samples tested in a laboratory or suitable sensors

**Supporting indicators:** [EII:HYD-006](#hyd-006); [EII:HYD-014](#hyd-014); [EII:HYD-013](#hyd-013)

**Primary domain:** D02

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "watershed", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `["nitrate_N", "ammonium_N", "total_N", "orthophosphate_P", "total_P"]`

**Record type:** family

**Candidate source routes:** `["iot", "amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future); AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-010","domain":"D02","related_domains":["D13"],"record_type":"family","variants":["nitrate_N","ammonium_N","total_N","orthophosphate_P","total_P"],"secondary":["measured","pressure"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["pressure"],"routes":["iot","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Water nutrients are concentrations of specified nutrient forms.
- **Direct observations / derivation:** Laboratory/sensor nitrate, ammonium, phosphate or total N/P, mg N/L or mg P/L; specify filtration and method.
- **Inference and limits:** Supports enrichment assessment; concentration is not load, source attribution or biological response.
- **Supporting indicators:** [EII:HYD-006](#hyd-006), [EII:HYD-014](#hyd-014), [EII:HYD-013](#hyd-013).

<a id="hyd-011"></a>

### EII:HYD-011 — Water conductivity / salinity / pH

**Definition:** Water conductivity, salinity and pH describe distinct water-chemistry properties.

**Direct observations / derivation:** Conductivity at reference temperature, µS/cm; salinity on declared scale; pH with calibrated electrode.

**Inference and limits:** Supports ionic and acidity constraints; conductivity is not a universal salinity conversion or contaminant assay.

**Display label:** Water salts and acidity

**Display measurement:** Field water probes and laboratory tests. Conductivity at reference temperature, µS/cm; salinity on declared scale; pH with calibrated electrode.

**Display interpretation:** Helps assess salt content and acidity. Conductivity does not identify individual pollutants or provide a universal measure of salinity.

**Measurement origin:** Field water probes and laboratory tests

**Supporting indicators:** [EII:HYD-010](#hyd-010); [EII:HYD-013](#hyd-013); [EII:HYD-015](#hyd-015)

**Primary domain:** D02

**Secondary domains:** `[]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "watershed", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["conductivity", "salinity", "pH"]`

**Record type:** family

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-011","domain":"D02","related_domains":[],"record_type":"family","variants":["conductivity","salinity","pH"],"secondary":["measured"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Water conductivity, salinity and pH describe distinct water-chemistry properties.
- **Direct observations / derivation:** Conductivity at reference temperature, µS/cm; salinity on declared scale; pH with calibrated electrode.
- **Inference and limits:** Supports ionic and acidity constraints; conductivity is not a universal salinity conversion or contaminant assay.
- **Supporting indicators:** [EII:HYD-010](#hyd-010), [EII:HYD-013](#hyd-013), [EII:HYD-015](#hyd-015).

<a id="hyd-012"></a>

### EII:HYD-012 — Evapotranspiration

**Definition:** Evapotranspiration combines water evaporation and plant transpiration.

**Direct observations / derivation:** Lysimeter/flux observations or energy/water-balance model, mm/day; distinguish actual ET from reference ET.

**Inference and limits:** Supports consumptive water-use assessment; models require meteorological and surface validation.

**Display label:** Evaporation and transpiration

**Display measurement:** Field water/flux instruments or weather-and-imagery models. Lysimeter/flux observations or energy/water-balance model, mm/day; distinguish actual ET from reference ET.

**Display interpretation:** Helps assess water lost through evaporation and plants. Estimates need weather and surface information, and differ from potential water demand.

**Measurement origin:** Field water/flux instruments or weather-and-imagery models

**Supporting indicators:** [EII:HYD-001](#hyd-001); [EII:VEG-011](#veg-011); [EII:ATM-005](#atm-005); [EII:DIS-006](#dis-006)

**Primary domain:** D02

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "modelled", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "watershed", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["veg", "iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS001, RS002; IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-012","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","modelled","process"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["function"],"routes":["veg","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Evapotranspiration combines water evaporation and plant transpiration.
- **Direct observations / derivation:** Lysimeter/flux observations or energy/water-balance model, mm/day; distinguish actual ET from reference ET.
- **Inference and limits:** Supports consumptive water-use assessment; models require meteorological and surface validation.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:VEG-011](#veg-011), [EII:ATM-005](#atm-005), [EII:DIS-006](#dis-006).

<a id="soi-001"></a>

### EII:SOI-001 — Soil texture

**Definition:** Texture is the particle-size distribution of the fine-earth fraction.

**Direct observations / derivation:** Sand/silt/clay mass percentages by declared dispersion and size limits.

**Inference and limits:** Supports hydraulic and substrate interpretation; structure and organic matter modify texture-based expectations.

**Display label:** Soil texture

**Display measurement:** Field soil samples analysed in a laboratory. Sand/silt/clay mass percentages by declared dispersion and size limits.

**Display interpretation:** Helps explain soil drainage and water storage. Soil structure and organic matter also affect these properties.

**Measurement origin:** Field soil samples analysed in a laboratory

**Supporting indicators:** [EII:SOI-003](#soi-003); [EII:HYD-005](#hyd-005); [EII:HYD-004](#hyd-004)

**Primary domain:** D03

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-001","domain":"D03","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Texture is the particle-size distribution of the fine-earth fraction.
- **Direct observations / derivation:** Sand/silt/clay mass percentages by declared dispersion and size limits.
- **Inference and limits:** Supports hydraulic and substrate interpretation; structure and organic matter modify texture-based expectations.
- **Supporting indicators:** [EII:SOI-003](#soi-003), [EII:HYD-005](#hyd-005), [EII:HYD-004](#hyd-004).

<a id="soi-002"></a>

### EII:SOI-002 — Bulk density / compaction

**Definition:** Bulk density and compaction describe mass per volume and mechanical resistance respectively.

**Direct observations / derivation:** Oven-dry soil mass/core volume, g/cm³; penetration resistance, MPa, at stated water content.

**Inference and limits:** Supports pore/rooting assessment; density thresholds vary with texture and resistance varies with moisture.

**Display label:** Soil density and compaction

**Display measurement:** Field soil cores, laboratory weighing and field penetration tests. Oven-dry soil mass/core volume, g/cm³; penetration resistance, MPa, at stated water content.

**Display interpretation:** Helps identify compacted soil and possible restrictions on roots. Results depend on soil type and moisture.

**Measurement origin:** Field soil cores, laboratory weighing and field penetration tests

**Supporting indicators:** [EII:SOI-001](#soi-001); [EII:SOI-004](#soi-004); [EII:HYD-001](#hyd-001)

**Primary domain:** D03

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["bulk_density", "penetration_resistance"]`

**Record type:** family

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-002","domain":"D03","related_domains":["D13"],"record_type":"family","variants":["bulk_density","penetration_resistance"],"secondary":["measured"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Bulk density and compaction describe mass per volume and mechanical resistance respectively.
- **Direct observations / derivation:** Oven-dry soil mass/core volume, g/cm³; penetration resistance, MPa, at stated water content.
- **Inference and limits:** Supports pore/rooting assessment; density thresholds vary with texture and resistance varies with moisture.
- **Supporting indicators:** [EII:SOI-001](#soi-001), [EII:SOI-004](#soi-004), [EII:HYD-001](#hyd-001).

<a id="soi-003"></a>

### EII:SOI-003 — Soil aggregate stability

**Definition:** Aggregate stability is resistance of aggregates to specified disruptive forces.

**Direct observations / derivation:** Wet-sieving stable fraction, % or mean-weight diameter, mm; declare pretreatment.

**Inference and limits:** Supports erosion-resistance interpretation; assay conditions and soil type limit comparability.

**Display label:** Soil aggregate stability

**Display measurement:** Field soil samples analysed in a laboratory. Wet-sieving stable fraction, % or mean-weight diameter, mm; declare pretreatment.

**Display interpretation:** Shows how well soil clumps resist breaking apart. This helps assess erosion risk, but different tests may give different results.

**Measurement origin:** Field soil samples analysed in a laboratory

**Supporting indicators:** [EII:HYD-004](#hyd-004); [EII:SOI-005](#soi-005); [EII:SOI-012](#soi-012)

**Primary domain:** D03

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-003","domain":"D03","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Aggregate stability is resistance of aggregates to specified disruptive forces.
- **Direct observations / derivation:** Wet-sieving stable fraction, % or mean-weight diameter, mm; declare pretreatment.
- **Inference and limits:** Supports erosion-resistance interpretation; assay conditions and soil type limit comparability.
- **Supporting indicators:** [EII:HYD-004](#hyd-004), [EII:SOI-005](#soi-005), [EII:SOI-012](#soi-012).

<a id="soi-004"></a>

### EII:SOI-004 — Soil porosity

**Definition:** Porosity is void volume divided by total soil volume.

**Direct observations / derivation:** Measured pore volumes or 1−bulk-density/particle-density, fraction; record particle-density assumption.

**Inference and limits:** Supports aeration/storage assessment; total porosity does not resolve connected macropores.

**Display label:** Soil pore space

**Display measurement:** Field soil samples analysed in a laboratory. Measured pore volumes or 1−bulk-density/particle-density, fraction; record particle-density assumption.

**Display interpretation:** Shows how much pore space soil contains. Total pore space alone does not show how easily air and water can move.

**Measurement origin:** Field soil samples analysed in a laboratory

**Supporting indicators:** [EII:SOI-002](#soi-002); [EII:HYD-004](#hyd-004); [EII:SOI-015](#soi-015)

**Primary domain:** D03

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-004","domain":"D03","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Porosity is void volume divided by total soil volume.
- **Direct observations / derivation:** Measured pore volumes or 1−bulk-density/particle-density, fraction; record particle-density assumption.
- **Inference and limits:** Supports aeration/storage assessment; total porosity does not resolve connected macropores.
- **Supporting indicators:** [EII:SOI-002](#soi-002), [EII:HYD-004](#hyd-004), [EII:SOI-015](#soi-015).

<a id="soi-005"></a>

### EII:SOI-005 — Soil organic carbon stock / concentration

**Definition:** SOC concentration and stock quantify organic C per dry soil mass and per area/depth respectively.

**Direct observations / derivation:** Organic C assay, g/kg; stock from C, compatible density, layer thickness and coarse fragments, Mg C/ha.

**Inference and limits:** Supports carbon-pool assessment; repeat stock comparisons require consistent depth or equivalent soil mass and uncertainty; neither % nor one survey proves sequestration.

**Display label:** Soil organic carbon

**Display measurement:** Field soil samples analysed in a laboratory. Organic C assay, g/kg; stock from C, compatible density, layer thickness and coarse fragments, Mg C/ha.

**Display interpretation:** Shows organic carbon concentration or the amount stored in a soil layer. Repeated, comparable stock measurements are needed to show accumulation.

**Measurement origin:** Field soil samples analysed in a laboratory

**Supporting indicators:** [EII:SOI-002](#soi-002); [EII:SOI-014](#soi-014); [EII:FUN-002](#fun-002)

**Primary domain:** D04

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["organic_C_concentration", "organic_C_stock"]`

**Record type:** family

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `["R03"]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Review scope:** specific_documentary_aspects_only

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-005","domain":"D04","related_domains":["D13"],"record_type":"family","variants":["organic_C_concentration","organic_C_stock"],"secondary":["measured","derived"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["state"],"routes":["amr"],"refs":["R03"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** SOC concentration and stock quantify organic C per dry soil mass and per area/depth respectively.
- **Direct observations / derivation:** Organic C assay, g/kg; stock from C, compatible density, layer thickness and coarse fragments, Mg C/ha.
- **Inference and limits:** Supports carbon-pool assessment; repeat stock comparisons require consistent depth or equivalent soil mass and uncertainty; neither % nor one survey proves sequestration.
- **Supporting indicators:** [EII:SOI-002](#soi-002), [EII:SOI-014](#soi-014), [EII:FUN-002](#fun-002).

<a id="soi-006"></a>

### EII:SOI-006 — Soil pH

**Definition:** Soil pH is acidity measured in a specified suspension.

**Direct observations / derivation:** Electrode response, pH units; declare water/salt extract and soil:solution ratio.

**Inference and limits:** Supports nutrient and microbial-habitat interpretation; assays are not interchangeable and pH alone does not establish fertility.

**Display label:** Soil pH

**Display measurement:** Field soil samples analysed in a laboratory. Electrode response, pH units; declare water/salt extract and soil:solution ratio.

**Display interpretation:** Helps explain nutrient availability and conditions for soil organisms. pH alone does not tell us whether soil is fertile.

**Measurement origin:** Field soil samples analysed in a laboratory

**Supporting indicators:** [EII:SOI-008](#soi-008); [EII:SOI-009](#soi-009); [EII:MIC-001](#mic-001)

**Primary domain:** D04

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-006","domain":"D04","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Soil pH is acidity measured in a specified suspension.
- **Direct observations / derivation:** Electrode response, pH units; declare water/salt extract and soil:solution ratio.
- **Inference and limits:** Supports nutrient and microbial-habitat interpretation; assays are not interchangeable and pH alone does not establish fertility.
- **Supporting indicators:** [EII:SOI-008](#soi-008), [EII:SOI-009](#soi-009), [EII:MIC-001](#mic-001).

<a id="soi-007"></a>

### EII:SOI-007 — Electrical conductivity / soil salinity

**Definition:** Soil EC measures ionic conductance in a declared extract or in situ.

**Direct observations / derivation:** Conductivity, dS/m, with temperature and extraction basis; distinguish ECe and bulk apparent EC.

**Inference and limits:** Supports salinity screening; moisture, clay and ions affect readings, so thresholds require a compatible method.

**Display label:** Soil salinity

**Display measurement:** Laboratory extracts or calibrated field conductivity probes. Conductivity, dS/m, with temperature and extraction basis; distinguish ECe and bulk apparent EC.

**Display interpretation:** Helps screen for salt stress. Moisture, clay and the test method also affect conductivity readings.

**Measurement origin:** Laboratory extracts or calibrated field conductivity probes

**Supporting indicators:** [EII:HYD-001](#hyd-001); [EII:SOI-001](#soi-001); [EII:SOI-019](#soi-019)

**Primary domain:** D04

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr", "iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context; IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-007","domain":"D04","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","proxy"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["state"],"routes":["amr","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Soil EC measures ionic conductance in a declared extract or in situ.
- **Direct observations / derivation:** Conductivity, dS/m, with temperature and extraction basis; distinguish ECe and bulk apparent EC.
- **Inference and limits:** Supports salinity screening; moisture, clay and ions affect readings, so thresholds require a compatible method.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:SOI-001](#soi-001), [EII:SOI-019](#soi-019).

<a id="soi-008"></a>

### EII:SOI-008 — Available nitrogen / phosphorus / potassium

**Definition:** Available N/P/K are method-defined nutrient fractions rather than total pools.

**Direct observations / derivation:** Specified mineral-N extraction, P test and exchangeable-K assay, mg/kg with nutrient basis declared.

**Inference and limits:** Supports agronomic nutrient assessment; availability depends on extraction, soil, crop, season and mineralisation.

**Display label:** Available soil nutrients

**Display measurement:** Field soil samples analysed in a laboratory. Specified mineral-N extraction, P test and exchangeable-K assay, mg/kg with nutrient basis declared.

**Display interpretation:** Helps assess potential nutrient supply to crops. Results depend on the soil test, season and crop needs.

**Measurement origin:** Field soil samples analysed in a laboratory

**Supporting indicators:** [EII:SOI-006](#soi-006); [EII:MIC-023](#mic-023); [EII:AGR-001](#agr-001)

**Primary domain:** D04

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["extractable_mineral_N", "method_defined_available_P", "exchangeable_K"]`

**Record type:** family

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-008","domain":"D04","related_domains":["D13"],"record_type":"family","variants":["extractable_mineral_N","method_defined_available_P","exchangeable_K"],"secondary":["measured"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Available N/P/K are method-defined nutrient fractions rather than total pools.
- **Direct observations / derivation:** Specified mineral-N extraction, P test and exchangeable-K assay, mg/kg with nutrient basis declared.
- **Inference and limits:** Supports agronomic nutrient assessment; availability depends on extraction, soil, crop, season and mineralisation.
- **Supporting indicators:** [EII:SOI-006](#soi-006), [EII:MIC-023](#mic-023), [EII:AGR-001](#agr-001).

<a id="soi-009"></a>

### EII:SOI-009 — Cation exchange capacity

**Definition:** CEC is exchangeable-cation capacity under stated chemical conditions.

**Direct observations / derivation:** Displacement/exchange assay, cmolc/kg; distinguish effective and buffered potential CEC.

**Inference and limits:** Supports nutrient-buffering interpretation; charge, pH and mineralogy affect capacity and actual occupancy.

**Display label:** Nutrient-holding capacity

**Display measurement:** Field soil samples analysed in a laboratory. Displacement/exchange assay, cmolc/kg; distinguish effective and buffered potential CEC.

**Display interpretation:** Helps assess soil's ability to hold nutrient ions. The nutrients actually present and soil acidity also matter.

**Measurement origin:** Field soil samples analysed in a laboratory

**Supporting indicators:** [EII:SOI-006](#soi-006); [EII:SOI-001](#soi-001); [EII:SOI-019](#soi-019)

**Primary domain:** D04

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-009","domain":"D04","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** CEC is exchangeable-cation capacity under stated chemical conditions.
- **Direct observations / derivation:** Displacement/exchange assay, cmolc/kg; distinguish effective and buffered potential CEC.
- **Inference and limits:** Supports nutrient-buffering interpretation; charge, pH and mineralogy affect capacity and actual occupancy.
- **Supporting indicators:** [EII:SOI-006](#soi-006), [EII:SOI-001](#soi-001), [EII:SOI-019](#soi-019).

<a id="soi-010"></a>

### EII:SOI-010 — Soil respiration / CO₂ efflux

**Definition:** Soil respiration is CO₂ release from soil under field or incubation conditions.

**Direct observations / derivation:** Chamber/infrared gas flux, µmol CO₂/m²/s, or incubation mass C/kg/time; identify roots and heterotrophs when possible.

**Inference and limits:** Indicates carbon turnover; high respiration can reflect productivity, warming or C loss and is not inherently healthier.

**Display label:** Soil respiration

**Display measurement:** Field gas chambers or laboratory soil incubations. Chamber/infrared gas flux, µmol CO₂/m²/s, or incubation mass C/kg/time; identify roots and heterotrophs when possible.

**Display interpretation:** Shows carbon dioxide released from soil by roots and organisms. A high rate can reflect activity or carbon loss, rather than better soil health.

**Measurement origin:** Field gas chambers or laboratory soil incubations

**Supporting indicators:** [EII:MIC-007](#mic-007); [EII:SOI-005](#soi-005); [EII:HYD-001](#hyd-001); [EII:SOI-011](#soi-011)

**Primary domain:** D05

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot", "community"], "temporal": ["event", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot", "amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future); AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-010","domain":"D05","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","plot","community"],"temporal":["event","season","year"]},"quaternary":["function"],"routes":["iot","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Soil respiration is CO₂ release from soil under field or incubation conditions.
- **Direct observations / derivation:** Chamber/infrared gas flux, µmol CO₂/m²/s, or incubation mass C/kg/time; identify roots and heterotrophs when possible.
- **Inference and limits:** Indicates carbon turnover; high respiration can reflect productivity, warming or C loss and is not inherently healthier.
- **Supporting indicators:** [EII:MIC-007](#mic-007), [EII:SOI-005](#soi-005), [EII:HYD-001](#hyd-001), [EII:SOI-011](#soi-011).

<a id="soi-011"></a>

### EII:SOI-011 — Soil temperature

**Definition:** Soil temperature is temperature at a declared depth.

**Direct observations / derivation:** Calibrated probe, °C, with depth and recording interval.

**Inference and limits:** Supports biological/hydraulic-rate interpretation; surface temperature cannot substitute for a root-zone profile.

**Display label:** Soil temperature

**Display measurement:** Soil temperature sensors. Calibrated probe, °C, with depth and recording interval.

**Display interpretation:** Helps explain conditions for roots and soil organisms. Temperature near the surface may differ from deeper soil.

**Measurement origin:** Soil temperature sensors

**Supporting indicators:** [EII:HYD-001](#hyd-001); [EII:SOI-010](#soi-010); [EII:DIS-006](#dis-006)

**Primary domain:** D03

**Secondary domains:** `[]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-011","domain":"D03","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Soil temperature is temperature at a declared depth.
- **Direct observations / derivation:** Calibrated probe, °C, with depth and recording interval.
- **Inference and limits:** Supports biological/hydraulic-rate interpretation; surface temperature cannot substitute for a root-zone profile.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:SOI-010](#soi-010), [EII:DIS-006](#dis-006).

<a id="soi-012"></a>

### EII:SOI-012 — Erosion rate / soil loss

**Definition:** Erosion/soil loss is exported or redistributed soil mass per area/time.

**Direct observations / derivation:** Runoff plots, sediment budgets or erosion models, Mg/ha/year; distinguish gross erosion from sediment delivery.

**Inference and limits:** Supports soil-conservation assessment; modelled susceptibility and channel loads do not uniquely establish local soil loss.

**Display label:** Soil erosion rate

**Display measurement:** Field erosion plots, repeat surveys or erosion models. Runoff plots, sediment budgets or erosion models, Mg/ha/year; distinguish gross erosion from sediment delivery.

**Display interpretation:** Helps assess how much soil is being lost or moved. Predicted erosion risk is different from measured soil loss.

**Measurement origin:** Field erosion plots, repeat surveys or erosion models

**Supporting indicators:** [EII:TER-009](#ter-009); [EII:HYD-009](#hyd-009); [EII:VEG-012](#veg-012)

**Primary domain:** D03

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "modelled", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["event", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["terrain", "amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021; AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-012","domain":"D03","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","modelled","process"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["function"],"routes":["terrain","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Erosion/soil loss is exported or redistributed soil mass per area/time.
- **Direct observations / derivation:** Runoff plots, sediment budgets or erosion models, Mg/ha/year; distinguish gross erosion from sediment delivery.
- **Inference and limits:** Supports soil-conservation assessment; modelled susceptibility and channel loads do not uniquely establish local soil loss.
- **Supporting indicators:** [EII:TER-009](#ter-009), [EII:HYD-009](#hyd-009), [EII:VEG-012](#veg-012).

<a id="soi-013"></a>

### EII:SOI-013 — Soil contamination / heavy metals

**Definition:** Contamination records concentration of specified metals or organic pollutants.

**Direct observations / derivation:** Validated chemical assay, mg/kg dry soil; report analyte, fraction and detection limits.

**Inference and limits:** Supports exposure screening; total concentration does not establish bioavailability or food-chain transfer.

**Display label:** Soil contaminants

**Display measurement:** Field soil samples analysed in a laboratory. Validated chemical assay, mg/kg dry soil; report analyte, fraction and detection limits.

**Display interpretation:** Shows the amount of a named pollutant in soil. Total concentration alone does not show how much organisms can absorb.

**Measurement origin:** Field soil samples analysed in a laboratory

**Supporting indicators:** [EII:SOI-006](#soi-006); [EII:SOI-005](#soi-005); [EII:SOI-022](#soi-022)

**Primary domain:** D04

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `["named_total_contaminant", "named_extractable_contaminant"]`

**Record type:** family

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-013","domain":"D04","related_domains":["D13"],"record_type":"family","variants":["named_total_contaminant","named_extractable_contaminant"],"secondary":["measured","pressure"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["pressure"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Contamination records concentration of specified metals or organic pollutants.
- **Direct observations / derivation:** Validated chemical assay, mg/kg dry soil; report analyte, fraction and detection limits.
- **Inference and limits:** Supports exposure screening; total concentration does not establish bioavailability or food-chain transfer.
- **Supporting indicators:** [EII:SOI-006](#soi-006), [EII:SOI-005](#soi-005), [EII:SOI-022](#soi-022).

<a id="mic-001"></a>

### EII:MIC-001 — Bacterial community composition

**Definition:** Bacterial composition describes taxonomic representation within a microbial sample.

**Direct observations / derivation:** 16S/shotgun reads assigned to taxa, proportions; absolute cells/g require independent calibration.

**Inference and limits:** Supports community comparisons; primer, extraction, copy-number and compositional biases prevent equating reads with cells or function.

**Display label:** Bacterial community

**Display measurement:** Laboratory DNA tests and bioinformatics. 16S/shotgun reads assigned to taxa, proportions; absolute cells/g require independent calibration.

**Display interpretation:** Shows which bacterial groups were detected and their relative shares. DNA read counts do not directly show cell numbers or activity.

**Measurement origin:** Laboratory DNA tests and bioinformatics

**Supporting indicators:** [EII:MIC-005](#mic-005); [EII:MIC-025](#mic-025); [EII:SOI-006](#soi-006)

**Primary domain:** D05

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `["R04", "R05"]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Review scope:** specific_documentary_aspects_only

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-001","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":["R04","R05"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** Bacterial composition describes taxonomic representation within a microbial sample.
- **Direct observations / derivation:** 16S/shotgun reads assigned to taxa, proportions; absolute cells/g require independent calibration.
- **Inference and limits:** Supports community comparisons; primer, extraction, copy-number and compositional biases prevent equating reads with cells or function.
- **Supporting indicators:** [EII:MIC-005](#mic-005), [EII:MIC-025](#mic-025), [EII:SOI-006](#soi-006).

<a id="mic-002"></a>

### EII:MIC-002 — Archaeal community composition

**Definition:** Archaeal composition describes sampled archaeal taxonomic representation.

**Direct observations / derivation:** Archaeal marker or shotgun assignments, proportions/copies with method declared.

**Inference and limits:** Supports archaeal habitat/pathway hypotheses; taxonomy does not prove ammonia oxidation or methane production.

**Display label:** Archaeal community

**Display measurement:** Laboratory DNA tests and bioinformatics. Archaeal marker or shotgun assignments, proportions/copies with method declared.

**Display interpretation:** Shows which archaeal groups were detected. Their presence does not prove that they are carrying out a particular process.

**Measurement origin:** Laboratory DNA tests and bioinformatics

**Supporting indicators:** [EII:MIC-011](#mic-011); [EII:CYC-003](#cyc-003); [EII:MIC-025](#mic-025)

**Primary domain:** D05

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `["R04"]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Review scope:** specific_documentary_aspects_only

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-002","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":["R04"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** Archaeal composition describes sampled archaeal taxonomic representation.
- **Direct observations / derivation:** Archaeal marker or shotgun assignments, proportions/copies with method declared.
- **Inference and limits:** Supports archaeal habitat/pathway hypotheses; taxonomy does not prove ammonia oxidation or methane production.
- **Supporting indicators:** [EII:MIC-011](#mic-011), [EII:CYC-003](#cyc-003), [EII:MIC-025](#mic-025).

<a id="mic-003"></a>

### EII:MIC-003 — Fungal community composition

**Definition:** Fungal composition describes sampled fungal taxonomic representation.

**Direct observations / derivation:** ITS/shotgun assignments and relative profiles; record reference release and guild assignment confidence.

**Inference and limits:** Supports fungal-community comparisons; guild labels and reads do not prove realised decomposition, symbiosis or disease.

**Display label:** Fungal community

**Display measurement:** Laboratory DNA tests and bioinformatics. ITS/shotgun assignments and relative profiles; record reference release and guild assignment confidence.

**Display interpretation:** Shows which fungal groups were detected. This can guide further study, but does not establish their effects on plants or decomposition.

**Measurement origin:** Laboratory DNA tests and bioinformatics

**Supporting indicators:** [EII:MIC-014](#mic-014); [EII:MIC-024](#mic-024); [EII:MIC-016](#mic-016)

**Primary domain:** D05

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `["R04"]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Review scope:** specific_documentary_aspects_only

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-003","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":["R04"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** Fungal composition describes sampled fungal taxonomic representation.
- **Direct observations / derivation:** ITS/shotgun assignments and relative profiles; record reference release and guild assignment confidence.
- **Inference and limits:** Supports fungal-community comparisons; guild labels and reads do not prove realised decomposition, symbiosis or disease.
- **Supporting indicators:** [EII:MIC-014](#mic-014), [EII:MIC-024](#mic-024), [EII:MIC-016](#mic-016).

<a id="mic-004"></a>

### EII:MIC-004 — Protist community composition

**Definition:** Protist composition describes sampled protistan taxonomic representation.

**Direct observations / derivation:** 18S/shotgun assignments, relative profiles under stated pipeline.

**Inference and limits:** Supports microbial-food-web hypotheses; marker coverage and taxonomic assignment limit functional interpretation.

**Display label:** Protist community

**Display measurement:** Laboratory DNA tests and bioinformatics. 18S/shotgun assignments, relative profiles under stated pipeline.

**Display interpretation:** Shows which protist groups were detected. Their ecological roles need additional evidence, not just species identification.

**Measurement origin:** Laboratory DNA tests and bioinformatics

**Supporting indicators:** [EII:MIC-005](#mic-005); [EII:BIO-013](#bio-013); [EII:MIC-025](#mic-025)

**Primary domain:** D05

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `["R04"]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Review scope:** specific_documentary_aspects_only

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-004","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":["R04"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** Protist composition describes sampled protistan taxonomic representation.
- **Direct observations / derivation:** 18S/shotgun assignments, relative profiles under stated pipeline.
- **Inference and limits:** Supports microbial-food-web hypotheses; marker coverage and taxonomic assignment limit functional interpretation.
- **Supporting indicators:** [EII:MIC-005](#mic-005), [EII:BIO-013](#bio-013), [EII:MIC-025](#mic-025).

<a id="mic-005"></a>

### EII:MIC-005 — Microbial alpha diversity

**Definition:** Microbial alpha diversity summarises within-sample richness/evenness.

**Direct observations / derivation:** ASV/taxon table and specified richness, Shannon or Hill metric; standardise coverage and filtering.

**Inference and limits:** Supports within-sample comparisons; increased diversity is not universally improved soil function.

**Display label:** Microbial diversity within a sample

**Display measurement:** Laboratory DNA tests and bioinformatics. ASV/taxon table and specified richness, Shannon or Hill metric; standardise coverage and filtering.

**Display interpretation:** Helps compare microbial diversity within samples. More diversity does not always mean better soil function.

**Measurement origin:** Laboratory DNA tests and bioinformatics

**Supporting indicators:** [EII:MIC-001](#mic-001); [EII:MIC-003](#mic-003); [EII:MIC-007](#mic-007)

**Primary domain:** D05

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-005","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Microbial alpha diversity summarises within-sample richness/evenness.
- **Direct observations / derivation:** ASV/taxon table and specified richness, Shannon or Hill metric; standardise coverage and filtering.
- **Inference and limits:** Supports within-sample comparisons; increased diversity is not universally improved soil function.
- **Supporting indicators:** [EII:MIC-001](#mic-001), [EII:MIC-003](#mic-003), [EII:MIC-007](#mic-007).

<a id="mic-006"></a>

### EII:MIC-006 — Microbial beta diversity

**Definition:** Microbial beta diversity describes compositional dissimilarity between samples.

**Direct observations / derivation:** Taxon profiles and declared Bray–Curtis, Jaccard, UniFrac or compositional distance.

**Inference and limits:** Supports community differentiation; dispersion, sequencing coverage and environmental confounding affect tests.

**Display label:** Microbial differences between samples

**Display measurement:** Laboratory DNA tests and bioinformatics. Taxon profiles and declared Bray–Curtis, Jaccard, UniFrac or compositional distance.

**Display interpretation:** Shows how different microbial communities are between samples. Sampling methods and environmental differences can affect the comparison.

**Measurement origin:** Laboratory DNA tests and bioinformatics

**Supporting indicators:** [EII:MIC-005](#mic-005); [EII:MIC-020](#mic-020); [EII:SOI-006](#soi-006)

**Primary domain:** D05

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-006","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Microbial beta diversity describes compositional dissimilarity between samples.
- **Direct observations / derivation:** Taxon profiles and declared Bray–Curtis, Jaccard, UniFrac or compositional distance.
- **Inference and limits:** Supports community differentiation; dispersion, sequencing coverage and environmental confounding affect tests.
- **Supporting indicators:** [EII:MIC-005](#mic-005), [EII:MIC-020](#mic-020), [EII:SOI-006](#soi-006).

<a id="mic-007"></a>

### EII:MIC-007 — Microbial biomass carbon / nitrogen

**Definition:** Microbial biomass C/N estimates living microbial carbon/nitrogen pools.

**Direct observations / derivation:** Fumigation-extraction or specified biomass assay, mg C or N/kg dry soil, with conversion factors.

**Inference and limits:** Supports biomass-pool comparison; method recovery and soil moisture matter, and biomass is not process efficiency.

**Display label:** Microbial biomass

**Display measurement:** Laboratory soil microbial-biomass assays. Fumigation-extraction or specified biomass assay, mg C or N/kg dry soil, with conversion factors.

**Display interpretation:** Estimates the size of the living microbial carbon or nitrogen pool. A larger pool does not necessarily mean faster or more efficient processes.

**Measurement origin:** Laboratory soil microbial-biomass assays

**Supporting indicators:** [EII:SOI-005](#soi-005); [EII:SOI-010](#soi-010); [EII:MIC-019](#mic-019)

**Primary domain:** D05

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot", "community"], "temporal": ["event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["microbial_biomass_C", "microbial_biomass_N"]`

**Record type:** family

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-007","domain":"D05","related_domains":["D13"],"record_type":"family","variants":["microbial_biomass_C","microbial_biomass_N"],"secondary":["measured"],"tertiary":{"spatial":["sample","plot","community"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Microbial biomass C/N estimates living microbial carbon/nitrogen pools.
- **Direct observations / derivation:** Fumigation-extraction or specified biomass assay, mg C or N/kg dry soil, with conversion factors.
- **Inference and limits:** Supports biomass-pool comparison; method recovery and soil moisture matter, and biomass is not process efficiency.
- **Supporting indicators:** [EII:SOI-005](#soi-005), [EII:SOI-010](#soi-010), [EII:MIC-019](#mic-019).

<a id="mic-008"></a>

### EII:MIC-008 — Fungal:bacterial abundance ratio

**Definition:** Fungal:bacterial ratio compares two method-defined microbial signals.

**Direct observations / derivation:** PLFA biomarkers, calibrated qPCR or other declared abundance measures, ratio; avoid raw cross-marker read ratios.

**Inference and limits:** Supports broad community comparison within a consistent assay; ratios do not establish health or functional dominance.

**Display label:** Fungal:bacterial ratio

**Display measurement:** Laboratory lipid or calibrated DNA assays. PLFA biomarkers, calibrated qPCR or other declared abundance measures, ratio; avoid raw cross-marker read ratios.

**Display interpretation:** Helps compare fungal and bacterial signals within the same test method. The ratio alone does not diagnose soil health.

**Measurement origin:** Laboratory lipid or calibrated DNA assays

**Supporting indicators:** [EII:MIC-007](#mic-007); [EII:MIC-003](#mic-003); [EII:MIC-001](#mic-001)

**Primary domain:** D05

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `["R05"]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Review scope:** specific_documentary_aspects_only

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-008","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":["R05"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** Fungal:bacterial ratio compares two method-defined microbial signals.
- **Direct observations / derivation:** PLFA biomarkers, calibrated qPCR or other declared abundance measures, ratio; avoid raw cross-marker read ratios.
- **Inference and limits:** Supports broad community comparison within a consistent assay; ratios do not establish health or functional dominance.
- **Supporting indicators:** [EII:MIC-007](#mic-007), [EII:MIC-003](#mic-003), [EII:MIC-001](#mic-001).

<a id="mic-009"></a>

### EII:MIC-009 — Carbon-degradation gene/pathway potential

**Definition:** Carbon-degradation genetic potential describes annotated genes/pathways for organic-C processing.

**Direct observations / derivation:** Shotgun/qPCR gene counts normalised to stated denominator; report annotation release and pathway completeness.

**Inference and limits:** Indicates encoded potential; gene presence does not establish expression, substrate access or decomposition rate.

**Display label:** Carbon-breakdown genes

**Display measurement:** Laboratory DNA tests and bioinformatics. Shotgun/qPCR gene counts normalised to stated denominator; report annotation release and pathway completeness.

**Display interpretation:** Shows genetic potential to break down organic material. Genes alone do not show how fast decomposition is happening.

**Measurement origin:** Laboratory DNA tests and bioinformatics

**Supporting indicators:** [EII:MIC-022](#mic-022); [EII:MIC-019](#mic-019); [EII:MIC-024](#mic-024)

**Primary domain:** D09

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "inferred"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `["R04"]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Review scope:** specific_documentary_aspects_only

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-009","domain":"D09","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","inferred"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":["R04"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** Carbon-degradation genetic potential describes annotated genes/pathways for organic-C processing.
- **Direct observations / derivation:** Shotgun/qPCR gene counts normalised to stated denominator; report annotation release and pathway completeness.
- **Inference and limits:** Indicates encoded potential; gene presence does not establish expression, substrate access or decomposition rate.
- **Supporting indicators:** [EII:MIC-022](#mic-022), [EII:MIC-019](#mic-019), [EII:MIC-024](#mic-024).

<a id="mic-010"></a>

### EII:MIC-010 — Nitrogen-fixation genetic potential

**Definition:** N-fixation genetic potential describes markers of biological nitrogen fixation.

**Direct observations / derivation:** nifH or validated pathway genes, copies/g or normalised abundance; evaluate homolog specificity.

**Inference and limits:** Supports diazotrophic-potential hypotheses; presence does not quantify fixation and some homologs have other functions.

**Display label:** Nitrogen-fixation genes

**Display measurement:** Laboratory DNA tests and bioinformatics. nifH or validated pathway genes, copies/g or normalised abundance; evaluate homolog specificity.

**Display interpretation:** Shows genetic potential to use nitrogen from the air. Measuring actual nitrogen fixation requires a separate process test.

**Measurement origin:** Laboratory DNA tests and bioinformatics

**Supporting indicators:** [EII:CYC-004](#cyc-004); [EII:MIC-022](#mic-022); [EII:SOI-008](#soi-008)

**Primary domain:** D09

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "inferred"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-010","domain":"D09","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","inferred"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** N-fixation genetic potential describes markers of biological nitrogen fixation.
- **Direct observations / derivation:** nifH or validated pathway genes, copies/g or normalised abundance; evaluate homolog specificity.
- **Inference and limits:** Supports diazotrophic-potential hypotheses; presence does not quantify fixation and some homologs have other functions.
- **Supporting indicators:** [EII:CYC-004](#cyc-004), [EII:MIC-022](#mic-022), [EII:SOI-008](#soi-008).

<a id="mic-011"></a>

### EII:MIC-011 — Nitrification genetic potential

**Definition:** Nitrification genetic potential describes ammonia/nitrite oxidation capacity encoded in DNA.

**Direct observations / derivation:** amoA and suitable pathway markers, copies/g or normalised abundance, with archaeal/bacterial/comammox coverage.

**Inference and limits:** Supports nitrifier-potential assessment; marker abundance does not establish realised nitrification.

**Display label:** Nitrification genes

**Display measurement:** Laboratory DNA tests and bioinformatics. amoA and suitable pathway markers, copies/g or normalised abundance, with archaeal/bacterial/comammox coverage.

**Display interpretation:** Shows genetic potential for certain nitrogen transformations. It does not measure how fast those transformations occur.

**Measurement origin:** Laboratory DNA tests and bioinformatics

**Supporting indicators:** [EII:MIC-023](#mic-023); [EII:MIC-022](#mic-022); [EII:SOI-008](#soi-008)

**Primary domain:** D09

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "inferred"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-011","domain":"D09","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","inferred"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Nitrification genetic potential describes ammonia/nitrite oxidation capacity encoded in DNA.
- **Direct observations / derivation:** amoA and suitable pathway markers, copies/g or normalised abundance, with archaeal/bacterial/comammox coverage.
- **Inference and limits:** Supports nitrifier-potential assessment; marker abundance does not establish realised nitrification.
- **Supporting indicators:** [EII:MIC-023](#mic-023), [EII:MIC-022](#mic-022), [EII:SOI-008](#soi-008).

<a id="mic-012"></a>

### EII:MIC-012 — Denitrification genetic potential

**Definition:** Denitrification potential records encoded nitrate/nitrite reduction and N₂O reduction pathways.

**Direct observations / derivation:** nirK/nirS, nor, nosZ and other stated genes, normalised abundance or copies/g; separate pathway steps.

**Inference and limits:** Supports pathway-potential hypotheses; incomplete pathways and environment prevent prediction of N₂O flux from DNA alone.

**Display label:** Denitrification genes

**Display measurement:** Laboratory DNA tests and bioinformatics. nirK/nirS, nor, nosZ and other stated genes, normalised abundance or copies/g; separate pathway steps.

**Display interpretation:** Shows genetic potential to convert nitrate into gases. Actual gas production depends on conditions and the steps present in the pathway.

**Measurement origin:** Laboratory DNA tests and bioinformatics

**Supporting indicators:** [EII:CYC-005](#cyc-005); [EII:CYC-002](#cyc-002); [EII:MIC-022](#mic-022); [EII:HYD-001](#hyd-001)

**Primary domain:** D09

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "inferred"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-012","domain":"D09","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","inferred"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Denitrification potential records encoded nitrate/nitrite reduction and N₂O reduction pathways.
- **Direct observations / derivation:** nirK/nirS, nor, nosZ and other stated genes, normalised abundance or copies/g; separate pathway steps.
- **Inference and limits:** Supports pathway-potential hypotheses; incomplete pathways and environment prevent prediction of N₂O flux from DNA alone.
- **Supporting indicators:** [EII:CYC-005](#cyc-005), [EII:CYC-002](#cyc-002), [EII:MIC-022](#mic-022), [EII:HYD-001](#hyd-001).

<a id="mic-013"></a>

### EII:MIC-013 — Phosphorus solubilisation / acquisition potential

**Definition:** P-acquisition potential describes encoded P mobilisation, mineralisation or uptake functions.

**Direct observations / derivation:** Annotated phosphatase, transport and other validated marker genes; distinguish mineralisation from solubilisation.

**Inference and limits:** Supports P-processing hypotheses; annotated capacity does not quantify P release or plant uptake.

**Display label:** Phosphorus-acquisition genes

**Display measurement:** Laboratory DNA tests and bioinformatics. Annotated phosphatase, transport and other validated marker genes; distinguish mineralisation from solubilisation.

**Display interpretation:** Shows possible genetic capacity to obtain or release phosphorus. It does not measure phosphorus made available to plants.

**Measurement origin:** Laboratory DNA tests and bioinformatics

**Supporting indicators:** [EII:MIC-019](#mic-019); [EII:SOI-008](#soi-008); [EII:CYC-006](#cyc-006)

**Primary domain:** D09

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "inferred"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-013","domain":"D09","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","inferred"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** P-acquisition potential describes encoded P mobilisation, mineralisation or uptake functions.
- **Direct observations / derivation:** Annotated phosphatase, transport and other validated marker genes; distinguish mineralisation from solubilisation.
- **Inference and limits:** Supports P-processing hypotheses; annotated capacity does not quantify P release or plant uptake.
- **Supporting indicators:** [EII:MIC-019](#mic-019), [EII:SOI-008](#soi-008), [EII:CYC-006](#cyc-006).

<a id="mic-014"></a>

### EII:MIC-014 — Mycorrhizal community / colonisation

**Definition:** Mycorrhizal composition and root colonisation describe distinct symbiotic observations.

**Direct observations / derivation:** Fungal assignments and microscopy of colonised root length, %; report structures and host.

**Inference and limits:** Supports assessment of symbiotic association; DNA presence or colonisation does not quantify nutrient transfer or benefit.

**Display label:** Root-associated fungi

**Display measurement:** Laboratory root microscopy and fungal DNA tests. Fungal assignments and microscopy of colonised root length, %; report structures and host.

**Display interpretation:** Shows fungi associated with roots or how much root is colonised. This does not by itself show nutrient transfer or plant benefit.

**Measurement origin:** Laboratory root microscopy and fungal DNA tests

**Supporting indicators:** [EII:VEG-017](#veg-017); [EII:SOI-008](#soi-008); [EII:INT-006](#int-006)

**Primary domain:** D08

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["mycorrhizal_composition", "root_colonisation"]`

**Record type:** family

**Candidate source routes:** `["bio", "amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future); AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-014","domain":"D08","related_domains":["D13"],"record_type":"family","variants":["mycorrhizal_composition","root_colonisation"],"secondary":["measured","derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Mycorrhizal composition and root colonisation describe distinct symbiotic observations.
- **Direct observations / derivation:** Fungal assignments and microscopy of colonised root length, %; report structures and host.
- **Inference and limits:** Supports assessment of symbiotic association; DNA presence or colonisation does not quantify nutrient transfer or benefit.
- **Supporting indicators:** [EII:VEG-017](#veg-017), [EII:SOI-008](#soi-008), [EII:INT-006](#int-006).

<a id="mic-015"></a>

### EII:MIC-015 — Rhizosphere-associated community structure

**Definition:** Rhizosphere structure is community composition in root-associated soil relative to a defined comparator.

**Direct observations / derivation:** Paired rhizosphere/bulk samples and taxon/function profiles, proportions or dissimilarity.

**Inference and limits:** Supports plant-associated enrichment hypotheses; soil gradients and sampling separation confound causal host effects.

**Display label:** Microbes around roots

**Display measurement:** Laboratory DNA tests and bioinformatics. Paired rhizosphere/bulk samples and taxon/function profiles, proportions or dissimilarity.

**Display interpretation:** Shows how microbes near roots differ from those in surrounding soil. Other soil differences may also explain the pattern.

**Measurement origin:** Laboratory DNA tests and bioinformatics

**Supporting indicators:** [EII:MIC-001](#mic-001); [EII:MIC-003](#mic-003); [EII:VEG-017](#veg-017)

**Primary domain:** D08

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-015","domain":"D08","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Rhizosphere structure is community composition in root-associated soil relative to a defined comparator.
- **Direct observations / derivation:** Paired rhizosphere/bulk samples and taxon/function profiles, proportions or dissimilarity.
- **Inference and limits:** Supports plant-associated enrichment hypotheses; soil gradients and sampling separation confound causal host effects.
- **Supporting indicators:** [EII:MIC-001](#mic-001), [EII:MIC-003](#mic-003), [EII:VEG-017](#veg-017).

<a id="mic-016"></a>

### EII:MIC-016 — Potential plant pathogens / beneficial taxa

**Definition:** Potential pathogens/beneficial taxa are organisms or markers associated with specified outcomes.

**Direct observations / derivation:** Validated taxon/virulence assignments or qPCR, detection and copies/g; retain strain and reference uncertainty.

**Inference and limits:** Supports targeted follow-up; species identity alone does not establish pathogenicity, viability or disease suppression.

**Display label:** Potential harmful or beneficial microbes

**Display measurement:** Laboratory DNA tests and bioinformatics. Validated taxon/virulence assignments or qPCR, detection and copies/g; retain strain and reference uncertainty.

**Display interpretation:** Flags organisms or genes that may be associated with disease or benefits. Confirming either effect needs additional tests.

**Measurement origin:** Laboratory DNA tests and bioinformatics

**Supporting indicators:** [EII:AGR-005](#agr-005); [EII:INT-009](#int-009); [EII:MIC-022](#mic-022)

**Primary domain:** D08

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "inferred"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["validated_pathogen_marker", "candidate_beneficial_taxon"]`

**Record type:** family

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-016","domain":"D08","related_domains":[],"record_type":"family","variants":["validated_pathogen_marker","candidate_beneficial_taxon"],"secondary":["derived","inferred"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Potential pathogens/beneficial taxa are organisms or markers associated with specified outcomes.
- **Direct observations / derivation:** Validated taxon/virulence assignments or qPCR, detection and copies/g; retain strain and reference uncertainty.
- **Inference and limits:** Supports targeted follow-up; species identity alone does not establish pathogenicity, viability or disease suppression.
- **Supporting indicators:** [EII:AGR-005](#agr-005), [EII:INT-009](#int-009), [EII:MIC-022](#mic-022).

<a id="mic-017"></a>

### EII:MIC-017 — Drought / salinity stress-response gene potential

**Definition:** Stress-response potential describes encoded responses to declared environmental stresses.

**Direct observations / derivation:** Annotated osmotic, oxidative or drought-associated genes, normalised abundance.

**Inference and limits:** Suggests possible response capacity; common multifunctional genes cannot prove community or ecosystem resilience.

**Display label:** Microbial stress-response genes

**Display measurement:** Laboratory DNA tests and bioinformatics. Annotated osmotic, oxidative or drought-associated genes, normalised abundance.

**Display interpretation:** Shows genes that may help microbes respond to stress. Their presence does not prove the community will withstand drought or salt.

**Measurement origin:** Laboratory DNA tests and bioinformatics

**Supporting indicators:** [EII:HYD-001](#hyd-001); [EII:SOI-007](#soi-007); [EII:RES-001](#res-001)

**Primary domain:** D12

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "inferred"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["disturbance_response", "restoration_assessment"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-017","domain":"D12","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","inferred"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Stress-response potential describes encoded responses to declared environmental stresses.
- **Direct observations / derivation:** Annotated osmotic, oxidative or drought-associated genes, normalised abundance.
- **Inference and limits:** Suggests possible response capacity; common multifunctional genes cannot prove community or ecosystem resilience.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:SOI-007](#soi-007), [EII:RES-001](#res-001).

<a id="mic-018"></a>

### EII:MIC-018 — Pollutant degradation gene potential

**Definition:** Pollutant-degradation potential describes encoded transformation pathways.

**Direct observations / derivation:** Validated marker/pathway abundance, copies/g or normalised counts; specify chemical target.

**Inference and limits:** Suggests biodegradation capacity; genes alone cannot establish removal rate, detoxification or complete mineralisation.

**Display label:** Pollutant-breakdown genes

**Display measurement:** Laboratory DNA tests and bioinformatics. Validated marker/pathway abundance, copies/g or normalised counts; specify chemical target.

**Display interpretation:** Shows genetic potential to transform named pollutants. Actual removal and whether products remain harmful need separate tests.

**Measurement origin:** Laboratory DNA tests and bioinformatics

**Supporting indicators:** [EII:SOI-013](#soi-013); [EII:CYC-009](#cyc-009); [EII:MIC-022](#mic-022)

**Primary domain:** D09

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "inferred"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-018","domain":"D09","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","inferred"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Pollutant-degradation potential describes encoded transformation pathways.
- **Direct observations / derivation:** Validated marker/pathway abundance, copies/g or normalised counts; specify chemical target.
- **Inference and limits:** Suggests biodegradation capacity; genes alone cannot establish removal rate, detoxification or complete mineralisation.
- **Supporting indicators:** [EII:SOI-013](#soi-013), [EII:CYC-009](#cyc-009), [EII:MIC-022](#mic-022).

<a id="mic-019"></a>

### EII:MIC-019 — Extracellular enzyme activity

**Definition:** Extracellular enzyme activity is substrate conversion under a specified assay.

**Direct observations / derivation:** Fluorometric/colorimetric product formation per dry soil mass/time, nmol/g/h; declare substrate, pH and temperature.

**Inference and limits:** Measures assay activity; often potential activity at supplied substrate levels rather than in situ flux.

**Display label:** Soil enzyme activity

**Display measurement:** Laboratory enzyme assays. Fluorometric/colorimetric product formation per dry soil mass/time, nmol/g/h; declare substrate, pH and temperature.

**Display interpretation:** Shows how quickly enzymes act in a laboratory test. The same process may run at a different rate in the field.

**Measurement origin:** Laboratory enzyme assays

**Supporting indicators:** [EII:SOI-011](#soi-011); [EII:SOI-006](#soi-006); [EII:MIC-024](#mic-024)

**Primary domain:** D05

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample"], "temporal": ["assay_interval", "sampling_event"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-019","domain":"D05","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample"],"temporal":["assay_interval","sampling_event"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Extracellular enzyme activity is substrate conversion under a specified assay.
- **Direct observations / derivation:** Fluorometric/colorimetric product formation per dry soil mass/time, nmol/g/h; declare substrate, pH and temperature.
- **Inference and limits:** Measures assay activity; often potential activity at supplied substrate levels rather than in situ flux.
- **Supporting indicators:** [EII:SOI-011](#soi-011), [EII:SOI-006](#soi-006), [EII:MIC-024](#mic-024).

<a id="mic-020"></a>

### EII:MIC-020 — Community turnover along land-use gradients

**Definition:** Land-use community turnover describes microbial differences along independently recorded management gradients.

**Direct observations / derivation:** Matched taxon profiles and land-use data, dissimilarity/effect size with repeated or paired design.

**Inference and limits:** Supports land-use associations; confounded soil, geography and season do not establish management causality.

**Display label:** Microbial changes across land uses

**Display measurement:** Laboratory DNA profiles paired with land-use records. Matched taxon profiles and land-use data, dissimilarity/effect size with repeated or paired design.

**Display interpretation:** Shows how microbial communities differ across land uses. Soil type, location and season can also explain differences.

**Measurement origin:** Laboratory DNA profiles paired with land-use records

**Supporting indicators:** [EII:MIC-006](#mic-006); [EII:DIS-004](#dis-004); [EII:SOI-006](#soi-006)

**Primary domain:** D05

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio", "land", "amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS005, RS006, RS009; Bioinformatics (future); AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-020","domain":"D05","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio","land","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Land-use community turnover describes microbial differences along independently recorded management gradients.
- **Direct observations / derivation:** Matched taxon profiles and land-use data, dissimilarity/effect size with repeated or paired design.
- **Inference and limits:** Supports land-use associations; confounded soil, geography and season do not establish management causality.
- **Supporting indicators:** [EII:MIC-006](#mic-006), [EII:DIS-004](#dis-004), [EII:SOI-006](#soi-006).

<a id="mic-021"></a>

### EII:MIC-021 — Spatial microbial community similarity / connectivity

**Definition:** Spatial similarity/connectivity describes community distance relationships or tested movement estimates.

**Direct observations / derivation:** Taxon dissimilarity versus geographic/environmental distance; connectivity only with explicit model or tracing evidence.

**Inference and limits:** Supports biogeographic pattern assessment; similarity or co-occurrence is not proof of dispersal or interaction.

**Display label:** Microbial similarity across places

**Display measurement:** Laboratory DNA profiles paired with sample locations. Taxon dissimilarity versus geographic/environmental distance; connectivity only with explicit model or tracing evidence.

**Display interpretation:** Shows how microbial communities vary across places. Similar communities do not prove that microbes move between them.

**Measurement origin:** Laboratory DNA profiles paired with sample locations

**Supporting indicators:** [EII:MIC-006](#mic-006); [EII:BIO-007](#bio-007); [EII:SOI-001](#soi-001)

**Primary domain:** D05

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-021","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","modelled"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Spatial similarity/connectivity describes community distance relationships or tested movement estimates.
- **Direct observations / derivation:** Taxon dissimilarity versus geographic/environmental distance; connectivity only with explicit model or tracing evidence.
- **Inference and limits:** Supports biogeographic pattern assessment; similarity or co-occurrence is not proof of dispersal or interaction.
- **Supporting indicators:** [EII:MIC-006](#mic-006), [EII:BIO-007](#bio-007), [EII:SOI-001](#soi-001).

<a id="mic-022"></a>

### EII:MIC-022 — Metatranscriptomic expression of functional genes

**Definition:** Metatranscriptomic expression describes sampled community RNA assigned to genes.

**Direct observations / derivation:** RNA reads with stated normalisation and matched DNA abundance where possible; report preservation and controls.

**Inference and limits:** Supports transcription-at-sampling interpretation; RNA quantity does not establish translated enzyme activity or process flux.

**Display label:** Microbial gene expression

**Display measurement:** Laboratory RNA sequencing and bioinformatics. RNA reads with stated normalisation and matched DNA abundance where possible; report preservation and controls.

**Display interpretation:** Shows which genes were being expressed when a sample was taken. This is not a direct measurement of the resulting process rate.

**Measurement origin:** Laboratory RNA sequencing and bioinformatics

**Supporting indicators:** [EII:MIC-009](#mic-009); [EII:MIC-019](#mic-019); [EII:MIC-023](#mic-023)

**Primary domain:** D05

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `["R04"]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Review scope:** specific_documentary_aspects_only

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-022","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":["R04"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** Metatranscriptomic expression describes sampled community RNA assigned to genes.
- **Direct observations / derivation:** RNA reads with stated normalisation and matched DNA abundance where possible; report preservation and controls.
- **Inference and limits:** Supports transcription-at-sampling interpretation; RNA quantity does not establish translated enzyme activity or process flux.
- **Supporting indicators:** [EII:MIC-009](#mic-009), [EII:MIC-019](#mic-019), [EII:MIC-023](#mic-023).

<a id="mic-023"></a>

### EII:MIC-023 — Nitrogen mineralisation / nitrification rate

**Definition:** Mineralisation/nitrification rates quantify separate realised N transformations.

**Direct observations / derivation:** Incubation changes in mineral-N, mg N/kg/day, or isotope-based gross rates; distinguish net and gross processes.

**Inference and limits:** Supports N-transformation assessment under assay conditions; substrate additions and incubations alter field behaviour.

**Display label:** Nitrogen transformation rates

**Display measurement:** Laboratory soil incubations or field nitrogen-rate tests. Incubation changes in mineral-N, mg N/kg/day, or isotope-based gross rates; distinguish net and gross processes.

**Display interpretation:** Measures nitrogen changes during a defined test. Laboratory conditions may differ from those in the field.

**Measurement origin:** Laboratory soil incubations or field nitrogen-rate tests

**Supporting indicators:** [EII:SOI-008](#soi-008); [EII:HYD-001](#hyd-001); [EII:MIC-011](#mic-011)

**Primary domain:** D09

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot", "ecosystem", "watershed"], "temporal": ["hour", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `["net_N_mineralisation", "gross_N_mineralisation", "net_nitrification", "gross_nitrification"]`

**Record type:** family

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-023","domain":"D09","related_domains":["D13"],"record_type":"family","variants":["net_N_mineralisation","gross_N_mineralisation","net_nitrification","gross_nitrification"],"secondary":["measured","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Mineralisation/nitrification rates quantify separate realised N transformations.
- **Direct observations / derivation:** Incubation changes in mineral-N, mg N/kg/day, or isotope-based gross rates; distinguish net and gross processes.
- **Inference and limits:** Supports N-transformation assessment under assay conditions; substrate additions and incubations alter field behaviour.
- **Supporting indicators:** [EII:SOI-008](#soi-008), [EII:HYD-001](#hyd-001), [EII:MIC-011](#mic-011).

<a id="mic-024"></a>

### EII:MIC-024 — Decomposition / litter mass-loss rate

**Definition:** Decomposition rate is loss or transformation of a defined organic substrate over time.

**Direct observations / derivation:** Litter dry-mass loss, %, or fitted decay constant k, time⁻¹; correct handling losses and describe bags/substrate.

**Inference and limits:** Supports realised decay assessment; leaching, fragmentation and fauna contribute, so mass loss is not solely microbial respiration.

**Display label:** Litter decomposition

**Display measurement:** Field litter bags or controlled laboratory tests. Litter dry-mass loss, %, or fitted decay constant k, time⁻¹; correct handling losses and describe bags/substrate.

**Display interpretation:** Shows how quickly litter loses mass. Microbes, animals, leaching and physical breakdown can all contribute.

**Measurement origin:** Field litter bags or controlled laboratory tests

**Supporting indicators:** [EII:MIC-019](#mic-019); [EII:SOI-010](#soi-010); [EII:SOI-011](#soi-011)

**Primary domain:** D09

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "derived", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot", "ecosystem"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-024","domain":"D09","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","derived","process"],"tertiary":{"spatial":["sample","plot","ecosystem"],"temporal":["day","season","year"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Decomposition rate is loss or transformation of a defined organic substrate over time.
- **Direct observations / derivation:** Litter dry-mass loss, %, or fitted decay constant k, time⁻¹; correct handling losses and describe bags/substrate.
- **Inference and limits:** Supports realised decay assessment; leaching, fragmentation and fauna contribute, so mass loss is not solely microbial respiration.
- **Supporting indicators:** [EII:MIC-019](#mic-019), [EII:SOI-010](#soi-010), [EII:SOI-011](#soi-011).

<a id="bio-001"></a>

### EII:BIO-001 — Species richness

**Definition:** Species richness is the number of distinct taxa in a declared sampling unit.

**Direct observations / derivation:** Standardised taxon detections and effort, species count; state coverage and taxonomic resolution.

**Inference and limits:** Supports detected diversity comparison; incomplete detection and effort prevent treating counts as total richness.

**Display label:** Species richness

**Display measurement:** Field species surveys or validated laboratory DNA detections. Standardised taxon detections and effort, species count; state coverage and taxonomic resolution.

**Display interpretation:** Shows how many species were detected. Sampling effort and missed species affect the total.

**Measurement origin:** Field species surveys or validated laboratory DNA detections

**Supporting indicators:** [EII:BIO-002](#bio-002); [EII:BIO-003](#bio-003); [EII:VEG-017](#veg-017)

**Primary domain:** D06

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:BIO-001","domain":"D06","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Species richness is the number of distinct taxa in a declared sampling unit.
- **Direct observations / derivation:** Standardised taxon detections and effort, species count; state coverage and taxonomic resolution.
- **Inference and limits:** Supports detected diversity comparison; incomplete detection and effort prevent treating counts as total richness.
- **Supporting indicators:** [EII:BIO-002](#bio-002), [EII:BIO-003](#bio-003), [EII:VEG-017](#veg-017).

<a id="bio-002"></a>

### EII:BIO-002 — Species abundance / occupancy

**Definition:** Abundance and occupancy are separate population quantities.

**Direct observations / derivation:** Counts/density and repeated detection histories; occupancy estimated with an explicit detection model, individuals/area or probability.

**Inference and limits:** Supports population status; detection/non-detection or sequence reads alone do not equal abundance or occupancy.

**Display label:** Species numbers and occupancy

**Display measurement:** Repeated field species surveys with detection models. Counts/density and repeated detection histories; occupancy estimated with an explicit detection model, individuals/area or probability.

**Display interpretation:** Helps assess population size or the likelihood a species uses a place. Failure to detect a species does not prove absence.

**Measurement origin:** Repeated field species surveys with detection models

**Supporting indicators:** [EII:BIO-001](#bio-001); [EII:BIO-014](#bio-014); [EII:BIO-011](#bio-011)

**Primary domain:** D06

**Secondary domains:** `[]`

**Classification dimensions:** `["observed", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["population_abundance", "modelled_occupancy"]`

**Record type:** family

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:BIO-002","domain":"D06","related_domains":[],"record_type":"family","variants":["population_abundance","modelled_occupancy"],"secondary":["observed","modelled"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Abundance and occupancy are separate population quantities.
- **Direct observations / derivation:** Counts/density and repeated detection histories; occupancy estimated with an explicit detection model, individuals/area or probability.
- **Inference and limits:** Supports population status; detection/non-detection or sequence reads alone do not equal abundance or occupancy.
- **Supporting indicators:** [EII:BIO-001](#bio-001), [EII:BIO-014](#bio-014), [EII:BIO-011](#bio-011).

<a id="bio-003"></a>

### EII:BIO-003 — Shannon / Simpson diversity

**Definition:** Shannon/Simpson indices summarise taxon abundance distribution.

**Direct observations / derivation:** H=−Σp ln p; Simpson specify concentration Σp², complement or reciprocal; dimensionless.

**Inference and limits:** Supports richness/evenness comparison; formulas and effort must match and one index does not establish integrity.

**Display label:** Species diversity indices

**Display measurement:** Field counts or laboratory taxon profiles, followed by calculation. H=−Σp ln p; Simpson specify concentration Σp², complement or reciprocal; dimensionless.

**Display interpretation:** Summarises species diversity and how evenly individuals are distributed. Compare only results using the same index and sampling approach.

**Measurement origin:** Field counts or laboratory taxon profiles, followed by calculation

**Supporting indicators:** [EII:BIO-001](#bio-001); [EII:BIO-002](#bio-002); [EII:BIO-004](#bio-004)

**Primary domain:** D06

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["Shannon_H", "Simpson_concentration", "Simpson_complement", "inverse_Simpson"]`

**Record type:** family

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:BIO-003","domain":"D06","related_domains":[],"record_type":"family","variants":["Shannon_H","Simpson_concentration","Simpson_complement","inverse_Simpson"],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Shannon/Simpson indices summarise taxon abundance distribution.
- **Direct observations / derivation:** H=−Σp ln p; Simpson specify concentration Σp², complement or reciprocal; dimensionless.
- **Inference and limits:** Supports richness/evenness comparison; formulas and effort must match and one index does not establish integrity.
- **Supporting indicators:** [EII:BIO-001](#bio-001), [EII:BIO-002](#bio-002), [EII:BIO-004](#bio-004).

<a id="bio-004"></a>

### EII:BIO-004 — Functional diversity

**Definition:** Functional diversity describes variation in measured organism traits.

**Direct observations / derivation:** Trait values, abundance weights and declared metric such as functional dispersion or Rao Q.

**Inference and limits:** Supports functional-composition comparisons; trait gaps and redundancy prevent equating diversity with process rate.

**Display label:** Trait diversity

**Display measurement:** Field/laboratory trait measurements and species counts. Trait values, abundance weights and declared metric such as functional dispersion or Rao Q.

**Display interpretation:** Shows how varied organisms' traits are. Trait diversity alone does not measure the processes those organisms perform.

**Measurement origin:** Field/laboratory trait measurements and species counts

**Supporting indicators:** [EII:BIO-001](#bio-001); [EII:VEG-017](#veg-017); [EII:FUN-001](#fun-001)

**Primary domain:** D06

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:BIO-004","domain":"D06","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Functional diversity describes variation in measured organism traits.
- **Direct observations / derivation:** Trait values, abundance weights and declared metric such as functional dispersion or Rao Q.
- **Inference and limits:** Supports functional-composition comparisons; trait gaps and redundancy prevent equating diversity with process rate.
- **Supporting indicators:** [EII:BIO-001](#bio-001), [EII:VEG-017](#veg-017), [EII:FUN-001](#fun-001).

<a id="bio-005"></a>

### EII:BIO-005 — Habitat area / quality

**Definition:** Habitat area and quality describe extent and separately assessed condition for a target ecosystem/taxon.

**Direct observations / derivation:** Validated habitat polygons, ha; quality from explicit field attributes/reference model, declared units.

**Inference and limits:** Supports habitat assessment; class labels or area do not prove suitability or integrity for every species.

**Display label:** Habitat area and condition

**Display measurement:** Satellite habitat maps and field condition surveys. Validated habitat polygons, ha; quality from explicit field attributes/reference model, declared units.

**Display interpretation:** Shows habitat extent or its condition for a stated purpose. A mapped habitat class is not suitable for every species.

**Measurement origin:** Satellite habitat maps and field condition surveys

**Supporting indicators:** [EII:BIO-002](#bio-002); [EII:TER-013](#ter-013); [EII:FUN-013](#fun-013)

**Primary domain:** D06

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "population", "community", "landscape"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["habitat_extent", "reference_based_quality"]`

**Record type:** family

**Candidate source routes:** `["land"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS005, RS006, RS009

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:BIO-005","domain":"D06","related_domains":[],"record_type":"family","variants":["habitat_extent","reference_based_quality"],"secondary":["derived","modelled"],"tertiary":{"spatial":["organism","population","community","landscape"],"temporal":["season","year"]},"quaternary":["state"],"routes":["land"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Habitat area and quality describe extent and separately assessed condition for a target ecosystem/taxon.
- **Direct observations / derivation:** Validated habitat polygons, ha; quality from explicit field attributes/reference model, declared units.
- **Inference and limits:** Supports habitat assessment; class labels or area do not prove suitability or integrity for every species.
- **Supporting indicators:** [EII:BIO-002](#bio-002), [EII:TER-013](#ter-013), [EII:FUN-013](#fun-013).

<a id="bio-006"></a>

### EII:BIO-006 — Landscape fragmentation / patch size

**Definition:** Fragmentation/patch size describe spatial subdivision of a stated habitat class.

**Direct observations / derivation:** Class map and patch metrics, ha, count or index; record grain, extent and adjacency.

**Inference and limits:** Supports habitat-pattern interpretation; fragmentation depends on focal habitat and is not uniformly harmful across taxa.

**Display label:** Habitat fragmentation

**Display measurement:** Satellite or field-validated habitat maps. Class map and patch metrics, ha, count or index; record grain, extent and adjacency.

**Display interpretation:** Shows how habitat is divided into patches. The consequences depend on the habitat and species being studied.

**Measurement origin:** Satellite or field-validated habitat maps

**Supporting indicators:** [EII:BIO-007](#bio-007); [EII:BIO-005](#bio-005); [EII:LAN-001](#lan-001)

**Primary domain:** D10

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["landscape", "watershed", "region"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["land"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS005, RS006, RS009

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:BIO-006","domain":"D10","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["state"],"routes":["land"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fragmentation/patch size describe spatial subdivision of a stated habitat class.
- **Direct observations / derivation:** Class map and patch metrics, ha, count or index; record grain, extent and adjacency.
- **Inference and limits:** Supports habitat-pattern interpretation; fragmentation depends on focal habitat and is not uniformly harmful across taxa.
- **Supporting indicators:** [EII:BIO-007](#bio-007), [EII:BIO-005](#bio-005), [EII:LAN-001](#lan-001).

<a id="bio-007"></a>

### EII:BIO-007 — Habitat connectivity / corridor suitability

**Definition:** Connectivity/corridor suitability describe structural connection or modelled movement opportunity.

**Direct observations / derivation:** Habitat distances, resistance surfaces and declared graph/circuit model; validate with movement/genetic evidence.

**Inference and limits:** Supports movement hypotheses; structural corridors do not prove functional use or gene flow.

**Display label:** Habitat connectivity

**Display measurement:** Habitat maps and movement models, checked with field/genetic evidence. Habitat distances, resistance surfaces and declared graph/circuit model; validate with movement/genetic evidence.

**Display interpretation:** Suggests possible movement routes between habitats. Animals or plants may not actually use the mapped connections.

**Measurement origin:** Habitat maps and movement models, checked with field/genetic evidence

**Supporting indicators:** [EII:BIO-002](#bio-002); [EII:BIO-015](#bio-015); [EII:LAN-004](#lan-004)

**Primary domain:** D10

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["structural_connectivity", "modelled_functional_connectivity"]`

**Record type:** family

**Candidate source routes:** `["land", "bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS005, RS006, RS009; Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:BIO-007","domain":"D10","related_domains":[],"record_type":"family","variants":["structural_connectivity","modelled_functional_connectivity"],"secondary":["derived","modelled"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["land","bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Connectivity/corridor suitability describe structural connection or modelled movement opportunity.
- **Direct observations / derivation:** Habitat distances, resistance surfaces and declared graph/circuit model; validate with movement/genetic evidence.
- **Inference and limits:** Supports movement hypotheses; structural corridors do not prove functional use or gene flow.
- **Supporting indicators:** [EII:BIO-002](#bio-002), [EII:BIO-015](#bio-015), [EII:LAN-004](#lan-004).

<a id="bio-008"></a>

### EII:BIO-008 — Pollinator abundance / visitation

**Definition:** Pollinator abundance/visitation record insects and visits to defined flowers.

**Direct observations / derivation:** Standardised counts per transect/time and visits/flower/hour, with weather and species recorded.

**Inference and limits:** Supports pollination activity assessment; visitation alone does not prove pollen transfer or successful reproduction.

**Display label:** Pollinator numbers and flower visits

**Display measurement:** Field insect counts and flower observations. Standardised counts per transect/time and visits/flower/hour, with weather and species recorded.

**Display interpretation:** Shows pollinator numbers or flower visits. Visits alone do not prove successful pollination.

**Measurement origin:** Field insect counts and flower observations

**Supporting indicators:** [EII:INT-001](#int-001); [EII:INT-002](#int-002); [EII:VEG-016](#veg-016)

**Primary domain:** D08

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "community", "plot"], "temporal": ["event", "season"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `["pollinator_count", "flower_visitation_rate"]`

**Record type:** family

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:BIO-008","domain":"D08","related_domains":["D13"],"record_type":"family","variants":["pollinator_count","flower_visitation_rate"],"secondary":["measured","process"],"tertiary":{"spatial":["organism","community","plot"],"temporal":["event","season"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Pollinator abundance/visitation record insects and visits to defined flowers.
- **Direct observations / derivation:** Standardised counts per transect/time and visits/flower/hour, with weather and species recorded.
- **Inference and limits:** Supports pollination activity assessment; visitation alone does not prove pollen transfer or successful reproduction.
- **Supporting indicators:** [EII:INT-001](#int-001), [EII:INT-002](#int-002), [EII:VEG-016](#veg-016).

<a id="bio-009"></a>

### EII:BIO-009 — Predation / natural pest-control rate

**Definition:** Predation/pest-control rate measures consumption or pest reduction in a stated experiment.

**Direct observations / derivation:** Sentinel-prey loss/time and paired exclusion/open treatment effects, %/day or pest-density difference.

**Inference and limits:** Supports biocontrol assessment; prey disappearance and experimental artefacts require predator verification.

**Display label:** Predation and pest control

**Display measurement:** Field predator/prey or pest-control experiments. Sentinel-prey loss/time and paired exclusion/open treatment effects, %/day or pest-density difference.

**Display interpretation:** Helps assess predators' contribution to pest control. Missing prey and changes in pests need careful checking.

**Measurement origin:** Field predator/prey or pest-control experiments

**Supporting indicators:** [EII:AGR-004](#agr-004); [EII:INT-003](#int-003); [EII:BIO-002](#bio-002)

**Primary domain:** D08

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "community", "plot"], "temporal": ["event", "season"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:BIO-009","domain":"D08","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["organism","community","plot"],"temporal":["event","season"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Predation/pest-control rate measures consumption or pest reduction in a stated experiment.
- **Direct observations / derivation:** Sentinel-prey loss/time and paired exclusion/open treatment effects, %/day or pest-density difference.
- **Inference and limits:** Supports biocontrol assessment; prey disappearance and experimental artefacts require predator verification.
- **Supporting indicators:** [EII:AGR-004](#agr-004), [EII:INT-003](#int-003), [EII:BIO-002](#bio-002).

<a id="bio-010"></a>

### EII:BIO-010 — Invasive species presence / spread

**Definition:** Invasive occurrence/spread records detection and changing distribution of a declared invasive taxon.

**Direct observations / derivation:** Verified occurrence/cover maps and repeat surveys, area or km/year; distinguish non-native from invasive.

**Inference and limits:** Supports invasion surveillance; detections do not by themselves establish ecological impact or absence elsewhere.

**Display label:** Invasive species presence and spread

**Display measurement:** Field surveys, imagery or validated laboratory DNA detections. Verified occurrence/cover maps and repeat surveys, area or km/year; distinguish non-native from invasive.

**Display interpretation:** Shows where a named invasive species is present or spreading. Presence alone does not measure its ecological damage.

**Measurement origin:** Field surveys, imagery or validated laboratory DNA detections

**Supporting indicators:** [EII:BIO-002](#bio-002); [EII:DIS-005](#dis-005); [EII:BIO-005](#bio-005)

**Primary domain:** D06

**Secondary domains:** `[]`

**Classification dimensions:** `["observed", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio", "land"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS005, RS006, RS009; Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:BIO-010","domain":"D06","related_domains":[],"record_type":"indicator","variants":[],"secondary":["observed","derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio","land"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Invasive occurrence/spread records detection and changing distribution of a declared invasive taxon.
- **Direct observations / derivation:** Verified occurrence/cover maps and repeat surveys, area or km/year; distinguish non-native from invasive.
- **Inference and limits:** Supports invasion surveillance; detections do not by themselves establish ecological impact or absence elsewhere.
- **Supporting indicators:** [EII:BIO-002](#bio-002), [EII:DIS-005](#dis-005), [EII:BIO-005](#bio-005).

<a id="bio-011"></a>

### EII:BIO-011 — Indicator / threatened species occurrence

**Definition:** Indicator/threatened occurrence records verified presence of taxa with a declared status or association.

**Direct observations / derivation:** Validated observations or eDNA detections with blanks, date, coordinates and status-list version.

**Inference and limits:** Supports conservation screening; non-detection is not absence and indicator associations require local validation.

**Display label:** Species of conservation interest

**Display measurement:** Field observations or validated laboratory DNA detections. Validated observations or eDNA detections with blanks, date, coordinates and status-list version.

**Display interpretation:** Helps locate species of conservation interest. Missed detections and local habitat needs must also be considered.

**Measurement origin:** Field observations or validated laboratory DNA detections

**Supporting indicators:** [EII:BIO-002](#bio-002); [EII:BIO-005](#bio-005); [EII:BIO-014](#bio-014)

**Primary domain:** D06

**Secondary domains:** `[]`

**Classification dimensions:** `["observed"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:BIO-011","domain":"D06","related_domains":[],"record_type":"indicator","variants":[],"secondary":["observed"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Indicator/threatened occurrence records verified presence of taxa with a declared status or association.
- **Direct observations / derivation:** Validated observations or eDNA detections with blanks, date, coordinates and status-list version.
- **Inference and limits:** Supports conservation screening; non-detection is not absence and indicator associations require local validation.
- **Supporting indicators:** [EII:BIO-002](#bio-002), [EII:BIO-005](#bio-005), [EII:BIO-014](#bio-014).

<a id="bio-012"></a>

### EII:BIO-012 — Acoustic biodiversity / soundscape indices

**Definition:** Soundscape indices summarise defined acoustic energy/complexity patterns.

**Direct observations / derivation:** Calibrated recordings and a specified acoustic index, dimensionless; distinguish classified calls from generic sound metrics.

**Inference and limits:** Supports acoustic-activity comparison; wind, rain and anthropogenic noise prevent treating an index as species richness.

**Display label:** Biological sounds

**Display measurement:** Field sound recorders and acoustic analysis. Calibrated recordings and a specified acoustic index, dimensionless; distinguish classified calls from generic sound metrics.

**Display interpretation:** Helps compare biological sounds and activity. Rain, wind and human noise can affect the result; sound indices are not species counts.

**Measurement origin:** Field sound recorders and acoustic analysis

**Supporting indicators:** [EII:BIO-001](#bio-001); [EII:BIO-002](#bio-002); [EII:HUM-008](#hum-008)

**Primary domain:** D06

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "population", "community", "landscape"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:BIO-012","domain":"D06","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","population","community","landscape"],"temporal":["season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Soundscape indices summarise defined acoustic energy/complexity patterns.
- **Direct observations / derivation:** Calibrated recordings and a specified acoustic index, dimensionless; distinguish classified calls from generic sound metrics.
- **Inference and limits:** Supports acoustic-activity comparison; wind, rain and anthropogenic noise prevent treating an index as species richness.
- **Supporting indicators:** [EII:BIO-001](#bio-001), [EII:BIO-002](#bio-002), [EII:HUM-008](#hum-008).

<a id="bio-013"></a>

### EII:BIO-013 — Food-web / interaction network structure

**Definition:** Interaction-network structure describes links among organisms and associated network metrics.

**Direct observations / derivation:** Observed/traced feeding or interaction events and link weights; calculate connectance/modularity with method declared.

**Inference and limits:** Supports trophic/network comparison; co-occurrence alone is not a validated interaction and incomplete sampling biases metrics.

**Display label:** Food webs and ecological networks

**Display measurement:** Field interaction observations, laboratory diet tests and network models. Observed/traced feeding or interaction events and link weights; calculate connectance/modularity with method declared.

**Display interpretation:** Helps describe who interacts with or eats whom. Species occurring together are not automatically interacting.

**Measurement origin:** Field interaction observations, laboratory diet tests and network models

**Supporting indicators:** [EII:INT-003](#int-003); [EII:INT-008](#int-008); [EII:BIO-002](#bio-002)

**Primary domain:** D08

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:BIO-013","domain":"D08","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","modelled"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Interaction-network structure describes links among organisms and associated network metrics.
- **Direct observations / derivation:** Observed/traced feeding or interaction events and link weights; calculate connectance/modularity with method declared.
- **Inference and limits:** Supports trophic/network comparison; co-occurrence alone is not a validated interaction and incomplete sampling biases metrics.
- **Supporting indicators:** [EII:INT-003](#int-003), [EII:INT-008](#int-008), [EII:BIO-002](#bio-002).

<a id="dis-001"></a>

### EII:DIS-001 — Normalised Burn Ratio (NBR)

**Definition:** NBR contrasts NIR with SWIR2 to characterise vegetation/char signals.

**Direct observations / derivation:** (NIR-SWIR2)/(NIR+SWIR2), dimensionless; dNBR is pre-fire minus post-fire NBR.

**Inference and limits:** Supports burn-impact mapping with field calibration; phenology, soil and initial vegetation alter severity relationships.

**Display label:** Burn ratio (NBR)

**Display measurement:** Satellite imagery before and after fire. (NIR-SWIR2)/(NIR+SWIR2), dimensionless; dNBR is pre-fire minus post-fire NBR.

**Display interpretation:** Helps locate fire-affected vegetation and compare burn impacts. The index needs field checks to estimate severity reliably.

**Measurement origin:** Satellite imagery before and after fire

**Supporting indicators:** [EII:DIS-003](#dis-003); [EII:VEG-014](#veg-014); [EII:RES-005](#res-005)

**Primary domain:** D12

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "ecosystem", "landscape"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["disturbance_response", "restoration_assessment"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["opt", "fire"]`

**Scientific reference keys:** `["R02"]`

**Display source keys:** RS001, RS002, RS016, RS017

**Research status:** curated_working_definition

**Review scope:** specific_documentary_aspects_only

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:DIS-001","domain":"D12","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["plot","ecosystem","landscape"],"temporal":["event","year","decade"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":["opt","fire"],"refs":["R02"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** NBR contrasts NIR with SWIR2 to characterise vegetation/char signals.
- **Direct observations / derivation:** (NIR-SWIR2)/(NIR+SWIR2), dimensionless; dNBR is pre-fire minus post-fire NBR.
- **Inference and limits:** Supports burn-impact mapping with field calibration; phenology, soil and initial vegetation alter severity relationships.
- **Supporting indicators:** [EII:DIS-003](#dis-003), [EII:VEG-014](#veg-014), [EII:RES-005](#res-005).

<a id="dis-002"></a>

### EII:DIS-002 — Fire fuel load / vertical continuity

**Definition:** Fuel load/continuity describe combustible biomass and its spatial arrangement.

**Direct observations / derivation:** Dry live/dead fuel mass, Mg/ha; height/spacing and moisture observations, m and %.

**Inference and limits:** Supports fire-behaviour assessment; fuel alone does not determine ignition, weather, exposure or damage.

**Display label:** Fire fuel load and arrangement

**Display measurement:** Field fuel surveys, LiDAR and calibrated imagery. Dry live/dead fuel mass, Mg/ha; height/spacing and moisture observations, m and %.

**Display interpretation:** Helps assess fuel that could carry a fire. Weather, ignition and fuel moisture also influence fire behaviour.

**Measurement origin:** Field fuel surveys, LiDAR and calibrated imagery

**Supporting indicators:** [EII:TER-013](#ter-013); [EII:ATM-005](#atm-005); [EII:DIS-007](#dis-007)

**Primary domain:** D12

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "ecosystem", "landscape"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["disturbance_response", "restoration_assessment"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["terrain", "fire"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021, RS016, RS017

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:DIS-002","domain":"D12","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","modelled"],"tertiary":{"spatial":["plot","ecosystem","landscape"],"temporal":["event","year","decade"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":["terrain","fire"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fuel load/continuity describe combustible biomass and its spatial arrangement.
- **Direct observations / derivation:** Dry live/dead fuel mass, Mg/ha; height/spacing and moisture observations, m and %.
- **Inference and limits:** Supports fire-behaviour assessment; fuel alone does not determine ignition, weather, exposure or damage.
- **Supporting indicators:** [EII:TER-013](#ter-013), [EII:ATM-005](#atm-005), [EII:DIS-007](#dis-007).

<a id="dis-003"></a>

### EII:DIS-003 — Fire occurrence / recurrence

**Definition:** Fire occurrence/recurrence describe confirmed events, affected area and intervals.

**Direct observations / derivation:** Validated event records/burn perimeters, dates, ha and years between events.

**Inference and limits:** Supports disturbance-history assessment; thermal hotspots are detections rather than perimeters or ignition counts.

**Display label:** Fire events and recurrence

**Display measurement:** Satellite detections and confirmed field/event records. Validated event records/burn perimeters, dates, ha and years between events.

**Display interpretation:** Shows recorded fire events and intervals between them. Satellite hotspots are not the same as fire boundaries.

**Measurement origin:** Satellite detections and confirmed field/event records

**Supporting indicators:** [EII:DIS-001](#dis-001); [EII:DIS-002](#dis-002); [EII:RES-005](#res-005)

**Primary domain:** D12

**Secondary domains:** `[]`

**Classification dimensions:** `["observed", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "ecosystem", "landscape"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["disturbance_response", "restoration_assessment"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["fire"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS016, RS017

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:DIS-003","domain":"D12","related_domains":[],"record_type":"indicator","variants":[],"secondary":["observed","derived"],"tertiary":{"spatial":["plot","ecosystem","landscape"],"temporal":["event","year","decade"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":["fire"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fire occurrence/recurrence describe confirmed events, affected area and intervals.
- **Direct observations / derivation:** Validated event records/burn perimeters, dates, ha and years between events.
- **Inference and limits:** Supports disturbance-history assessment; thermal hotspots are detections rather than perimeters or ignition counts.
- **Supporting indicators:** [EII:DIS-001](#dis-001), [EII:DIS-002](#dis-002), [EII:RES-005](#res-005).

<a id="dis-004"></a>

### EII:DIS-004 — Land-cover / land-use class

**Definition:** Land cover and land use are distinct surface classes and activities.

**Direct observations / derivation:** Validated imagery classes and independent management records, categorical with class probabilities/accuracy.

**Inference and limits:** Supports context mapping; tree cover is not necessarily forest use and imagery rarely identifies practices uniquely.

**Display label:** Land cover and land use

**Display measurement:** Satellite classifications and field land-use records. Validated imagery classes and independent management records, categorical with class probabilities/accuracy.

**Display interpretation:** Shows surface cover or recorded land use. Satellite images do not always reveal how land is managed.

**Measurement origin:** Satellite classifications and field land-use records

**Supporting indicators:** [EII:DIS-005](#dis-005); [EII:VEG-017](#veg-017); [EII:FUN-007](#fun-007)

**Primary domain:** D10

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["derived", "context"]`

**Spatial/temporal dimensions:** `{"spatial": ["landscape", "watershed", "region"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["context"]`

**Family / variant distinctions:** `["land_cover", "land_use"]`

**Record type:** family

**Candidate source routes:** `["land", "amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS005, RS006, RS009; AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:DIS-004","domain":"D10","related_domains":["D13"],"record_type":"family","variants":["land_cover","land_use"],"secondary":["derived","context"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["context"],"routes":["land","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Land cover and land use are distinct surface classes and activities.
- **Direct observations / derivation:** Validated imagery classes and independent management records, categorical with class probabilities/accuracy.
- **Inference and limits:** Supports context mapping; tree cover is not necessarily forest use and imagery rarely identifies practices uniquely.
- **Supporting indicators:** [EII:DIS-005](#dis-005), [EII:VEG-017](#veg-017), [EII:FUN-007](#fun-007).

<a id="dis-005"></a>

### EII:DIS-005 — Land-cover transition rate

**Definition:** Transition rate is area changing between harmonised land classes per time.

**Direct observations / derivation:** Comparable validated class maps, ha/year or %/year; account for class and algorithm changes.

**Inference and limits:** Supports conversion/abandonment assessment; map disagreement may be classification error rather than real change.

**Display label:** Land-cover change rate

**Display measurement:** Comparable land-cover maps from different dates. Comparable validated class maps, ha/year or %/year; account for class and algorithm changes.

**Display interpretation:** Shows changes between land-cover classes. Different mapping methods can create apparent changes that are not real.

**Measurement origin:** Comparable land-cover maps from different dates

**Supporting indicators:** [EII:DIS-004](#dis-004); [EII:BIO-005](#bio-005); [EII:FUN-009](#fun-009)

**Primary domain:** D10

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["landscape", "watershed", "region"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["land"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS005, RS006, RS009

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:DIS-005","domain":"D10","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","pressure"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["pressure"],"routes":["land"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Transition rate is area changing between harmonised land classes per time.
- **Direct observations / derivation:** Comparable validated class maps, ha/year or %/year; account for class and algorithm changes.
- **Inference and limits:** Supports conversion/abandonment assessment; map disagreement may be classification error rather than real change.
- **Supporting indicators:** [EII:DIS-004](#dis-004), [EII:BIO-005](#bio-005), [EII:FUN-009](#fun-009).

<a id="dis-006"></a>

### EII:DIS-006 — Air temperature / precipitation

**Definition:** Air temperature and precipitation describe separate atmospheric variables.

**Direct observations / derivation:** Shielded air thermometer, °C; gauge accumulation, mm per interval; record height/exposure and catch corrections.

**Inference and limits:** Supports climate-baseline assessment; interpolated grids are estimates and short records do not define long-term climate.

**Display label:** Air temperature and rainfall

**Display measurement:** Weather-station sensors and rain gauges. Shielded air thermometer, °C; gauge accumulation, mm per interval; record height/exposure and catch corrections.

**Display interpretation:** Helps describe weather and longer-term patterns. Short records cannot establish a reliable long-term climate baseline.

**Measurement origin:** Weather-station sensors and rain gauges

**Supporting indicators:** [EII:ATM-001](#atm-001); [EII:ATM-002](#atm-002); [EII:DIS-008](#dis-008)

**Primary domain:** D01

**Secondary domains:** `[]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "landscape", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["air_temperature", "precipitation"]`

**Record type:** family

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:DIS-006","domain":"D01","related_domains":[],"record_type":"family","variants":["air_temperature","precipitation"],"secondary":["measured"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Air temperature and precipitation describe separate atmospheric variables.
- **Direct observations / derivation:** Shielded air thermometer, °C; gauge accumulation, mm per interval; record height/exposure and catch corrections.
- **Inference and limits:** Supports climate-baseline assessment; interpolated grids are estimates and short records do not define long-term climate.
- **Supporting indicators:** [EII:ATM-001](#atm-001), [EII:ATM-002](#atm-002), [EII:DIS-008](#dis-008).

<a id="dis-007"></a>

### EII:DIS-007 — Drought index / aridity

**Definition:** Drought/aridity indices quantify distinct water-deficit or long-term dryness concepts.

**Direct observations / derivation:** SPI from precipitation, SPEI from climatic water balance, or P/PET aridity; specify index, window and baseline.

**Inference and limits:** Supports deficit comparison; meteorological, soil and hydrological drought may diverge and PET method affects results.

**Display label:** Drought and dryness indices

**Display measurement:** Weather records, soil/flow data and drought calculations. SPI from precipitation, SPEI from climatic water balance, or P/PET aridity; specify index, window and baseline.

**Display interpretation:** Helps compare dry conditions. A rainfall shortage, dry soil and low river flow may not occur at the same time.

**Measurement origin:** Weather records, soil/flow data and drought calculations

**Supporting indicators:** [EII:HYD-001](#hyd-001); [EII:HYD-006](#hyd-006); [EII:HYD-012](#hyd-012)

**Primary domain:** D01

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "landscape", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["SPI", "SPEI", "aridity_ratio"]`

**Record type:** family

**Candidate source routes:** `["drought", "iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS015; IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:DIS-007","domain":"D01","related_domains":[],"record_type":"family","variants":["SPI","SPEI","aridity_ratio"],"secondary":["derived","modelled"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["drought","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Drought/aridity indices quantify distinct water-deficit or long-term dryness concepts.
- **Direct observations / derivation:** SPI from precipitation, SPEI from climatic water balance, or P/PET aridity; specify index, window and baseline.
- **Inference and limits:** Supports deficit comparison; meteorological, soil and hydrological drought may diverge and PET method affects results.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:HYD-006](#hyd-006), [EII:HYD-012](#hyd-012).

<a id="dis-008"></a>

### EII:DIS-008 — Heatwave / frost frequency

**Definition:** Heatwave/frost frequency counts temperature events under stated thresholds/durations.

**Direct observations / derivation:** Temperature series and event rule, events/year or days/year; distinguish air frost from plant-tissue exposure.

**Inference and limits:** Supports thermal-extreme exposure assessment; biological injury depends on phenology, cultivar and duration.

**Display label:** Heatwave and frost frequency

**Display measurement:** Weather-station temperature records. Temperature series and event rule, events/year or days/year; distinguish air frost from plant-tissue exposure.

**Display interpretation:** Shows how often defined heat or frost events occur. Plant damage also depends on timing, duration and plant type.

**Measurement origin:** Weather-station temperature records

**Supporting indicators:** [EII:DIS-006](#dis-006); [EII:VEG-016](#veg-016); [EII:AGR-005](#agr-005)

**Primary domain:** D01

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "landscape", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["heatwave_frequency", "frost_frequency"]`

**Record type:** family

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:DIS-008","domain":"D01","related_domains":[],"record_type":"family","variants":["heatwave_frequency","frost_frequency"],"secondary":["derived"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Heatwave/frost frequency counts temperature events under stated thresholds/durations.
- **Direct observations / derivation:** Temperature series and event rule, events/year or days/year; distinguish air frost from plant-tissue exposure.
- **Inference and limits:** Supports thermal-extreme exposure assessment; biological injury depends on phenology, cultivar and duration.
- **Supporting indicators:** [EII:DIS-006](#dis-006), [EII:VEG-016](#veg-016), [EII:AGR-005](#agr-005).

<a id="dis-009"></a>

### EII:DIS-009 — Soil/vegetation recovery after disturbance

**Definition:** Post-disturbance recovery describes a trajectory towards a stated baseline/reference.

**Direct observations / derivation:** Repeat soil/vegetation measurements, baseline-normalised effect, slope or time to threshold.

**Inference and limits:** Supports resilience assessment; regreening is not recovery of composition, soil carbon or all functions.

**Display label:** Recovery after disturbance

**Display measurement:** Repeat field measurements or satellite images. Repeat soil/vegetation measurements, baseline-normalised effect, slope or time to threshold.

**Display interpretation:** Helps track recovery after disturbance. Greener vegetation does not necessarily mean that species, soils and functions have recovered.

**Measurement origin:** Repeat field measurements or satellite images

**Supporting indicators:** [EII:RES-001](#res-001); [EII:RES-002](#res-002); [EII:VEG-017](#veg-017); [EII:FUN-001](#fun-001)

**Primary domain:** D12

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["disturbance_response", "restoration_assessment"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["veg", "bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS001, RS002; Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:DIS-009","domain":"D12","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","modelled"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":["veg","bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Post-disturbance recovery describes a trajectory towards a stated baseline/reference.
- **Direct observations / derivation:** Repeat soil/vegetation measurements, baseline-normalised effect, slope or time to threshold.
- **Inference and limits:** Supports resilience assessment; regreening is not recovery of composition, soil carbon or all functions.
- **Supporting indicators:** [EII:RES-001](#res-001), [EII:RES-002](#res-002), [EII:VEG-017](#veg-017), [EII:FUN-001](#fun-001).

<a id="dis-010"></a>

### EII:DIS-010 — Future climate exposure / suitability

**Definition:** Future exposure/suitability is a conditional climate/ecological model output.

**Direct observations / derivation:** Scenario ensemble, downscaling and explicit suitability model, probability or change in relevant variable.

**Inference and limits:** Supports conditional planning; projections are not observations and extrapolation/reference bias require validation.

**Display label:** Future climate exposure and suitability

**Display measurement:** Climate scenarios and ecological models. Scenario ensemble, downscaling and explicit suitability model, probability or change in relevant variable.

**Display interpretation:** Shows possible future conditions under stated scenarios. These are model estimates, not observations of what will happen.

**Measurement origin:** Climate scenarios and ecological models

**Supporting indicators:** [EII:DIS-006](#dis-006); [EII:DIS-007](#dis-007); [EII:VEG-017](#veg-017); [EII:RES-007](#res-007)

**Primary domain:** D12

**Secondary domains:** `[]`

**Classification dimensions:** `["modelled", "predictive"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "ecosystem", "landscape"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["exposure", "planning"]`

**Family / variant distinctions:** `["scenario_exposure", "modelled_species_suitability"]`

**Record type:** family

**Candidate source routes:** `[]`

**Scientific reference keys:** `[]`

**Display source keys:** Field/lab/model source to register

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:DIS-010","domain":"D12","related_domains":[],"record_type":"family","variants":["scenario_exposure","modelled_species_suitability"],"secondary":["modelled","predictive"],"tertiary":{"spatial":["plot","ecosystem","landscape"],"temporal":["event","year","decade"]},"quaternary":["exposure","planning"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Future exposure/suitability is a conditional climate/ecological model output.
- **Direct observations / derivation:** Scenario ensemble, downscaling and explicit suitability model, probability or change in relevant variable.
- **Inference and limits:** Supports conditional planning; projections are not observations and extrapolation/reference bias require validation.
- **Supporting indicators:** [EII:DIS-006](#dis-006), [EII:DIS-007](#dis-007), [EII:VEG-017](#veg-017), [EII:RES-007](#res-007).

<a id="dis-011"></a>

### EII:DIS-011 — SAR-derived inundation / surface change

**Definition:** SAR inundation/surface change are radar-derived interpretations of backscatter/coherence.

**Direct observations / derivation:** Calibrated radar backscatter, dB, and declared classification/change algorithm, area or index.

**Inference and limits:** Supports cloud-independent change detection; roughness, vegetation, geometry and soil moisture produce ambiguous signals.

**Display label:** Radar-detected flooding and change

**Display measurement:** Radar satellite imagery. Calibrated radar backscatter, dB, and declared classification/change algorithm, area or index.

**Display interpretation:** Helps detect flooding or surface changes using radar. Soil moisture, vegetation and surface texture can produce similar signals.

**Measurement origin:** Radar satellite imagery

**Supporting indicators:** [EII:HYD-008](#hyd-008); [EII:HYD-001](#hyd-001); [EII:DIS-004](#dis-004)

**Primary domain:** D02

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "watershed", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["radar_inundation_mask", "radar_change_metric"]`

**Record type:** family

**Candidate source routes:** `["sar", "flood"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS001, RS014

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:DIS-011","domain":"D02","related_domains":[],"record_type":"family","variants":["radar_inundation_mask","radar_change_metric"],"secondary":["derived","proxy"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["sar","flood"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** SAR inundation/surface change are radar-derived interpretations of backscatter/coherence.
- **Direct observations / derivation:** Calibrated radar backscatter, dB, and declared classification/change algorithm, area or index.
- **Inference and limits:** Supports cloud-independent change detection; roughness, vegetation, geometry and soil moisture produce ambiguous signals.
- **Supporting indicators:** [EII:HYD-008](#hyd-008), [EII:HYD-001](#hyd-001), [EII:DIS-004](#dis-004).

<a id="dis-012"></a>

### EII:DIS-012 — Hyperspectral material / vegetation trait signatures

**Definition:** Hyperspectral signatures are densely sampled spectral observations used for trait/material retrieval.

**Direct observations / derivation:** Spectral radiance/reflectance by wavelength; traits require calibrated inversion, declared trait units.

**Inference and limits:** Supports material/trait hypotheses; spectra are not uniquely diagnostic without independent samples and validation.

**Display label:** Detailed spectral signatures

**Display measurement:** Specialised hyperspectral satellite, airborne or field instruments. Spectral radiance/reflectance by wavelength; traits require calibrated inversion, declared trait units.

**Display interpretation:** Can help estimate materials or plant traits from detailed spectra. Independent samples are needed to check the interpretation.

**Measurement origin:** Specialised hyperspectral satellite, airborne or field instruments

**Supporting indicators:** [EII:VEG-013](#veg-013); [EII:SOI-005](#soi-005); [EII:VEG-017](#veg-017)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `[]`

**Scientific reference keys:** `[]`

**Display source keys:** Field/lab/model source to register

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:DIS-012","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Hyperspectral signatures are densely sampled spectral observations used for trait/material retrieval.
- **Direct observations / derivation:** Spectral radiance/reflectance by wavelength; traits require calibrated inversion, declared trait units.
- **Inference and limits:** Supports material/trait hypotheses; spectra are not uniquely diagnostic without independent samples and validation.
- **Supporting indicators:** [EII:VEG-013](#veg-013), [EII:SOI-005](#soi-005), [EII:VEG-017](#veg-017).

<a id="fun-001"></a>

### EII:FUN-001 — Primary productivity (GPP/NPP)

**Definition:** GPP is gross carbon fixation; NPP is GPP minus autotrophic respiration.

**Direct observations / derivation:** Carbon flux/biomass observations and partitioning/model, g C/m²/year; record whether GPP or NPP.

**Inference and limits:** Supports production assessment; eddy-covariance net exchange needs partitioning and greenness is not direct productivity.

**Display label:** Plant carbon production (GPP/NPP)

**Display measurement:** Field carbon/biomass measurements and calibrated production models. Carbon flux/biomass observations and partitioning/model, g C/m²/year; record whether GPP or NPP.

**Display interpretation:** Helps assess carbon fixed by plants and carbon retained for growth. These quantities differ, and often require modelling.

**Measurement origin:** Field carbon/biomass measurements and calibrated production models

**Supporting indicators:** [EII:VEG-011](#veg-011); [EII:VEG-014](#veg-014); [EII:SOI-010](#soi-010); [EII:CYC-001](#cyc-001)

**Primary domain:** D11

**Secondary domains:** `[]`

**Classification dimensions:** `["modelled", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "ecosystem", "watershed"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `["GPP", "NPP"]`

**Record type:** family

**Candidate source routes:** `["veg", "iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS001, RS002; IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:FUN-001","domain":"D11","related_domains":[],"record_type":"family","variants":["GPP","NPP"],"secondary":["modelled","process"],"tertiary":{"spatial":["plot","ecosystem","watershed"],"temporal":["season","year"]},"quaternary":["function"],"routes":["veg","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** GPP is gross carbon fixation; NPP is GPP minus autotrophic respiration.
- **Direct observations / derivation:** Carbon flux/biomass observations and partitioning/model, g C/m²/year; record whether GPP or NPP.
- **Inference and limits:** Supports production assessment; eddy-covariance net exchange needs partitioning and greenness is not direct productivity.
- **Supporting indicators:** [EII:VEG-011](#veg-011), [EII:VEG-014](#veg-014), [EII:SOI-010](#soi-010), [EII:CYC-001](#cyc-001).

<a id="fun-002"></a>

### EII:FUN-002 — Carbon sequestration / stock change

**Definition:** Carbon stock change is repeated pool difference; net sequestration requires a defined system carbon balance.

**Direct observations / derivation:** Comparable stocks over time, Mg C/ha/year, with transfers and fluxes for net balance.

**Inference and limits:** Supports storage-change assessment; redistribution, harvested export and off-site emissions prevent equating one pool gain with net climate benefit.

**Display label:** Carbon storage change

**Display measurement:** Repeat field/laboratory carbon stocks and whole-system carbon accounts. Comparable stocks over time, Mg C/ha/year, with transfers and fluxes for net balance.

**Display interpretation:** Helps assess changes in stored carbon. A gain in one pool does not prove a net climate benefit for the whole system.

**Measurement origin:** Repeat field/laboratory carbon stocks and whole-system carbon accounts

**Supporting indicators:** [EII:SOI-005](#soi-005); [EII:VEG-014](#veg-014); [EII:CYC-001](#cyc-001); [EII:CYC-002](#cyc-002)

**Primary domain:** D09

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["derived", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot", "ecosystem", "watershed"], "temporal": ["hour", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `["specified_pool_stock_change", "net_ecosystem_carbon_balance"]`

**Record type:** family

**Candidate source routes:** `["amr", "veg"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS001, RS002; AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:FUN-002","domain":"D09","related_domains":["D13"],"record_type":"family","variants":["specified_pool_stock_change","net_ecosystem_carbon_balance"],"secondary":["derived","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["amr","veg"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Carbon stock change is repeated pool difference; net sequestration requires a defined system carbon balance.
- **Direct observations / derivation:** Comparable stocks over time, Mg C/ha/year, with transfers and fluxes for net balance.
- **Inference and limits:** Supports storage-change assessment; redistribution, harvested export and off-site emissions prevent equating one pool gain with net climate benefit.
- **Supporting indicators:** [EII:SOI-005](#soi-005), [EII:VEG-014](#veg-014), [EII:CYC-001](#cyc-001), [EII:CYC-002](#cyc-002).

<a id="fun-003"></a>

### EII:FUN-003 — Nutrient retention / leaching

**Definition:** Nutrient retention/leaching quantify distinct retained and exported nutrient masses.

**Direct observations / derivation:** Input/output water and nutrient mass balance, kg N/P/ha/year; drainage flux × concentration for leaching.

**Inference and limits:** Supports nutrient-loss assessment; concentration decline alone is not retention and missing pathways bias budgets.

**Display label:** Nutrient retention and leaching

**Display measurement:** Field water-flow measurements, laboratory nutrient tests and budgets. Input/output water and nutrient mass balance, kg N/P/ha/year; drainage flux × concentration for leaching.

**Display interpretation:** Helps assess nutrients retained or lost through water. Changes in concentration alone do not show the total amount retained.

**Measurement origin:** Field water-flow measurements, laboratory nutrient tests and budgets

**Supporting indicators:** [EII:HYD-010](#hyd-010); [EII:HYD-006](#hyd-006); [EII:CYC-007](#cyc-007)

**Primary domain:** D09

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "modelled", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot", "ecosystem", "watershed"], "temporal": ["hour", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `["nutrient_retention", "nutrient_leaching"]`

**Record type:** family

**Candidate source routes:** `["amr", "iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context; IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:FUN-003","domain":"D09","related_domains":["D13"],"record_type":"family","variants":["nutrient_retention","nutrient_leaching"],"secondary":["measured","modelled","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["amr","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Nutrient retention/leaching quantify distinct retained and exported nutrient masses.
- **Direct observations / derivation:** Input/output water and nutrient mass balance, kg N/P/ha/year; drainage flux × concentration for leaching.
- **Inference and limits:** Supports nutrient-loss assessment; concentration decline alone is not retention and missing pathways bias budgets.
- **Supporting indicators:** [EII:HYD-010](#hyd-010), [EII:HYD-006](#hyd-006), [EII:CYC-007](#cyc-007).

<a id="fun-004"></a>

### EII:FUN-004 — Crop yield / yield stability

**Definition:** Yield and stability describe harvest mass and interannual variation respectively.

**Direct observations / derivation:** Harvest dry/standard-moisture mass per area, Mg/ha; multi-year CV or specified stability metric.

**Inference and limits:** Supports productivity and variability assessment; mean differences, weather, inputs and price do not imply ecological resilience alone.

**Display label:** Crop yield and stability

**Display measurement:** Field harvest measurements and farm yield records. Harvest dry/standard-moisture mass per area, Mg/ha; multi-year CV or specified stability metric.

**Display interpretation:** Shows crop output and how much it varies between years. Weather and inputs affect results, so stable yields alone do not prove ecological resilience.

**Measurement origin:** Field harvest measurements and farm yield records

**Supporting indicators:** [EII:AGR-001](#agr-001); [EII:AGR-002](#agr-002); [EII:DIS-006](#dis-006)

**Primary domain:** D13

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "farm", "landscape"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["state", "production_assessment"]`

**Family / variant distinctions:** `["crop_yield", "interannual_yield_stability"]`

**Record type:** family

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:FUN-004","domain":"D13","related_domains":[],"record_type":"family","variants":["crop_yield","interannual_yield_stability"],"secondary":["measured","derived"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["state","production_assessment"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Yield and stability describe harvest mass and interannual variation respectively.
- **Direct observations / derivation:** Harvest dry/standard-moisture mass per area, Mg/ha; multi-year CV or specified stability metric.
- **Inference and limits:** Supports productivity and variability assessment; mean differences, weather, inputs and price do not imply ecological resilience alone.
- **Supporting indicators:** [EII:AGR-001](#agr-001), [EII:AGR-002](#agr-002), [EII:DIS-006](#dis-006).

<a id="fun-005"></a>

### EII:FUN-005 — Groundcover persistence

**Definition:** Groundcover persistence describes duration/continuity of protective vegetation/residues.

**Direct observations / derivation:** Repeated cover fractions and days above a stated cover threshold, days/year; distinguish green and residue cover.

**Inference and limits:** Supports soil-exposure assessment; sufficient cover and water competition vary with site and crop.

**Display label:** Groundcover duration

**Display measurement:** Repeated field cover surveys or satellite images. Repeated cover fractions and days above a stated cover threshold, days/year; distinguish green and residue cover.

**Display interpretation:** Shows how long vegetation or residues protect the soil. Cover can also compete with crops for water.

**Measurement origin:** Repeated field cover surveys or satellite images

**Supporting indicators:** [EII:VEG-012](#veg-012); [EII:HYD-001](#hyd-001); [EII:SOI-012](#soi-012)

**Primary domain:** D13

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "farm", "landscape"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["state", "production_assessment"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["veg", "amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS001, RS002; AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:FUN-005","domain":"D13","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["state","production_assessment"],"routes":["veg","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Groundcover persistence describes duration/continuity of protective vegetation/residues.
- **Direct observations / derivation:** Repeated cover fractions and days above a stated cover threshold, days/year; distinguish green and residue cover.
- **Inference and limits:** Supports soil-exposure assessment; sufficient cover and water competition vary with site and crop.
- **Supporting indicators:** [EII:VEG-012](#veg-012), [EII:HYD-001](#hyd-001), [EII:SOI-012](#soi-012).

<a id="fun-006"></a>

### EII:FUN-006 — Grazing pressure / stocking intensity

**Definition:** Grazing/stocking intensity quantify animal pressure on a defined land area and period.

**Direct observations / derivation:** Animal-unit days/ha plus forage removal/utilisation, %, with grazing season and feed imports.

**Inference and limits:** Supports grazing-pressure assessment; stocking rate alone does not establish overgrazing without forage supply and vegetation response.

**Display label:** Grazing intensity

**Display measurement:** Farm livestock records and field forage measurements. Animal-unit days/ha plus forage removal/utilisation, %, with grazing season and feed imports.

**Display interpretation:** Helps compare grazing pressure. Whether it is excessive depends on forage supply, season and vegetation response.

**Measurement origin:** Farm livestock records and field forage measurements

**Supporting indicators:** [EII:VEG-014](#veg-014); [EII:SOI-002](#soi-002); [EII:AGR-009](#agr-009)

**Primary domain:** D13

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "farm", "landscape"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:FUN-006","domain":"D13","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","pressure"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["pressure"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Grazing/stocking intensity quantify animal pressure on a defined land area and period.
- **Direct observations / derivation:** Animal-unit days/ha plus forage removal/utilisation, %, with grazing season and feed imports.
- **Inference and limits:** Supports grazing-pressure assessment; stocking rate alone does not establish overgrazing without forage supply and vegetation response.
- **Supporting indicators:** [EII:VEG-014](#veg-014), [EII:SOI-002](#soi-002), [EII:AGR-009](#agr-009).

<a id="fun-007"></a>

### EII:FUN-007 — Irrigation / fertiliser / pesticide input

**Definition:** Input intensity records separate irrigation, fertiliser and pesticide applications.

**Direct observations / derivation:** Metered water, m³/ha; nutrients, kg N/P/K/ha; active ingredients, kg/ha, with dates/formulations.

**Inference and limits:** Supports resource/pressure assessment; quantities alone do not describe toxicity, losses or agronomic benefit.

**Display label:** Water, fertiliser and pesticide inputs

**Display measurement:** Farm input records and water meters. Metered water, m³/ha; nutrients, kg N/P/K/ha; active ingredients, kg/ha, with dates/formulations.

**Display interpretation:** Shows water, fertiliser and pesticide inputs. Quantities alone do not show benefits, losses or toxicity.

**Measurement origin:** Farm input records and water meters

**Supporting indicators:** [EII:AGR-001](#agr-001); [EII:AGR-002](#agr-002); [EII:AGR-003](#agr-003); [EII:HUM-005](#hum-005)

**Primary domain:** D13

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "farm", "landscape"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `["irrigation_input", "fertiliser_input", "pesticide_input"]`

**Record type:** family

**Candidate source routes:** `["amr", "iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context; IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:FUN-007","domain":"D13","related_domains":[],"record_type":"family","variants":["irrigation_input","fertiliser_input","pesticide_input"],"secondary":["measured","pressure"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["pressure"],"routes":["amr","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Input intensity records separate irrigation, fertiliser and pesticide applications.
- **Direct observations / derivation:** Metered water, m³/ha; nutrients, kg N/P/K/ha; active ingredients, kg/ha, with dates/formulations.
- **Inference and limits:** Supports resource/pressure assessment; quantities alone do not describe toxicity, losses or agronomic benefit.
- **Supporting indicators:** [EII:AGR-001](#agr-001), [EII:AGR-002](#agr-002), [EII:AGR-003](#agr-003), [EII:HUM-005](#hum-005).

<a id="fun-008"></a>

### EII:FUN-008 — Field-margin / hedgerow length and condition

**Definition:** Field-margin/hedgerow structure records extent and separately measured condition.

**Direct observations / derivation:** Mapped length/width, m, area, ha, and botanical/structural attributes.

**Inference and limits:** Supports habitat and buffer assessment; length alone does not establish pollination or nutrient filtering.

**Display label:** Field margins and hedgerows

**Display measurement:** Field vegetation surveys, aerial images or habitat maps. Mapped length/width, m, area, ha, and botanical/structural attributes.

**Display interpretation:** Shows the amount and condition of field-edge vegetation. Length alone does not prove habitat quality or effective filtering.

**Measurement origin:** Field vegetation surveys, aerial images or habitat maps

**Supporting indicators:** [EII:BIO-008](#bio-008); [EII:VEG-017](#veg-017); [EII:LAN-002](#lan-002)

**Primary domain:** D10

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["observed", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["landscape", "watershed", "region"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["terrain", "land", "amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021, RS004, RS005, RS006, RS009; AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:FUN-008","domain":"D10","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["observed","derived"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["state"],"routes":["terrain","land","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Field-margin/hedgerow structure records extent and separately measured condition.
- **Direct observations / derivation:** Mapped length/width, m, area, ha, and botanical/structural attributes.
- **Inference and limits:** Supports habitat and buffer assessment; length alone does not establish pollination or nutrient filtering.
- **Supporting indicators:** [EII:BIO-008](#bio-008), [EII:VEG-017](#veg-017), [EII:LAN-002](#lan-002).

<a id="fun-009"></a>

### EII:FUN-009 — Human settlement / roads / infrastructure

**Definition:** Settlement/roads/infrastructure quantify built extent and network occupation.

**Direct observations / derivation:** Validated footprints and networks, ha, % built-up or km/km²; population products are modelled separately.

**Inference and limits:** Supports land-pressure/accessibility assessment; mapped infrastructure does not establish actual usage or impacts.

**Display label:** Settlements and infrastructure

**Display measurement:** Satellite settlement maps and field infrastructure records. Validated footprints and networks, ha, % built-up or km/km²; population products are modelled separately.

**Display interpretation:** Shows the spread of settlements and infrastructure. Their ecological effects depend on use, design and location.

**Measurement origin:** Satellite settlement maps and field infrastructure records

**Supporting indicators:** [EII:TER-015](#ter-015); [EII:BIO-006](#bio-006); [EII:HUM-001](#hum-001)

**Primary domain:** D14

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["farm", "watershed", "region"], "temporal": ["year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["settlement"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS019

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:FUN-009","domain":"D14","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","pressure"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["pressure"],"routes":["settlement"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Settlement/roads/infrastructure quantify built extent and network occupation.
- **Direct observations / derivation:** Validated footprints and networks, ha, % built-up or km/km²; population products are modelled separately.
- **Inference and limits:** Supports land-pressure/accessibility assessment; mapped infrastructure does not establish actual usage or impacts.
- **Supporting indicators:** [EII:TER-015](#ter-015), [EII:BIO-006](#bio-006), [EII:HUM-001](#hum-001).

<a id="fun-010"></a>

### EII:FUN-010 — Material / biomass availability

**Definition:** Material/biomass availability is an inventory of accessible resources under specified constraints.

**Direct observations / derivation:** Measured stocks and replenishment/harvest models, Mg and Mg/year, with ownership/ecological/access exclusions.

**Inference and limits:** Supports supply screening; standing biomass is not necessarily sustainably harvestable resource.

**Display label:** Available biomass and materials

**Display measurement:** Field inventories, farm records and resource-supply estimates. Measured stocks and replenishment/harvest models, Mg and Mg/year, with ownership/ecological/access exclusions.

**Display interpretation:** Helps estimate available biomass or materials. The amount present is not necessarily the amount that can be harvested sustainably.

**Measurement origin:** Field inventories, farm records and resource-supply estimates

**Supporting indicators:** [EII:VEG-014](#veg-014); [EII:FUN-004](#fun-004); [EII:HUM-003](#hum-003)

**Primary domain:** D14

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["farm", "watershed", "region"], "temporal": ["year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["veg", "amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS001, RS002; AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:FUN-010","domain":"D14","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","modelled"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["state"],"routes":["veg","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Material/biomass availability is an inventory of accessible resources under specified constraints.
- **Direct observations / derivation:** Measured stocks and replenishment/harvest models, Mg and Mg/year, with ownership/ecological/access exclusions.
- **Inference and limits:** Supports supply screening; standing biomass is not necessarily sustainably harvestable resource.
- **Supporting indicators:** [EII:VEG-014](#veg-014), [EII:FUN-004](#fun-004), [EII:HUM-003](#hum-003).

<a id="fun-011"></a>

### EII:FUN-011 — Ecological footprint / resource demand

**Definition:** Ecological footprint/resource demand describe method-defined consumption pressures.

**Direct observations / derivation:** Resource-flow accounts or footprint conversion, physical units or global hectares; declare accounting method and boundary.

**Inference and limits:** Supports demand comparison; assumptions and trade allocation matter and footprint is not a direct local ecosystem measurement.

**Display label:** Ecological footprint and resource demand

**Display measurement:** Resource accounts and footprint calculations. Resource-flow accounts or footprint conversion, physical units or global hectares; declare accounting method and boundary.

**Display interpretation:** Helps compare resource demand. Results depend on the accounting method and do not directly measure local ecosystem condition.

**Measurement origin:** Resource accounts and footprint calculations

**Supporting indicators:** [EII:HUM-003](#hum-003); [EII:HUM-004](#hum-004); [EII:HUM-005](#hum-005)

**Primary domain:** D14

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["derived", "modelled", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["farm", "watershed", "region"], "temporal": ["year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `["ecological_footprint", "physical_resource_demand"]`

**Record type:** family

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:FUN-011","domain":"D14","related_domains":["D13"],"record_type":"family","variants":["ecological_footprint","physical_resource_demand"],"secondary":["derived","modelled","pressure"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["pressure"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Ecological footprint/resource demand describe method-defined consumption pressures.
- **Direct observations / derivation:** Resource-flow accounts or footprint conversion, physical units or global hectares; declare accounting method and boundary.
- **Inference and limits:** Supports demand comparison; assumptions and trade allocation matter and footprint is not a direct local ecosystem measurement.
- **Supporting indicators:** [EII:HUM-003](#hum-003), [EII:HUM-004](#hum-004), [EII:HUM-005](#hum-005).

<a id="fun-012"></a>

### EII:FUN-012 — Composite soil-health index

**Definition:** A composite soil-health index combines specified soil metrics against explicit reference conditions.

**Direct observations / derivation:** Named variables, weights, transformations and missing-data rules, dimensionless declared score.

**Inference and limits:** Supports within-framework condition screening; no universal score or threshold and opposing components can be hidden.

**Display label:** Soil-health score

**Display measurement:** Combined field and laboratory soil tests. Named variables, weights, transformations and missing-data rules, dimensionless declared score.

**Display interpretation:** Combines several soil measurements into a score. The chosen measures and weights matter, and there is no universal soil-health score.

**Measurement origin:** Combined field and laboratory soil tests

**Supporting indicators:** [EII:SOI-003](#soi-003); [EII:SOI-005](#soi-005); [EII:MIC-007](#mic-007); [EII:SOI-013](#soi-013)

**Primary domain:** D11

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["composite"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "ecosystem", "watershed"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["condition", "assessment"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:FUN-012","domain":"D11","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["composite"],"tertiary":{"spatial":["plot","ecosystem","watershed"],"temporal":["season","year"]},"quaternary":["condition","assessment"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** A composite soil-health index combines specified soil metrics against explicit reference conditions.
- **Direct observations / derivation:** Named variables, weights, transformations and missing-data rules, dimensionless declared score.
- **Inference and limits:** Supports within-framework condition screening; no universal score or threshold and opposing components can be hidden.
- **Supporting indicators:** [EII:SOI-003](#soi-003), [EII:SOI-005](#soi-005), [EII:MIC-007](#mic-007), [EII:SOI-013](#soi-013).

<a id="fun-013"></a>

### EII:FUN-013 — Ecosystem condition / integrity index

**Definition:** Ecosystem condition/integrity index combines selected ecosystem properties relative to a declared reference.

**Direct observations / derivation:** Explicit extent, composition, structure and function metrics with weights, score and uncertainty.

**Inference and limits:** Supports reference-based condition comparison; sensitive to ecosystem type, baseline, weights and incomplete coverage.

**Display label:** Ecosystem-condition score

**Display measurement:** Combined habitat maps, species surveys and process measurements. Explicit extent, composition, structure and function metrics with weights, score and uncertainty.

**Display interpretation:** Summarises ecosystem condition against a chosen reference. Results depend on what is measured and the reference used.

**Measurement origin:** Combined habitat maps, species surveys and process measurements

**Supporting indicators:** [EII:BIO-005](#bio-005); [EII:BIO-002](#bio-002); [EII:TER-013](#ter-013); [EII:FUN-001](#fun-001)

**Primary domain:** D11

**Secondary domains:** `[]`

**Classification dimensions:** `["composite", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["condition", "assessment"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["land", "bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS005, RS006, RS009; Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:FUN-013","domain":"D11","related_domains":[],"record_type":"indicator","variants":[],"secondary":["composite","modelled"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["condition","assessment"],"routes":["land","bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Ecosystem condition/integrity index combines selected ecosystem properties relative to a declared reference.
- **Direct observations / derivation:** Explicit extent, composition, structure and function metrics with weights, score and uncertainty.
- **Inference and limits:** Supports reference-based condition comparison; sensitive to ecosystem type, baseline, weights and incomplete coverage.
- **Supporting indicators:** [EII:BIO-005](#bio-005), [EII:BIO-002](#bio-002), [EII:TER-013](#ter-013), [EII:FUN-001](#fun-001).

<a id="fun-014"></a>

### EII:FUN-014 — Planetary / regional boundary exceedance

**Definition:** Boundary exceedance compares a specified control variable against a cited threshold and scale.

**Direct observations / derivation:** Observed/modelled variable and versioned threshold; report signed difference or appropriate ratio with uncertainty.

**Inference and limits:** Supports framework-specific pressure assessment; a global threshold cannot be allocated locally without an explicit scientifically justified method.

**Display label:** Ecological boundary exceedance

**Display measurement:** Scientific monitoring/model results compared with a stated threshold. Observed/modelled variable and versioned threshold; report signed difference or appropriate ratio with uncertainty.

**Display interpretation:** Shows whether a chosen measure is above or below a stated threshold. Global thresholds cannot simply be applied to a farm or region.

**Measurement origin:** Scientific monitoring/model results compared with a stated threshold

**Supporting indicators:** [EII:PB-001](#pb-001); [EII:PB-002](#pb-002); [EII:PB-003](#pb-003); [EII:PB-004](#pb-004)

**Primary domain:** D15

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["region", "planet"], "temporal": ["year", "decade"]}`

**Ecological purpose:** `["system_pressure", "threshold_comparison"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `[]`

**Scientific reference keys:** `[]`

**Display source keys:** Field/lab/model source to register

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:FUN-014","domain":"D15","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","modelled"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Boundary exceedance compares a specified control variable against a cited threshold and scale.
- **Direct observations / derivation:** Observed/modelled variable and versioned threshold; report signed difference or appropriate ratio with uncertainty.
- **Inference and limits:** Supports framework-specific pressure assessment; a global threshold cannot be allocated locally without an explicit scientifically justified method.
- **Supporting indicators:** [EII:PB-001](#pb-001), [EII:PB-002](#pb-002), [EII:PB-003](#pb-003), [EII:PB-004](#pb-004).

<a id="atm-001"></a>

### EII:ATM-001 — Air temperature

**Definition:** Temperature of air at a specified height/exposure.

**Direct observations / derivation:** Shielded calibrated sensor, °C; averages require declared interval.

**Inference and limits:** Supports heat/cold exposure assessment; local microclimates and sensor shielding affect comparability.

**Display label:** Air temperature

**Display measurement:** Weather-station temperature sensors. Shielded calibrated sensor, °C; averages require declared interval.

**Display interpretation:** Shows local heat and cold conditions. Nearby shade, exposure and sensor placement affect readings.

**Measurement origin:** Weather-station temperature sensors

**Supporting indicators:** [EII:DIS-006](#dis-006); [EII:DIS-008](#dis-008); [EII:VEG-016](#veg-016)

**Primary domain:** D01

**Secondary domains:** `[]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "landscape", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:ATM-001","domain":"D01","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Temperature of air at a specified height/exposure.
- **Direct observations / derivation:** Shielded calibrated sensor, °C; averages require declared interval.
- **Inference and limits:** Supports heat/cold exposure assessment; local microclimates and sensor shielding affect comparability.
- **Supporting indicators:** [EII:DIS-006](#dis-006), [EII:DIS-008](#dis-008), [EII:VEG-016](#veg-016).

<a id="atm-002"></a>

### EII:ATM-002 — Precipitation amount/intensity

**Definition:** Liquid-equivalent precipitation accumulated or received per time.

**Direct observations / derivation:** Gauge/radar observations, mm and mm/h; snow and wind require corrections.

**Inference and limits:** Supports water inputs and erosion forcing; spatial variability prevents assuming a point gauge represents a watershed.

**Display label:** Rainfall and snowfall

**Display measurement:** Rain/snow gauges or weather radar. Gauge/radar observations, mm and mm/h; snow and wind require corrections.

**Display interpretation:** Shows water arriving as rain or snow and how quickly it falls. One gauge may not represent a whole watershed.

**Measurement origin:** Rain/snow gauges or weather radar

**Supporting indicators:** [EII:HYD-006](#hyd-006); [EII:HYD-001](#hyd-001); [EII:SOI-012](#soi-012)

**Primary domain:** D01

**Secondary domains:** `[]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "landscape", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:ATM-002","domain":"D01","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Liquid-equivalent precipitation accumulated or received per time.
- **Direct observations / derivation:** Gauge/radar observations, mm and mm/h; snow and wind require corrections.
- **Inference and limits:** Supports water inputs and erosion forcing; spatial variability prevents assuming a point gauge represents a watershed.
- **Supporting indicators:** [EII:HYD-006](#hyd-006), [EII:HYD-001](#hyd-001), [EII:SOI-012](#soi-012).

<a id="atm-003"></a>

### EII:ATM-003 — Relative humidity/vapour-pressure deficit

**Definition:** RH is saturation-relative water vapour; VPD is saturation minus actual vapour pressure.

**Direct observations / derivation:** Calibrated temperature/RH, %; calculate VPD, kPa, with stated temperature basis.

**Inference and limits:** Supports atmospheric drying-demand assessment; VPD is not soil drought or actual transpiration.

**Display label:** Air humidity and drying demand

**Display measurement:** Weather-station temperature and humidity sensors. Calibrated temperature/RH, %; calculate VPD, kPa, with stated temperature basis.

**Display interpretation:** Helps assess how strongly the air can draw water from plants. This does not show how dry the soil is.

**Measurement origin:** Weather-station temperature and humidity sensors

**Supporting indicators:** [EII:HYD-001](#hyd-001); [EII:HYD-012](#hyd-012); [EII:VEG-015](#veg-015)

**Primary domain:** D01

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "landscape", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["relative_humidity", "vapour_pressure_deficit"]`

**Record type:** family

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:ATM-003","domain":"D01","related_domains":[],"record_type":"family","variants":["relative_humidity","vapour_pressure_deficit"],"secondary":["measured","derived"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** RH is saturation-relative water vapour; VPD is saturation minus actual vapour pressure.
- **Direct observations / derivation:** Calibrated temperature/RH, %; calculate VPD, kPa, with stated temperature basis.
- **Inference and limits:** Supports atmospheric drying-demand assessment; VPD is not soil drought or actual transpiration.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:HYD-012](#hyd-012), [EII:VEG-015](#veg-015).

<a id="atm-004"></a>

### EII:ATM-004 — Photosynthetically active radiation

**Definition:** Photon flux in the declared photosynthetic wavelength range.

**Direct observations / derivation:** Quantum sensor, µmol photons/m²/s, commonly 400–700 nm; integrate daily separately.

**Inference and limits:** Supports light availability; intercepted/absorbed radiation and canopy physiology determine production.

**Display label:** Light for photosynthesis

**Display measurement:** Field light sensors. Quantum sensor, µmol photons/m²/s, commonly 400–700 nm; integrate daily separately.

**Display interpretation:** Shows light available for photosynthesis. The amount plants absorb and use also depends on the canopy and plant condition.

**Measurement origin:** Field light sensors

**Supporting indicators:** [EII:VEG-011](#veg-011); [EII:FUN-001](#fun-001); [EII:TER-004](#ter-004)

**Primary domain:** D01

**Secondary domains:** `[]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "landscape", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:ATM-004","domain":"D01","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Photon flux in the declared photosynthetic wavelength range.
- **Direct observations / derivation:** Quantum sensor, µmol photons/m²/s, commonly 400–700 nm; integrate daily separately.
- **Inference and limits:** Supports light availability; intercepted/absorbed radiation and canopy physiology determine production.
- **Supporting indicators:** [EII:VEG-011](#veg-011), [EII:FUN-001](#fun-001), [EII:TER-004](#ter-004).

<a id="atm-005"></a>

### EII:ATM-005 — Wind speed/direction

**Definition:** Airflow magnitude and compass direction at a stated height.

**Direct observations / derivation:** Calibrated anemometer, m/s and degrees, with averaging/gust convention.

**Inference and limits:** Supports aerodynamic demand, dispersal and fire context; roughness and shelter affect local exposure.

**Display label:** Wind speed and direction

**Display measurement:** Weather-station wind sensors. Calibrated anemometer, m/s and degrees, with averaging/gust convention.

**Display interpretation:** Helps assess exposure, drying and possible spread of fire or airborne material. Shelter and measurement height affect readings.

**Measurement origin:** Weather-station wind sensors

**Supporting indicators:** [EII:HYD-012](#hyd-012); [EII:DIS-002](#dis-002); [EII:BIO-008](#bio-008)

**Primary domain:** D01

**Secondary domains:** `[]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "landscape", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:ATM-005","domain":"D01","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Airflow magnitude and compass direction at a stated height.
- **Direct observations / derivation:** Calibrated anemometer, m/s and degrees, with averaging/gust convention.
- **Inference and limits:** Supports aerodynamic demand, dispersal and fire context; roughness and shelter affect local exposure.
- **Supporting indicators:** [EII:HYD-012](#hyd-012), [EII:DIS-002](#dis-002), [EII:BIO-008](#bio-008).

<a id="atm-006"></a>

### EII:ATM-006 — Atmospheric CO₂ concentration

**Definition:** CO₂ mole fraction in a declared air sample.

**Direct observations / derivation:** Calibrated gas analyser, µmol/mol or ppm, with dry-air convention.

**Inference and limits:** Supports carbon-cycle context; local concentration changes are not ecosystem flux without transport analysis.

**Display label:** Atmospheric CO₂ concentration

**Display measurement:** Air-sampling gas analysers. Calibrated gas analyser, µmol/mol or ppm, with dry-air convention.

**Display interpretation:** Shows carbon dioxide in the air. Local concentration changes do not directly measure carbon uptake or release by an ecosystem.

**Measurement origin:** Air-sampling gas analysers

**Supporting indicators:** [EII:CYC-001](#cyc-001); [EII:FUN-001](#fun-001); [EII:PB-001](#pb-001)

**Primary domain:** D01

**Secondary domains:** `[]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "landscape", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:ATM-006","domain":"D01","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** CO₂ mole fraction in a declared air sample.
- **Direct observations / derivation:** Calibrated gas analyser, µmol/mol or ppm, with dry-air convention.
- **Inference and limits:** Supports carbon-cycle context; local concentration changes are not ecosystem flux without transport analysis.
- **Supporting indicators:** [EII:CYC-001](#cyc-001), [EII:FUN-001](#fun-001), [EII:PB-001](#pb-001).

<a id="atm-007"></a>

### EII:ATM-007 — Ozone exposure

**Definition:** Near-surface ozone concentration and separately computed cumulative exposure.

**Direct observations / derivation:** Calibrated analyser, nmol/mol; dose/exposure metrics require declared threshold and time window.

**Inference and limits:** Supports plant pollution-risk assessment; stomatal uptake, phenology and species determine injury.

**Display label:** Ozone exposure

**Display measurement:** Air-quality monitoring sensors. Calibrated analyser, nmol/mol; dose/exposure metrics require declared threshold and time window.

**Display interpretation:** Helps assess ozone exposure that could harm plants. Actual damage depends on plant type, timing and ozone uptake.

**Measurement origin:** Air-quality monitoring sensors

**Supporting indicators:** [EII:VEG-015](#veg-015); [EII:ATM-003](#atm-003); [EII:VEG-017](#veg-017)

**Primary domain:** D01

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "derived", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "landscape", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:ATM-007","domain":"D01","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","derived","pressure"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["pressure"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Near-surface ozone concentration and separately computed cumulative exposure.
- **Direct observations / derivation:** Calibrated analyser, nmol/mol; dose/exposure metrics require declared threshold and time window.
- **Inference and limits:** Supports plant pollution-risk assessment; stomatal uptake, phenology and species determine injury.
- **Supporting indicators:** [EII:VEG-015](#veg-015), [EII:ATM-003](#atm-003), [EII:VEG-017](#veg-017).

<a id="atm-008"></a>

### EII:ATM-008 — PM₂.₅/PM₁₀ concentration

**Definition:** Airborne particle mass within defined aerodynamic size fractions.

**Direct observations / derivation:** Gravimetric/reference-calibrated sensor, µg/m³, with humidity and averaging metadata.

**Inference and limits:** Supports particulate exposure assessment; optical sensors need calibration and mass does not identify composition/source.

**Display label:** Fine airborne particles

**Display measurement:** Air-sampling laboratory tests or calibrated particle sensors. Gravimetric/reference-calibrated sensor, µg/m³, with humidity and averaging metadata.

**Display interpretation:** Shows the amount of fine airborne particles. Particle mass alone does not identify their chemicals or where they came from.

**Measurement origin:** Air-sampling laboratory tests or calibrated particle sensors

**Supporting indicators:** [EII:ATM-005](#atm-005); [EII:HUM-008](#hum-008); [EII:PB-009](#pb-009)

**Primary domain:** D01

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "landscape", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `["PM2_5", "PM10"]`

**Record type:** family

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:ATM-008","domain":"D01","related_domains":[],"record_type":"family","variants":["PM2_5","PM10"],"secondary":["measured","pressure"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["pressure"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Airborne particle mass within defined aerodynamic size fractions.
- **Direct observations / derivation:** Gravimetric/reference-calibrated sensor, µg/m³, with humidity and averaging metadata.
- **Inference and limits:** Supports particulate exposure assessment; optical sensors need calibration and mass does not identify composition/source.
- **Supporting indicators:** [EII:ATM-005](#atm-005), [EII:HUM-008](#hum-008), [EII:PB-009](#pb-009).

<a id="atm-009"></a>

### EII:ATM-009 — Snow cover/snow water equivalent

**Definition:** Snow-covered fraction and stored liquid-equivalent water are separate quantities.

**Direct observations / derivation:** Mapped snow fraction, %; snow depth/density survey or retrieval, mm water equivalent.

**Inference and limits:** Supports meltwater-storage assessment; cover alone does not establish volume or melt rate.

**Display label:** Snow cover and stored water

**Display measurement:** Satellite snow maps and field depth/density surveys. Mapped snow fraction, %; snow depth/density survey or retrieval, mm water equivalent.

**Display interpretation:** Helps assess snow-covered area and stored meltwater. Snow cover alone does not show how much water the snow contains.

**Measurement origin:** Satellite snow maps and field depth/density surveys

**Supporting indicators:** [EII:ATM-001](#atm-001); [EII:HYD-006](#hyd-006); [EII:HYD-001](#hyd-001)

**Primary domain:** D01

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "landscape", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["snow_cover", "snow_water_equivalent"]`

**Record type:** family

**Candidate source routes:** `["opt", "iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS001, RS002; IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:ATM-009","domain":"D01","related_domains":[],"record_type":"family","variants":["snow_cover","snow_water_equivalent"],"secondary":["measured","derived"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["opt","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Snow-covered fraction and stored liquid-equivalent water are separate quantities.
- **Direct observations / derivation:** Mapped snow fraction, %; snow depth/density survey or retrieval, mm water equivalent.
- **Inference and limits:** Supports meltwater-storage assessment; cover alone does not establish volume or melt rate.
- **Supporting indicators:** [EII:ATM-001](#atm-001), [EII:HYD-006](#hyd-006), [EII:HYD-001](#hyd-001).

<a id="hyd-013"></a>

### EII:HYD-013 — Dissolved oxygen

**Definition:** Oxygen dissolved in water, on concentration or saturation basis.

**Direct observations / derivation:** Calibrated optical/electrochemical probe or titration, mg/L and % saturation, with temperature/salinity.

**Inference and limits:** Supports oxygen-habitat assessment; diurnal cycles and flow matter and low oxygen is not uniquely eutrophication.

**Display label:** Dissolved oxygen

**Display measurement:** Field oxygen probes or laboratory water tests. Calibrated optical/electrochemical probe or titration, mg/L and % saturation, with temperature/salinity.

**Display interpretation:** Helps assess whether water contains enough oxygen for aquatic life. Levels can vary with temperature, flow and time of day.

**Measurement origin:** Field oxygen probes or laboratory water tests

**Supporting indicators:** [EII:HYD-014](#hyd-014); [EII:HYD-015](#hyd-015); [EII:HYD-010](#hyd-010)

**Primary domain:** D02

**Secondary domains:** `[]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "watershed", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `["R10"]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Review scope:** specific_documentary_aspects_only

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-013","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":["R10"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** Oxygen dissolved in water, on concentration or saturation basis.
- **Direct observations / derivation:** Calibrated optical/electrochemical probe or titration, mg/L and % saturation, with temperature/salinity.
- **Inference and limits:** Supports oxygen-habitat assessment; diurnal cycles and flow matter and low oxygen is not uniquely eutrophication.
- **Supporting indicators:** [EII:HYD-014](#hyd-014), [EII:HYD-015](#hyd-015), [EII:HYD-010](#hyd-010).

<a id="hyd-014"></a>

### EII:HYD-014 — Water chlorophyll-a

**Definition:** Chlorophyll-a pigment concentration in a water sample.

**Direct observations / derivation:** Extracted pigment assay, µg/L; fluorescence/remote retrievals need calibration.

**Inference and limits:** Supports phytoplankton-biomass assessment; pigment per cell, taxonomic composition and turbidity vary.

**Display label:** Water chlorophyll-a

**Display measurement:** Laboratory pigment tests or calibrated fluorescence/imagery. Extracted pigment assay, µg/L; fluorescence/remote retrievals need calibration.

**Display interpretation:** Helps estimate the amount of microscopic algae in water. Pigment levels and cloudiness can affect the estimate.

**Measurement origin:** Laboratory pigment tests or calibrated fluorescence/imagery

**Supporting indicators:** [EII:HYD-010](#hyd-010); [EII:HYD-013](#hyd-013); [EII:HYD-009](#hyd-009)

**Primary domain:** D02

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "watershed", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["marine", "iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS018; IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-014","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","proxy"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["marine","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Chlorophyll-a pigment concentration in a water sample.
- **Direct observations / derivation:** Extracted pigment assay, µg/L; fluorescence/remote retrievals need calibration.
- **Inference and limits:** Supports phytoplankton-biomass assessment; pigment per cell, taxonomic composition and turbidity vary.
- **Supporting indicators:** [EII:HYD-010](#hyd-010), [EII:HYD-013](#hyd-013), [EII:HYD-009](#hyd-009).

<a id="hyd-015"></a>

### EII:HYD-015 — Water temperature

**Definition:** Temperature of water at specified depth/time.

**Direct observations / derivation:** Calibrated profile/probe, °C.

**Inference and limits:** Supports thermal habitat and oxygen-solubility assessment; surface estimates do not represent deep-water conditions.

**Display label:** Water temperature

**Display measurement:** Water temperature sensors or suitable satellite estimates. Calibrated profile/probe, °C.

**Display interpretation:** Shows thermal conditions for aquatic life. Surface temperature may not represent deeper water.

**Measurement origin:** Water temperature sensors or suitable satellite estimates

**Supporting indicators:** [EII:HYD-013](#hyd-013); [EII:HYD-006](#hyd-006); [EII:ATM-001](#atm-001)

**Primary domain:** D02

**Secondary domains:** `[]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "watershed", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["marine", "iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS018; IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-015","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["marine","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Temperature of water at specified depth/time.
- **Direct observations / derivation:** Calibrated profile/probe, °C.
- **Inference and limits:** Supports thermal habitat and oxygen-solubility assessment; surface estimates do not represent deep-water conditions.
- **Supporting indicators:** [EII:HYD-013](#hyd-013), [EII:HYD-006](#hyd-006), [EII:ATM-001](#atm-001).

<a id="hyd-016"></a>

### EII:HYD-016 — Surface-water occurrence/hydroperiod

**Definition:** Frequency or duration of surface inundation.

**Direct observations / derivation:** Valid water detections/valid observations, %; continuous gauge/time series for days inundated.

**Inference and limits:** Supports wetland persistence assessment; cloud/sensor sampling biases fractions and groundwater saturation may be invisible.

**Display label:** Surface-water presence and duration

**Display measurement:** Repeated satellite water maps or field water-level sensors. Valid water detections/valid observations, %; continuous gauge/time series for days inundated.

**Display interpretation:** Shows how often or how long surface water is present. Missed observations and hidden soil saturation can affect the result.

**Measurement origin:** Repeated satellite water maps or field water-level sensors

**Supporting indicators:** [EII:HYD-008](#hyd-008); [EII:HYD-007](#hyd-007); [EII:BIO-005](#bio-005)

**Primary domain:** D02

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "watershed", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["water", "iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS013; IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-016","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["water","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Frequency or duration of surface inundation.
- **Direct observations / derivation:** Valid water detections/valid observations, %; continuous gauge/time series for days inundated.
- **Inference and limits:** Supports wetland persistence assessment; cloud/sensor sampling biases fractions and groundwater saturation may be invisible.
- **Supporting indicators:** [EII:HYD-008](#hyd-008), [EII:HYD-007](#hyd-007), [EII:BIO-005](#bio-005).

<a id="hyd-017"></a>

### EII:HYD-017 — Environmental-flow deficit

**Definition:** Deviation of actual flow from a specified ecological-flow requirement.

**Direct observations / derivation:** Discharge series and justified seasonal reference, m³/s, deficit duration or volume.

**Inference and limits:** Supports aquatic stress assessment; thresholds must be basin/species specific and flow quality also matters.

**Display label:** Ecological flow shortfall

**Display measurement:** River-flow records and a local ecological-flow reference. Discharge series and justified seasonal reference, m³/s, deficit duration or volume.

**Display interpretation:** Helps identify flows below a locally defined ecological need. The threshold must fit the river and its species.

**Measurement origin:** River-flow records and a local ecological-flow reference

**Supporting indicators:** [EII:HYD-006](#hyd-006); [EII:HYD-015](#hyd-015); [EII:BIO-002](#bio-002)

**Primary domain:** D02

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "watershed", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-017","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","pressure"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["pressure"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Deviation of actual flow from a specified ecological-flow requirement.
- **Direct observations / derivation:** Discharge series and justified seasonal reference, m³/s, deficit duration or volume.
- **Inference and limits:** Supports aquatic stress assessment; thresholds must be basin/species specific and flow quality also matters.
- **Supporting indicators:** [EII:HYD-006](#hyd-006), [EII:HYD-015](#hyd-015), [EII:BIO-002](#bio-002).

<a id="hyd-018"></a>

### EII:HYD-018 — Water nutrient load

**Definition:** Mass of a specified nutrient transported per time.

**Direct observations / derivation:** Time-resolved concentration × discharge, kg N/P/day; integrate with appropriate sampling.

**Inference and limits:** Supports export assessment; sparse sampling misses storm pulses and does not establish source attribution.

**Display label:** Nutrients carried by water

**Display measurement:** River-flow measurements combined with laboratory nutrient tests. Time-resolved concentration × discharge, kg N/P/day; integrate with appropriate sampling.

**Display interpretation:** Shows how much nutrient is carried by water. Storms can carry large amounts that occasional samples miss.

**Measurement origin:** River-flow measurements combined with laboratory nutrient tests

**Supporting indicators:** [EII:HYD-010](#hyd-010); [EII:HYD-006](#hyd-006); [EII:FUN-003](#fun-003)

**Primary domain:** D02

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["derived", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "watershed", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot", "amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future); AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-018","domain":"D02","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["function"],"routes":["iot","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Mass of a specified nutrient transported per time.
- **Direct observations / derivation:** Time-resolved concentration × discharge, kg N/P/day; integrate with appropriate sampling.
- **Inference and limits:** Supports export assessment; sparse sampling misses storm pulses and does not establish source attribution.
- **Supporting indicators:** [EII:HYD-010](#hyd-010), [EII:HYD-006](#hyd-006), [EII:FUN-003](#fun-003).

<a id="hyd-019"></a>

### EII:HYD-019 — Faecal indicator bacteria

**Definition:** Concentration of specified culturable or molecular faecal indicators.

**Direct observations / derivation:** Validated assay, CFU/100 mL, MPN/100 mL or gene copies with method separated.

**Inference and limits:** Supports contamination screening; indicators do not quantify every pathogen and molecular detections may include nonviable material.

**Display label:** Faecal indicator bacteria

**Display measurement:** Water samples tested in a microbiology laboratory. Validated assay, CFU/100 mL, MPN/100 mL or gene copies with method separated.

**Display interpretation:** Helps screen for faecal contamination. Indicator bacteria do not identify every pathogen or guarantee that water is safe.

**Measurement origin:** Water samples tested in a microbiology laboratory

**Supporting indicators:** [EII:HYD-006](#hyd-006); [EII:HYD-015](#hyd-015); [EII:HYD-011](#hyd-011)

**Primary domain:** D02

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-019","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","proxy"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Concentration of specified culturable or molecular faecal indicators.
- **Direct observations / derivation:** Validated assay, CFU/100 mL, MPN/100 mL or gene copies with method separated.
- **Inference and limits:** Supports contamination screening; indicators do not quantify every pathogen and molecular detections may include nonviable material.
- **Supporting indicators:** [EII:HYD-006](#hyd-006), [EII:HYD-015](#hyd-015), [EII:HYD-011](#hyd-011).

<a id="hyd-020"></a>

### EII:HYD-020 — Water contaminant residues

**Definition:** Concentration of named pesticides, pharmaceuticals or other chemicals in water.

**Direct observations / derivation:** Validated chemical analysis, µg/L, with recovery and detection limits.

**Inference and limits:** Supports chemical-exposure assessment; toxicity depends on mixtures, duration and organism and non-detects are censored observations.

**Display label:** Chemical residues in water

**Display measurement:** Water samples tested in a chemistry laboratory. Validated chemical analysis, µg/L, with recovery and detection limits.

**Display interpretation:** Shows named chemical residues in water. Their effects depend on concentration, exposure time, mixtures and organisms.

**Measurement origin:** Water samples tested in a chemistry laboratory

**Supporting indicators:** [EII:HYD-006](#hyd-006); [EII:FUN-007](#fun-007); [EII:HUM-005](#hum-005)

**Primary domain:** D02

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "watershed", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-020","domain":"D02","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","pressure"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["pressure"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Concentration of named pesticides, pharmaceuticals or other chemicals in water.
- **Direct observations / derivation:** Validated chemical analysis, µg/L, with recovery and detection limits.
- **Inference and limits:** Supports chemical-exposure assessment; toxicity depends on mixtures, duration and organism and non-detects are censored observations.
- **Supporting indicators:** [EII:HYD-006](#hyd-006), [EII:FUN-007](#fun-007), [EII:HUM-005](#hum-005).

<a id="hyd-021"></a>

### EII:HYD-021 — Water transparency/Secchi depth

**Definition:** Depth at which a standard disk becomes invisible under a declared protocol.

**Direct observations / derivation:** Disk visibility depth, m, recording light and viewing conditions.

**Inference and limits:** Supports optical habitat comparison; algae, sediment and dissolved colour contribute jointly.

**Display label:** Water clarity

**Display measurement:** Field Secchi-disk measurements. Disk visibility depth, m, recording light and viewing conditions.

**Display interpretation:** Shows how clear water is. Algae, sediment and dissolved colour can all reduce clarity.

**Measurement origin:** Field Secchi-disk measurements

**Supporting indicators:** [EII:HYD-014](#hyd-014); [EII:HYD-009](#hyd-009); [EII:HYD-015](#hyd-015)

**Primary domain:** D02

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "watershed", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `[]`

**Scientific reference keys:** `[]`

**Display source keys:** Field/lab/model source to register

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-021","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","proxy"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Depth at which a standard disk becomes invisible under a declared protocol.
- **Direct observations / derivation:** Disk visibility depth, m, recording light and viewing conditions.
- **Inference and limits:** Supports optical habitat comparison; algae, sediment and dissolved colour contribute jointly.
- **Supporting indicators:** [EII:HYD-014](#hyd-014), [EII:HYD-009](#hyd-009), [EII:HYD-015](#hyd-015).

<a id="hyd-022"></a>

### EII:HYD-022 — Ocean carbonate chemistry

**Definition:** Dissolved inorganic carbon, alkalinity and associated carbonate speciation.

**Direct observations / derivation:** Paired measured carbonate-system quantities, µmol/kg, with temperature/salinity; calculate pH or saturation consistently.

**Inference and limits:** Supports acidification assessment; a single pH observation does not resolve the entire carbonate system.

**Display label:** Ocean carbonate chemistry

**Display measurement:** Laboratory seawater chemistry tests and carbonate calculations. Paired measured carbonate-system quantities, µmol/kg, with temperature/salinity; calculate pH or saturation consistently.

**Display interpretation:** Helps understand ocean acidity and conditions for shell-forming organisms. One pH reading does not describe the full chemical balance.

**Measurement origin:** Laboratory seawater chemistry tests and carbonate calculations

**Supporting indicators:** [EII:HYD-011](#hyd-011); [EII:HYD-015](#hyd-015); [EII:PB-008](#pb-008)

**Primary domain:** D02

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["site", "watershed", "region"], "temporal": ["hour", "day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["marine"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS018

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HYD-022","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["marine"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Dissolved inorganic carbon, alkalinity and associated carbonate speciation.
- **Direct observations / derivation:** Paired measured carbonate-system quantities, µmol/kg, with temperature/salinity; calculate pH or saturation consistently.
- **Inference and limits:** Supports acidification assessment; a single pH observation does not resolve the entire carbonate system.
- **Supporting indicators:** [EII:HYD-011](#hyd-011), [EII:HYD-015](#hyd-015), [EII:PB-008](#pb-008).

<a id="soi-014"></a>

### EII:SOI-014 — Coarse fragments/soil depth

**Definition:** Stone volume fraction and depth of the defined soil profile.

**Direct observations / derivation:** Field cores/pits, %, cm; distinguish rock, roots and fine earth.

**Inference and limits:** Supports rooting/storage and carbon-stock corrections; shallow sampling cannot establish whole-profile stocks.

**Display label:** Stones and soil depth

**Display measurement:** Field soil pits and cores. Field cores/pits, %, cm; distinguish rock, roots and fine earth.

**Display interpretation:** Shows soil depth and the amount of stones. Both affect rooting space, water storage and carbon-stock estimates.

**Measurement origin:** Field soil pits and cores

**Supporting indicators:** [EII:SOI-005](#soi-005); [EII:SOI-002](#soi-002); [EII:HYD-005](#hyd-005)

**Primary domain:** D03

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["coarse_fragment_volume_fraction", "soil_depth"]`

**Record type:** family

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-014","domain":"D03","related_domains":["D13"],"record_type":"family","variants":["coarse_fragment_volume_fraction","soil_depth"],"secondary":["measured"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Stone volume fraction and depth of the defined soil profile.
- **Direct observations / derivation:** Field cores/pits, %, cm; distinguish rock, roots and fine earth.
- **Inference and limits:** Supports rooting/storage and carbon-stock corrections; shallow sampling cannot establish whole-profile stocks.
- **Supporting indicators:** [EII:SOI-005](#soi-005), [EII:SOI-002](#soi-002), [EII:HYD-005](#hyd-005).

<a id="soi-015"></a>

### EII:SOI-015 — Saturated hydraulic conductivity

**Definition:** Water-transmission capacity under saturated conditions.

**Direct observations / derivation:** Permeameter or field hydraulic test, mm/h or m/s with geometry specified.

**Inference and limits:** Supports drainage assessment; preferential flow and small sample volume limit extrapolation.

**Display label:** Water movement through saturated soil

**Display measurement:** Field soil samples analysed in a laboratory. Permeameter or field hydraulic test, mm/h or m/s with geometry specified.

**Display interpretation:** Shows how easily water moves through saturated soil. Small samples may miss channels that carry water quickly in the field.

**Measurement origin:** Field soil samples analysed in a laboratory

**Supporting indicators:** [EII:SOI-004](#soi-004); [EII:HYD-004](#hyd-004); [EII:HYD-001](#hyd-001)

**Primary domain:** D03

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["event", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-015","domain":"D03","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Water-transmission capacity under saturated conditions.
- **Direct observations / derivation:** Permeameter or field hydraulic test, mm/h or m/s with geometry specified.
- **Inference and limits:** Supports drainage assessment; preferential flow and small sample volume limit extrapolation.
- **Supporting indicators:** [EII:SOI-004](#soi-004), [EII:HYD-004](#hyd-004), [EII:HYD-001](#hyd-001).

<a id="soi-016"></a>

### EII:SOI-016 — Soil matric potential

**Definition:** Energy state of soil water relative to a reference.

**Direct observations / derivation:** Tensiometer/validated sensor, kPa, at declared depth; specify sign convention.

**Inference and limits:** Supports plant-water access assessment; texture and osmotic potential must also be considered.

**Display label:** Soil water tension

**Display measurement:** Field soil-water pressure sensors. Tensiometer/validated sensor, kPa, at declared depth; specify sign convention.

**Display interpretation:** Shows how tightly soil holds water. Salt content also affects how easily plants can take it up.

**Measurement origin:** Field soil-water pressure sensors

**Supporting indicators:** [EII:HYD-001](#hyd-001); [EII:SOI-007](#soi-007); [EII:HYD-005](#hyd-005)

**Primary domain:** D03

**Secondary domains:** `[]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-016","domain":"D03","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Energy state of soil water relative to a reference.
- **Direct observations / derivation:** Tensiometer/validated sensor, kPa, at declared depth; specify sign convention.
- **Inference and limits:** Supports plant-water access assessment; texture and osmotic potential must also be considered.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:SOI-007](#soi-007), [EII:HYD-005](#hyd-005).

<a id="soi-017"></a>

### EII:SOI-017 — Macropore abundance/connectivity

**Definition:** Large-pore fraction and spatial connectivity under a declared size threshold.

**Direct observations / derivation:** Imaging, dye tracing or pore analysis, fraction and declared connectivity metric.

**Inference and limits:** Supports preferential-flow hypotheses; static pore structure does not directly quantify solute transport.

**Display label:** Large soil pores

**Display measurement:** Laboratory pore imaging or field dye-tracing tests. Imaging, dye tracing or pore analysis, fraction and declared connectivity metric.

**Display interpretation:** Shows large soil pores and how they connect. Their presence alone does not measure actual water or nutrient movement.

**Measurement origin:** Laboratory pore imaging or field dye-tracing tests

**Supporting indicators:** [EII:SOI-015](#soi-015); [EII:SOI-004](#soi-004); [EII:FUN-003](#fun-003)

**Primary domain:** D03

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-017","domain":"D03","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Large-pore fraction and spatial connectivity under a declared size threshold.
- **Direct observations / derivation:** Imaging, dye tracing or pore analysis, fraction and declared connectivity metric.
- **Inference and limits:** Supports preferential-flow hypotheses; static pore structure does not directly quantify solute transport.
- **Supporting indicators:** [EII:SOI-015](#soi-015), [EII:SOI-004](#soi-004), [EII:FUN-003](#fun-003).

<a id="soi-018"></a>

### EII:SOI-018 — Total soil nitrogen/C:N ratio

**Definition:** Total N pool and organic-C to total-N mass ratio.

**Direct observations / derivation:** Elemental assays, g N/kg and dimensionless C:N, with matching sample basis.

**Inference and limits:** Supports substrate/stoichiometric comparison; total N does not equal mineral-N availability and ratio alone does not determine immobilisation.

**Display label:** Total soil nitrogen and carbon:nitrogen ratio

**Display measurement:** Field soil samples analysed in a laboratory. Elemental assays, g N/kg and dimensionless C:N, with matching sample basis.

**Display interpretation:** Helps compare total nitrogen and the balance of carbon to nitrogen. This does not directly measure nutrients available to plants.

**Measurement origin:** Field soil samples analysed in a laboratory

**Supporting indicators:** [EII:SOI-005](#soi-005); [EII:SOI-008](#soi-008); [EII:MIC-023](#mic-023)

**Primary domain:** D04

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["total_N", "C_to_N_ratio"]`

**Record type:** family

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-018","domain":"D04","related_domains":["D13"],"record_type":"family","variants":["total_N","C_to_N_ratio"],"secondary":["measured","derived"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Total N pool and organic-C to total-N mass ratio.
- **Direct observations / derivation:** Elemental assays, g N/kg and dimensionless C:N, with matching sample basis.
- **Inference and limits:** Supports substrate/stoichiometric comparison; total N does not equal mineral-N availability and ratio alone does not determine immobilisation.
- **Supporting indicators:** [EII:SOI-005](#soi-005), [EII:SOI-008](#soi-008), [EII:MIC-023](#mic-023).

<a id="soi-019"></a>

### EII:SOI-019 — Exchangeable sodium percentage/SAR

**Definition:** Method-defined indices of sodium dominance in exchange or solution chemistry.

**Direct observations / derivation:** ESP=100 exchangeable Na/CEC; SAR=Na/√((Ca+Mg)/2) with standard concentration basis.

**Inference and limits:** Supports sodicity screening; EC, mineralogy and compatible extraction are needed to infer dispersion risk.

**Display label:** Soil sodium indices

**Display measurement:** Field soil samples analysed in a laboratory. ESP=100 exchangeable Na/CEC; SAR=Na/√((Ca+Mg)/2) with standard concentration basis.

**Display interpretation:** Helps screen for sodium levels that may damage soil structure. Salt content and soil minerals also matter.

**Measurement origin:** Field soil samples analysed in a laboratory

**Supporting indicators:** [EII:SOI-007](#soi-007); [EII:SOI-009](#soi-009); [EII:SOI-003](#soi-003)

**Primary domain:** D04

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["derived", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `["ESP", "SAR"]`

**Record type:** family

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-019","domain":"D04","related_domains":["D13"],"record_type":"family","variants":["ESP","SAR"],"secondary":["derived","pressure"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["pressure"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Method-defined indices of sodium dominance in exchange or solution chemistry.
- **Direct observations / derivation:** ESP=100 exchangeable Na/CEC; SAR=Na/√((Ca+Mg)/2) with standard concentration basis.
- **Inference and limits:** Supports sodicity screening; EC, mineralogy and compatible extraction are needed to infer dispersion risk.
- **Supporting indicators:** [EII:SOI-007](#soi-007), [EII:SOI-009](#soi-009), [EII:SOI-003](#soi-003).

<a id="soi-020"></a>

### EII:SOI-020 — Soil inorganic carbon

**Definition:** Carbon held in carbonates and other inorganic forms on a specified basis.

**Direct observations / derivation:** Carbonate/inorganic C assay, g C/kg; stocks need depth/density/coarse fractions.

**Inference and limits:** Supports carbonate and C-budget assessment; carbonate accumulation is not automatically net atmospheric sequestration.

**Display label:** Soil mineral carbon

**Display measurement:** Field soil samples analysed in a laboratory. Carbonate/inorganic C assay, g C/kg; stocks need depth/density/coarse fractions.

**Display interpretation:** Shows carbon stored in soil minerals such as carbonates. More carbonate does not automatically mean more carbon removed from the atmosphere.

**Measurement origin:** Field soil samples analysed in a laboratory

**Supporting indicators:** [EII:SOI-005](#soi-005); [EII:SOI-006](#soi-006); [EII:FUN-002](#fun-002)

**Primary domain:** D04

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-020","domain":"D04","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Carbon held in carbonates and other inorganic forms on a specified basis.
- **Direct observations / derivation:** Carbonate/inorganic C assay, g C/kg; stocks need depth/density/coarse fractions.
- **Inference and limits:** Supports carbonate and C-budget assessment; carbonate accumulation is not automatically net atmospheric sequestration.
- **Supporting indicators:** [EII:SOI-005](#soi-005), [EII:SOI-006](#soi-006), [EII:FUN-002](#fun-002).

<a id="soi-021"></a>

### EII:SOI-021 — Labile/particulate/mineral-associated organic carbon

**Definition:** Distinct operational fractions of soil organic carbon.

**Direct observations / derivation:** Declared oxidation or physical fractionation, g C/kg; record size/density cut-offs and recoveries.

**Inference and limits:** Supports carbon-pool comparison; operational pools do not uniquely represent turnover time or permanence.

**Display label:** Soil organic-carbon fractions

**Display measurement:** Field soil samples analysed in a laboratory. Declared oxidation or physical fractionation, g C/kg; record size/density cut-offs and recoveries.

**Display interpretation:** Helps compare different soil organic-carbon fractions. The fractions do not give an exact lifetime for stored carbon.

**Measurement origin:** Field soil samples analysed in a laboratory

**Supporting indicators:** [EII:SOI-005](#soi-005); [EII:SOI-001](#soi-001); [EII:MIC-024](#mic-024)

**Primary domain:** D04

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["labile_C", "particulate_organic_C", "mineral_associated_organic_C"]`

**Record type:** family

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-021","domain":"D04","related_domains":["D13"],"record_type":"family","variants":["labile_C","particulate_organic_C","mineral_associated_organic_C"],"secondary":["measured"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Distinct operational fractions of soil organic carbon.
- **Direct observations / derivation:** Declared oxidation or physical fractionation, g C/kg; record size/density cut-offs and recoveries.
- **Inference and limits:** Supports carbon-pool comparison; operational pools do not uniquely represent turnover time or permanence.
- **Supporting indicators:** [EII:SOI-005](#soi-005), [EII:SOI-001](#soi-001), [EII:MIC-024](#mic-024).

<a id="soi-022"></a>

### EII:SOI-022 — Bioavailable contaminant fraction

**Definition:** Method-defined mobile/extractable fraction of a named contaminant.

**Direct observations / derivation:** Specified extraction, porewater or organism assay, mg/kg or µg/L.

**Inference and limits:** Supports exposure refinement; extraction is an approximation and organism-specific uptake requires validation.

**Display label:** Potentially available contaminants

**Display measurement:** Field soil samples analysed in a laboratory. Specified extraction, porewater or organism assay, mg/kg or µg/L.

**Display interpretation:** Helps estimate the fraction of a pollutant organisms might absorb. Laboratory extraction is an approximation that needs checking for the organism concerned.

**Measurement origin:** Field soil samples analysed in a laboratory

**Supporting indicators:** [EII:SOI-013](#soi-013); [EII:SOI-006](#soi-006); [EII:SOI-005](#soi-005)

**Primary domain:** D04

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `[]`

**Scientific reference keys:** `[]`

**Display source keys:** Field/lab/model source to register

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-022","domain":"D04","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","proxy"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["state"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Method-defined mobile/extractable fraction of a named contaminant.
- **Direct observations / derivation:** Specified extraction, porewater or organism assay, mg/kg or µg/L.
- **Inference and limits:** Supports exposure refinement; extraction is an approximation and organism-specific uptake requires validation.
- **Supporting indicators:** [EII:SOI-013](#soi-013), [EII:SOI-006](#soi-006), [EII:SOI-005](#soi-005).

<a id="soi-023"></a>

### EII:SOI-023 — Soil redox potential

**Definition:** Electrode potential indicating local oxidation–reduction conditions.

**Direct observations / derivation:** Calibrated redox electrodes, mV with reference electrode, pH, depth and equilibration.

**Inference and limits:** Supports anaerobic-process interpretation; mixed potentials and microsites prevent unique chemical speciation.

**Display label:** Soil oxidation–reduction conditions

**Display measurement:** Field redox electrodes. Calibrated redox electrodes, mV with reference electrode, pH, depth and equilibration.

**Display interpretation:** Helps assess whether soil conditions favour oxygen-dependent or oxygen-poor processes. Small areas within the soil may differ.

**Measurement origin:** Field redox electrodes

**Supporting indicators:** [EII:HYD-001](#hyd-001); [EII:MIC-012](#mic-012); [EII:CYC-003](#cyc-003)

**Primary domain:** D04

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:SOI-023","domain":"D04","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","proxy"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Electrode potential indicating local oxidation–reduction conditions.
- **Direct observations / derivation:** Calibrated redox electrodes, mV with reference electrode, pH, depth and equilibration.
- **Inference and limits:** Supports anaerobic-process interpretation; mixed potentials and microsites prevent unique chemical speciation.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:MIC-012](#mic-012), [EII:CYC-003](#cyc-003).

<a id="mic-025"></a>

### EII:MIC-025 — Absolute microbial load

**Definition:** Number or biomass of microbial cells in a defined soil/sample quantity.

**Direct observations / derivation:** Calibrated flow counts, spike-in sequencing or validated qPCR, cells/g or copies/g; gene copies are not automatically cells.

**Inference and limits:** Supports interpretation of relative profiles; extraction recovery, viability and copy number remain method-dependent.

**Display label:** Microbial numbers

**Display measurement:** Laboratory cell counts or calibrated molecular tests. Calibrated flow counts, spike-in sequencing or validated qPCR, cells/g or copies/g; gene copies are not automatically cells.

**Display interpretation:** Helps estimate microbial numbers rather than just relative shares. Recovery and gene copies per cell affect some methods.

**Measurement origin:** Laboratory cell counts or calibrated molecular tests

**Supporting indicators:** [EII:MIC-001](#mic-001); [EII:MIC-007](#mic-007); [EII:MIC-005](#mic-005)

**Primary domain:** D05

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `["R05"]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Review scope:** specific_documentary_aspects_only

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-025","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":["R05"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** Number or biomass of microbial cells in a defined soil/sample quantity.
- **Direct observations / derivation:** Calibrated flow counts, spike-in sequencing or validated qPCR, cells/g or copies/g; gene copies are not automatically cells.
- **Inference and limits:** Supports interpretation of relative profiles; extraction recovery, viability and copy number remain method-dependent.
- **Supporting indicators:** [EII:MIC-001](#mic-001), [EII:MIC-007](#mic-007), [EII:MIC-005](#mic-005).

<a id="mic-026"></a>

### EII:MIC-026 — Soil fauna abundance/biomass

**Definition:** Abundance or dry mass of defined soil-animal groups.

**Direct observations / derivation:** Standardised cores/extraction/hand sorting, individuals/m² or g/m², with depth and season.

**Inference and limits:** Supports below-ground community assessment; extraction efficiency varies and total abundance does not identify function.

**Display label:** Soil animal numbers and biomass

**Display measurement:** Field soil samples with laboratory animal extraction/counting. Standardised cores/extraction/hand sorting, individuals/m² or g/m², with depth and season.

**Display interpretation:** Shows the number or mass of soil animals. Their roles depend on which groups are present, not just the total.

**Measurement origin:** Field soil samples with laboratory animal extraction/counting

**Supporting indicators:** [EII:MIC-024](#mic-024); [EII:SOI-003](#soi-003); [EII:MIC-027](#mic-027)

**Primary domain:** D05

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot", "community"], "temporal": ["event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-026","domain":"D05","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["sample","plot","community"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Abundance or dry mass of defined soil-animal groups.
- **Direct observations / derivation:** Standardised cores/extraction/hand sorting, individuals/m² or g/m², with depth and season.
- **Inference and limits:** Supports below-ground community assessment; extraction efficiency varies and total abundance does not identify function.
- **Supporting indicators:** [EII:MIC-024](#mic-024), [EII:SOI-003](#soi-003), [EII:MIC-027](#mic-027).

<a id="mic-027"></a>

### EII:MIC-027 — Nematode trophic composition

**Definition:** Relative representation of identified nematode feeding guilds.

**Direct observations / derivation:** Extracted counts and validated guild assignment, proportions; derived indices require stated rules.

**Inference and limits:** Supports soil-food-web comparison; guild uncertainty, season and extraction bias affect inference.

**Display label:** Nematode feeding groups

**Display measurement:** Laboratory extraction and identification of nematodes. Extracted counts and validated guild assignment, proportions; derived indices require stated rules.

**Display interpretation:** Helps describe the feeding groups of soil nematodes. Sampling and identification affect the picture of the soil food web.

**Measurement origin:** Laboratory extraction and identification of nematodes

**Supporting indicators:** [EII:MIC-026](#mic-026); [EII:MIC-007](#mic-007); [EII:BIO-013](#bio-013)

**Primary domain:** D05

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio", "amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future); AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-027","domain":"D05","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Relative representation of identified nematode feeding guilds.
- **Direct observations / derivation:** Extracted counts and validated guild assignment, proportions; derived indices require stated rules.
- **Inference and limits:** Supports soil-food-web comparison; guild uncertainty, season and extraction bias affect inference.
- **Supporting indicators:** [EII:MIC-026](#mic-026), [EII:MIC-007](#mic-007), [EII:BIO-013](#bio-013).

<a id="mic-028"></a>

### EII:MIC-028 — Metaproteomic functional profile

**Definition:** Proteins detected and assigned to functions in a sample.

**Direct observations / derivation:** Mass-spectrometry peptide identifications/intensities with reference database and false-discovery control.

**Inference and limits:** Supports protein-presence assessment; detection does not itself quantify catalytic flux or species-specific activity.

**Display label:** Microbial protein profile

**Display measurement:** Laboratory protein analysis and bioinformatics. Mass-spectrometry peptide identifications/intensities with reference database and false-discovery control.

**Display interpretation:** Shows proteins detected in a microbial sample. Protein detection alone does not measure how quickly a process is running.

**Measurement origin:** Laboratory protein analysis and bioinformatics

**Supporting indicators:** [EII:MIC-022](#mic-022); [EII:MIC-019](#mic-019); [EII:MIC-023](#mic-023)

**Primary domain:** D05

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-028","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Proteins detected and assigned to functions in a sample.
- **Direct observations / derivation:** Mass-spectrometry peptide identifications/intensities with reference database and false-discovery control.
- **Inference and limits:** Supports protein-presence assessment; detection does not itself quantify catalytic flux or species-specific activity.
- **Supporting indicators:** [EII:MIC-022](#mic-022), [EII:MIC-019](#mic-019), [EII:MIC-023](#mic-023).

<a id="mic-029"></a>

### EII:MIC-029 — Metabolomic profile

**Definition:** Detected concentrations or relative signals of specified metabolites.

**Direct observations / derivation:** Targeted/untargeted assays, molar concentration or normalised intensity; distinguish confirmed from putative identities.

**Inference and limits:** Supports biochemical-state hypotheses; pools integrate production, consumption and transport rather than proving flux.

**Display label:** Biological metabolite profile

**Display measurement:** Laboratory chemical analysis of biological samples. Targeted/untargeted assays, molar concentration or normalised intensity; distinguish confirmed from putative identities.

**Display interpretation:** Shows chemicals present in a biological sample. Their amounts reflect both production and use, not just one process rate.

**Measurement origin:** Laboratory chemical analysis of biological samples

**Supporting indicators:** [EII:MIC-028](#mic-028); [EII:MIC-023](#mic-023); [EII:SOI-010](#soi-010)

**Primary domain:** D05

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-029","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Detected concentrations or relative signals of specified metabolites.
- **Direct observations / derivation:** Targeted/untargeted assays, molar concentration or normalised intensity; distinguish confirmed from putative identities.
- **Inference and limits:** Supports biochemical-state hypotheses; pools integrate production, consumption and transport rather than proving flux.
- **Supporting indicators:** [EII:MIC-028](#mic-028), [EII:MIC-023](#mic-023), [EII:SOI-010](#soi-010).

<a id="mic-030"></a>

### EII:MIC-030 — Microbial carbon-use efficiency

**Definition:** Fraction of assimilated carbon allocated to microbial growth under a defined method.

**Direct observations / derivation:** Growth and respiration from matched tracer/assay, growth/(growth+respiration) where applicable, fraction.

**Inference and limits:** Supports allocation-efficiency comparison; method, substrate and timescale alter estimates and field carbon persistence needs additional evidence.

**Display label:** Microbial carbon-use efficiency

**Display measurement:** Laboratory tracer tests of microbial growth and respiration. Growth and respiration from matched tracer/assay, growth/(growth+respiration) where applicable, fraction.

**Display interpretation:** Helps estimate how microbes divide carbon between growth and respiration. Results depend on the test conditions and substrate used.

**Measurement origin:** Laboratory tracer tests of microbial growth and respiration

**Supporting indicators:** [EII:MIC-007](#mic-007); [EII:SOI-010](#soi-010); [EII:SOI-021](#soi-021)

**Primary domain:** D05

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["derived", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio", "amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future); AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:MIC-030","domain":"D05","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["function"],"routes":["bio","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fraction of assimilated carbon allocated to microbial growth under a defined method.
- **Direct observations / derivation:** Growth and respiration from matched tracer/assay, growth/(growth+respiration) where applicable, fraction.
- **Inference and limits:** Supports allocation-efficiency comparison; method, substrate and timescale alter estimates and field carbon persistence needs additional evidence.
- **Supporting indicators:** [EII:MIC-007](#mic-007), [EII:SOI-010](#soi-010), [EII:SOI-021](#soi-021).

<a id="bio-014"></a>

### EII:BIO-014 — Environmental-DNA taxon detection

**Definition:** Presence of taxon-associated DNA in a defined environmental sample.

**Direct observations / derivation:** Validated sequence/qPCR detections with field/extraction blanks and replicates, detection or copies/volume.

**Inference and limits:** Supports occurrence surveillance; DNA transport, persistence and contamination prevent assuming local living abundance.

**Display label:** Environmental DNA detections

**Display measurement:** Field water/soil samples analysed for DNA in a laboratory. Validated sequence/qPCR detections with field/extraction blanks and replicates, detection or copies/volume.

**Display interpretation:** Helps detect organisms from DNA left in water, soil or other samples. DNA may travel or remain after an organism has gone.

**Measurement origin:** Field water/soil samples analysed for DNA in a laboratory

**Supporting indicators:** [EII:BIO-002](#bio-002); [EII:HYD-006](#hyd-006); [EII:BIO-011](#bio-011)

**Primary domain:** D06

**Secondary domains:** `[]`

**Classification dimensions:** `["observed", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:BIO-014","domain":"D06","related_domains":[],"record_type":"indicator","variants":[],"secondary":["observed","derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Presence of taxon-associated DNA in a defined environmental sample.
- **Direct observations / derivation:** Validated sequence/qPCR detections with field/extraction blanks and replicates, detection or copies/volume.
- **Inference and limits:** Supports occurrence surveillance; DNA transport, persistence and contamination prevent assuming local living abundance.
- **Supporting indicators:** [EII:BIO-002](#bio-002), [EII:HYD-006](#hyd-006), [EII:BIO-011](#bio-011).

<a id="bio-015"></a>

### EII:BIO-015 — Genetic diversity/population differentiation

**Definition:** Variation within and among sampled populations at specified loci.

**Direct observations / derivation:** Genotypes, heterozygosity, nucleotide diversity or FST with locus/sample design recorded.

**Inference and limits:** Supports population genetic comparisons; demographic history, sampling and selection confound connectivity interpretations.

**Display label:** Population genetic diversity

**Display measurement:** Laboratory genotyping of sampled organisms. Genotypes, heterozygosity, nucleotide diversity or FST with locus/sample design recorded.

**Display interpretation:** Shows genetic variation within and between populations. Past population changes and sampling can also explain genetic differences.

**Measurement origin:** Laboratory genotyping of sampled organisms

**Supporting indicators:** [EII:BIO-007](#bio-007); [EII:BIO-002](#bio-002); [EII:BIO-016](#bio-016)

**Primary domain:** D06

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:BIO-015","domain":"D06","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Variation within and among sampled populations at specified loci.
- **Direct observations / derivation:** Genotypes, heterozygosity, nucleotide diversity or FST with locus/sample design recorded.
- **Inference and limits:** Supports population genetic comparisons; demographic history, sampling and selection confound connectivity interpretations.
- **Supporting indicators:** [EII:BIO-007](#bio-007), [EII:BIO-002](#bio-002), [EII:BIO-016](#bio-016).

<a id="bio-016"></a>

### EII:BIO-016 — Population growth/recruitment/survival

**Definition:** Separate demographic rates for a focal species and interval.

**Direct observations / derivation:** Repeated counts, marked individuals or age cohorts; λ, recruits/area/time and survival probability.

**Inference and limits:** Supports population trajectory assessment; detection, migration and age structure require modelling.

**Display label:** Population growth and survival

**Display measurement:** Repeated field counts and marked-individual surveys. Repeated counts, marked individuals or age cohorts; λ, recruits/area/time and survival probability.

**Display interpretation:** Helps track population growth, new individuals and survival. Movement and missed detections must also be considered.

**Measurement origin:** Repeated field counts and marked-individual surveys

**Supporting indicators:** [EII:BIO-002](#bio-002); [EII:BIO-005](#bio-005); [EII:BIO-011](#bio-011)

**Primary domain:** D06

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "modelled", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:BIO-016","domain":"D06","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","modelled","process"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["function"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Separate demographic rates for a focal species and interval.
- **Direct observations / derivation:** Repeated counts, marked individuals or age cohorts; λ, recruits/area/time and survival probability.
- **Inference and limits:** Supports population trajectory assessment; detection, migration and age structure require modelling.
- **Supporting indicators:** [EII:BIO-002](#bio-002), [EII:BIO-005](#bio-005), [EII:BIO-011](#bio-011).

<a id="bio-017"></a>

### EII:BIO-017 — Community-weighted traits

**Definition:** Abundance-weighted trait mean of a defined community.

**Direct observations / derivation:** Species trait table and comparable abundance weights; units of the selected trait.

**Inference and limits:** Supports trait-composition interpretation; database gaps and within-species variability affect accuracy.

**Display label:** Typical community traits

**Display measurement:** Field species counts combined with trait measurements or databases. Species trait table and comparable abundance weights; units of the selected trait.

**Display interpretation:** Shows the typical traits of the organisms present, weighted by abundance. Missing trait data can bias the result.

**Measurement origin:** Field species counts combined with trait measurements or databases

**Supporting indicators:** [EII:BIO-004](#bio-004); [EII:BIO-002](#bio-002); [EII:VEG-017](#veg-017)

**Primary domain:** D06

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:BIO-017","domain":"D06","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Abundance-weighted trait mean of a defined community.
- **Direct observations / derivation:** Species trait table and comparable abundance weights; units of the selected trait.
- **Inference and limits:** Supports trait-composition interpretation; database gaps and within-species variability affect accuracy.
- **Supporting indicators:** [EII:BIO-004](#bio-004), [EII:BIO-002](#bio-002), [EII:VEG-017](#veg-017).

<a id="bio-018"></a>

### EII:BIO-018 — Freshwater macroinvertebrate composition

**Definition:** Taxonomic/functional composition in standardised aquatic samples.

**Direct observations / derivation:** Kick/core sampling and identification, abundance and declared region-specific index if used.

**Inference and limits:** Supports aquatic-condition assessment; substrate, season and sampling method require reference-specific interpretation.

**Display label:** Freshwater invertebrate community

**Display measurement:** Field aquatic samples identified in a laboratory. Kick/core sampling and identification, abundance and declared region-specific index if used.

**Display interpretation:** Helps assess aquatic communities and river condition. Habitat, season and the sampling method affect interpretation.

**Measurement origin:** Field aquatic samples identified in a laboratory

**Supporting indicators:** [EII:HYD-013](#hyd-013); [EII:HYD-010](#hyd-010); [EII:HYD-006](#hyd-006)

**Primary domain:** D06

**Secondary domains:** `[]`

**Classification dimensions:** `["observed", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:BIO-018","domain":"D06","related_domains":[],"record_type":"indicator","variants":[],"secondary":["observed","derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Taxonomic/functional composition in standardised aquatic samples.
- **Direct observations / derivation:** Kick/core sampling and identification, abundance and declared region-specific index if used.
- **Inference and limits:** Supports aquatic-condition assessment; substrate, season and sampling method require reference-specific interpretation.
- **Supporting indicators:** [EII:HYD-013](#hyd-013), [EII:HYD-010](#hyd-010), [EII:HYD-006](#hyd-006).

<a id="bio-019"></a>

### EII:BIO-019 — Live coral cover/bleaching prevalence

**Definition:** Proportion of substrate with living coral and proportion of observed colonies bleached.

**Direct observations / derivation:** Validated transect/photo observations, % with depth and denominator stated.

**Inference and limits:** Supports reef-condition assessment; habitat class maps do not directly measure live cover, bleaching or mortality.

**Display label:** Live coral cover and bleaching

**Display measurement:** Field reef transects and validated underwater photographs. Validated transect/photo observations, % with depth and denominator stated.

**Display interpretation:** Shows living coral cover or how common bleaching is. Habitat maps alone cannot establish either measure.

**Measurement origin:** Field reef transects and validated underwater photographs

**Supporting indicators:** [EII:HYD-015](#hyd-015); [EII:HYD-022](#hyd-022); [EII:BIO-005](#bio-005)

**Primary domain:** D06

**Secondary domains:** `[]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "population", "community", "landscape"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["live_coral_cover", "bleaching_prevalence"]`

**Record type:** family

**Candidate source routes:** `["reef", "marine"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS012, RS018

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:BIO-019","domain":"D06","related_domains":[],"record_type":"family","variants":["live_coral_cover","bleaching_prevalence"],"secondary":["measured"],"tertiary":{"spatial":["organism","population","community","landscape"],"temporal":["season","year"]},"quaternary":["state"],"routes":["reef","marine"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Proportion of substrate with living coral and proportion of observed colonies bleached.
- **Direct observations / derivation:** Validated transect/photo observations, % with depth and denominator stated.
- **Inference and limits:** Supports reef-condition assessment; habitat class maps do not directly measure live cover, bleaching or mortality.
- **Supporting indicators:** [EII:HYD-015](#hyd-015), [EII:HYD-022](#hyd-022), [EII:BIO-005](#bio-005).

<a id="bio-020"></a>

### EII:BIO-020 — Mangrove extent/condition

**Definition:** Area of mangrove habitat and separately assessed structural/physiological condition.

**Direct observations / derivation:** Validated maps, ha; field canopy, mortality or salinity observations in declared units.

**Inference and limits:** Supports coastal habitat assessment; area stability does not imply unchanged condition or function.

**Display label:** Mangrove area and condition

**Display measurement:** Satellite mangrove maps and field condition surveys. Validated maps, ha; field canopy, mortality or salinity observations in declared units.

**Display interpretation:** Shows mangrove extent and measured condition. Stable area does not necessarily mean unchanged health or function.

**Measurement origin:** Satellite mangrove maps and field condition surveys

**Supporting indicators:** [EII:BIO-005](#bio-005); [EII:TER-013](#ter-013); [EII:HYD-011](#hyd-011)

**Primary domain:** D06

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "population", "community", "landscape"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `["mangrove_extent", "specified_condition_attribute"]`

**Record type:** family

**Candidate source routes:** `["mangrove"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS011

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:BIO-020","domain":"D06","related_domains":[],"record_type":"family","variants":["mangrove_extent","specified_condition_attribute"],"secondary":["derived","measured"],"tertiary":{"spatial":["organism","population","community","landscape"],"temporal":["season","year"]},"quaternary":["state"],"routes":["mangrove"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Area of mangrove habitat and separately assessed structural/physiological condition.
- **Direct observations / derivation:** Validated maps, ha; field canopy, mortality or salinity observations in declared units.
- **Inference and limits:** Supports coastal habitat assessment; area stability does not imply unchanged condition or function.
- **Supporting indicators:** [EII:BIO-005](#bio-005), [EII:TER-013](#ter-013), [EII:HYD-011](#hyd-011).

<a id="veg-018"></a>

### EII:VEG-018 — Fraction of absorbed PAR

**Definition:** Fraction of incoming photosynthetic radiation absorbed by vegetation.

**Direct observations / derivation:** Above/below-canopy radiation measurements or validated retrieval, fraction; specify green versus total absorption.

**Inference and limits:** Supports light-use production models; absorption is not conversion into fixed carbon.

**Display label:** Absorbed photosynthetic light

**Display measurement:** Field light sensors or calibrated satellite estimates. Above/below-canopy radiation measurements or validated retrieval, fraction; specify green versus total absorption.

**Display interpretation:** Shows the share of useful light vegetation absorbs. Absorbing light does not mean all of it becomes plant growth.

**Measurement origin:** Field light sensors or calibrated satellite estimates

**Supporting indicators:** [EII:ATM-004](#atm-004); [EII:VEG-011](#veg-011); [EII:FUN-001](#fun-001)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["veg"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS001, RS002

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-018","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","modelled"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["veg"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fraction of incoming photosynthetic radiation absorbed by vegetation.
- **Direct observations / derivation:** Above/below-canopy radiation measurements or validated retrieval, fraction; specify green versus total absorption.
- **Inference and limits:** Supports light-use production models; absorption is not conversion into fixed carbon.
- **Supporting indicators:** [EII:ATM-004](#atm-004), [EII:VEG-011](#veg-011), [EII:FUN-001](#fun-001).

<a id="veg-019"></a>

### EII:VEG-019 — Solar-induced chlorophyll fluorescence

**Definition:** Radiance emitted by chlorophyll following solar excitation.

**Direct observations / derivation:** Spectrally resolved retrieval, mW/m²/sr/nm with wavelength/geometry specified.

**Inference and limits:** Supports photosynthetic-state assessment; canopy escape probability and energy partitioning prevent a universal GPP conversion.

**Display label:** Chlorophyll fluorescence

**Display measurement:** Specialised field or satellite spectral instruments. Spectrally resolved retrieval, mW/m²/sr/nm with wavelength/geometry specified.

**Display interpretation:** Can help study how vegetation responds during photosynthesis. The signal cannot be converted to carbon uptake without a suitable model.

**Measurement origin:** Specialised field or satellite spectral instruments

**Supporting indicators:** [EII:FUN-001](#fun-001); [EII:ATM-004](#atm-004); [EII:VEG-013](#veg-013)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "proxy"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `[]`

**Scientific reference keys:** `[]`

**Display source keys:** Field/lab/model source to register

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-019","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Radiance emitted by chlorophyll following solar excitation.
- **Direct observations / derivation:** Spectrally resolved retrieval, mW/m²/sr/nm with wavelength/geometry specified.
- **Inference and limits:** Supports photosynthetic-state assessment; canopy escape probability and energy partitioning prevent a universal GPP conversion.
- **Supporting indicators:** [EII:FUN-001](#fun-001), [EII:ATM-004](#atm-004), [EII:VEG-013](#veg-013).

<a id="veg-020"></a>

### EII:VEG-020 — Leaf water potential/stomatal conductance

**Definition:** Separate measures of plant water-energy state and leaf gas-exchange conductance.

**Direct observations / derivation:** Pressure chamber, MPa; porometer/gas exchange, mol H₂O/m²/s, recording time and conditions.

**Inference and limits:** Supports physiological water-stress assessment; species, leaf age and atmospheric demand affect response.

**Display label:** Plant water status and leaf gas exchange

**Display measurement:** Field pressure-chamber and leaf gas-exchange tests. Pressure chamber, MPa; porometer/gas exchange, mol H₂O/m²/s, recording time and conditions.

**Display interpretation:** Helps assess plant water status and control of water loss. Time of day, weather and plant type affect the response.

**Measurement origin:** Field pressure-chamber and leaf gas-exchange tests

**Supporting indicators:** [EII:SOI-016](#soi-016); [EII:ATM-003](#atm-003); [EII:VEG-015](#veg-015)

**Primary domain:** D07

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot"], "temporal": ["event", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `["leaf_water_potential", "stomatal_conductance"]`

**Record type:** family

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-020","domain":"D07","related_domains":["D13"],"record_type":"family","variants":["leaf_water_potential","stomatal_conductance"],"secondary":["measured","process"],"tertiary":{"spatial":["organism","plot"],"temporal":["event","season","year"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Separate measures of plant water-energy state and leaf gas-exchange conductance.
- **Direct observations / derivation:** Pressure chamber, MPa; porometer/gas exchange, mol H₂O/m²/s, recording time and conditions.
- **Inference and limits:** Supports physiological water-stress assessment; species, leaf age and atmospheric demand affect response.
- **Supporting indicators:** [EII:SOI-016](#soi-016), [EII:ATM-003](#atm-003), [EII:VEG-015](#veg-015).

<a id="veg-021"></a>

### EII:VEG-021 — Plant mortality/recruitment

**Definition:** Rates of death and establishment in a defined plant population.

**Direct observations / derivation:** Repeated mapped stems/seedlings, %/year or individuals/ha/year.

**Inference and limits:** Supports stand demographic assessment; delayed detection and seedling-to-adult transitions must be considered.

**Display label:** Plant deaths and new establishment

**Display measurement:** Repeated field plant surveys. Repeated mapped stems/seedlings, %/year or individuals/ha/year.

**Display interpretation:** Shows plant deaths and new establishment. Seedlings may not survive to become mature plants.

**Measurement origin:** Repeated field plant surveys

**Supporting indicators:** [EII:VEG-017](#veg-017); [EII:BIO-016](#bio-016); [EII:DIS-009](#dis-009)

**Primary domain:** D07

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `["mortality_rate", "recruitment_rate"]`

**Record type:** family

**Candidate source routes:** `["veg"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS001, RS002

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-021","domain":"D07","related_domains":[],"record_type":"family","variants":["mortality_rate","recruitment_rate"],"secondary":["measured","process"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["function"],"routes":["veg"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Rates of death and establishment in a defined plant population.
- **Direct observations / derivation:** Repeated mapped stems/seedlings, %/year or individuals/ha/year.
- **Inference and limits:** Supports stand demographic assessment; delayed detection and seedling-to-adult transitions must be considered.
- **Supporting indicators:** [EII:VEG-017](#veg-017), [EII:BIO-016](#bio-016), [EII:DIS-009](#dis-009).

<a id="veg-022"></a>

### EII:VEG-022 — Root biomass/depth distribution

**Definition:** Root dry mass and allocation through soil depth.

**Direct observations / derivation:** Washed cores, ingrowth methods or calibrated imaging, g/m² by depth; distinguish live/dead and diameter classes.

**Inference and limits:** Supports below-ground allocation/rooting assessment; sampling misses spatial heterogeneity and standing mass does not equal uptake.

**Display label:** Root mass and depth

**Display measurement:** Field root samples analysed in a laboratory. Washed cores, ingrowth methods or calibrated imaging, g/m² by depth; distinguish live/dead and diameter classes.

**Display interpretation:** Shows root mass and how deep roots occur. Root mass alone does not measure nutrient or water uptake.

**Measurement origin:** Field root samples analysed in a laboratory

**Supporting indicators:** [EII:HYD-001](#hyd-001); [EII:SOI-014](#soi-014); [EII:VEG-020](#veg-020)

**Primary domain:** D07

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "plot", "landscape"], "temporal": ["day", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:VEG-022","domain":"D07","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Root dry mass and allocation through soil depth.
- **Direct observations / derivation:** Washed cores, ingrowth methods or calibrated imaging, g/m² by depth; distinguish live/dead and diameter classes.
- **Inference and limits:** Supports below-ground allocation/rooting assessment; sampling misses spatial heterogeneity and standing mass does not equal uptake.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:SOI-014](#soi-014), [EII:VEG-020](#veg-020).

<a id="int-001"></a>

### EII:INT-001 — Pollen deposition/pollen limitation

**Definition:** Pollen delivered to stigmas and reproduction limited by pollen supply.

**Direct observations / derivation:** Stigma pollen counts; supplemented-versus-control fruit/seed set, counts and effect size.

**Inference and limits:** Supports pollination-function assessment; pollen quality and resource limitation require separate controls.

**Display label:** Pollen delivery and pollen limitation

**Display measurement:** Field pollination experiments and laboratory pollen counts. Stigma pollen counts; supplemented-versus-control fruit/seed set, counts and effect size.

**Display interpretation:** Helps assess pollen delivery and whether extra pollen improves reproduction. Water and nutrient shortages can also limit seed production.

**Measurement origin:** Field pollination experiments and laboratory pollen counts

**Supporting indicators:** [EII:BIO-008](#bio-008); [EII:INT-002](#int-002); [EII:VEG-016](#veg-016)

**Primary domain:** D08

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "community", "plot"], "temporal": ["event", "season"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:INT-001","domain":"D08","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["organism","community","plot"],"temporal":["event","season"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Pollen delivered to stigmas and reproduction limited by pollen supply.
- **Direct observations / derivation:** Stigma pollen counts; supplemented-versus-control fruit/seed set, counts and effect size.
- **Inference and limits:** Supports pollination-function assessment; pollen quality and resource limitation require separate controls.
- **Supporting indicators:** [EII:BIO-008](#bio-008), [EII:INT-002](#int-002), [EII:VEG-016](#veg-016).

<a id="int-002"></a>

### EII:INT-002 — Fruit/seed set

**Definition:** Fraction of flowers/ovules developing into fruits/seeds under stated conditions.

**Direct observations / derivation:** Repeated reproductive counts, % with denominator and abortion timing declared.

**Inference and limits:** Supports reproductive-success assessment; pollination, weather, nutrition and herbivory jointly determine outcomes.

**Display label:** Fruit and seed formation

**Display measurement:** Repeated field flower, fruit and seed counts. Repeated reproductive counts, % with denominator and abortion timing declared.

**Display interpretation:** Shows how many flowers produce fruits or seeds. Pollination, weather, nutrition and damage all affect the result.

**Measurement origin:** Repeated field flower, fruit and seed counts

**Supporting indicators:** [EII:INT-001](#int-001); [EII:BIO-008](#bio-008); [EII:VEG-020](#veg-020)

**Primary domain:** D08

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "community", "plot"], "temporal": ["event", "season"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:INT-002","domain":"D08","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["organism","community","plot"],"temporal":["event","season"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fraction of flowers/ovules developing into fruits/seeds under stated conditions.
- **Direct observations / derivation:** Repeated reproductive counts, % with denominator and abortion timing declared.
- **Inference and limits:** Supports reproductive-success assessment; pollination, weather, nutrition and herbivory jointly determine outcomes.
- **Supporting indicators:** [EII:INT-001](#int-001), [EII:BIO-008](#bio-008), [EII:VEG-020](#veg-020).

<a id="int-003"></a>

### EII:INT-003 — Herbivory rate

**Definition:** Plant tissue consumed/damaged per area or interval.

**Direct observations / derivation:** Repeated leaf-area loss or biomass removal, %/time; distinguish herbivore from disease damage.

**Inference and limits:** Supports consumer-pressure assessment; standing damage is not automatically current feeding rate.

**Display label:** Plant consumption by herbivores

**Display measurement:** Field measurements of eaten tissue or lost biomass. Repeated leaf-area loss or biomass removal, %/time; distinguish herbivore from disease damage.

**Display interpretation:** Shows plant tissue eaten or damaged by herbivores. Existing damage may not reflect the current feeding rate.

**Measurement origin:** Field measurements of eaten tissue or lost biomass

**Supporting indicators:** [EII:AGR-004](#agr-004); [EII:BIO-009](#bio-009); [EII:VEG-014](#veg-014)

**Primary domain:** D08

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "community", "plot"], "temporal": ["event", "season"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:INT-003","domain":"D08","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["organism","community","plot"],"temporal":["event","season"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Plant tissue consumed/damaged per area or interval.
- **Direct observations / derivation:** Repeated leaf-area loss or biomass removal, %/time; distinguish herbivore from disease damage.
- **Inference and limits:** Supports consumer-pressure assessment; standing damage is not automatically current feeding rate.
- **Supporting indicators:** [EII:AGR-004](#agr-004), [EII:BIO-009](#bio-009), [EII:VEG-014](#veg-014).

<a id="int-004"></a>

### EII:INT-004 — Competition effect

**Definition:** Performance difference attributable to competitor presence in a controlled comparison.

**Direct observations / derivation:** Neighbour-removal/addition experiment, growth/reproduction effect size.

**Inference and limits:** Supports competition inference within the tested context; observational co-occurrence cannot establish direction or mechanism.

**Display label:** Competition between organisms

**Display measurement:** Controlled field or greenhouse neighbour-removal tests. Neighbour-removal/addition experiment, growth/reproduction effect size.

**Display interpretation:** Tests whether neighbours reduce a plant's growth or reproduction. Finding species together does not prove competition.

**Measurement origin:** Controlled field or greenhouse neighbour-removal tests

**Supporting indicators:** [EII:VEG-014](#veg-014); [EII:HYD-001](#hyd-001); [EII:SOI-008](#soi-008)

**Primary domain:** D08

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["derived", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "community", "plot"], "temporal": ["event", "season"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:INT-004","domain":"D08","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["organism","community","plot"],"temporal":["event","season"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Performance difference attributable to competitor presence in a controlled comparison.
- **Direct observations / derivation:** Neighbour-removal/addition experiment, growth/reproduction effect size.
- **Inference and limits:** Supports competition inference within the tested context; observational co-occurrence cannot establish direction or mechanism.
- **Supporting indicators:** [EII:VEG-014](#veg-014), [EII:HYD-001](#hyd-001), [EII:SOI-008](#soi-008).

<a id="int-005"></a>

### EII:INT-005 — Facilitation effect

**Definition:** Performance benefit attributable to another organism under defined conditions.

**Direct observations / derivation:** Controlled neighbour/nurse treatment comparisons, survival/growth effect size.

**Inference and limits:** Supports facilitation inference; effects may reverse with resource conditions or life stage.

**Display label:** Benefits between organisms

**Display measurement:** Controlled field or greenhouse association tests. Controlled neighbour/nurse treatment comparisons, survival/growth effect size.

**Display interpretation:** Tests whether one organism helps another grow or survive. The benefit can change with conditions and life stage.

**Measurement origin:** Controlled field or greenhouse association tests

**Supporting indicators:** [EII:BIO-016](#bio-016); [EII:VEG-020](#veg-020); [EII:HYD-001](#hyd-001)

**Primary domain:** D08

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["derived", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["organism", "community", "plot"], "temporal": ["event", "season"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:INT-005","domain":"D08","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["organism","community","plot"],"temporal":["event","season"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Performance benefit attributable to another organism under defined conditions.
- **Direct observations / derivation:** Controlled neighbour/nurse treatment comparisons, survival/growth effect size.
- **Inference and limits:** Supports facilitation inference; effects may reverse with resource conditions or life stage.
- **Supporting indicators:** [EII:BIO-016](#bio-016), [EII:VEG-020](#veg-020), [EII:HYD-001](#hyd-001).

<a id="int-006"></a>

### EII:INT-006 — Mycorrhizal nutrient transfer

**Definition:** Nutrient transfer associated with a defined fungal–plant pathway.

**Direct observations / derivation:** Isotopic tracing/compartment controls and plant nutrient recovery, mass/time or fraction.

**Inference and limits:** Supports demonstrated transfer under experiment; colonisation alone cannot establish mutual benefit or field-scale flux.

**Display label:** Nutrient transfer through root fungi

**Display measurement:** Controlled isotope-tracing tests in field/laboratory systems. Isotopic tracing/compartment controls and plant nutrient recovery, mass/time or fraction.

**Display interpretation:** Tests nutrient transfer associated with root fungi. Fungal presence alone does not prove transfer or benefit to the plant.

**Measurement origin:** Controlled isotope-tracing tests in field/laboratory systems

**Supporting indicators:** [EII:MIC-014](#mic-014); [EII:SOI-008](#soi-008); [EII:AGR-001](#agr-001)

**Primary domain:** D08

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio", "amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future); AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:INT-006","domain":"D08","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["function"],"routes":["bio","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Nutrient transfer associated with a defined fungal–plant pathway.
- **Direct observations / derivation:** Isotopic tracing/compartment controls and plant nutrient recovery, mass/time or fraction.
- **Inference and limits:** Supports demonstrated transfer under experiment; colonisation alone cannot establish mutual benefit or field-scale flux.
- **Supporting indicators:** [EII:MIC-014](#mic-014), [EII:SOI-008](#soi-008), [EII:AGR-001](#agr-001).

<a id="int-007"></a>

### EII:INT-007 — Seed dispersal/removal

**Definition:** Movement or removal of seeds by specified processes.

**Direct observations / derivation:** Tracked seeds, traps or validated molecular assignments, distance and fraction/time.

**Inference and limits:** Supports dispersal-function assessment; seed disappearance may be predation and movement does not ensure establishment.

**Display label:** Seed dispersal and removal

**Display measurement:** Field seed tracking/traps and suitable laboratory tracing. Tracked seeds, traps or validated molecular assignments, distance and fraction/time.

**Display interpretation:** Shows how seeds move or disappear. Removed seeds may be eaten rather than dispersed successfully.

**Measurement origin:** Field seed tracking/traps and suitable laboratory tracing

**Supporting indicators:** [EII:BIO-016](#bio-016); [EII:VEG-021](#veg-021); [EII:BIO-007](#bio-007)

**Primary domain:** D08

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:INT-007","domain":"D08","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["function"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Movement or removal of seeds by specified processes.
- **Direct observations / derivation:** Tracked seeds, traps or validated molecular assignments, distance and fraction/time.
- **Inference and limits:** Supports dispersal-function assessment; seed disappearance may be predation and movement does not ensure establishment.
- **Supporting indicators:** [EII:BIO-016](#bio-016), [EII:VEG-021](#veg-021), [EII:BIO-007](#bio-007).

<a id="int-008"></a>

### EII:INT-008 — Diet/trophic-link evidence

**Definition:** Observed consumption or traced dietary contribution between organisms.

**Direct observations / derivation:** Gut/faecal metabarcoding, observation or isotopes, detections or estimated contribution with mixing assumptions.

**Inference and limits:** Supports trophic linkage; secondary predation, DNA persistence and isotope baselines complicate quantification.

**Display label:** Diet and feeding relationships

**Display measurement:** Field feeding observations and laboratory DNA/isotope tests. Gut/faecal metabarcoding, observation or isotopes, detections or estimated contribution with mixing assumptions.

**Display interpretation:** Helps identify feeding relationships. DNA and isotope evidence need careful interpretation to estimate dietary contributions.

**Measurement origin:** Field feeding observations and laboratory DNA/isotope tests

**Supporting indicators:** [EII:BIO-013](#bio-013); [EII:BIO-002](#bio-002); [EII:MIC-024](#mic-024)

**Primary domain:** D08

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:INT-008","domain":"D08","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Observed consumption or traced dietary contribution between organisms.
- **Direct observations / derivation:** Gut/faecal metabarcoding, observation or isotopes, detections or estimated contribution with mixing assumptions.
- **Inference and limits:** Supports trophic linkage; secondary predation, DNA persistence and isotope baselines complicate quantification.
- **Supporting indicators:** [EII:BIO-013](#bio-013), [EII:BIO-002](#bio-002), [EII:MIC-024](#mic-024).

<a id="int-009"></a>

### EII:INT-009 — Disease suppression in bioassays

**Definition:** Reduction in specified disease outcomes under a controlled soil/community treatment.

**Direct observations / derivation:** Matched inoculation/control disease incidence or severity, % or effect size.

**Inference and limits:** Supports suppression under tested conditions; marker/taxon detection alone does not demonstrate protection or field efficacy.

**Display label:** Disease suppression tests

**Display measurement:** Controlled laboratory or greenhouse disease tests. Matched inoculation/control disease incidence or severity, % or effect size.

**Display interpretation:** Tests whether a soil or microbial treatment reduces disease. A successful laboratory test does not guarantee the same field result.

**Measurement origin:** Controlled laboratory or greenhouse disease tests

**Supporting indicators:** [EII:MIC-016](#mic-016); [EII:AGR-005](#agr-005); [EII:MIC-007](#mic-007)

**Primary domain:** D08

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr", "bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context; Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:INT-009","domain":"D08","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["function"],"routes":["amr","bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Reduction in specified disease outcomes under a controlled soil/community treatment.
- **Direct observations / derivation:** Matched inoculation/control disease incidence or severity, % or effect size.
- **Inference and limits:** Supports suppression under tested conditions; marker/taxon detection alone does not demonstrate protection or field efficacy.
- **Supporting indicators:** [EII:MIC-016](#mic-016), [EII:AGR-005](#agr-005), [EII:MIC-007](#mic-007).

<a id="cyc-001"></a>

### EII:CYC-001 — Net ecosystem CO₂ exchange

**Definition:** Net CO₂ transfer between an ecosystem and atmosphere under an explicit sign convention.

**Direct observations / derivation:** Eddy covariance/chambers and flux processing, µmol/m²/s or g C/m²/year.

**Inference and limits:** Supports net carbon-exchange assessment; gap filling, storage and lateral/harvest exports are needed for a complete carbon balance.

**Display label:** Net ecosystem carbon dioxide exchange

**Display measurement:** Field carbon dioxide flux instruments. Eddy covariance/chambers and flux processing, µmol/m²/s or g C/m²/year.

**Display interpretation:** Shows net carbon dioxide exchange between an ecosystem and air. Harvests and other carbon movements are needed for a full carbon balance.

**Measurement origin:** Field carbon dioxide flux instruments

**Supporting indicators:** [EII:FUN-001](#fun-001); [EII:SOI-010](#soi-010); [EII:FUN-002](#fun-002)

**Primary domain:** D09

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "derived", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot", "ecosystem", "watershed"], "temporal": ["hour", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:CYC-001","domain":"D09","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","derived","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Net CO₂ transfer between an ecosystem and atmosphere under an explicit sign convention.
- **Direct observations / derivation:** Eddy covariance/chambers and flux processing, µmol/m²/s or g C/m²/year.
- **Inference and limits:** Supports net carbon-exchange assessment; gap filling, storage and lateral/harvest exports are needed for a complete carbon balance.
- **Supporting indicators:** [EII:FUN-001](#fun-001), [EII:SOI-010](#soi-010), [EII:FUN-002](#fun-002).

<a id="cyc-002"></a>

### EII:CYC-002 — N₂O flux

**Definition:** Net nitrous-oxide transfer across a stated surface.

**Direct observations / derivation:** Chamber or micrometeorological flux, µg N/m²/h, with N versus N₂O mass convention explicit.

**Inference and limits:** Supports emission assessment; pulses and pathway mixtures mean gene abundance cannot substitute for measurements.

**Display label:** Nitrous oxide exchange

**Display measurement:** Field gas chambers or micrometeorological instruments. Chamber or micrometeorological flux, µg N/m²/h, with N versus N₂O mass convention explicit.

**Display interpretation:** Shows nitrous oxide released or taken up. Short-lived emission bursts can be missed by occasional measurements.

**Measurement origin:** Field gas chambers or micrometeorological instruments

**Supporting indicators:** [EII:MIC-012](#mic-012); [EII:HYD-001](#hyd-001); [EII:SOI-008](#soi-008)

**Primary domain:** D09

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot", "ecosystem", "watershed"], "temporal": ["hour", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot", "amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future); AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:CYC-002","domain":"D09","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["iot","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Net nitrous-oxide transfer across a stated surface.
- **Direct observations / derivation:** Chamber or micrometeorological flux, µg N/m²/h, with N versus N₂O mass convention explicit.
- **Inference and limits:** Supports emission assessment; pulses and pathway mixtures mean gene abundance cannot substitute for measurements.
- **Supporting indicators:** [EII:MIC-012](#mic-012), [EII:HYD-001](#hyd-001), [EII:SOI-008](#soi-008).

<a id="cyc-003"></a>

### EII:CYC-003 — Methane flux

**Definition:** Net methane production/oxidation expressed as surface exchange.

**Direct observations / derivation:** Gas flux observations, mg CH₄/m²/day, with temporal coverage.

**Inference and limits:** Supports methane-budget assessment; emission is net production, oxidation and transport and cannot be inferred solely from archaeal taxa.

**Display label:** Methane exchange

**Display measurement:** Field gas chambers or other methane flux instruments. Gas flux observations, mg CH₄/m²/day, with temporal coverage.

**Display interpretation:** Shows net methane exchange. Production, consumption and gas movement all contribute to the measured result.

**Measurement origin:** Field gas chambers or other methane flux instruments

**Supporting indicators:** [EII:SOI-023](#soi-023); [EII:HYD-016](#hyd-016); [EII:MIC-002](#mic-002)

**Primary domain:** D09

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot", "ecosystem", "watershed"], "temporal": ["hour", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:CYC-003","domain":"D09","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Net methane production/oxidation expressed as surface exchange.
- **Direct observations / derivation:** Gas flux observations, mg CH₄/m²/day, with temporal coverage.
- **Inference and limits:** Supports methane-budget assessment; emission is net production, oxidation and transport and cannot be inferred solely from archaeal taxa.
- **Supporting indicators:** [EII:SOI-023](#soi-023), [EII:HYD-016](#hyd-016), [EII:MIC-002](#mic-002).

<a id="cyc-004"></a>

### EII:CYC-004 — Biological nitrogen-fixation rate

**Definition:** N input through biological conversion of atmospheric N₂.

**Direct observations / derivation:** Validated ¹⁵N₂ incorporation or calibrated alternative, mg N/kg/time or kg N/ha/year.

**Inference and limits:** Supports realised fixation assessment; tracer availability and scaling assumptions matter and nifH is not a rate.

**Display label:** Biological nitrogen-fixation rate

**Display measurement:** Field/laboratory isotope tests of nitrogen fixation. Validated ¹⁵N₂ incorporation or calibrated alternative, mg N/kg/time or kg N/ha/year.

**Display interpretation:** Measures nitrogen added through biological fixation. Scaling a small test to a field introduces uncertainty.

**Measurement origin:** Field/laboratory isotope tests of nitrogen fixation

**Supporting indicators:** [EII:MIC-010](#mic-010); [EII:SOI-008](#soi-008); [EII:VEG-017](#veg-017)

**Primary domain:** D09

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr", "bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context; Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:CYC-004","domain":"D09","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["function"],"routes":["amr","bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** N input through biological conversion of atmospheric N₂.
- **Direct observations / derivation:** Validated ¹⁵N₂ incorporation or calibrated alternative, mg N/kg/time or kg N/ha/year.
- **Inference and limits:** Supports realised fixation assessment; tracer availability and scaling assumptions matter and nifH is not a rate.
- **Supporting indicators:** [EII:MIC-010](#mic-010), [EII:SOI-008](#soi-008), [EII:VEG-017](#veg-017).

<a id="cyc-005"></a>

### EII:CYC-005 — Denitrification rate

**Definition:** Nitrate/nitrite reduction to gaseous N products under specified conditions.

**Direct observations / derivation:** Isotope or validated gas assay, mass N/area/time; distinguish total N gases from N₂O alone.

**Inference and limits:** Supports N-removal assessment; assay inhibition and oxygen/substrate manipulation can bias field estimates.

**Display label:** Denitrification rate

**Display measurement:** Laboratory or field nitrogen-gas/isotope assays. Isotope or validated gas assay, mass N/area/time; distinguish total N gases from N₂O alone.

**Display interpretation:** Measures conversion of nitrate into nitrogen gases. Nitrous oxide alone does not show the whole process.

**Measurement origin:** Laboratory or field nitrogen-gas/isotope assays

**Supporting indicators:** [EII:MIC-012](#mic-012); [EII:CYC-002](#cyc-002); [EII:SOI-023](#soi-023)

**Primary domain:** D09

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot", "ecosystem", "watershed"], "temporal": ["hour", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:CYC-005","domain":"D09","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Nitrate/nitrite reduction to gaseous N products under specified conditions.
- **Direct observations / derivation:** Isotope or validated gas assay, mass N/area/time; distinguish total N gases from N₂O alone.
- **Inference and limits:** Supports N-removal assessment; assay inhibition and oxygen/substrate manipulation can bias field estimates.
- **Supporting indicators:** [EII:MIC-012](#mic-012), [EII:CYC-002](#cyc-002), [EII:SOI-023](#soi-023).

<a id="cyc-006"></a>

### EII:CYC-006 — Phosphorus mineralisation rate

**Definition:** Release of inorganic P from organic substrates under a stated assay.

**Direct observations / derivation:** Time-resolved P fractions/tracers, mg P/kg/time.

**Inference and limits:** Supports P-transformation assessment; sorption, immobilisation and enzyme potential complicate net-rate interpretation.

**Display label:** Phosphorus release from organic matter

**Display measurement:** Laboratory phosphorus assays or tracer experiments. Time-resolved P fractions/tracers, mg P/kg/time.

**Display interpretation:** Measures release of inorganic phosphorus from organic material. Binding to soil and microbial uptake can affect the net result.

**Measurement origin:** Laboratory phosphorus assays or tracer experiments

**Supporting indicators:** [EII:MIC-013](#mic-013); [EII:MIC-019](#mic-019); [EII:SOI-008](#soi-008)

**Primary domain:** D09

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot", "ecosystem", "watershed"], "temporal": ["hour", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:CYC-006","domain":"D09","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Release of inorganic P from organic substrates under a stated assay.
- **Direct observations / derivation:** Time-resolved P fractions/tracers, mg P/kg/time.
- **Inference and limits:** Supports P-transformation assessment; sorption, immobilisation and enzyme potential complicate net-rate interpretation.
- **Supporting indicators:** [EII:MIC-013](#mic-013), [EII:MIC-019](#mic-019), [EII:SOI-008](#soi-008).

<a id="cyc-007"></a>

### EII:CYC-007 — Nitrogen/phosphorus balance

**Definition:** Inputs minus outputs of each nutrient for a declared system and interval.

**Direct observations / derivation:** Fertiliser, fixation, deposition, harvest, runoff/leaching and gas terms, kg N/P/ha/year.

**Inference and limits:** Supports surplus/deficit assessment; incomplete budgets do not establish retained stocks or specific losses.

**Display label:** Nitrogen and phosphorus balance

**Display measurement:** Farm/ecosystem input-output records and flux measurements. Fertiliser, fixation, deposition, harvest, runoff/leaching and gas terms, kg N/P/ha/year.

**Display interpretation:** Shows whether recorded nutrient inputs exceed outputs. Missing losses or inputs can distort the balance.

**Measurement origin:** Farm/ecosystem input-output records and flux measurements

**Supporting indicators:** [EII:FUN-007](#fun-007); [EII:FUN-004](#fun-004); [EII:FUN-003](#fun-003); [EII:CYC-004](#cyc-004)

**Primary domain:** D09

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["derived", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot", "ecosystem", "watershed"], "temporal": ["hour", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:CYC-007","domain":"D09","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Inputs minus outputs of each nutrient for a declared system and interval.
- **Direct observations / derivation:** Fertiliser, fixation, deposition, harvest, runoff/leaching and gas terms, kg N/P/ha/year.
- **Inference and limits:** Supports surplus/deficit assessment; incomplete budgets do not establish retained stocks or specific losses.
- **Supporting indicators:** [EII:FUN-007](#fun-007), [EII:FUN-004](#fun-004), [EII:FUN-003](#fun-003), [EII:CYC-004](#cyc-004).

<a id="cyc-008"></a>

### EII:CYC-008 — Nutrient resorption efficiency

**Definition:** Fraction of a nutrient recovered from leaves before senescence.

**Direct observations / derivation:** Matched green/senescent tissue nutrient assays, %, correcting for leaf mass loss.

**Inference and limits:** Supports internal recycling assessment; species, timing and incomplete senescence affect estimates.

**Display label:** Nutrient recovery before leaf fall

**Display measurement:** Laboratory nutrient tests of green and fallen leaves. Matched green/senescent tissue nutrient assays, %, correcting for leaf mass loss.

**Display interpretation:** Shows how much nutrient plants recover before leaves fall. Leaf mass changes and sampling time affect the estimate.

**Measurement origin:** Laboratory nutrient tests of green and fallen leaves

**Supporting indicators:** [EII:VEG-016](#veg-016); [EII:SOI-008](#soi-008); [EII:MIC-024](#mic-024)

**Primary domain:** D09

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["derived", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot", "ecosystem", "watershed"], "temporal": ["hour", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:CYC-008","domain":"D09","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fraction of a nutrient recovered from leaves before senescence.
- **Direct observations / derivation:** Matched green/senescent tissue nutrient assays, %, correcting for leaf mass loss.
- **Inference and limits:** Supports internal recycling assessment; species, timing and incomplete senescence affect estimates.
- **Supporting indicators:** [EII:VEG-016](#veg-016), [EII:SOI-008](#soi-008), [EII:MIC-024](#mic-024).

<a id="cyc-009"></a>

### EII:CYC-009 — Measured contaminant transformation

**Definition:** Change of a specified chemical attributable to a stated transformation pathway.

**Direct observations / derivation:** Repeated parent/metabolite mass balance or isotope mineralisation, %/time or mass/time.

**Inference and limits:** Supports transformation assessment; sorption/export are not degradation and products may remain toxic.

**Display label:** Pollutant transformation

**Display measurement:** Laboratory chemical/tracer tests on repeated samples. Repeated parent/metabolite mass balance or isotope mineralisation, %/time or mass/time.

**Display interpretation:** Tests whether a pollutant is transformed. Disappearance alone may mean storage or movement, and breakdown products may still be harmful.

**Measurement origin:** Laboratory chemical/tracer tests on repeated samples

**Supporting indicators:** [EII:MIC-018](#mic-018); [EII:SOI-013](#soi-013); [EII:SOI-022](#soi-022)

**Primary domain:** D09

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot", "ecosystem", "watershed"], "temporal": ["hour", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:CYC-009","domain":"D09","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Change of a specified chemical attributable to a stated transformation pathway.
- **Direct observations / derivation:** Repeated parent/metabolite mass balance or isotope mineralisation, %/time or mass/time.
- **Inference and limits:** Supports transformation assessment; sorption/export are not degradation and products may remain toxic.
- **Supporting indicators:** [EII:MIC-018](#mic-018), [EII:SOI-013](#soi-013), [EII:SOI-022](#soi-022).

<a id="cyc-010"></a>

### EII:CYC-010 — Dissolved organic carbon export

**Definition:** Organic carbon transported in the operationally dissolved water fraction.

**Direct observations / derivation:** Filtered DOC assay × discharge, mg C/L and kg C/time, with filter definition.

**Inference and limits:** Supports aquatic carbon-export assessment; concentration alone is not load or source attribution.

**Display label:** Dissolved organic carbon export

**Display measurement:** Laboratory water-carbon tests combined with flow measurements. Filtered DOC assay × discharge, mg C/L and kg C/time, with filter definition.

**Display interpretation:** Shows carbon carried away in dissolved form by water. Concentration alone does not show the total amount exported.

**Measurement origin:** Laboratory water-carbon tests combined with flow measurements

**Supporting indicators:** [EII:HYD-006](#hyd-006); [EII:SOI-005](#soi-005); [EII:CYC-001](#cyc-001)

**Primary domain:** D09

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "plot", "ecosystem", "watershed"], "temporal": ["hour", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:CYC-010","domain":"D09","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Organic carbon transported in the operationally dissolved water fraction.
- **Direct observations / derivation:** Filtered DOC assay × discharge, mg C/L and kg C/time, with filter definition.
- **Inference and limits:** Supports aquatic carbon-export assessment; concentration alone is not load or source attribution.
- **Supporting indicators:** [EII:HYD-006](#hyd-006), [EII:SOI-005](#soi-005), [EII:CYC-001](#cyc-001).

<a id="lan-001"></a>

### EII:LAN-001 — Edge density/core habitat area

**Definition:** Habitat boundary per area and habitat interior beyond a stated edge distance.

**Direct observations / derivation:** Validated patch polygons, m/ha and ha; declare focal class, grain and edge rule.

**Inference and limits:** Supports edge-exposure assessment; species-specific edge responses and map resolution govern meaning.

**Display label:** Habitat edges and interior area

**Display measurement:** Field-validated satellite or aerial habitat maps. Validated patch polygons, m/ha and ha; declare focal class, grain and edge rule.

**Display interpretation:** Shows habitat edges and remaining interior areas. Effects depend on the species and the distance at which edges matter.

**Measurement origin:** Field-validated satellite or aerial habitat maps

**Supporting indicators:** [EII:BIO-006](#bio-006); [EII:BIO-005](#bio-005); [EII:LAN-002](#lan-002)

**Primary domain:** D10

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["landscape", "watershed", "region"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["land"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS005, RS006, RS009

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:LAN-001","domain":"D10","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["state"],"routes":["land"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Habitat boundary per area and habitat interior beyond a stated edge distance.
- **Direct observations / derivation:** Validated patch polygons, m/ha and ha; declare focal class, grain and edge rule.
- **Inference and limits:** Supports edge-exposure assessment; species-specific edge responses and map resolution govern meaning.
- **Supporting indicators:** [EII:BIO-006](#bio-006), [EII:BIO-005](#bio-005), [EII:LAN-002](#lan-002).

<a id="lan-002"></a>

### EII:LAN-002 — Landscape composition/diversity

**Definition:** Area proportions and diversity of declared land/habitat classes.

**Direct observations / derivation:** Harmonised classes and area weights, proportions and specified diversity index.

**Inference and limits:** Supports mosaic comparison; class diversity does not itself imply species diversity or functional integrity.

**Display label:** Landscape mix and diversity

**Display measurement:** Land-cover or habitat maps. Harmonised classes and area weights, proportions and specified diversity index.

**Display interpretation:** Shows the mix of land or habitat types. A varied landscape does not automatically contain more species or work better ecologically.

**Measurement origin:** Land-cover or habitat maps

**Supporting indicators:** [EII:DIS-004](#dis-004); [EII:BIO-001](#bio-001); [EII:FUN-008](#fun-008)

**Primary domain:** D10

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["landscape", "watershed", "region"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["land"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS005, RS006, RS009

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:LAN-002","domain":"D10","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["state"],"routes":["land"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Area proportions and diversity of declared land/habitat classes.
- **Direct observations / derivation:** Harmonised classes and area weights, proportions and specified diversity index.
- **Inference and limits:** Supports mosaic comparison; class diversity does not itself imply species diversity or functional integrity.
- **Supporting indicators:** [EII:DIS-004](#dis-004), [EII:BIO-001](#bio-001), [EII:FUN-008](#fun-008).

<a id="lan-003"></a>

### EII:LAN-003 — Riparian buffer extent/continuity

**Definition:** Width, area and gaps in defined streamside vegetation.

**Direct observations / derivation:** Stream/vegetation maps and field checks, m, ha and % continuity.

**Inference and limits:** Supports buffering/habitat assessment; width alone does not quantify pollutant removal or flood protection.

**Display label:** Streamside vegetation buffers

**Display measurement:** Stream maps, imagery and field vegetation surveys. Stream/vegetation maps and field checks, m, ha and % continuity.

**Display interpretation:** Shows the width and continuity of vegetation beside water. Width alone does not prove effective nutrient filtering or flood protection.

**Measurement origin:** Stream maps, imagery and field vegetation surveys

**Supporting indicators:** [EII:FUN-003](#fun-003); [EII:HYD-018](#hyd-018); [EII:BIO-007](#bio-007)

**Primary domain:** D10

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["landscape", "watershed", "region"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["terrain", "land", "amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021, RS004, RS005, RS006, RS009; AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:LAN-003","domain":"D10","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["state"],"routes":["terrain","land","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Width, area and gaps in defined streamside vegetation.
- **Direct observations / derivation:** Stream/vegetation maps and field checks, m, ha and % continuity.
- **Inference and limits:** Supports buffering/habitat assessment; width alone does not quantify pollutant removal or flood protection.
- **Supporting indicators:** [EII:FUN-003](#fun-003), [EII:HYD-018](#hyd-018), [EII:BIO-007](#bio-007).

<a id="lan-004"></a>

### EII:LAN-004 — Barrier density/permeability

**Definition:** Number/extent of obstacles and species-specific movement passability.

**Direct observations / derivation:** Roads, dams/fences and verified passage data, barriers/km or crossing probability.

**Inference and limits:** Supports movement constraint assessment; mapped barriers vary in permeability with species and flow/traffic.

**Display label:** Movement barriers

**Display measurement:** Infrastructure maps and field passage observations. Roads, dams/fences and verified passage data, barriers/km or crossing probability.

**Display interpretation:** Shows obstacles to movement and how passable they may be. The same barrier can affect different species differently.

**Measurement origin:** Infrastructure maps and field passage observations

**Supporting indicators:** [EII:BIO-007](#bio-007); [EII:BIO-015](#bio-015); [EII:HYD-017](#hyd-017)

**Primary domain:** D10

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "modelled", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["landscape", "watershed", "region"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["settlement", "terrain"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS019, RS021

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:LAN-004","domain":"D10","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","modelled","pressure"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["pressure"],"routes":["settlement","terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Number/extent of obstacles and species-specific movement passability.
- **Direct observations / derivation:** Roads, dams/fences and verified passage data, barriers/km or crossing probability.
- **Inference and limits:** Supports movement constraint assessment; mapped barriers vary in permeability with species and flow/traffic.
- **Supporting indicators:** [EII:BIO-007](#bio-007), [EII:BIO-015](#bio-015), [EII:HYD-017](#hyd-017).

<a id="lan-005"></a>

### EII:LAN-005 — Burned/converted area by habitat

**Definition:** Disturbance area intersected with harmonised habitat classes.

**Direct observations / derivation:** Validated event/transition polygons over habitat maps, ha and % affected.

**Inference and limits:** Supports habitat-specific exposure assessment; classification and event-boundary errors propagate.

**Display label:** Burned or converted habitat area

**Display measurement:** Satellite disturbance maps combined with habitat maps. Validated event/transition polygons over habitat maps, ha and % affected.

**Display interpretation:** Shows how much of each habitat has burned or changed use. Errors in habitat and event maps affect the totals.

**Measurement origin:** Satellite disturbance maps combined with habitat maps

**Supporting indicators:** [EII:DIS-003](#dis-003); [EII:DIS-005](#dis-005); [EII:BIO-005](#bio-005)

**Primary domain:** D10

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["landscape", "watershed", "region"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["fire", "land"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS016, RS017, RS004, RS005, RS006, RS009

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:LAN-005","domain":"D10","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","pressure"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["pressure"],"routes":["fire","land"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Disturbance area intersected with harmonised habitat classes.
- **Direct observations / derivation:** Validated event/transition polygons over habitat maps, ha and % affected.
- **Inference and limits:** Supports habitat-specific exposure assessment; classification and event-boundary errors propagate.
- **Supporting indicators:** [EII:DIS-003](#dis-003), [EII:DIS-005](#dis-005), [EII:BIO-005](#bio-005).

<a id="lan-006"></a>

### EII:LAN-006 — Topographic position/terrain curvature

**Definition:** Relative terrain position and curvature at a declared neighbourhood scale.

**Direct observations / derivation:** DTM derivatives or local elevation contrast, m, index or curvature units as defined.

**Inference and limits:** Supports drainage/exposure context; neighbourhood choice changes meaning and does not measure soil properties.

**Display label:** Terrain position and shape

**Display measurement:** LiDAR or other terrain models. DTM derivatives or local elevation contrast, m, index or curvature units as defined.

**Display interpretation:** Helps describe ridges, hollows and curved slopes. Terrain shape suggests conditions but does not directly measure soil properties.

**Measurement origin:** LiDAR or other terrain models

**Supporting indicators:** [EII:TER-002](#ter-002); [EII:TER-005](#ter-005); [EII:HYD-001](#hyd-001)

**Primary domain:** D10

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "context"]`

**Spatial/temporal dimensions:** `{"spatial": ["landscape", "watershed", "region"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["context"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["terrain"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS021

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:LAN-006","domain":"D10","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","context"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["context"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Relative terrain position and curvature at a declared neighbourhood scale.
- **Direct observations / derivation:** DTM derivatives or local elevation contrast, m, index or curvature units as defined.
- **Inference and limits:** Supports drainage/exposure context; neighbourhood choice changes meaning and does not measure soil properties.
- **Supporting indicators:** [EII:TER-002](#ter-002), [EII:TER-005](#ter-005), [EII:HYD-001](#hyd-001).

<a id="fun-015"></a>

### EII:FUN-015 — Net ecosystem metabolism

**Definition:** Gross ecosystem production minus ecosystem respiration for a declared system.

**Direct observations / derivation:** Aquatic oxygen/CO₂ time series with gas exchange, or validated flux balance, mass/area/time.

**Inference and limits:** Supports autotrophic/heterotrophic balance assessment; transport and diel mixing must be modelled.

**Display label:** Net ecosystem production–respiration balance

**Display measurement:** Field oxygen/carbon dioxide time series and exchange models. Aquatic oxygen/CO₂ time series with gas exchange, or validated flux balance, mass/area/time.

**Display interpretation:** Shows the balance between ecosystem production and respiration. Water movement and gas exchange must be included in aquatic estimates.

**Measurement origin:** Field oxygen/carbon dioxide time series and exchange models

**Supporting indicators:** [EII:HYD-013](#hyd-013); [EII:HYD-014](#hyd-014); [EII:CYC-001](#cyc-001)

**Primary domain:** D11

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "ecosystem", "watershed"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:FUN-015","domain":"D11","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["plot","ecosystem","watershed"],"temporal":["season","year"]},"quaternary":["function"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Gross ecosystem production minus ecosystem respiration for a declared system.
- **Direct observations / derivation:** Aquatic oxygen/CO₂ time series with gas exchange, or validated flux balance, mass/area/time.
- **Inference and limits:** Supports autotrophic/heterotrophic balance assessment; transport and diel mixing must be modelled.
- **Supporting indicators:** [EII:HYD-013](#hyd-013), [EII:HYD-014](#hyd-014), [EII:CYC-001](#cyc-001).

<a id="fun-016"></a>

### EII:FUN-016 — Trophic transfer efficiency

**Definition:** Production passed between specified trophic levels relative to lower-level production.

**Direct observations / derivation:** Comparable production/energy estimates, %, with food-web and spatial boundary.

**Inference and limits:** Supports energy-transfer assessment; standing biomass ratios are not production efficiencies.

**Display label:** Food-chain transfer efficiency

**Display measurement:** Field/laboratory production estimates across feeding levels. Comparable production/energy estimates, %, with food-web and spatial boundary.

**Display interpretation:** Helps estimate how much production passes between feeding levels. The ratio of standing biomass is not the same as energy-transfer efficiency.

**Measurement origin:** Field/laboratory production estimates across feeding levels

**Supporting indicators:** [EII:BIO-013](#bio-013); [EII:INT-008](#int-008); [EII:FUN-001](#fun-001)

**Primary domain:** D11

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:FUN-016","domain":"D11","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["function"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Production passed between specified trophic levels relative to lower-level production.
- **Direct observations / derivation:** Comparable production/energy estimates, %, with food-web and spatial boundary.
- **Inference and limits:** Supports energy-transfer assessment; standing biomass ratios are not production efficiencies.
- **Supporting indicators:** [EII:BIO-013](#bio-013), [EII:INT-008](#int-008), [EII:FUN-001](#fun-001).

<a id="fun-017"></a>

### EII:FUN-017 — Ecosystem multifunctionality

**Definition:** Joint performance of multiple specified ecosystem functions.

**Direct observations / derivation:** Named function measurements and declared averaging/threshold/ordination method, score or number above threshold.

**Inference and limits:** Supports multivariate function comparison; function selection, scaling and trade-offs control results.

**Display label:** Combined ecosystem functions

**Display measurement:** Combined measurements of named ecosystem functions. Named function measurements and declared averaging/threshold/ordination method, score or number above threshold.

**Display interpretation:** Combines evidence about several ecosystem functions. The selected functions and scoring method affect the result.

**Measurement origin:** Combined measurements of named ecosystem functions

**Supporting indicators:** [EII:FUN-001](#fun-001); [EII:FUN-003](#fun-003); [EII:BIO-009](#bio-009); [EII:MIC-024](#mic-024)

**Primary domain:** D11

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["composite"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "ecosystem", "watershed"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["condition", "assessment"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:FUN-017","domain":"D11","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["composite"],"tertiary":{"spatial":["plot","ecosystem","watershed"],"temporal":["season","year"]},"quaternary":["condition","assessment"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Joint performance of multiple specified ecosystem functions.
- **Direct observations / derivation:** Named function measurements and declared averaging/threshold/ordination method, score or number above threshold.
- **Inference and limits:** Supports multivariate function comparison; function selection, scaling and trade-offs control results.
- **Supporting indicators:** [EII:FUN-001](#fun-001), [EII:FUN-003](#fun-003), [EII:BIO-009](#bio-009), [EII:MIC-024](#mic-024).

<a id="fun-018"></a>

### EII:FUN-018 — Water purification/removal efficiency

**Definition:** Fraction or mass of specified pollutant removed across a defined system.

**Direct observations / derivation:** Matched inflow/outflow concentration and flow, % and mass/time including retained/transformed fate.

**Inference and limits:** Supports treatment-function assessment; dilution, storage and export must be separated from permanent removal.

**Display label:** Water purification

**Display measurement:** Field flow measurements and laboratory inflow/outflow chemistry. Matched inflow/outflow concentration and flow, % and mass/time including retained/transformed fate.

**Display interpretation:** Shows how much of a named pollutant a system removes. Dilution or temporary storage should not be counted as permanent removal.

**Measurement origin:** Field flow measurements and laboratory inflow/outflow chemistry

**Supporting indicators:** [EII:HYD-018](#hyd-018); [EII:FUN-003](#fun-003); [EII:CYC-009](#cyc-009)

**Primary domain:** D11

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "ecosystem", "watershed"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:FUN-018","domain":"D11","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["plot","ecosystem","watershed"],"temporal":["season","year"]},"quaternary":["function"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fraction or mass of specified pollutant removed across a defined system.
- **Direct observations / derivation:** Matched inflow/outflow concentration and flow, % and mass/time including retained/transformed fate.
- **Inference and limits:** Supports treatment-function assessment; dilution, storage and export must be separated from permanent removal.
- **Supporting indicators:** [EII:HYD-018](#hyd-018), [EII:FUN-003](#fun-003), [EII:CYC-009](#cyc-009).

<a id="fun-019"></a>

### EII:FUN-019 — Thermal regulation effect

**Definition:** Temperature difference attributable to a specified vegetation/ecosystem feature.

**Direct observations / derivation:** Matched shaded/open or intervention/control temperature observations, °C, with weather/time controls.

**Inference and limits:** Supports cooling assessment; association alone does not isolate causal cooling and scales differ.

**Display label:** Ecosystem cooling

**Display measurement:** Matched field temperature sensors or thermal images. Matched shaded/open or intervention/control temperature observations, °C, with weather/time controls.

**Display interpretation:** Helps assess cooling associated with vegetation or habitat. Comparable weather and control locations are needed to isolate the effect.

**Measurement origin:** Matched field temperature sensors or thermal images

**Supporting indicators:** [EII:HYD-003](#hyd-003); [EII:ATM-001](#atm-001); [EII:VEG-012](#veg-012)

**Primary domain:** D11

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "ecosystem", "watershed"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["function"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["thermal", "iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS002; IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:FUN-019","domain":"D11","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["plot","ecosystem","watershed"],"temporal":["season","year"]},"quaternary":["function"],"routes":["thermal","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Temperature difference attributable to a specified vegetation/ecosystem feature.
- **Direct observations / derivation:** Matched shaded/open or intervention/control temperature observations, °C, with weather/time controls.
- **Inference and limits:** Supports cooling assessment; association alone does not isolate causal cooling and scales differ.
- **Supporting indicators:** [EII:HYD-003](#hyd-003), [EII:ATM-001](#atm-001), [EII:VEG-012](#veg-012).

<a id="fun-020"></a>

### EII:FUN-020 — Soil-function deficit profile

**Definition:** Separate departures of stated soil functions from justified references.

**Direct observations / derivation:** Function-specific measurements and uncertainty, native units or standardised differences, kept disaggregated.

**Inference and limits:** Supports targeted assessment; reference choice and trade-offs preclude a universal soil-quality verdict.

**Display label:** Soil-function shortfalls

**Display measurement:** Separate field and laboratory soil-function tests. Function-specific measurements and uncertainty, native units or standardised differences, kept disaggregated.

**Display interpretation:** Shows which soil functions fall below chosen references. Different functions may show different strengths and weaknesses.

**Measurement origin:** Separate field and laboratory soil-function tests

**Supporting indicators:** [EII:HYD-004](#hyd-004); [EII:MIC-023](#mic-023); [EII:SOI-005](#soi-005); [EII:SOI-013](#soi-013)

**Primary domain:** D11

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "ecosystem", "watershed"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["state"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:FUN-020","domain":"D11","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["plot","ecosystem","watershed"],"temporal":["season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Separate departures of stated soil functions from justified references.
- **Direct observations / derivation:** Function-specific measurements and uncertainty, native units or standardised differences, kept disaggregated.
- **Inference and limits:** Supports targeted assessment; reference choice and trade-offs preclude a universal soil-quality verdict.
- **Supporting indicators:** [EII:HYD-004](#hyd-004), [EII:MIC-023](#mic-023), [EII:SOI-005](#soi-005), [EII:SOI-013](#soi-013).

<a id="res-001"></a>

### EII:RES-001 — Disturbance resistance

**Definition:** Magnitude of retained condition/function during a specified disturbance.

**Direct observations / derivation:** Matched baseline/reference and disturbance observations, ratio or change with formula declared.

**Inference and limits:** Supports resistance comparison for one response variable; unrelated variables may respond differently and controls are needed.

**Display label:** Resistance to disturbance

**Display measurement:** Field/satellite measurements before and during disturbance. Matched baseline/reference and disturbance observations, ratio or change with formula declared.

**Display interpretation:** Shows how much a measured property changes during disturbance. Resistance may differ between species, soils and functions.

**Measurement origin:** Field/satellite measurements before and during disturbance

**Supporting indicators:** [EII:DIS-009](#dis-009); [EII:FUN-001](#fun-001); [EII:HYD-001](#hyd-001)

**Primary domain:** D12

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "ecosystem", "landscape"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["disturbance_response", "restoration_assessment"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["veg", "amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS001, RS002; AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:RES-001","domain":"D12","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["plot","ecosystem","landscape"],"temporal":["event","year","decade"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":["veg","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Magnitude of retained condition/function during a specified disturbance.
- **Direct observations / derivation:** Matched baseline/reference and disturbance observations, ratio or change with formula declared.
- **Inference and limits:** Supports resistance comparison for one response variable; unrelated variables may respond differently and controls are needed.
- **Supporting indicators:** [EII:DIS-009](#dis-009), [EII:FUN-001](#fun-001), [EII:HYD-001](#hyd-001).

<a id="res-002"></a>

### EII:RES-002 — Recovery rate/time

**Definition:** Speed of return towards a declared condition/function reference.

**Direct observations / derivation:** Repeated response trajectory, change/time or time to threshold with censoring if unrecovered.

**Inference and limits:** Supports recovery comparison; reference drift and sampling frequency affect estimated recovery.

**Display label:** Recovery speed and time

**Display measurement:** Repeated field/satellite measurements after disturbance. Repeated response trajectory, change/time or time to threshold with censoring if unrecovered.

**Display interpretation:** Shows how quickly a measured property returns towards a reference. The chosen baseline and survey timing affect recovery estimates.

**Measurement origin:** Repeated field/satellite measurements after disturbance

**Supporting indicators:** [EII:DIS-009](#dis-009); [EII:VEG-017](#veg-017); [EII:FUN-001](#fun-001)

**Primary domain:** D12

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "ecosystem", "landscape"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["disturbance_response", "restoration_assessment"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["veg"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS001, RS002

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:RES-002","domain":"D12","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","modelled"],"tertiary":{"spatial":["plot","ecosystem","landscape"],"temporal":["event","year","decade"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":["veg"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Speed of return towards a declared condition/function reference.
- **Direct observations / derivation:** Repeated response trajectory, change/time or time to threshold with censoring if unrecovered.
- **Inference and limits:** Supports recovery comparison; reference drift and sampling frequency affect estimated recovery.
- **Supporting indicators:** [EII:DIS-009](#dis-009), [EII:VEG-017](#veg-017), [EII:FUN-001](#fun-001).

<a id="res-003"></a>

### EII:RES-003 — Temporal variability/stability

**Definition:** Variation of a declared ecological variable across a stated period.

**Direct observations / derivation:** Repeat data, variance, CV or mean/SD with sampling interval and trend treatment.

**Inference and limits:** Supports temporal-stability comparison; low variability may reflect persistent degradation and mean dependence matters.

**Display label:** Variation and stability over time

**Display measurement:** Repeated field, sensor, satellite or farm measurements. Repeat data, variance, CV or mean/SD with sampling interval and trend treatment.

**Display interpretation:** Shows how much a property varies over time. A consistently degraded system can also have low variability.

**Measurement origin:** Repeated field, sensor, satellite or farm measurements

**Supporting indicators:** [EII:FUN-004](#fun-004); [EII:DIS-006](#dis-006); [EII:RES-004](#res-004)

**Primary domain:** D12

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "ecosystem", "landscape"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["disturbance_response", "restoration_assessment"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["veg", "amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS001, RS002; AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:RES-003","domain":"D12","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["plot","ecosystem","landscape"],"temporal":["event","year","decade"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":["veg","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Variation of a declared ecological variable across a stated period.
- **Direct observations / derivation:** Repeat data, variance, CV or mean/SD with sampling interval and trend treatment.
- **Inference and limits:** Supports temporal-stability comparison; low variability may reflect persistent degradation and mean dependence matters.
- **Supporting indicators:** [EII:FUN-004](#fun-004), [EII:DIS-006](#dis-006), [EII:RES-004](#res-004).

<a id="res-004"></a>

### EII:RES-004 — Response diversity/asynchrony

**Definition:** Differences in component responses to the same environmental variation.

**Direct observations / derivation:** Species/function time series and declared covariance/asynchrony metric.

**Inference and limits:** Supports portfolio-buffering hypotheses; trait diversity alone does not demonstrate asynchronous realised responses.

**Display label:** Differences in species responses

**Display measurement:** Repeated field species/function measurements. Species/function time series and declared covariance/asynchrony metric.

**Display interpretation:** Shows whether species respond differently over time. Different responses may help buffer change, but this needs actual time-series evidence.

**Measurement origin:** Repeated field species/function measurements

**Supporting indicators:** [EII:BIO-004](#bio-004); [EII:BIO-002](#bio-002); [EII:RES-003](#res-003)

**Primary domain:** D12

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["disturbance_response", "restoration_assessment"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:RES-004","domain":"D12","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Differences in component responses to the same environmental variation.
- **Direct observations / derivation:** Species/function time series and declared covariance/asynchrony metric.
- **Inference and limits:** Supports portfolio-buffering hypotheses; trait diversity alone does not demonstrate asynchronous realised responses.
- **Supporting indicators:** [EII:BIO-004](#bio-004), [EII:BIO-002](#bio-002), [EII:RES-003](#res-003).

<a id="res-005"></a>

### EII:RES-005 — Post-fire compositional/function recovery

**Definition:** Recovery of specified taxonomic and process variables following confirmed fire.

**Direct observations / derivation:** Repeat matched community/process measures against pre-fire/reference, distance or recovery time.

**Inference and limits:** Supports multidimensional recovery assessment; satellite regreening does not establish full biodiversity/function recovery.

**Display label:** Recovery after fire

**Display measurement:** Repeated field community/function surveys and fire imagery. Repeat matched community/process measures against pre-fire/reference, distance or recovery time.

**Display interpretation:** Tracks species and functions after fire. Green cover can return before the original community or functions recover.

**Measurement origin:** Repeated field community/function surveys and fire imagery

**Supporting indicators:** [EII:DIS-001](#dis-001); [EII:DIS-003](#dis-003); [EII:VEG-017](#veg-017); [EII:MIC-024](#mic-024)

**Primary domain:** D12

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["disturbance_response", "restoration_assessment"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["fire", "veg", "bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS016, RS017, RS004, RS001, RS002; Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:RES-005","domain":"D12","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":["fire","veg","bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Recovery of specified taxonomic and process variables following confirmed fire.
- **Direct observations / derivation:** Repeat matched community/process measures against pre-fire/reference, distance or recovery time.
- **Inference and limits:** Supports multidimensional recovery assessment; satellite regreening does not establish full biodiversity/function recovery.
- **Supporting indicators:** [EII:DIS-001](#dis-001), [EII:DIS-003](#dis-003), [EII:VEG-017](#veg-017), [EII:MIC-024](#mic-024).

<a id="res-006"></a>

### EII:RES-006 — Early-warning time-series signals

**Definition:** Declared statistical signals hypothesised to precede state transitions.

**Direct observations / derivation:** Long standardised series, lag autocorrelation/variance or other specified metric with detrending/null tests.

**Inference and limits:** Supports exploratory transition surveillance; noise, forcing and sampling artefacts create false positives and no deterministic tipping forecast.

**Display label:** Possible early-warning signals

**Display measurement:** Long sensor or ecological monitoring time series. Long standardised series, lag autocorrelation/variance or other specified metric with detrending/null tests.

**Display interpretation:** Flags patterns that might precede a major change. Noise and changing external conditions can produce false warnings.

**Measurement origin:** Long sensor or ecological monitoring time series

**Supporting indicators:** [EII:RES-003](#res-003); [EII:DIS-006](#dis-006); [EII:HYD-001](#hyd-001)

**Primary domain:** D12

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "predictive"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "ecosystem", "landscape"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["exposure", "planning"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:RES-006","domain":"D12","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","predictive"],"tertiary":{"spatial":["plot","ecosystem","landscape"],"temporal":["event","year","decade"]},"quaternary":["exposure","planning"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Declared statistical signals hypothesised to precede state transitions.
- **Direct observations / derivation:** Long standardised series, lag autocorrelation/variance or other specified metric with detrending/null tests.
- **Inference and limits:** Supports exploratory transition surveillance; noise, forcing and sampling artefacts create false positives and no deterministic tipping forecast.
- **Supporting indicators:** [EII:RES-003](#res-003), [EII:DIS-006](#dis-006), [EII:HYD-001](#hyd-001).

<a id="res-007"></a>

### EII:RES-007 — Scenario sensitivity/model uncertainty

**Definition:** Response of a modelled ecological quantity to scenarios, parameters and model choice.

**Direct observations / derivation:** Validated ensemble outputs, distributions and variance components in target-variable units.

**Inference and limits:** Supports conditional confidence assessment; ensembles need not span all structural uncertainty and are not observed future outcomes.

**Display label:** Uncertainty in scenario predictions

**Display measurement:** Comparisons across climate/ecological model runs. Validated ensemble outputs, distributions and variance components in target-variable units.

**Display interpretation:** Shows how predictions change with scenarios and assumptions. The tested models may not cover every source of uncertainty.

**Measurement origin:** Comparisons across climate/ecological model runs

**Supporting indicators:** [EII:DIS-010](#dis-010); [EII:RES-001](#res-001); [EII:DIS-007](#dis-007)

**Primary domain:** D12

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "ecosystem", "landscape"], "temporal": ["event", "year", "decade"]}`

**Ecological purpose:** `["disturbance_response", "restoration_assessment"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `[]`

**Scientific reference keys:** `[]`

**Display source keys:** Field/lab/model source to register

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:RES-007","domain":"D12","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","modelled"],"tertiary":{"spatial":["plot","ecosystem","landscape"],"temporal":["event","year","decade"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Response of a modelled ecological quantity to scenarios, parameters and model choice.
- **Direct observations / derivation:** Validated ensemble outputs, distributions and variance components in target-variable units.
- **Inference and limits:** Supports conditional confidence assessment; ensembles need not span all structural uncertainty and are not observed future outcomes.
- **Supporting indicators:** [EII:DIS-010](#dis-010), [EII:RES-001](#res-001), [EII:DIS-007](#dis-007).

<a id="agr-001"></a>

### EII:AGR-001 — Agronomic nitrogen-use efficiency

**Definition:** Declared crop production or uptake response per N input.

**Direct observations / derivation:** Yield/N-input or fertilised-minus-control yield/N-input, kg product/kg N; label partial factor productivity versus agronomic efficiency.

**Inference and limits:** Supports N-performance comparison; definitions differ and high yield/input does not establish low N loss.

**Display label:** Crop nitrogen-use efficiency

**Display measurement:** Farm yield and nitrogen-input records. Yield/N-input or fertilised-minus-control yield/N-input, kg product/kg N; label partial factor productivity versus agronomic efficiency.

**Display interpretation:** Helps compare crop output or response per nitrogen input. The chosen efficiency measure does not directly show nitrogen losses.

**Measurement origin:** Farm yield and nitrogen-input records

**Supporting indicators:** [EII:FUN-004](#fun-004); [EII:FUN-007](#fun-007); [EII:CYC-007](#cyc-007)

**Primary domain:** D13

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "farm", "landscape"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["state", "production_assessment"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:AGR-001","domain":"D13","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["state","production_assessment"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Declared crop production or uptake response per N input.
- **Direct observations / derivation:** Yield/N-input or fertilised-minus-control yield/N-input, kg product/kg N; label partial factor productivity versus agronomic efficiency.
- **Inference and limits:** Supports N-performance comparison; definitions differ and high yield/input does not establish low N loss.
- **Supporting indicators:** [EII:FUN-004](#fun-004), [EII:FUN-007](#fun-007), [EII:CYC-007](#cyc-007).

<a id="agr-002"></a>

### EII:AGR-002 — Crop water productivity

**Definition:** Crop output per stated water input or consumptive use.

**Direct observations / derivation:** Harvest mass divided by ET, irrigation or total supply, kg/m³ with denominator declared.

**Inference and limits:** Supports water-performance comparison; irrigation efficiency and basin water savings require return-flow analysis.

**Display label:** Crop water productivity

**Display measurement:** Farm harvest records combined with water meters or water-use estimates. Harvest mass divided by ET, irrigation or total supply, kg/m³ with denominator declared.

**Display interpretation:** Shows crop output per amount of water supplied or used. Higher farm efficiency does not necessarily mean less basin-wide water consumption.

**Measurement origin:** Farm harvest records combined with water meters or water-use estimates

**Supporting indicators:** [EII:FUN-004](#fun-004); [EII:FUN-007](#fun-007); [EII:HYD-012](#hyd-012)

**Primary domain:** D13

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "farm", "landscape"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["state", "production_assessment"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr", "iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context; IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:AGR-002","domain":"D13","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["state","production_assessment"],"routes":["amr","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Crop output per stated water input or consumptive use.
- **Direct observations / derivation:** Harvest mass divided by ET, irrigation or total supply, kg/m³ with denominator declared.
- **Inference and limits:** Supports water-performance comparison; irrigation efficiency and basin water savings require return-flow analysis.
- **Supporting indicators:** [EII:FUN-004](#fun-004), [EII:FUN-007](#fun-007), [EII:HYD-012](#hyd-012).

<a id="agr-003"></a>

### EII:AGR-003 — Pesticide hazard/risk indicator

**Definition:** Method-specific aggregation of chemical hazard and, for risk, exposure.

**Direct observations / derivation:** Application records, active ingredients and named toxicity/exposure model, declared score.

**Inference and limits:** Supports screening under a stated framework; kg applied alone is not ecological risk and species/mixtures matter.

**Display label:** Pesticide hazard and risk

**Display measurement:** Farm pesticide records and chemical hazard/exposure models. Application records, active ingredients and named toxicity/exposure model, declared score.

**Display interpretation:** Helps screen pesticide hazards or modelled risks. Applied mass alone does not describe toxicity or actual exposure.

**Measurement origin:** Farm pesticide records and chemical hazard/exposure models

**Supporting indicators:** [EII:FUN-007](#fun-007); [EII:HYD-020](#hyd-020); [EII:BIO-008](#bio-008)

**Primary domain:** D13

**Secondary domains:** `[]`

**Classification dimensions:** `["composite", "modelled", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "farm", "landscape"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["condition", "assessment"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:AGR-003","domain":"D13","related_domains":[],"record_type":"indicator","variants":[],"secondary":["composite","modelled","pressure"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["condition","assessment"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Method-specific aggregation of chemical hazard and, for risk, exposure.
- **Direct observations / derivation:** Application records, active ingredients and named toxicity/exposure model, declared score.
- **Inference and limits:** Supports screening under a stated framework; kg applied alone is not ecological risk and species/mixtures matter.
- **Supporting indicators:** [EII:FUN-007](#fun-007), [EII:HYD-020](#hyd-020), [EII:BIO-008](#bio-008).

<a id="agr-004"></a>

### EII:AGR-004 — Pest population/crop damage

**Definition:** Abundance of named pests and separately measured plant injury.

**Direct observations / derivation:** Standardised trap/scout counts and damaged tissue/production fraction, counts/area and %.

**Inference and limits:** Supports pest-pressure assessment; trap counts require calibration and economic injury thresholds are context-specific.

**Display label:** Pest numbers and crop damage

**Display measurement:** Field pest counts, traps and crop-damage surveys. Standardised trap/scout counts and damaged tissue/production fraction, counts/area and %.

**Display interpretation:** Shows pest numbers or crop damage. Trap counts do not directly tell us the likely yield loss.

**Measurement origin:** Field pest counts, traps and crop-damage surveys

**Supporting indicators:** [EII:BIO-009](#bio-009); [EII:INT-003](#int-003); [EII:FUN-004](#fun-004)

**Primary domain:** D13

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "farm", "landscape"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:AGR-004","domain":"D13","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","pressure"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["pressure"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Abundance of named pests and separately measured plant injury.
- **Direct observations / derivation:** Standardised trap/scout counts and damaged tissue/production fraction, counts/area and %.
- **Inference and limits:** Supports pest-pressure assessment; trap counts require calibration and economic injury thresholds are context-specific.
- **Supporting indicators:** [EII:BIO-009](#bio-009), [EII:INT-003](#int-003), [EII:FUN-004](#fun-004).

<a id="agr-005"></a>

### EII:AGR-005 — Crop disease incidence/severity

**Definition:** Proportion of plants diseased and amount of affected tissue are separate quantities.

**Direct observations / derivation:** Confirmed diagnostics and field scoring, % plants and % tissue or declared scale.

**Inference and limits:** Supports disease-burden assessment; symptoms may have abiotic causes and marker presence does not establish disease.

**Display label:** Crop disease incidence and severity

**Display measurement:** Field disease surveys with laboratory diagnosis when needed. Confirmed diagnostics and field scoring, % plants and % tissue or declared scale.

**Display interpretation:** Shows how common or severe crop disease is. Similar symptoms can have non-disease causes, so diagnosis matters.

**Measurement origin:** Field disease surveys with laboratory diagnosis when needed

**Supporting indicators:** [EII:MIC-016](#mic-016); [EII:INT-009](#int-009); [EII:VEG-015](#veg-015)

**Primary domain:** D13

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["sample", "community"], "temporal": ["sampling_event", "season", "year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `["disease_incidence", "disease_severity"]`

**Record type:** family

**Candidate source routes:** `["amr", "bio"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context; Bioinformatics (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:AGR-005","domain":"D13","related_domains":[],"record_type":"family","variants":["disease_incidence","disease_severity"],"secondary":["measured","pressure"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["pressure"],"routes":["amr","bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Proportion of plants diseased and amount of affected tissue are separate quantities.
- **Direct observations / derivation:** Confirmed diagnostics and field scoring, % plants and % tissue or declared scale.
- **Inference and limits:** Supports disease-burden assessment; symptoms may have abiotic causes and marker presence does not establish disease.
- **Supporting indicators:** [EII:MIC-016](#mic-016), [EII:INT-009](#int-009), [EII:VEG-015](#veg-015).

<a id="agr-006"></a>

### EII:AGR-006 — Crop/rotation diversity

**Definition:** Diversity of cultivated taxa and their sequence through time.

**Direct observations / derivation:** Crop identities, area shares and rotation records, richness or declared diversity metric.

**Inference and limits:** Supports diversification assessment; diversity alone does not prove reduced inputs, resilience or functional complementarity.

**Display label:** Crop and rotation diversity

**Display measurement:** Farm crop, area and rotation records. Crop identities, area shares and rotation records, richness or declared diversity metric.

**Display interpretation:** Shows the variety of crops and rotations. Diversity alone does not prove better yields, resilience or lower input use.

**Measurement origin:** Farm crop, area and rotation records

**Supporting indicators:** [EII:VEG-017](#veg-017); [EII:FUN-004](#fun-004); [EII:BIO-004](#bio-004)

**Primary domain:** D13

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "context"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "farm", "landscape"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["context", "production_assessment"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:AGR-006","domain":"D13","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","context"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["context","production_assessment"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Diversity of cultivated taxa and their sequence through time.
- **Direct observations / derivation:** Crop identities, area shares and rotation records, richness or declared diversity metric.
- **Inference and limits:** Supports diversification assessment; diversity alone does not prove reduced inputs, resilience or functional complementarity.
- **Supporting indicators:** [EII:VEG-017](#veg-017), [EII:FUN-004](#fun-004), [EII:BIO-004](#bio-004).

<a id="agr-007"></a>

### EII:AGR-007 — Land equivalent ratio

**Definition:** Relative land productivity of an intercrop compared with its specified monocultures.

**Direct observations / derivation:** Σ(intercrop component yield/monocrop reference yield), dimensionless, using matched seasons and inputs.

**Inference and limits:** Supports land-productivity comparison; reference choice and unequal inputs prevent universal superiority claims.

**Display label:** Mixed-crop land productivity

**Display measurement:** Field harvests from mixed crops and comparable single-crop plots. Σ(intercrop component yield/monocrop reference yield), dimensionless, using matched seasons and inputs.

**Display interpretation:** Compares land productivity of mixed crops with separate crops. The comparison needs suitable reference yields and comparable inputs.

**Measurement origin:** Field harvests from mixed crops and comparable single-crop plots

**Supporting indicators:** [EII:FUN-004](#fun-004); [EII:AGR-006](#agr-006); [EII:AGR-001](#agr-001)

**Primary domain:** D13

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "farm", "landscape"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["state", "production_assessment"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:AGR-007","domain":"D13","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["state","production_assessment"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Relative land productivity of an intercrop compared with its specified monocultures.
- **Direct observations / derivation:** Σ(intercrop component yield/monocrop reference yield), dimensionless, using matched seasons and inputs.
- **Inference and limits:** Supports land-productivity comparison; reference choice and unequal inputs prevent universal superiority claims.
- **Supporting indicators:** [EII:FUN-004](#fun-004), [EII:AGR-006](#agr-006), [EII:AGR-001](#agr-001).

<a id="agr-008"></a>

### EII:AGR-008 — Harvest nutrient removal

**Definition:** Nutrient mass exported in harvested products.

**Direct observations / derivation:** Harvest dry mass × nutrient concentration, kg N/P/K/ha/season.

**Inference and limits:** Supports nutrient-budget assessment; residues, losses and harvested moisture require explicit accounting.

**Display label:** Nutrients removed in harvest

**Display measurement:** Harvest records and laboratory crop-nutrient tests. Harvest dry mass × nutrient concentration, kg N/P/K/ha/season.

**Display interpretation:** Shows nutrients removed in harvests. Other nutrient inputs and losses are needed for the whole farm balance.

**Measurement origin:** Harvest records and laboratory crop-nutrient tests

**Supporting indicators:** [EII:FUN-004](#fun-004); [EII:CYC-007](#cyc-007); [EII:SOI-008](#soi-008)

**Primary domain:** D13

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "process"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "farm", "landscape"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["function", "production_assessment"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:AGR-008","domain":"D13","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["function","production_assessment"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Nutrient mass exported in harvested products.
- **Direct observations / derivation:** Harvest dry mass × nutrient concentration, kg N/P/K/ha/season.
- **Inference and limits:** Supports nutrient-budget assessment; residues, losses and harvested moisture require explicit accounting.
- **Supporting indicators:** [EII:FUN-004](#fun-004), [EII:CYC-007](#cyc-007), [EII:SOI-008](#soi-008).

<a id="agr-009"></a>

### EII:AGR-009 — Forage utilisation/feed dependence

**Definition:** Fraction of forage consumed and imported feed contribution are separate metrics.

**Direct observations / derivation:** Before/after forage dry mass and feed accounts, % utilisation and % imported dry matter/nutrients.

**Inference and limits:** Supports grazing/resource assessment; trampling/wastage must be separated from intake and imports shift impacts off-site.

**Display label:** Forage use and imported feed

**Display measurement:** Farm feed accounts and field forage measurements. Before/after forage dry mass and feed accounts, % utilisation and % imported dry matter/nutrients.

**Display interpretation:** Helps assess forage use and reliance on imported feed. Trampling, waste and impacts outside the farm also matter.

**Measurement origin:** Farm feed accounts and field forage measurements

**Supporting indicators:** [EII:FUN-006](#fun-006); [EII:VEG-014](#veg-014); [EII:HUM-003](#hum-003)

**Primary domain:** D13

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "farm", "landscape"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `["forage_utilisation", "imported_feed_share"]`

**Record type:** family

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:AGR-009","domain":"D13","related_domains":[],"record_type":"family","variants":["forage_utilisation","imported_feed_share"],"secondary":["derived","pressure"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["pressure"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fraction of forage consumed and imported feed contribution are separate metrics.
- **Direct observations / derivation:** Before/after forage dry mass and feed accounts, % utilisation and % imported dry matter/nutrients.
- **Inference and limits:** Supports grazing/resource assessment; trampling/wastage must be separated from intake and imports shift impacts off-site.
- **Supporting indicators:** [EII:FUN-006](#fun-006), [EII:VEG-014](#veg-014), [EII:HUM-003](#hum-003).

<a id="agr-010"></a>

### EII:AGR-010 — Tillage/traffic disturbance intensity

**Definition:** Recorded mechanical soil disturbance rather than an agricultural philosophy label.

**Direct observations / derivation:** Passes, implement depth, axle load, area and dates, declared component units.

**Inference and limits:** Supports management-pressure comparison; index weighting is method-specific and physical outcome needs direct soil measurements.

**Display label:** Tillage and machinery disturbance

**Display measurement:** Farm machinery/operation records and field checks. Passes, implement depth, axle load, area and dates, declared component units.

**Display interpretation:** Shows recorded disturbance from machinery or tillage. Actual effects need soil measurements, not just counts of operations.

**Measurement origin:** Farm machinery/operation records and field checks

**Supporting indicators:** [EII:SOI-002](#soi-002); [EII:SOI-003](#soi-003); [EII:SOI-012](#soi-012)

**Primary domain:** D13

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "context", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "farm", "landscape"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["context"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:AGR-010","domain":"D13","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","context","pressure"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["context"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Recorded mechanical soil disturbance rather than an agricultural philosophy label.
- **Direct observations / derivation:** Passes, implement depth, axle load, area and dates, declared component units.
- **Inference and limits:** Supports management-pressure comparison; index weighting is method-specific and physical outcome needs direct soil measurements.
- **Supporting indicators:** [EII:SOI-002](#soi-002), [EII:SOI-003](#soi-003), [EII:SOI-012](#soi-012).

<a id="agr-011"></a>

### EII:AGR-011 — Farm nutrient/energy balance

**Definition:** Separate nutrient and energy flow accounts across a declared farm boundary.

**Direct observations / derivation:** Inputs/outputs and inventory changes, kg N/P/year and MJ/year; document allocation/imports.

**Inference and limits:** Supports resource-efficiency comparison; boundary omissions and unequal products can reverse comparisons.

**Display label:** Farm nutrient and energy balance

**Display measurement:** Farm input-output accounts and metered energy records. Inputs/outputs and inventory changes, kg N/P/year and MJ/year; document allocation/imports.

**Display interpretation:** Shows farm nutrient and energy inputs and outputs. Missing imports, losses and differences in products can change the comparison.

**Measurement origin:** Farm input-output accounts and metered energy records

**Supporting indicators:** [EII:CYC-007](#cyc-007); [EII:HUM-004](#hum-004); [EII:HUM-003](#hum-003)

**Primary domain:** D13

**Secondary domains:** `[]`

**Classification dimensions:** `["derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["plot", "farm", "landscape"], "temporal": ["season", "year"]}`

**Ecological purpose:** `["state", "production_assessment"]`

**Family / variant distinctions:** `["nutrient_balance", "energy_balance"]`

**Record type:** family

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:AGR-011","domain":"D13","related_domains":[],"record_type":"family","variants":["nutrient_balance","energy_balance"],"secondary":["derived"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["state","production_assessment"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Separate nutrient and energy flow accounts across a declared farm boundary.
- **Direct observations / derivation:** Inputs/outputs and inventory changes, kg N/P/year and MJ/year; document allocation/imports.
- **Inference and limits:** Supports resource-efficiency comparison; boundary omissions and unequal products can reverse comparisons.
- **Supporting indicators:** [EII:CYC-007](#cyc-007), [EII:HUM-004](#hum-004), [EII:HUM-003](#hum-003).

<a id="hum-001"></a>

### EII:HUM-001 — Impervious surface fraction

**Definition:** Proportion of ground covered by effectively water-impermeable surfaces.

**Direct observations / derivation:** Validated land-surface classification/field verification, %, with distinction between built-up and sealed surfaces.

**Inference and limits:** Supports runoff/heat-pressure assessment; drainage connectivity and permeable construction modify impacts.

**Display label:** Sealed ground cover

**Display measurement:** Satellite/aerial classifications and field surface checks. Validated land-surface classification/field verification, %, with distinction between built-up and sealed surfaces.

**Display interpretation:** Shows how much ground is sealed. Runoff also depends on drainage connections and whether some built surfaces let water through.

**Measurement origin:** Satellite/aerial classifications and field surface checks

**Supporting indicators:** [EII:FUN-009](#fun-009); [EII:HYD-006](#hyd-006); [EII:HYD-003](#hyd-003)

**Primary domain:** D14

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["farm", "watershed", "region"], "temporal": ["year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["settlement", "land"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS019, RS004, RS005, RS006, RS009

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HUM-001","domain":"D14","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","pressure"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["pressure"],"routes":["settlement","land"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Proportion of ground covered by effectively water-impermeable surfaces.
- **Direct observations / derivation:** Validated land-surface classification/field verification, %, with distinction between built-up and sealed surfaces.
- **Inference and limits:** Supports runoff/heat-pressure assessment; drainage connectivity and permeable construction modify impacts.
- **Supporting indicators:** [EII:FUN-009](#fun-009), [EII:HYD-006](#hyd-006), [EII:HYD-003](#hyd-003).

<a id="hum-002"></a>

### EII:HUM-002 — Land-use intensity

**Definition:** Measured physical activity/input density under a declared land-use system.

**Direct observations / derivation:** Harvest frequency, stocking, input or traffic measures per area/time; retain separate components or name index.

**Inference and limits:** Supports pressure comparison; land-use label alone does not quantify intensity or ecological effect.

**Display label:** Land-use intensity

**Display measurement:** Farm/land-management activity records. Harvest frequency, stocking, input or traffic measures per area/time; retain separate components or name index.

**Display interpretation:** Helps compare the intensity of recorded land use. Land-use names alone do not show the level of pressure.

**Measurement origin:** Farm/land-management activity records

**Supporting indicators:** [EII:FUN-006](#fun-006); [EII:FUN-007](#fun-007); [EII:AGR-010](#agr-010)

**Primary domain:** D14

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "derived", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["farm", "watershed", "region"], "temporal": ["year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr", "land"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS005, RS006, RS009; AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HUM-002","domain":"D14","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","derived","pressure"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["pressure"],"routes":["amr","land"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Measured physical activity/input density under a declared land-use system.
- **Direct observations / derivation:** Harvest frequency, stocking, input or traffic measures per area/time; retain separate components or name index.
- **Inference and limits:** Supports pressure comparison; land-use label alone does not quantify intensity or ecological effect.
- **Supporting indicators:** [EII:FUN-006](#fun-006), [EII:FUN-007](#fun-007), [EII:AGR-010](#agr-010).

<a id="hum-003"></a>

### EII:HUM-003 — Material-flow account/circularity

**Definition:** Physical material inputs, outputs and recycled fractions across a declared system.

**Direct observations / derivation:** Mass balance by material, Mg/year and recycled/input fraction, excluding double counting.

**Inference and limits:** Supports resource-flow comparison; recycled fraction does not demonstrate low total demand or low ecological impact.

**Display label:** Material use and recycling

**Display measurement:** Material input-output and recycling accounts. Mass balance by material, Mg/year and recycled/input fraction, excluding double counting.

**Display interpretation:** Shows material use and recycling. A high recycled share does not necessarily mean low overall resource demand.

**Measurement origin:** Material input-output and recycling accounts

**Supporting indicators:** [EII:FUN-010](#fun-010); [EII:HUM-004](#hum-004); [EII:HUM-006](#hum-006)

**Primary domain:** D14

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["derived", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["farm", "watershed", "region"], "temporal": ["year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `["material_flow", "recycled_input_fraction"]`

**Record type:** family

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HUM-003","domain":"D14","related_domains":["D13"],"record_type":"family","variants":["material_flow","recycled_input_fraction"],"secondary":["derived","pressure"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["pressure"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Physical material inputs, outputs and recycled fractions across a declared system.
- **Direct observations / derivation:** Mass balance by material, Mg/year and recycled/input fraction, excluding double counting.
- **Inference and limits:** Supports resource-flow comparison; recycled fraction does not demonstrate low total demand or low ecological impact.
- **Supporting indicators:** [EII:FUN-010](#fun-010), [EII:HUM-004](#hum-004), [EII:HUM-006](#hum-006).

<a id="hum-004"></a>

### EII:HUM-004 — Energy demand/return

**Definition:** Energy consumed and useful energy output relative to a stated investment.

**Direct observations / derivation:** Metered/embodied energy accounting, MJ/year and output/input ratio with system boundary.

**Inference and limits:** Supports energetic comparison; fuel mix, service delivered and lifecycle allocation must be retained.

**Display label:** Energy demand and return

**Display measurement:** Energy meters and lifecycle energy accounts. Metered/embodied energy accounting, MJ/year and output/input ratio with system boundary.

**Display interpretation:** Shows energy demand or energy returned for the investment. Energy sources and the services produced affect fair comparisons.

**Measurement origin:** Energy meters and lifecycle energy accounts

**Supporting indicators:** [EII:AGR-011](#agr-011); [EII:HUM-003](#hum-003); [EII:HUM-006](#hum-006)

**Primary domain:** D14

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "derived", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["farm", "watershed", "region"], "temporal": ["year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `["energy_demand", "energy_return_ratio"]`

**Record type:** family

**Candidate source routes:** `["amr", "iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context; IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HUM-004","domain":"D14","related_domains":["D13"],"record_type":"family","variants":["energy_demand","energy_return_ratio"],"secondary":["measured","derived","pressure"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["pressure"],"routes":["amr","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Energy consumed and useful energy output relative to a stated investment.
- **Direct observations / derivation:** Metered/embodied energy accounting, MJ/year and output/input ratio with system boundary.
- **Inference and limits:** Supports energetic comparison; fuel mix, service delivered and lifecycle allocation must be retained.
- **Supporting indicators:** [EII:AGR-011](#agr-011), [EII:HUM-003](#hum-003), [EII:HUM-006](#hum-006).

<a id="hum-005"></a>

### EII:HUM-005 — Water withdrawal/consumption

**Definition:** Water abstracted and water not returned within the declared system are distinct flows.

**Direct observations / derivation:** Meters and water balance, m³/year with source and return-flow timing.

**Inference and limits:** Supports water-pressure assessment; withdrawal is not equivalent to basin consumption or scarcity impact.

**Display label:** Water withdrawal and consumption

**Display measurement:** Water meters and supply/return-flow accounts. Meters and water balance, m³/year with source and return-flow timing.

**Display interpretation:** Shows water taken from sources and water not returned. Withdrawal and consumption have different effects on water availability.

**Measurement origin:** Water meters and supply/return-flow accounts

**Supporting indicators:** [EII:FUN-007](#fun-007); [EII:HYD-012](#hyd-012); [EII:HYD-017](#hyd-017)

**Primary domain:** D14

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["measured", "derived", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["farm", "watershed", "region"], "temporal": ["year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `["water_withdrawal", "water_consumption"]`

**Record type:** family

**Candidate source routes:** `["iot", "amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future); AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HUM-005","domain":"D14","related_domains":["D13"],"record_type":"family","variants":["water_withdrawal","water_consumption"],"secondary":["measured","derived","pressure"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["pressure"],"routes":["iot","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Water abstracted and water not returned within the declared system are distinct flows.
- **Direct observations / derivation:** Meters and water balance, m³/year with source and return-flow timing.
- **Inference and limits:** Supports water-pressure assessment; withdrawal is not equivalent to basin consumption or scarcity impact.
- **Supporting indicators:** [EII:FUN-007](#fun-007), [EII:HYD-012](#hyd-012), [EII:HYD-017](#hyd-017).

<a id="hum-006"></a>

### EII:HUM-006 — Lifecycle greenhouse-gas intensity

**Definition:** Method-defined greenhouse-gas emissions per functional unit over a declared lifecycle.

**Direct observations / derivation:** Activity data × versioned emission factors and GWP horizon, kg CO₂e/unit service/product.

**Inference and limits:** Supports climate-impact comparison; allocation, land-use change and omitted processes affect comparability.

**Display label:** Lifecycle greenhouse-gas emissions

**Display measurement:** Lifecycle activity records and published emission factors. Activity data × versioned emission factors and GWP horizon, kg CO₂e/unit service/product.

**Display interpretation:** Helps compare climate emissions per product or service. Results depend on which lifecycle stages and emissions are included.

**Measurement origin:** Lifecycle activity records and published emission factors

**Supporting indicators:** [EII:CYC-002](#cyc-002); [EII:CYC-003](#cyc-003); [EII:AGR-011](#agr-011); [EII:FUN-002](#fun-002)

**Primary domain:** D14

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["derived", "modelled", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["farm", "watershed", "region"], "temporal": ["year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HUM-006","domain":"D14","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived","modelled","pressure"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["pressure"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Method-defined greenhouse-gas emissions per functional unit over a declared lifecycle.
- **Direct observations / derivation:** Activity data × versioned emission factors and GWP horizon, kg CO₂e/unit service/product.
- **Inference and limits:** Supports climate-impact comparison; allocation, land-use change and omitted processes affect comparability.
- **Supporting indicators:** [EII:CYC-002](#cyc-002), [EII:CYC-003](#cyc-003), [EII:AGR-011](#agr-011), [EII:FUN-002](#fun-002).

<a id="hum-007"></a>

### EII:HUM-007 — Artificial light at night

**Definition:** Nighttime light exposure at the sensor or biological receptor.

**Direct observations / derivation:** Calibrated radiance/illuminance and spectrum, W/m²/sr or lux; declare viewing and time.

**Inference and limits:** Supports exposure assessment; satellite brightness does not directly represent organism-level dose or biological harm.

**Display label:** Artificial light at night

**Display measurement:** Field light sensors or suitable nighttime satellite observations. Calibrated radiance/illuminance and spectrum, W/m²/sr or lux; declare viewing and time.

**Display interpretation:** Shows artificial light exposure at night. Satellite brightness may differ from the light experienced by organisms.

**Measurement origin:** Field light sensors or suitable nighttime satellite observations

**Supporting indicators:** [EII:BIO-012](#bio-012); [EII:BIO-002](#bio-002); [EII:FUN-009](#fun-009)

**Primary domain:** D14

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["farm", "watershed", "region"], "temporal": ["year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HUM-007","domain":"D14","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","pressure"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["pressure"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Nighttime light exposure at the sensor or biological receptor.
- **Direct observations / derivation:** Calibrated radiance/illuminance and spectrum, W/m²/sr or lux; declare viewing and time.
- **Inference and limits:** Supports exposure assessment; satellite brightness does not directly represent organism-level dose or biological harm.
- **Supporting indicators:** [EII:BIO-012](#bio-012), [EII:BIO-002](#bio-002), [EII:FUN-009](#fun-009).

<a id="hum-008"></a>

### EII:HUM-008 — Anthropogenic noise exposure

**Definition:** Acoustic pressure spectrum and level attributable to declared human sources.

**Direct observations / derivation:** Calibrated sound records, dB referenced to stated medium/pressure; weighting and time interval explicit.

**Inference and limits:** Supports disturbance-exposure assessment; hearing ranges, backgrounds and source attribution affect biological interpretation.

**Display label:** Human-made noise

**Display measurement:** Field sound recordings and calibrated noise meters. Calibrated sound records, dB referenced to stated medium/pressure; weighting and time interval explicit.

**Display interpretation:** Shows exposure to human-made noise. Different species hear different frequencies and may respond differently.

**Measurement origin:** Field sound recordings and calibrated noise meters

**Supporting indicators:** [EII:BIO-012](#bio-012); [EII:BIO-002](#bio-002); [EII:FUN-009](#fun-009)

**Primary domain:** D14

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["farm", "watershed", "region"], "temporal": ["year"]}`

**Ecological purpose:** `["pressure"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["iot"]`

**Scientific reference keys:** `[]`

**Display source keys:** IoT (future)

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HUM-008","domain":"D14","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","pressure"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["pressure"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Acoustic pressure spectrum and level attributable to declared human sources.
- **Direct observations / derivation:** Calibrated sound records, dB referenced to stated medium/pressure; weighting and time interval explicit.
- **Inference and limits:** Supports disturbance-exposure assessment; hearing ranges, backgrounds and source attribution affect biological interpretation.
- **Supporting indicators:** [EII:BIO-012](#bio-012), [EII:BIO-002](#bio-002), [EII:FUN-009](#fun-009).

<a id="hum-009"></a>

### EII:HUM-009 — Resource import dependence

**Definition:** Fraction of specified resource demand supplied from outside a declared area/system.

**Direct observations / derivation:** Physical supply and demand accounts, % or mass/year with trade origin.

**Inference and limits:** Supports dependency assessment; imported-resource share alone does not determine environmental sustainability.

**Display label:** Dependence on imported resources

**Display measurement:** Supply, trade and resource-demand accounts. Physical supply and demand accounts, % or mass/year with trade origin.

**Display interpretation:** Shows reliance on resources from outside an area. Import dependence alone does not establish environmental sustainability.

**Measurement origin:** Supply, trade and resource-demand accounts

**Supporting indicators:** [EII:HUM-003](#hum-003); [EII:HUM-005](#hum-005); [EII:AGR-009](#agr-009)

**Primary domain:** D14

**Secondary domains:** `["D13"]`

**Classification dimensions:** `["derived", "context"]`

**Spatial/temporal dimensions:** `{"spatial": ["farm", "watershed", "region"], "temporal": ["year"]}`

**Ecological purpose:** `["context"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["amr"]`

**Scientific reference keys:** `[]`

**Display source keys:** AMRKB context

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:HUM-009","domain":"D14","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived","context"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["context"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fraction of specified resource demand supplied from outside a declared area/system.
- **Direct observations / derivation:** Physical supply and demand accounts, % or mass/year with trade origin.
- **Inference and limits:** Supports dependency assessment; imported-resource share alone does not determine environmental sustainability.
- **Supporting indicators:** [EII:HUM-003](#hum-003), [EII:HUM-005](#hum-005), [EII:AGR-009](#agr-009).

<a id="pb-001"></a>

### EII:PB-001 — Atmospheric CO₂/radiative forcing control variables

**Definition:** Version-specific climate control variables used by a cited boundary framework.

**Direct observations / derivation:** Global CO₂ concentration, ppm, and/or forcing, W/m², with reference baseline and threshold source.

**Inference and limits:** Supports framework-based climate-pressure comparison; do not treat local CO₂ or a farm footprint as a global boundary value.

**Display label:** Global carbon dioxide and climate forcing

**Display measurement:** Global air monitoring and climate-forcing models. Global CO₂ concentration, ppm, and/or forcing, W/m², with reference baseline and threshold source.

**Display interpretation:** Helps compare global climate pressures with a stated framework. Local carbon dioxide readings are not a global boundary measure.

**Measurement origin:** Global air monitoring and climate-forcing models

**Supporting indicators:** [EII:ATM-006](#atm-006); [EII:HUM-006](#hum-006); [EII:FUN-014](#fun-014)

**Primary domain:** D15

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "modelled", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["region", "planet"], "temporal": ["year", "decade"]}`

**Ecological purpose:** `["system_pressure", "threshold_comparison"]`

**Family / variant distinctions:** `["CO2_concentration", "radiative_forcing"]`

**Record type:** family

**Candidate source routes:** `[]`

**Scientific reference keys:** `[]`

**Display source keys:** Field/lab/model source to register

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:PB-001","domain":"D15","related_domains":[],"record_type":"family","variants":["CO2_concentration","radiative_forcing"],"secondary":["measured","modelled","pressure"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Version-specific climate control variables used by a cited boundary framework.
- **Direct observations / derivation:** Global CO₂ concentration, ppm, and/or forcing, W/m², with reference baseline and threshold source.
- **Inference and limits:** Supports framework-based climate-pressure comparison; do not treat local CO₂ or a farm footprint as a global boundary value.
- **Supporting indicators:** [EII:ATM-006](#atm-006), [EII:HUM-006](#hum-006), [EII:FUN-014](#fun-014).

<a id="pb-002"></a>

### EII:PB-002 — Biosphere genetic/functional integrity controls

**Definition:** Distinct framework-defined measures of genetic loss and functional alteration.

**Direct observations / derivation:** Named extinction-rate estimate and framework-specific functional control variable; record version and uncertainty.

**Inference and limits:** Supports global biosphere assessment; local richness cannot substitute for global extinction or functional alteration.

**Display label:** Large-scale biodiversity and function loss

**Display measurement:** Large-scale biodiversity monitoring and scientific models. Named extinction-rate estimate and framework-specific functional control variable; record version and uncertainty.

**Display interpretation:** Helps assess large-scale loss of biodiversity and ecosystem function. Local species counts cannot represent the whole global picture.

**Measurement origin:** Large-scale biodiversity monitoring and scientific models

**Supporting indicators:** [EII:BIO-016](#bio-016); [EII:FUN-001](#fun-001); [EII:FUN-014](#fun-014)

**Primary domain:** D15

**Secondary domains:** `[]`

**Classification dimensions:** `["modelled", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["region", "planet"], "temporal": ["year", "decade"]}`

**Ecological purpose:** `["system_pressure", "threshold_comparison"]`

**Family / variant distinctions:** `["genetic_integrity_control", "functional_integrity_control"]`

**Record type:** family

**Candidate source routes:** `[]`

**Scientific reference keys:** `[]`

**Display source keys:** Field/lab/model source to register

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:PB-002","domain":"D15","related_domains":[],"record_type":"family","variants":["genetic_integrity_control","functional_integrity_control"],"secondary":["modelled","pressure"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Distinct framework-defined measures of genetic loss and functional alteration.
- **Direct observations / derivation:** Named extinction-rate estimate and framework-specific functional control variable; record version and uncertainty.
- **Inference and limits:** Supports global biosphere assessment; local richness cannot substitute for global extinction or functional alteration.
- **Supporting indicators:** [EII:BIO-016](#bio-016), [EII:FUN-001](#fun-001), [EII:FUN-014](#fun-014).

<a id="pb-003"></a>

### EII:PB-003 — Biogeochemical N/P control variables

**Definition:** Version-specific human alteration of large-scale nitrogen/phosphorus flows.

**Direct observations / derivation:** Global/regional fixation, application or ocean-export budgets, mass/year, under cited framework.

**Inference and limits:** Supports nutrient-pressure comparison; farm surplus is not interchangeable with a global boundary control variable.

**Display label:** Large-scale nitrogen and phosphorus pressures

**Display measurement:** Large-scale nutrient-flow inventories and models. Global/regional fixation, application or ocean-export budgets, mass/year, under cited framework.

**Display interpretation:** Helps assess large-scale human changes to nitrogen and phosphorus flows. A farm nutrient surplus is a different measure.

**Measurement origin:** Large-scale nutrient-flow inventories and models

**Supporting indicators:** [EII:CYC-004](#cyc-004); [EII:CYC-007](#cyc-007); [EII:HYD-018](#hyd-018)

**Primary domain:** D15

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "modelled", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["region", "planet"], "temporal": ["year", "decade"]}`

**Ecological purpose:** `["system_pressure", "threshold_comparison"]`

**Family / variant distinctions:** `["N_control", "P_control"]`

**Record type:** family

**Candidate source routes:** `[]`

**Scientific reference keys:** `[]`

**Display source keys:** Field/lab/model source to register

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:PB-003","domain":"D15","related_domains":[],"record_type":"family","variants":["N_control","P_control"],"secondary":["derived","modelled","pressure"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Version-specific human alteration of large-scale nitrogen/phosphorus flows.
- **Direct observations / derivation:** Global/regional fixation, application or ocean-export budgets, mass/year, under cited framework.
- **Inference and limits:** Supports nutrient-pressure comparison; farm surplus is not interchangeable with a global boundary control variable.
- **Supporting indicators:** [EII:CYC-004](#cyc-004), [EII:CYC-007](#cyc-007), [EII:HYD-018](#hyd-018).

<a id="pb-004"></a>

### EII:PB-004 — Freshwater blue/green change controls

**Definition:** Framework-specific departures of surface flow and root-zone moisture from reference variability.

**Direct observations / derivation:** Spatially aggregated streamflow/soil-moisture anomalies under the cited version's procedure.

**Inference and limits:** Supports freshwater-change assessment; withdrawal, drought index and anomaly controls represent different concepts.

**Display label:** Large-scale river-flow and soil-moisture change

**Display measurement:** Large-scale river-flow and soil-moisture observations/models. Spatially aggregated streamflow/soil-moisture anomalies under the cited version's procedure.

**Display interpretation:** Helps assess large-scale changes in river flows and soil moisture. Water withdrawals and drought indices measure different things.

**Measurement origin:** Large-scale river-flow and soil-moisture observations/models

**Supporting indicators:** [EII:HYD-001](#hyd-001); [EII:HYD-006](#hyd-006); [EII:HUM-005](#hum-005)

**Primary domain:** D15

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "modelled", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["region", "planet"], "temporal": ["year", "decade"]}`

**Ecological purpose:** `["system_pressure", "threshold_comparison"]`

**Family / variant distinctions:** `["blue_water_change", "green_water_change"]`

**Record type:** family

**Candidate source routes:** `["drought"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS015

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:PB-004","domain":"D15","related_domains":[],"record_type":"family","variants":["blue_water_change","green_water_change"],"secondary":["derived","modelled","pressure"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":["drought"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Framework-specific departures of surface flow and root-zone moisture from reference variability.
- **Direct observations / derivation:** Spatially aggregated streamflow/soil-moisture anomalies under the cited version's procedure.
- **Inference and limits:** Supports freshwater-change assessment; withdrawal, drought index and anomaly controls represent different concepts.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:HYD-006](#hyd-006), [EII:HUM-005](#hum-005).

<a id="pb-005"></a>

### EII:PB-005 — Land-system change control variables

**Definition:** Framework-specific remaining forest/biome extent relative to reference.

**Direct observations / derivation:** Harmonised biome-specific land/forest maps and specified reference fractions.

**Inference and limits:** Supports land-system-pressure comparison; tree cover alone does not establish native forest integrity or an allocated regional boundary.

**Display label:** Forest and biome extent change

**Display measurement:** Biome/forest maps compared with a stated reference. Harmonised biome-specific land/forest maps and specified reference fractions.

**Display interpretation:** Helps assess changes in forest or biome extent. Tree cover alone does not show native forest condition.

**Measurement origin:** Biome/forest maps compared with a stated reference

**Supporting indicators:** [EII:DIS-004](#dis-004); [EII:DIS-005](#dis-005); [EII:BIO-005](#bio-005)

**Primary domain:** D15

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["region", "planet"], "temporal": ["year", "decade"]}`

**Ecological purpose:** `["system_pressure", "threshold_comparison"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["land"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS004, RS005, RS006, RS009

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:PB-005","domain":"D15","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","pressure"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":["land"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Framework-specific remaining forest/biome extent relative to reference.
- **Direct observations / derivation:** Harmonised biome-specific land/forest maps and specified reference fractions.
- **Inference and limits:** Supports land-system-pressure comparison; tree cover alone does not establish native forest integrity or an allocated regional boundary.
- **Supporting indicators:** [EII:DIS-004](#dis-004), [EII:DIS-005](#dis-005), [EII:BIO-005](#bio-005).

<a id="pb-006"></a>

### EII:PB-006 — Stratospheric ozone

**Definition:** Column ozone used with a specified global/reference comparison.

**Direct observations / derivation:** Validated atmospheric column retrieval/observations, Dobson units, with latitude/season.

**Inference and limits:** Supports stratospheric protection assessment; surface ozone is a distinct variable and local readings cannot substitute.

**Display label:** Stratospheric ozone

**Display measurement:** Satellite atmospheric retrievals and ozone monitoring instruments. Validated atmospheric column retrieval/observations, Dobson units, with latitude/season.

**Display interpretation:** Helps assess the ozone layer's protection. Ozone near the ground is a different environmental issue.

**Measurement origin:** Satellite atmospheric retrievals and ozone monitoring instruments

**Supporting indicators:** [EII:ATM-007](#atm-007); [EII:FUN-014](#fun-014); [EII:PB-001](#pb-001)

**Primary domain:** D15

**Secondary domains:** `[]`

**Classification dimensions:** `["measured", "derived"]`

**Spatial/temporal dimensions:** `{"spatial": ["region", "planet"], "temporal": ["year", "decade"]}`

**Ecological purpose:** `["system_pressure", "threshold_comparison"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `[]`

**Scientific reference keys:** `[]`

**Display source keys:** Field/lab/model source to register

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:PB-006","domain":"D15","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Column ozone used with a specified global/reference comparison.
- **Direct observations / derivation:** Validated atmospheric column retrieval/observations, Dobson units, with latitude/season.
- **Inference and limits:** Supports stratospheric protection assessment; surface ozone is a distinct variable and local readings cannot substitute.
- **Supporting indicators:** [EII:ATM-007](#atm-007), [EII:FUN-014](#fun-014), [EII:PB-001](#pb-001).

<a id="pb-007"></a>

### EII:PB-007 — Novel-entity releases/assessment coverage

**Definition:** Version-specific pollution pressure and capacity to assess/manage released substances.

**Direct observations / derivation:** Chemical release inventories, mass/time and declared assessment/coverage metrics.

**Inference and limits:** Supports pollution-governance screening based on empirical accounts; no universally interchangeable concentration threshold exists for all novel entities.

**Display label:** New chemical releases and assessment coverage

**Display measurement:** Chemical release inventories and assessment records. Chemical release inventories, mass/time and declared assessment/coverage metrics.

**Display interpretation:** Helps track releases of new chemicals and how well they are assessed. No single safe concentration applies to all substances.

**Measurement origin:** Chemical release inventories and assessment records

**Supporting indicators:** [EII:SOI-013](#soi-013); [EII:HYD-020](#hyd-020); [EII:AGR-003](#agr-003)

**Primary domain:** D15

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["region", "planet"], "temporal": ["year", "decade"]}`

**Ecological purpose:** `["system_pressure", "threshold_comparison"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `[]`

**Scientific reference keys:** `[]`

**Display source keys:** Field/lab/model source to register

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:PB-007","domain":"D15","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","pressure"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Version-specific pollution pressure and capacity to assess/manage released substances.
- **Direct observations / derivation:** Chemical release inventories, mass/time and declared assessment/coverage metrics.
- **Inference and limits:** Supports pollution-governance screening based on empirical accounts; no universally interchangeable concentration threshold exists for all novel entities.
- **Supporting indicators:** [EII:SOI-013](#soi-013), [EII:HYD-020](#hyd-020), [EII:AGR-003](#agr-003).

<a id="pb-008"></a>

### EII:PB-008 — Ocean acidification control variable

**Definition:** Version-specific ocean carbonate saturation relative to a stated reference.

**Direct observations / derivation:** Carbonate chemistry and computed aragonite saturation, dimensionless with reference fraction declared.

**Inference and limits:** Supports acidification-pressure assessment; local pH alone does not establish the global control variable or all biological effects.

**Display label:** Ocean acidification

**Display measurement:** Ocean chemistry observations and carbonate calculations. Carbonate chemistry and computed aragonite saturation, dimensionless with reference fraction declared.

**Display interpretation:** Helps assess ocean chemistry affecting shell formation. Local pH alone cannot establish the global boundary measure.

**Measurement origin:** Ocean chemistry observations and carbonate calculations

**Supporting indicators:** [EII:HYD-022](#hyd-022); [EII:HYD-015](#hyd-015); [EII:BIO-019](#bio-019)

**Primary domain:** D15

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["region", "planet"], "temporal": ["year", "decade"]}`

**Ecological purpose:** `["system_pressure", "threshold_comparison"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `["marine"]`

**Scientific reference keys:** `[]`

**Display source keys:** RS018

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:PB-008","domain":"D15","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","pressure"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":["marine"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Version-specific ocean carbonate saturation relative to a stated reference.
- **Direct observations / derivation:** Carbonate chemistry and computed aragonite saturation, dimensionless with reference fraction declared.
- **Inference and limits:** Supports acidification-pressure assessment; local pH alone does not establish the global control variable or all biological effects.
- **Supporting indicators:** [EII:HYD-022](#hyd-022), [EII:HYD-015](#hyd-015), [EII:BIO-019](#bio-019).

<a id="pb-009"></a>

### EII:PB-009 — Atmospheric aerosol loading control variable

**Definition:** Version-specific aerosol optical loading/distribution measure.

**Direct observations / derivation:** Validated aerosol optical depth or specified hemispheric contrast, dimensionless.

**Inference and limits:** Supports framework-based aerosol assessment; PM mass, optical depth and regional climate effects are not interchangeable.

**Display label:** Large-scale aerosol loading

**Display measurement:** Satellite aerosol observations and atmospheric analysis. Validated aerosol optical depth or specified hemispheric contrast, dimensionless.

**Display interpretation:** Helps assess large-scale airborne particle effects. Particle mass and their effect on sunlight are different measures.

**Measurement origin:** Satellite aerosol observations and atmospheric analysis

**Supporting indicators:** [EII:ATM-008](#atm-008); [EII:ATM-005](#atm-005); [EII:FUN-014](#fun-014)

**Primary domain:** D15

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "pressure"]`

**Spatial/temporal dimensions:** `{"spatial": ["region", "planet"], "temporal": ["year", "decade"]}`

**Ecological purpose:** `["system_pressure", "threshold_comparison"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `[]`

**Scientific reference keys:** `[]`

**Display source keys:** Field/lab/model source to register

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:PB-009","domain":"D15","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","pressure"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Version-specific aerosol optical loading/distribution measure.
- **Direct observations / derivation:** Validated aerosol optical depth or specified hemispheric contrast, dimensionless.
- **Inference and limits:** Supports framework-based aerosol assessment; PM mass, optical depth and regional climate effects are not interchangeable.
- **Supporting indicators:** [EII:ATM-008](#atm-008), [EII:ATM-005](#atm-005), [EII:FUN-014](#fun-014).

<a id="pb-010"></a>

### EII:PB-010 — Regional ecological threshold departure

**Definition:** Departure of a measured ecological variable from a justified regional threshold.

**Direct observations / derivation:** Named variable, reference, threshold derivation and uncertainty in compatible units; report sign/direction.

**Inference and limits:** Supports regional assessment; thresholds require local evidence and are not automatic downscalings of planetary boundaries.

**Display label:** Departure from regional ecological thresholds

**Display measurement:** Regional observations/models and a locally justified threshold. Named variable, reference, threshold derivation and uncertainty in compatible units; report sign/direction.

**Display interpretation:** Shows departure from a locally justified ecological threshold. Global thresholds cannot be transferred automatically to a region.

**Measurement origin:** Regional observations/models and a locally justified threshold

**Supporting indicators:** [EII:FUN-014](#fun-014); [EII:HYD-017](#hyd-017); [EII:FUN-013](#fun-013)

**Primary domain:** D15

**Secondary domains:** `[]`

**Classification dimensions:** `["derived", "modelled"]`

**Spatial/temporal dimensions:** `{"spatial": ["region", "planet"], "temporal": ["year", "decade"]}`

**Ecological purpose:** `["system_pressure", "threshold_comparison"]`

**Family / variant distinctions:** `[]`

**Record type:** indicator

**Candidate source routes:** `[]`

**Scientific reference keys:** `[]`

**Display source keys:** Field/lab/model source to register

**Research status:** curated_working_definition

**Earlier inventory v0.2.0 wording (historical):**

<!-- eii:{"id":"EII:PB-010","domain":"D15","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","modelled"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Departure of a measured ecological variable from a justified regional threshold.
- **Direct observations / derivation:** Named variable, reference, threshold derivation and uncertainty in compatible units; report sign/direction.
- **Inference and limits:** Supports regional assessment; thresholds require local evidence and are not automatic downscalings of planetary boundaries.
- **Supporting indicators:** [EII:FUN-014](#fun-014), [EII:HYD-017](#hyd-017), [EII:FUN-013](#fun-013).



## Historical research appendix — Trails4Soil

The following complete crosswalk retains its original provenance and provisional wording. Management-practice mappings are excluded from the active inventory and do not establish verified indicators or source bindings.

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



## Historical scientific supplements

Source editions below are retained separately. Earlier wording is not silently reconciled with current records. Classification guides, source registries, formulas, source references, family distinctions and exploratory examples retain their qualifications. Templates and maintenance rules are in the Research Protocol.



### Historical inventory v0.2.0 — SOC stock calculation example

### SOC stock calculation example

Using organic C concentration in g/kg, compatible fine-earth bulk density in g/cm³, layer thickness in cm and coarse-fragment volume fraction, a commonly used stock form is:

`SOC stock (Mg C/ha) = C (g/kg) × BD_fine (g/cm³) × thickness (cm) × (1 − coarse_fragment_volume_fraction) × 0.1`.

The density denominator and fragment correction must match: do not apply the correction twice if density already expresses dry fine-earth mass per total sample volume. Sum declared layers; use consistent/equivalent soil mass for repeated comparisons where density changes. Concentration, stock and stock-change rate remain separate variants/records. [FAO Annex 4](https://www.fao.org/fileadmin/user_upload/GSP/MRV/GSP_MRV_Protocol_A4_EN_002.pdf).



### Historical Inventory v0.2.0 appendices — Appendix B — Scientific reference and verification register

**Historical Inventory v0.2.0 appendices; original research status and qualifications retained.**

## Appendix B — Scientific reference and verification register

All definitions are curated working entries. A citation verifies only the specific documentary aspect described below, not every inference, local calibration or monitoring protocol. Uncited entries remain pending individual literature/protocol review. Frameworks guide coverage and terminology; formal EBV/ECV/SEEA equivalence has not been asserted. The 2023 planetary-boundary paper is a versioned conceptual reference; this inventory reports no current number of transgressed boundaries, current threshold values or automatic local allocations.

| Key | Primary/authoritative reference | Scope of documentary check |
|---|---|---|
| R01 | [USGS — Landsat Enhanced Vegetation Index](https://www.usgs.gov/landsat-missions/landsat-enhanced-vegetation-index) | Standard EVI formula and band/scaling context; documentary check, not local validation. |
| R02 | [USGS — Landsat Normalized Burn Ratio](https://www.usgs.gov/landsat-missions/landsat-normalized-burn-ratio) | NBR formula and product context; not universal severity thresholds. |
| R03 | [FAO — SOC stock calculation sub-protocol, Annex 4](https://www.fao.org/fileadmin/user_upload/GSP/MRV/GSP_MRV_Protocol_A4_EN_002.pdf) | SOC stock inputs and compatible density/coarse-fragment basis. |
| R04 | [EMBL-EBI — MGnify](https://www.ebi.ac.uk/about/teams/microbiome-informatics/mgnify/) | Taxonomic and functional-potential outputs, versioned pipelines; no project dataset accession bound. |
| R05 | [Vandeputte et al. (2017) — Quantitative microbiome profiling](https://www.nature.com/articles/nature24460) | Primary study on relative versus quantitative abundance; gut study supports the compositional measurement caution, not soil-specific effect claims. |
| R06 | [GEO BON — EBV strategy v2](https://geobon.org/downloads/governance-documents/Essential_Biodiversity_Variable_Strategy_v2.pdf) | Biodiversity observation framework; no claim that EII entries are certified EBVs. |
| R07 | [WMO/GCOS — About Essential Climate Variables](https://gcos.wmo.int/site/global-climate-observing-system-gcos/essential-climate-variables/about-essential-climate-variables) | Climate observation framework; no one-to-one ECV crosswalk established. |
| R08 | [UN — SEEA Ecosystem Accounting](https://seea.un.org/en/methodology/ecosystem-accounting) | Extent/condition/function accounting framework; EII composites remain locally specified. |
| R09 | [Richardson et al. (2023) — Earth beyond six of nine planetary boundaries](https://doi.org/10.1126/sciadv.adh2458) | Historical framework reference for control-variable families; not a current boundary-status assessment or a local allocation method. |
| R11 | [USGS — Normalized Difference Moisture Index](https://www.usgs.gov/landsat-missions/normalized-difference-moisture-index) | NIR/SWIR vegetation-moisture contrast and product context. |
| R12 | [USGS — Scaling Landsat Collection 2 Level 2 Data](https://www.usgs.gov/software/scaling-landsat-collection-2-level-2-data) | Reflectance scaling before vegetation-index calculation and thermal conversion. |
| R10 | [USGS — Dissolved Oxygen and Water](https://www.usgs.gov/water-science-school/science/dissolved-oxygen-and-water) | Dissolved oxygen as a water-quality variable and ecological context. |

Framework coverage notes: D1 draws on climate observation concepts (R07); D6 covers biodiversity observations (R06); D11 retains extent/condition/function distinctions (R08); D15 lists empirical variables and framework-defined comparisons (R09). Boundary thresholds and ecological reference states remain model/framework choices requiring justification; they are not interchangeable universal measurements.



### Historical Inventory v0.2.0 appendices — Appendix C — Cross-domain interpretation examples

**Historical Inventory v0.2.0 appendices; original research status and qualifications retained.**

## Appendix C — Cross-domain interpretation examples

| Question | Indicator combination | Required qualification |
|---|---|---|
| Does a greener canopy indicate better water status? | VEG-001, VEG-011, VEG-013, HYD-001, VEG-020, ATM-003 | Separate leaf area, chlorophyll, water access and atmospheric demand; calibrate by species and season. |
| Is carbon actually accumulating? | SOI-005 stock variant, SOI-002, SOI-014, FUN-002, CYC-001 | Repeat compatible stocks with uncertainty, account for depth/mass, export and gas fluxes; SOC % alone is insufficient. |
| Are nitrogen-cycling genes expressing realised function? | MIC-010/011/012, MIC-022, MIC-023, CYC-004/005, CYC-002 | DNA → transcription → process are distinct observations; sample together and measure substrate/environment. |
| Does a technical agricultural intervention improve outcomes? | AMRKB method context; FUN-004, AGR-001/002, SOI-003/005, HYD-018, BIO-008 | Compare matched controls over time; retain trade-offs and confounders rather than presuming benefit from a method label. |
| Does mapped connectivity support biological movement? | BIO-007, LAN-004, BIO-015, INT-007, BIO-016 | Validate pathways with movement/genetic evidence and demographic context; spatial similarity is insufficient. |
| Has a disturbed ecosystem recovered? | DIS-009, RES-001/002/005, VEG-017, BIO-002, FUN-001, MIC-024 | Use explicit reference conditions and multiple responses; greenness recovery alone is narrow evidence. |



### Historical Register pair v0.2.1 scientific supplements — Classifications

**Historical Register pair v0.2.1 scientific supplements; original research status and qualifications retained.**

## Classifications

The 15 domains organise the main register. This table adds how the indicator is obtained, the scales where it is commonly used, and its ecological purpose.

The listed scales are guides. A soil sample, sensor reading and satellite pixel represent different areas and times; they need suitable methods before being compared. Genetic potential, gene expression and actual process rates also remain different kinds of evidence.

| Indicator | How it is obtained | Typical spatial scale | Typical time scale | Ecological use |
|---|---|---|---|---|
| <small>[ATM-001 — Air temperature](#atm-001)</small> | Direct measurement | site, landscape, region | hour, day, season, year | Condition |
| <small>[ATM-002 — Rainfall and snowfall](#atm-002)</small> | Direct measurement | site, landscape, region | hour, day, season, year | Condition |
| <small>[ATM-003 — Air humidity and drying demand](#atm-003)</small> | Direct measurement, Calculation | site, landscape, region | hour, day, season, year | Condition |
| <small>[ATM-004 — Light for photosynthesis](#atm-004)</small> | Direct measurement | site, landscape, region | hour, day, season, year | Condition |
| <small>[ATM-005 — Wind speed and direction](#atm-005)</small> | Direct measurement | site, landscape, region | hour, day, season, year | Condition |
| <small>[ATM-006 — Atmospheric CO₂ concentration](#atm-006)</small> | Direct measurement | site, landscape, region | hour, day, season, year | Condition |
| <small>[ATM-007 — Ozone exposure](#atm-007)</small> | Direct measurement, Calculation, Environmental pressure | site, landscape, region | hour, day, season, year | Environmental pressure |
| <small>[ATM-008 — Fine airborne particles](#atm-008)</small> | Direct measurement, Environmental pressure | site, landscape, region | hour, day, season, year | Environmental pressure |
| <small>[ATM-009 — Snow cover and stored water](#atm-009)</small> | Direct measurement, Calculation | site, landscape, region | hour, day, season, year | Condition |
| <small>[DIS-006 — Air temperature and rainfall](#dis-006)</small> | Direct measurement | site, landscape, region | hour, day, season, year | Condition |
| <small>[DIS-007 — Drought and dryness indices](#dis-007)</small> | Calculation, Model estimate | site, landscape, region | hour, day, season, year | Condition |
| <small>[DIS-008 — Heatwave and frost frequency](#dis-008)</small> | Calculation | site, landscape, region | hour, day, season, year | Condition |
| <small>[HYD-003 — Land surface temperature](#hyd-003)</small> | Calculation, Indirect sign | site, landscape, region | hour, day, season, year | Condition |
| <small>[TER-004 — Solar radiation](#ter-004)</small> | Direct measurement, Model estimate | site, landscape, region | hour, day, season, year | Condition |
| <small>[DIS-011 — Radar-detected flooding and change](#dis-011)</small> | Calculation, Indirect sign | site, watershed, region | hour, day, season, year | Condition |
| <small>[HYD-001 — Soil moisture](#hyd-001)</small> | Direct measurement, Model estimate | site, watershed, region | hour, day, season, year | Condition |
| <small>[HYD-006 — River flow](#hyd-006)</small> | Direct measurement, Calculation | site, watershed, region | hour, day, season, year | Condition |
| <small>[HYD-007 — Groundwater level and recharge](#hyd-007)</small> | Direct measurement, Model estimate | site, watershed, region | hour, day, season, year | Condition |
| <small>[HYD-008 — Flood area and frequency](#hyd-008)</small> | Calculation, Model estimate | site, watershed, region | hour, day, season, year | Condition |
| <small>[HYD-009 — Water cloudiness and suspended sediment](#hyd-009)</small> | Direct measurement, Indirect sign | site, watershed, region | hour, day, season, year | Condition |
| <small>[HYD-010 — Water nutrient concentrations](#hyd-010)</small> | Direct measurement, Environmental pressure | site, watershed, region | hour, day, season, year | Environmental pressure |
| <small>[HYD-011 — Water salts and acidity](#hyd-011)</small> | Direct measurement | site, watershed, region | hour, day, season, year | Condition |
| <small>[HYD-012 — Evaporation and transpiration](#hyd-012)</small> | Direct measurement, Model estimate, Process measurement | site, watershed, region | hour, day, season, year | Ecosystem process |
| <small>[HYD-013 — Dissolved oxygen](#hyd-013)</small> | Direct measurement | site, watershed, region | hour, day, season, year | Condition |
| <small>[HYD-014 — Water chlorophyll-a](#hyd-014)</small> | Direct measurement, Indirect sign | site, watershed, region | hour, day, season, year | Condition |
| <small>[HYD-015 — Water temperature](#hyd-015)</small> | Direct measurement | site, watershed, region | hour, day, season, year | Condition |
| <small>[HYD-016 — Surface-water presence and duration](#hyd-016)</small> | Calculation | site, watershed, region | hour, day, season, year | Condition |
| <small>[HYD-017 — Ecological flow shortfall](#hyd-017)</small> | Calculation, Environmental pressure | site, watershed, region | hour, day, season, year | Environmental pressure |
| <small>[HYD-018 — Nutrients carried by water](#hyd-018)</small> | Calculation, Process measurement | site, watershed, region | hour, day, season, year | Ecosystem process |
| <small>[HYD-019 — Faecal indicator bacteria](#hyd-019)</small> | Direct measurement, Indirect sign | sample, community | sample date, season, year | Condition |
| <small>[HYD-020 — Chemical residues in water](#hyd-020)</small> | Direct measurement, Environmental pressure | site, watershed, region | hour, day, season, year | Environmental pressure |
| <small>[HYD-021 — Water clarity](#hyd-021)</small> | Direct measurement, Indirect sign | site, watershed, region | hour, day, season, year | Condition |
| <small>[HYD-022 — Ocean carbonate chemistry](#hyd-022)</small> | Direct measurement, Calculation | site, watershed, region | hour, day, season, year | Condition |
| <small>[TER-005 — Topographic wetness index](#ter-005)</small> | Calculation, Indirect sign | site, watershed, region | hour, day, season, year | Condition |
| <small>[TER-006 — Runoff pathways](#ter-006)</small> | Calculation, Model estimate | site, watershed, region | hour, day, season, year | Condition |
| <small>[HYD-004 — Infiltration rate](#hyd-004)</small> | Direct measurement, Process measurement | sample, plot | event, season, year | Ecosystem process |
| <small>[HYD-005 — Soil water storage](#hyd-005)</small> | Direct measurement, Calculation | sample, plot | event, season, year | Condition |
| <small>[SOI-001 — Soil texture](#soi-001)</small> | Direct measurement | sample, plot | event, season, year | Condition |
| <small>[SOI-002 — Soil density and compaction](#soi-002)</small> | Direct measurement | sample, plot | event, season, year | Condition |
| <small>[SOI-003 — Soil aggregate stability](#soi-003)</small> | Direct measurement | sample, plot | event, season, year | Condition |
| <small>[SOI-004 — Soil pore space](#soi-004)</small> | Direct measurement, Calculation | sample, plot | event, season, year | Condition |
| <small>[SOI-011 — Soil temperature](#soi-011)</small> | Direct measurement | sample, plot | event, season, year | Condition |
| <small>[SOI-012 — Soil erosion rate](#soi-012)</small> | Direct measurement, Model estimate, Process measurement | sample, plot | event, season, year | Ecosystem process |
| <small>[SOI-014 — Stones and soil depth](#soi-014)</small> | Direct measurement | sample, plot | event, season, year | Condition |
| <small>[SOI-015 — Water movement through saturated soil](#soi-015)</small> | Direct measurement, Process measurement | sample, plot | event, season, year | Ecosystem process |
| <small>[SOI-016 — Soil water tension](#soi-016)</small> | Direct measurement | sample, plot | event, season, year | Condition |
| <small>[SOI-017 — Large soil pores](#soi-017)</small> | Direct measurement, Calculation | sample, plot | event, season, year | Condition |
| <small>[TER-007 — Surface roughness](#ter-007)</small> | Calculation | sample, plot | event, season, year | Condition |
| <small>[TER-009 — Erosion channels](#ter-009)</small> | Direct observation, Calculation | sample, plot | event, season, year | Condition |
| <small>[SOI-005 — Soil organic carbon](#soi-005)</small> | Direct measurement, Calculation | sample, plot | season, year | Condition |
| <small>[SOI-006 — Soil pH](#soi-006)</small> | Direct measurement | sample, plot | season, year | Condition |
| <small>[SOI-007 — Soil salinity](#soi-007)</small> | Direct measurement, Indirect sign | sample, plot | season, year | Condition |
| <small>[SOI-008 — Available soil nutrients](#soi-008)</small> | Direct measurement | sample, plot | season, year | Condition |
| <small>[SOI-009 — Nutrient-holding capacity](#soi-009)</small> | Direct measurement | sample, plot | season, year | Condition |
| <small>[SOI-013 — Soil contaminants](#soi-013)</small> | Direct measurement, Environmental pressure | sample, plot | season, year | Environmental pressure |
| <small>[SOI-018 — Total soil nitrogen and carbon:nitrogen ratio](#soi-018)</small> | Direct measurement, Calculation | sample, plot | season, year | Condition |
| <small>[SOI-019 — Soil sodium indices](#soi-019)</small> | Calculation, Environmental pressure | sample, plot | season, year | Environmental pressure |
| <small>[SOI-020 — Soil mineral carbon](#soi-020)</small> | Direct measurement, Calculation | sample, plot | season, year | Condition |
| <small>[SOI-021 — Soil organic-carbon fractions](#soi-021)</small> | Direct measurement | sample, plot | season, year | Condition |
| <small>[SOI-022 — Potentially available contaminants](#soi-022)</small> | Direct measurement, Indirect sign | sample, plot | season, year | Condition |
| <small>[SOI-023 — Soil oxidation–reduction conditions](#soi-023)</small> | Direct measurement, Indirect sign | sample, plot | season, year | Condition |
| <small>[MIC-001 — Bacterial community](#mic-001)</small> | Calculation | sample, community | sample date, season, year | Condition |
| <small>[MIC-002 — Archaeal community](#mic-002)</small> | Calculation | sample, community | sample date, season, year | Condition |
| <small>[MIC-003 — Fungal community](#mic-003)</small> | Calculation | sample, community | sample date, season, year | Condition |
| <small>[MIC-004 — Protist community](#mic-004)</small> | Calculation | sample, community | sample date, season, year | Condition |
| <small>[MIC-005 — Microbial diversity within a sample](#mic-005)</small> | Calculation | sample, community | sample date, season, year | Condition |
| <small>[MIC-006 — Microbial differences between samples](#mic-006)</small> | Calculation | sample, community | sample date, season, year | Condition |
| <small>[MIC-007 — Microbial biomass](#mic-007)</small> | Direct measurement | sample, plot, community | event, season, year | Condition |
| <small>[MIC-008 — Fungal:bacterial ratio](#mic-008)</small> | Calculation, Indirect sign | sample, community | sample date, season, year | Condition |
| <small>[MIC-019 — Soil enzyme activity](#mic-019)</small> | Direct measurement, Process measurement | sample | laboratory test period, sample date | Ecosystem process |
| <small>[MIC-020 — Microbial changes across land uses](#mic-020)</small> | Calculation | sample, community | sample date, season, year | Condition |
| <small>[MIC-021 — Microbial similarity across places](#mic-021)</small> | Calculation, Model estimate | sample, community | sample date, season, year | Condition |
| <small>[MIC-022 — Microbial gene expression](#mic-022)</small> | Calculation, Indirect sign | sample, community | sample date, season, year | Condition |
| <small>[MIC-025 — Microbial numbers](#mic-025)</small> | Direct measurement, Calculation | sample, community | sample date, season, year | Condition |
| <small>[MIC-026 — Soil animal numbers and biomass](#mic-026)</small> | Direct measurement | sample, plot, community | event, season, year | Condition |
| <small>[MIC-027 — Nematode feeding groups](#mic-027)</small> | Calculation | sample, community | sample date, season, year | Condition |
| <small>[MIC-028 — Microbial protein profile](#mic-028)</small> | Calculation, Indirect sign | sample, community | sample date, season, year | Condition |
| <small>[MIC-029 — Biological metabolite profile](#mic-029)</small> | Direct measurement, Calculation | sample, community | sample date, season, year | Condition |
| <small>[MIC-030 — Microbial carbon-use efficiency](#mic-030)</small> | Calculation, Process measurement | sample, community | sample date, season, year | Ecosystem process |
| <small>[SOI-010 — Soil respiration](#soi-010)</small> | Direct measurement, Process measurement | sample, plot, community | event, season, year | Ecosystem process |
| <small>[BIO-001 — Species richness](#bio-001)</small> | Calculation | sample, community | sample date, season, year | Condition |
| <small>[BIO-002 — Species numbers and occupancy](#bio-002)</small> | Direct observation, Model estimate | sample, community | sample date, season, year | Condition |
| <small>[BIO-003 — Species diversity indices](#bio-003)</small> | Calculation | sample, community | sample date, season, year | Condition |
| <small>[BIO-004 — Trait diversity](#bio-004)</small> | Calculation | sample, community | sample date, season, year | Condition |
| <small>[BIO-005 — Habitat area and condition](#bio-005)</small> | Calculation, Model estimate | organism, population, community, landscape | season, year | Condition |
| <small>[BIO-010 — Invasive species presence and spread](#bio-010)</small> | Direct observation, Calculation | sample, community | sample date, season, year | Condition |
| <small>[BIO-011 — Species of conservation interest](#bio-011)</small> | Direct observation | sample, community | sample date, season, year | Condition |
| <small>[BIO-012 — Biological sounds](#bio-012)</small> | Calculation, Indirect sign | organism, population, community, landscape | season, year | Condition |
| <small>[BIO-014 — Environmental DNA detections](#bio-014)</small> | Direct observation, Calculation | sample, community | sample date, season, year | Condition |
| <small>[BIO-015 — Population genetic diversity](#bio-015)</small> | Calculation | sample, community | sample date, season, year | Condition |
| <small>[BIO-016 — Population growth and survival](#bio-016)</small> | Direct measurement, Model estimate, Process measurement | sample, community | sample date, season, year | Ecosystem process |
| <small>[BIO-017 — Typical community traits](#bio-017)</small> | Calculation | sample, community | sample date, season, year | Condition |
| <small>[BIO-018 — Freshwater invertebrate community](#bio-018)</small> | Direct observation, Calculation | sample, community | sample date, season, year | Condition |
| <small>[BIO-019 — Live coral cover and bleaching](#bio-019)</small> | Direct measurement | organism, population, community, landscape | season, year | Condition |
| <small>[BIO-020 — Mangrove area and condition](#bio-020)</small> | Calculation, Direct measurement | organism, population, community, landscape | season, year | Condition |
| <small>[DIS-012 — Detailed spectral signatures](#dis-012)</small> | Calculation, Indirect sign | organism, plot, landscape | day, season, year | Condition |
| <small>[HYD-002 — Canopy moisture index (NDMI)](#hyd-002)</small> | Calculation, Indirect sign | organism, plot, landscape | day, season, year | Condition |
| <small>[TER-010 — Tree height](#ter-010)</small> | Direct measurement, Calculation | organism, plot | event, season, year | Condition |
| <small>[TER-011 — Canopy volume](#ter-011)</small> | Calculation, Indirect sign | organism, plot | event, season, year | Condition |
| <small>[TER-012 — Canopy gaps and crown cover](#ter-012)</small> | Calculation | organism, plot, landscape | day, season, year | Condition |
| <small>[TER-013 — Vegetation layers](#ter-013)</small> | Calculation, Indirect sign | organism, plot, landscape | day, season, year | Condition |
| <small>[VEG-001 — Vegetation greenness (NDVI)](#veg-001)</small> | Calculation, Indirect sign | organism, plot, landscape | day, season, year | Condition |
| <small>[VEG-002 — Green vegetation index (GNDVI)](#veg-002)</small> | Calculation, Indirect sign | organism, plot, landscape | day, season, year | Condition |
| <small>[VEG-003 — Red-edge vegetation index (NDRE)](#veg-003)</small> | Calculation, Indirect sign | organism, plot, landscape | day, season, year | Condition |
| <small>[VEG-004 — Soil-adjusted vegetation index (SAVI)](#veg-004)</small> | Calculation, Indirect sign | organism, plot, landscape | day, season, year | Condition |
| <small>[VEG-005 — Enhanced vegetation index (EVI)](#veg-005)</small> | Calculation, Indirect sign | organism, plot, landscape | day, season, year | Condition |
| <small>[VEG-006 — Green–red vegetation index (GRVI)](#veg-006)</small> | Calculation, Indirect sign | organism, plot, landscape | day, season, year | Condition |
| <small>[VEG-007 — Excess green (ExG)](#veg-007)</small> | Calculation, Indirect sign | organism, plot, landscape | day, season, year | Condition |
| <small>[VEG-008 — Visible vegetation index (VARI)](#veg-008)</small> | Calculation, Indirect sign | organism, plot, landscape | day, season, year | Condition |
| <small>[VEG-009 — Green leaf index (GLI)](#veg-009)</small> | Calculation, Indirect sign | organism, plot, landscape | day, season, year | Condition |
| <small>[VEG-010 — RGB vegetation index (RGBVI)](#veg-010)</small> | Calculation, Indirect sign | organism, plot, landscape | day, season, year | Condition |
| <small>[VEG-011 — Leaf Area Index (LAI)](#veg-011)</small> | Direct measurement, Model estimate | organism, plot, landscape | day, season, year | Condition |
| <small>[VEG-012 — Vegetation cover](#veg-012)</small> | Direct observation, Calculation | organism, plot, landscape | day, season, year | Condition |
| <small>[VEG-013 — Chlorophyll content](#veg-013)</small> | Direct measurement, Model estimate | organism, plot, landscape | day, season, year | Condition |
| <small>[VEG-014 — Above-ground biomass](#veg-014)</small> | Direct measurement, Model estimate | organism, plot, landscape | day, season, year | Condition |
| <small>[VEG-015 — Plant water stress and canopy temperature](#veg-015)</small> | Calculation, Indirect sign | organism, plot, landscape | day, season, year | Condition |
| <small>[VEG-016 — Seasonal plant timing](#veg-016)</small> | Direct observation, Calculation | organism, plot, landscape | day, season, year | Condition |
| <small>[VEG-017 — Plant species and crop varieties](#veg-017)</small> | Direct observation, Calculation | sample, community | sample date, season, year | Condition |
| <small>[VEG-018 — Absorbed photosynthetic light](#veg-018)</small> | Direct measurement, Model estimate | organism, plot, landscape | day, season, year | Condition |
| <small>[VEG-019 — Chlorophyll fluorescence](#veg-019)</small> | Calculation, Indirect sign | organism, plot, landscape | day, season, year | Condition |
| <small>[VEG-020 — Plant water status and leaf gas exchange](#veg-020)</small> | Direct measurement, Process measurement | organism, plot | event, season, year | Ecosystem process |
| <small>[VEG-021 — Plant deaths and new establishment](#veg-021)</small> | Direct measurement, Process measurement | organism, plot, landscape | day, season, year | Ecosystem process |
| <small>[VEG-022 — Root mass and depth](#veg-022)</small> | Direct measurement | organism, plot, landscape | day, season, year | Condition |
| <small>[BIO-008 — Pollinator numbers and flower visits](#bio-008)</small> | Direct measurement, Process measurement | organism, community, plot | event, season | Ecosystem process |
| <small>[BIO-009 — Predation and pest control](#bio-009)</small> | Direct measurement, Process measurement | organism, community, plot | event, season | Ecosystem process |
| <small>[BIO-013 — Food webs and ecological networks](#bio-013)</small> | Calculation, Model estimate | sample, community | sample date, season, year | Condition |
| <small>[INT-001 — Pollen delivery and pollen limitation](#int-001)</small> | Direct measurement, Process measurement | organism, community, plot | event, season | Ecosystem process |
| <small>[INT-002 — Fruit and seed formation](#int-002)</small> | Direct measurement, Calculation | organism, community, plot | event, season | Condition |
| <small>[INT-003 — Plant consumption by herbivores](#int-003)</small> | Direct measurement, Process measurement | organism, community, plot | event, season | Ecosystem process |
| <small>[INT-004 — Competition between organisms](#int-004)</small> | Calculation, Process measurement | organism, community, plot | event, season | Ecosystem process |
| <small>[INT-005 — Benefits between organisms](#int-005)</small> | Calculation, Process measurement | organism, community, plot | event, season | Ecosystem process |
| <small>[INT-006 — Nutrient transfer through root fungi](#int-006)</small> | Direct measurement, Process measurement | sample, community | sample date, season, year | Ecosystem process |
| <small>[INT-007 — Seed dispersal and removal](#int-007)</small> | Direct measurement, Process measurement | sample, community | sample date, season, year | Ecosystem process |
| <small>[INT-008 — Diet and feeding relationships](#int-008)</small> | Direct measurement, Calculation | sample, community | sample date, season, year | Condition |
| <small>[INT-009 — Disease suppression tests](#int-009)</small> | Direct measurement, Process measurement | sample, community | sample date, season, year | Ecosystem process |
| <small>[MIC-014 — Root-associated fungi](#mic-014)</small> | Direct measurement, Calculation | sample, community | sample date, season, year | Condition |
| <small>[MIC-015 — Microbes around roots](#mic-015)</small> | Calculation | sample, community | sample date, season, year | Condition |
| <small>[MIC-016 — Potential harmful or beneficial microbes](#mic-016)</small> | Calculation, Estimate from evidence | sample, community | sample date, season, year | Condition |
| <small>[CYC-001 — Net ecosystem carbon dioxide exchange](#cyc-001)</small> | Direct measurement, Calculation, Process measurement | sample, plot, ecosystem, watershed | hour, season, year | Ecosystem process |
| <small>[CYC-002 — Nitrous oxide exchange](#cyc-002)</small> | Direct measurement, Process measurement | sample, plot, ecosystem, watershed | hour, season, year | Ecosystem process |
| <small>[CYC-003 — Methane exchange](#cyc-003)</small> | Direct measurement, Process measurement | sample, plot, ecosystem, watershed | hour, season, year | Ecosystem process |
| <small>[CYC-004 — Biological nitrogen-fixation rate](#cyc-004)</small> | Direct measurement, Process measurement | sample, community | sample date, season, year | Ecosystem process |
| <small>[CYC-005 — Denitrification rate](#cyc-005)</small> | Direct measurement, Process measurement | sample, plot, ecosystem, watershed | hour, season, year | Ecosystem process |
| <small>[CYC-006 — Phosphorus release from organic matter](#cyc-006)</small> | Direct measurement, Process measurement | sample, plot, ecosystem, watershed | hour, season, year | Ecosystem process |
| <small>[CYC-007 — Nitrogen and phosphorus balance](#cyc-007)</small> | Calculation, Process measurement | sample, plot, ecosystem, watershed | hour, season, year | Ecosystem process |
| <small>[CYC-008 — Nutrient recovery before leaf fall](#cyc-008)</small> | Calculation, Process measurement | sample, plot, ecosystem, watershed | hour, season, year | Ecosystem process |
| <small>[CYC-009 — Pollutant transformation](#cyc-009)</small> | Direct measurement, Process measurement | sample, plot, ecosystem, watershed | hour, season, year | Ecosystem process |
| <small>[CYC-010 — Dissolved organic carbon export](#cyc-010)</small> | Calculation, Process measurement | sample, plot, ecosystem, watershed | hour, season, year | Ecosystem process |
| <small>[FUN-002 — Carbon storage change](#fun-002)</small> | Calculation, Process measurement | sample, plot, ecosystem, watershed | hour, season, year | Ecosystem process |
| <small>[FUN-003 — Nutrient retention and leaching](#fun-003)</small> | Direct measurement, Model estimate, Process measurement | sample, plot, ecosystem, watershed | hour, season, year | Ecosystem process |
| <small>[MIC-009 — Carbon-breakdown genes](#mic-009)</small> | Calculation, Estimate from evidence | sample, community | sample date, season, year | Condition |
| <small>[MIC-010 — Nitrogen-fixation genes](#mic-010)</small> | Calculation, Estimate from evidence | sample, community | sample date, season, year | Condition |
| <small>[MIC-011 — Nitrification genes](#mic-011)</small> | Calculation, Estimate from evidence | sample, community | sample date, season, year | Condition |
| <small>[MIC-012 — Denitrification genes](#mic-012)</small> | Calculation, Estimate from evidence | sample, community | sample date, season, year | Condition |
| <small>[MIC-013 — Phosphorus-acquisition genes](#mic-013)</small> | Calculation, Estimate from evidence | sample, community | sample date, season, year | Condition |
| <small>[MIC-018 — Pollutant-breakdown genes](#mic-018)</small> | Calculation, Estimate from evidence | sample, community | sample date, season, year | Condition |
| <small>[MIC-023 — Nitrogen transformation rates](#mic-023)</small> | Direct measurement, Process measurement | sample, plot, ecosystem, watershed | hour, season, year | Ecosystem process |
| <small>[MIC-024 — Litter decomposition](#mic-024)</small> | Direct measurement, Calculation, Process measurement | sample, plot, ecosystem | day, season, year | Ecosystem process |
| <small>[BIO-006 — Habitat fragmentation](#bio-006)</small> | Calculation | landscape, watershed, region | event, year, decade | Condition |
| <small>[BIO-007 — Habitat connectivity](#bio-007)</small> | Calculation, Model estimate | sample, community | sample date, season, year | Condition |
| <small>[DIS-004 — Land cover and land use](#dis-004)</small> | Calculation, Background information | landscape, watershed, region | event, year, decade | Background information |
| <small>[DIS-005 — Land-cover change rate](#dis-005)</small> | Calculation, Environmental pressure | landscape, watershed, region | event, year, decade | Environmental pressure |
| <small>[FUN-008 — Field margins and hedgerows](#fun-008)</small> | Direct observation, Calculation | landscape, watershed, region | event, year, decade | Condition |
| <small>[LAN-001 — Habitat edges and interior area](#lan-001)</small> | Calculation | landscape, watershed, region | event, year, decade | Condition |
| <small>[LAN-002 — Landscape mix and diversity](#lan-002)</small> | Calculation | landscape, watershed, region | event, year, decade | Condition |
| <small>[LAN-003 — Streamside vegetation buffers](#lan-003)</small> | Calculation | landscape, watershed, region | event, year, decade | Condition |
| <small>[LAN-004 — Movement barriers](#lan-004)</small> | Calculation, Model estimate, Environmental pressure | landscape, watershed, region | event, year, decade | Environmental pressure |
| <small>[LAN-005 — Burned or converted habitat area](#lan-005)</small> | Calculation, Environmental pressure | landscape, watershed, region | event, year, decade | Environmental pressure |
| <small>[LAN-006 — Terrain position and shape](#lan-006)</small> | Calculation, Background information | landscape, watershed, region | event, year, decade | Background information |
| <small>[TER-001 — Ground elevation](#ter-001)</small> | Direct measurement, Calculation | landscape, watershed, region | event, year, decade | Condition |
| <small>[TER-002 — Slope gradient](#ter-002)</small> | Calculation, Background information | landscape, watershed, region | event, year, decade | Background information |
| <small>[TER-003 — Slope direction](#ter-003)</small> | Calculation, Background information | landscape, watershed, region | event, year, decade | Background information |
| <small>[TER-008 — Terrace shape and wall condition](#ter-008)</small> | Direct measurement, Background information | landscape, watershed, region | event, year, decade | Background information |
| <small>[TER-014 — Ground and canopy change](#ter-014)</small> | Calculation | landscape, watershed, region | event, year, decade | Condition |
| <small>[FUN-001 — Plant carbon production (GPP/NPP)](#fun-001)</small> | Model estimate, Process measurement | plot, ecosystem, watershed | season, year | Ecosystem process |
| <small>[FUN-012 — Soil-health score](#fun-012)</small> | Combined score | plot, ecosystem, watershed | season, year | Condition assessment, Assessment |
| <small>[FUN-013 — Ecosystem-condition score](#fun-013)</small> | Combined score, Model estimate | sample, community | sample date, season, year | Condition assessment, Assessment |
| <small>[FUN-015 — Net ecosystem production–respiration balance](#fun-015)</small> | Calculation, Process measurement | plot, ecosystem, watershed | season, year | Ecosystem process |
| <small>[FUN-016 — Food-chain transfer efficiency](#fun-016)</small> | Calculation, Process measurement | sample, community | sample date, season, year | Ecosystem process |
| <small>[FUN-017 — Combined ecosystem functions](#fun-017)</small> | Combined score | plot, ecosystem, watershed | season, year | Condition assessment, Assessment |
| <small>[FUN-018 — Water purification](#fun-018)</small> | Calculation, Process measurement | plot, ecosystem, watershed | season, year | Ecosystem process |
| <small>[FUN-019 — Ecosystem cooling](#fun-019)</small> | Calculation, Process measurement | plot, ecosystem, watershed | season, year | Ecosystem process |
| <small>[FUN-020 — Soil-function shortfalls](#fun-020)</small> | Calculation | plot, ecosystem, watershed | season, year | Condition |
| <small>[DIS-001 — Burn ratio (NBR)](#dis-001)</small> | Calculation, Indirect sign | plot, ecosystem, landscape | event, year, decade | Response to disturbance, Restoration monitoring |
| <small>[DIS-002 — Fire fuel load and arrangement](#dis-002)</small> | Direct measurement, Model estimate | plot, ecosystem, landscape | event, year, decade | Response to disturbance, Restoration monitoring |
| <small>[DIS-003 — Fire events and recurrence](#dis-003)</small> | Direct observation, Calculation | plot, ecosystem, landscape | event, year, decade | Response to disturbance, Restoration monitoring |
| <small>[DIS-009 — Recovery after disturbance](#dis-009)</small> | Calculation, Model estimate | sample, community | sample date, season, year | Response to disturbance, Restoration monitoring |
| <small>[DIS-010 — Future climate exposure and suitability](#dis-010)</small> | Model estimate, Future estimate | plot, ecosystem, landscape | event, year, decade | Exposure, Planning |
| <small>[MIC-017 — Microbial stress-response genes](#mic-017)</small> | Calculation, Estimate from evidence | sample, community | sample date, season, year | Response to disturbance, Restoration monitoring |
| <small>[RES-001 — Resistance to disturbance](#res-001)</small> | Calculation | plot, ecosystem, landscape | event, year, decade | Response to disturbance, Restoration monitoring |
| <small>[RES-002 — Recovery speed and time](#res-002)</small> | Calculation, Model estimate | plot, ecosystem, landscape | event, year, decade | Response to disturbance, Restoration monitoring |
| <small>[RES-003 — Variation and stability over time](#res-003)</small> | Calculation | plot, ecosystem, landscape | event, year, decade | Response to disturbance, Restoration monitoring |
| <small>[RES-004 — Differences in species responses](#res-004)</small> | Calculation | sample, community | sample date, season, year | Response to disturbance, Restoration monitoring |
| <small>[RES-005 — Recovery after fire](#res-005)</small> | Calculation | sample, community | sample date, season, year | Response to disturbance, Restoration monitoring |
| <small>[RES-006 — Possible early-warning signals](#res-006)</small> | Calculation, Future estimate | plot, ecosystem, landscape | event, year, decade | Exposure, Planning |
| <small>[RES-007 — Uncertainty in scenario predictions](#res-007)</small> | Calculation, Model estimate | plot, ecosystem, landscape | event, year, decade | Response to disturbance, Restoration monitoring |
| <small>[AGR-001 — Crop nitrogen-use efficiency](#agr-001)</small> | Calculation | plot, farm, landscape | season, year | Condition, Production assessment |
| <small>[AGR-002 — Crop water productivity](#agr-002)</small> | Calculation | plot, farm, landscape | season, year | Condition, Production assessment |
| <small>[AGR-003 — Pesticide hazard and risk](#agr-003)</small> | Combined score, Model estimate, Environmental pressure | plot, farm, landscape | season, year | Condition assessment, Assessment |
| <small>[AGR-004 — Pest numbers and crop damage](#agr-004)</small> | Direct measurement, Environmental pressure | plot, farm, landscape | season, year | Environmental pressure |
| <small>[AGR-005 — Crop disease incidence and severity](#agr-005)</small> | Direct measurement, Environmental pressure | sample, community | sample date, season, year | Environmental pressure |
| <small>[AGR-006 — Crop and rotation diversity](#agr-006)</small> | Calculation, Background information | plot, farm, landscape | season, year | Background information, Production assessment |
| <small>[AGR-007 — Mixed-crop land productivity](#agr-007)</small> | Calculation | plot, farm, landscape | season, year | Condition, Production assessment |
| <small>[AGR-008 — Nutrients removed in harvest](#agr-008)</small> | Calculation, Process measurement | plot, farm, landscape | season, year | Ecosystem process, Production assessment |
| <small>[AGR-009 — Forage use and imported feed](#agr-009)</small> | Calculation, Environmental pressure | plot, farm, landscape | season, year | Environmental pressure |
| <small>[AGR-010 — Tillage and machinery disturbance](#agr-010)</small> | Direct measurement, Background information, Environmental pressure | plot, farm, landscape | season, year | Background information |
| <small>[AGR-011 — Farm nutrient and energy balance](#agr-011)</small> | Calculation | plot, farm, landscape | season, year | Condition, Production assessment |
| <small>[FUN-004 — Crop yield and stability](#fun-004)</small> | Direct measurement, Calculation | plot, farm, landscape | season, year | Condition, Production assessment |
| <small>[FUN-005 — Groundcover duration](#fun-005)</small> | Calculation | plot, farm, landscape | season, year | Condition, Production assessment |
| <small>[FUN-006 — Grazing intensity](#fun-006)</small> | Direct measurement, Environmental pressure | plot, farm, landscape | season, year | Environmental pressure |
| <small>[FUN-007 — Water, fertiliser and pesticide inputs](#fun-007)</small> | Direct measurement, Environmental pressure | plot, farm, landscape | season, year | Environmental pressure |
| <small>[FUN-009 — Settlements and infrastructure](#fun-009)</small> | Calculation, Environmental pressure | farm, watershed, region | year | Environmental pressure |
| <small>[FUN-010 — Available biomass and materials](#fun-010)</small> | Direct measurement, Model estimate | farm, watershed, region | year | Condition |
| <small>[FUN-011 — Ecological footprint and resource demand](#fun-011)</small> | Calculation, Model estimate, Environmental pressure | farm, watershed, region | year | Environmental pressure |
| <small>[HUM-001 — Sealed ground cover](#hum-001)</small> | Calculation, Environmental pressure | farm, watershed, region | year | Environmental pressure |
| <small>[HUM-002 — Land-use intensity](#hum-002)</small> | Direct measurement, Calculation, Environmental pressure | farm, watershed, region | year | Environmental pressure |
| <small>[HUM-003 — Material use and recycling](#hum-003)</small> | Calculation, Environmental pressure | farm, watershed, region | year | Environmental pressure |
| <small>[HUM-004 — Energy demand and return](#hum-004)</small> | Direct measurement, Calculation, Environmental pressure | farm, watershed, region | year | Environmental pressure |
| <small>[HUM-005 — Water withdrawal and consumption](#hum-005)</small> | Direct measurement, Calculation, Environmental pressure | farm, watershed, region | year | Environmental pressure |
| <small>[HUM-006 — Lifecycle greenhouse-gas emissions](#hum-006)</small> | Calculation, Model estimate, Environmental pressure | farm, watershed, region | year | Environmental pressure |
| <small>[HUM-007 — Artificial light at night](#hum-007)</small> | Direct measurement, Environmental pressure | farm, watershed, region | year | Environmental pressure |
| <small>[HUM-008 — Human-made noise](#hum-008)</small> | Direct measurement, Environmental pressure | farm, watershed, region | year | Environmental pressure |
| <small>[HUM-009 — Dependence on imported resources](#hum-009)</small> | Calculation, Background information | farm, watershed, region | year | Background information |
| <small>[TER-015 — Built-feature geometry](#ter-015)</small> | Direct observation, Background information | farm, watershed, region | year | Background information |
| <small>[FUN-014 — Ecological boundary exceedance](#fun-014)</small> | Calculation, Model estimate | region, planet | year, decade | Large-scale pressure, Comparison with a threshold |
| <small>[PB-001 — Global carbon dioxide and climate forcing](#pb-001)</small> | Direct measurement, Model estimate, Environmental pressure | region, planet | year, decade | Large-scale pressure, Comparison with a threshold |
| <small>[PB-002 — Large-scale biodiversity and function loss](#pb-002)</small> | Model estimate, Environmental pressure | region, planet | year, decade | Large-scale pressure, Comparison with a threshold |
| <small>[PB-003 — Large-scale nitrogen and phosphorus pressures](#pb-003)</small> | Calculation, Model estimate, Environmental pressure | region, planet | year, decade | Large-scale pressure, Comparison with a threshold |
| <small>[PB-004 — Large-scale river-flow and soil-moisture change](#pb-004)</small> | Calculation, Model estimate, Environmental pressure | region, planet | year, decade | Large-scale pressure, Comparison with a threshold |
| <small>[PB-005 — Forest and biome extent change](#pb-005)</small> | Calculation, Environmental pressure | region, planet | year, decade | Large-scale pressure, Comparison with a threshold |
| <small>[PB-006 — Stratospheric ozone](#pb-006)</small> | Direct measurement, Calculation | region, planet | year, decade | Large-scale pressure, Comparison with a threshold |
| <small>[PB-007 — New chemical releases and assessment coverage](#pb-007)</small> | Calculation, Environmental pressure | region, planet | year, decade | Large-scale pressure, Comparison with a threshold |
| <small>[PB-008 — Ocean acidification](#pb-008)</small> | Calculation, Environmental pressure | region, planet | year, decade | Large-scale pressure, Comparison with a threshold |
| <small>[PB-009 — Large-scale aerosol loading](#pb-009)</small> | Calculation, Environmental pressure | region, planet | year, decade | Large-scale pressure, Comparison with a threshold |
| <small>[PB-010 — Departure from regional ecological thresholds](#pb-010)</small> | Calculation, Model estimate | region, planet | year, decade | Large-scale pressure, Comparison with a threshold |



### Historical Register pair v0.2.1 scientific supplements — Observation methods and information products

**Historical Register pair v0.2.1 scientific supplements; original research status and qualifications retained.**

## Observation methods and information products

| Method / platform | Primary observations or products | Typical EII use | Main qualification |
|---|---|---|---|
| RGB drone, camera or orthophoto | Visible colour channels and mapped surface features | Vegetation cover, terraces, built geometry | Lighting, colour processing, scale and geometric accuracy affect comparisons. |
| Multispectral / hyperspectral sensing | Reflectance at specified wavelengths | Greenness, pigment and moisture contrasts; calibrated traits | Band ratios directly describe spectra; physiology requires validation. No hyperspectral dataset was bound from GISDS. |
| Thermal imaging | Thermal radiance and retrieved surface temperature | Surface heating and canopy temperature anomalies | Emissivity, atmosphere and acquisition time matter; surface temperature differs from air temperature. |
| Satellite radar (SAR) | Backscatter/coherence and interpreted classifications | Inundation and surface-change screening | Moisture, roughness, vegetation and viewing geometry can produce similar signals. |
| LiDAR / structure-from-motion | Point clouds, terrain and surface models | Height, crown geometry, terrain and repeat change | Ground classification, co-registration and occlusion affect results; geometry is not biomass directly. |
| Weather / hydrology stations and future IoT | Temperature, rainfall, humidity, flow and calibrated sensor streams | Climate, water balance, exposure and event monitoring | Record sensor calibration, depth/height, gaps, drift and temporal support. |
| Soil / water laboratory assays | Carbon, nutrients, chemistry and physical properties | Pools, concentrations, contamination and retention | Extraction, dry/wet basis, detection limits and compatible units must be declared. |
| Field ecological surveys | Organisms, abundance, traits, visits and demographic observations | Biodiversity, interactions and population change | Sampling effort and imperfect detection constrain inference. |
| Amplicon / shotgun sequencing | Marker sequences, taxonomic profiles and encoded genes | Community composition and genetic potential | Relative reads are not absolute abundance; DNA potential is not expression or process flux. |
| RNA, proteins and metabolites | Transcripts, detected proteins and metabolite pools | Biochemical state and activity-related evidence | These evidence layers remain distinct; pools/signals do not directly measure realised flux. |
| Controlled process assays / flux measurements | Transformation, growth, respiration or exchange rates | Nitrogen cycling, decomposition and carbon balances | Assay conditions and field representativeness determine applicability. |



### Historical Register pair v0.2.1 scientific supplements — Source register

**Historical Register pair v0.2.1 scientific supplements; original research status and qualifications retained.**

## Source register

| Source ref | Resource / contribution | Interpretation note |
|---|---|---|
| RS001 | [Copernicus Browser](https://browser.dataspace.copernicus.eu/) — Satellite imagery and indices | GeoTIFF; raw versus rendered export matters |
| RS002 | [USGS EarthExplorer](https://earthexplorer.usgs.gov/) — Landsat reflectance and temperature | Follow product scaling and quality masks |
| RS004 | [Copernicus Land Monitoring Service](https://land.copernicus.eu/en) — Land cover and environmental variables | Check resolution, period and product documentation |
| RS005 | [ESA WorldCover](https://viewer.esa-worldcover.org/) — 10 m land-cover maps: 2020 and 2021 | Algorithms differ between years; GeoTIFF and QGIS styles |
| RS006 | [Dynamic World](https://www.dynamicworld.app/) — 10 m land-cover classes and probabilities | Per-observation classification varies with conditions |
| RS009 | [MapBiomas](https://mapbiomas.org/) — Annual land-cover and land-use maps | Coverage, collections and methods vary |
| RS011 | [Global Mangrove Watch](https://www.globalmangrovewatch.org/) — Mangrove extent, change and alerts | Check indicator applicability at local scale |
| RS012 | [Allen Coral Atlas](https://allencoralatlas.org/) — Coral-reef habitat maps and monitoring | Attribution required; coverage and depth limits |
| RS013 | [JRC Global Surface Water](https://global-surface-water.appspot.com/) — Water occurrence, seasonality and change | GeoTIFF; custom analysis in GIS or Earth Engine; check release notes |
| RS014 | [GloFAS / Global Flood Monitoring](https://global-flood.emergency.copernicus.eu/) — Flood forecasts and satellite inundation | Forecasts and satellite observations are distinct |
| RS015 | [Copernicus Drought Observatories](https://drought.emergency.copernicus.eu/) — European and global drought indicators | Includes satellite, meteorological and model inputs |
| RS016 | [EFFIS](https://forest-fire.emergency.copernicus.eu/) — Fires, burned areas, danger and risk | Separate detected events, burned area and forecast danger |
| RS017 | [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/) — Active fires and thermal anomalies | CSV/KML/shapefile; hotspots are not burn boundaries |
| RS018 | [Copernicus Marine MyOcean Pro](https://data.marine.copernicus.eu/viewer/expert) — Marine observations and models | Commonly NetCDF; distinguish model from observation |
| RS019 | [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/) — Built-up areas, settlements and population | Population is estimated; check product resolution |
| RS021 | [ICGC viewers and downloads](https://www.icgc.cat/en/Tools-and-viewers/Viewers) — Orthophotos, LiDAR and cartography | Includes airborne rather than satellite sensing |
| AMRKB context | Technical agricultural methods and management context | A method label provides context; ecological effects require observations and controlled comparison. |
| IoT (future) | Future calibrated environmental sensor datasets | Sensor depth/height, calibration, drift and gaps affect interpretation. |
| Bioinformatics (future) | Future biological observations and pipeline outputs | Sample support, controls, normalisation and reference databases affect interpretation. |




### Historical Register pair v0.2.1 scientific supplements — Scientific references

**Historical Register pair v0.2.1 scientific supplements; original research status and qualifications retained.**

## Scientific references

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



### Historical Register pair v0.2.1 scientific supplements — Indicator families and distinct quantities

**Historical Register pair v0.2.1 scientific supplements; original research status and qualifications retained.**

## Indicator families and distinct quantities

Some original labels group separate quantities under one stable ID. Select the appropriate component when recording measurements. Carbon concentration and stock, GPP and NPP, groundwater level and recharge, and conductivity and pH describe different quantities and must remain separate.

| Indicator group | Distinct quantities |
|---|---|
| <small>[VEG-015 — Plant water stress and canopy temperature](#veg-015)</small> | canopy temperature anomaly, validated water stress index |
| <small>[VEG-016 — Seasonal plant timing](#veg-016)</small> | green up date, senescence date, season duration |
| <small>[VEG-017 — Plant species and crop varieties](#veg-017)</small> | species composition, cultivar composition |
| <small>[TER-008 — Terrace shape and wall condition](#ter-008)</small> | terrace geometry, wall condition |
| <small>[TER-012 — Canopy gaps and crown cover](#ter-012)</small> | gap fraction, crown cover |
| <small>[TER-014 — Ground and canopy change](#ter-014)</small> | ground height change, canopy height change, volume change |
| <small>[HYD-001 — Soil moisture](#hyd-001)</small> | surface moisture, root zone moisture |
| <small>[HYD-005 — Soil water storage](#hyd-005)</small> | water retention at potential, plant available water capacity |
| <small>[HYD-007 — Groundwater level and recharge](#hyd-007)</small> | groundwater level, recharge rate |
| <small>[HYD-008 — Flood area and frequency](#hyd-008)</small> | inundated extent, observed event frequency, modelled return period |
| <small>[HYD-009 — Water cloudiness and suspended sediment](#hyd-009)</small> | turbidity, suspended sediment concentration |
| <small>[HYD-010 — Water nutrient concentrations](#hyd-010)</small> | nitrate N, ammonium N, total N, orthophosphate P, total P |
| <small>[HYD-011 — Water salts and acidity](#hyd-011)</small> | conductivity, salinity, pH |
| <small>[SOI-002 — Soil density and compaction](#soi-002)</small> | bulk density, penetration resistance |
| <small>[SOI-005 — Soil organic carbon](#soi-005)</small> | organic carbon concentration, organic carbon stock |
| <small>[SOI-008 — Available soil nutrients](#soi-008)</small> | extractable mineral N, method defined available P, exchangeable K |
| <small>[SOI-013 — Soil contaminants](#soi-013)</small> | named total contaminant, named extractable contaminant |
| <small>[MIC-007 — Microbial biomass](#mic-007)</small> | microbial biomass C, microbial biomass N |
| <small>[MIC-014 — Root-associated fungi](#mic-014)</small> | mycorrhizal composition, root colonisation |
| <small>[MIC-016 — Potential harmful or beneficial microbes](#mic-016)</small> | validated pathogen marker, candidate beneficial taxon |
| <small>[MIC-023 — Nitrogen transformation rates](#mic-023)</small> | net N mineralisation, gross N mineralisation, net nitrification, gross nitrification |
| <small>[BIO-002 — Species numbers and occupancy](#bio-002)</small> | population abundance, modelled occupancy |
| <small>[BIO-003 — Species diversity indices](#bio-003)</small> | Shannon H, Simpson concentration, Simpson complement, inverse Simpson |
| <small>[BIO-005 — Habitat area and condition](#bio-005)</small> | habitat extent, reference based quality |
| <small>[BIO-007 — Habitat connectivity](#bio-007)</small> | structural connectivity, modelled functional connectivity |
| <small>[BIO-008 — Pollinator numbers and flower visits](#bio-008)</small> | pollinator count, flower visitation rate |
| <small>[DIS-004 — Land cover and land use](#dis-004)</small> | land cover, land use |
| <small>[DIS-006 — Air temperature and rainfall](#dis-006)</small> | air temperature, precipitation |
| <small>[DIS-007 — Drought and dryness indices](#dis-007)</small> | SPI, SPEI, aridity ratio |
| <small>[DIS-008 — Heatwave and frost frequency](#dis-008)</small> | heatwave frequency, frost frequency |
| <small>[DIS-010 — Future climate exposure and suitability](#dis-010)</small> | scenario exposure, modelled species suitability |
| <small>[DIS-011 — Radar-detected flooding and change](#dis-011)</small> | radar inundation mask, radar change metric |
| <small>[FUN-001 — Plant carbon production (GPP/NPP)](#fun-001)</small> | GPP, NPP |
| <small>[FUN-002 — Carbon storage change](#fun-002)</small> | specified pool stock change, net ecosystem carbon balance |
| <small>[FUN-003 — Nutrient retention and leaching](#fun-003)</small> | nutrient retention, nutrient leaching |
| <small>[FUN-004 — Crop yield and stability](#fun-004)</small> | crop yield, interannual yield stability |
| <small>[FUN-007 — Water, fertiliser and pesticide inputs](#fun-007)</small> | irrigation input, fertiliser input, pesticide input |
| <small>[FUN-011 — Ecological footprint and resource demand](#fun-011)</small> | ecological footprint, physical resource demand |
| <small>[ATM-003 — Air humidity and drying demand](#atm-003)</small> | relative humidity, vapour pressure deficit |
| <small>[ATM-008 — Fine airborne particles](#atm-008)</small> | PM2 5, PM10 |
| <small>[ATM-009 — Snow cover and stored water](#atm-009)</small> | snow cover, snow water equivalent |
| <small>[SOI-014 — Stones and soil depth](#soi-014)</small> | coarse fragment volume fraction, soil depth |
| <small>[SOI-018 — Total soil nitrogen and carbon:nitrogen ratio](#soi-018)</small> | total N, C to N ratio |
| <small>[SOI-019 — Soil sodium indices](#soi-019)</small> | ESP, SAR |
| <small>[SOI-021 — Soil organic-carbon fractions](#soi-021)</small> | labile C, particulate organic carbon, mineral associated organic carbon |
| <small>[BIO-019 — Live coral cover and bleaching](#bio-019)</small> | live coral cover, bleaching prevalence |
| <small>[BIO-020 — Mangrove area and condition](#bio-020)</small> | mangrove extent, specified condition attribute |
| <small>[VEG-020 — Plant water status and leaf gas exchange](#veg-020)</small> | leaf water potential, stomatal conductance |
| <small>[VEG-021 — Plant deaths and new establishment](#veg-021)</small> | mortality rate, recruitment rate |
| <small>[AGR-005 — Crop disease incidence and severity](#agr-005)</small> | disease incidence, disease severity |
| <small>[AGR-009 — Forage use and imported feed](#agr-009)</small> | forage utilisation, imported feed share |
| <small>[AGR-011 — Farm nutrient and energy balance](#agr-011)</small> | nutrient balance, energy balance |
| <small>[HUM-003 — Material use and recycling](#hum-003)</small> | material flow, recycled input fraction |
| <small>[HUM-004 — Energy demand and return](#hum-004)</small> | energy demand, energy return ratio |
| <small>[HUM-005 — Water withdrawal and consumption](#hum-005)</small> | water withdrawal, water consumption |
| <small>[PB-001 — Global carbon dioxide and climate forcing](#pb-001)</small> | CO2 concentration, radiative forcing |
| <small>[PB-002 — Large-scale biodiversity and function loss](#pb-002)</small> | genetic integrity control, functional integrity control |
| <small>[PB-003 — Large-scale nitrogen and phosphorus pressures](#pb-003)</small> | N control, P control |
| <small>[PB-004 — Large-scale river-flow and soil-moisture change](#pb-004)</small> | blue water change, green water change |



### Historical Register pair v0.2.1 scientific supplements — Cross-domain questions

**Historical Register pair v0.2.1 scientific supplements; original research status and qualifications retained.**

## Cross-domain questions

| Question | Helpful measurements | What to keep in mind |
|---|---|---|
| Are greener plants getting enough water? | Vegetation greenness, leaf area, soil moisture, plant water status and air humidity | Greenness can also change with plant type, leaf cover and nutrients. |
| Which terraces are losing soil? | Slope, terrace condition, erosion channels, vegetation cover, infiltration and rainfall | Terrain can suggest risk; measuring sediment or repeat ground change helps establish actual loss. |
| Is soil storing more carbon? | Soil carbon stock, soil density, stones/depth and repeated carbon measurements | Compare the same depth or soil mass. A higher carbon percentage alone is not proof of more stored carbon. |
| Does a farming method improve outcomes? | Crop yield, water and nitrogen use, soil structure/carbon, nutrient losses and pollinator visits | Compare similar treated and untreated areas over time. Look for trade-offs as well as benefits. |
| Are nitrogen-cycling genes linked to activity? | Genetic markers, gene expression, nitrogen transformation rates and gas measurements | Having a gene, expressing it and carrying out a process are different evidence steps. |
| Do habitat connections support movement? | Habitat maps, barriers, movement observations and population genetics | A mapped corridor is only a possible route until use is demonstrated. |
| Has an ecosystem recovered? | Plant species, population numbers, soil functions and production measured repeatedly | Green cover may return before the original species or functions recover. |
| Where could fire spread most easily? | Fuel amount/arrangement, dryness, wind, slope and fire history | Fuel and weather describe hazard; ignition and the people or habitats exposed also matter. |


[Research Protocol](EII_Research_Protocol.md) · [Machine Reference JSON](EII_Machine_Reference.json) · [Citation](CITATION.cff).
