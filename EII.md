# EII — Ecological Indicator Inventory

**Master inventory · Version 0.2.0 · 13 October 2026**  
**Scope:** Scientific and technological ecological variables, derived indicators, process measurements, pressures and explicitly qualified inferences.  
**Coverage:** 235 records across the original 15 domains; all 120 v0.1.0 IDs retained.  
**Status:** Extended Stage A inventory with operational working definitions. This is a research reference, not a validated monitoring standard or an exhaustive list of every possible indicator.

## Purpose and reviewed source baseline

EII is the higher-level indicator reference: contributing catalogues describe data, technologies, methods or management context; EII describes what an indicator represents, how it is obtained, what conclusions it supports and which other indicators help interpret it. One indicator can have multiple acquisition routes without becoming multiple ecological concepts.

Reviewed local documents:

- `EII/EII.md`, v0.1.0, created 10 October 2026: 120 records in eight legacy groups, plus the earlier 15-domain scope from **EII Overview**.
- `GISDS/Cartography_Database_Sources.md`, v1.0, updated 12 October 2026, and its README: 22 stable catalogue IDs, `RS001`–`RS022`. These are mainly platforms/catalogue resources, not bound dataset records.
- `AMRKB/README.md`, v0.1.0, created 12 October 2026: scope and proposed architecture only. No implemented observation database, record IDs or agricultural dataset register was found.

The overview chats were also reviewed for intended scope. The actual files were located in `/Users/jonathan/Github/ecological-information/`; the ChatGPT project mirror's `sources/` directory was empty. This edition was first prepared as a separate output and has now been applied to the existing repository `EII/EII.md`. GISDS, AMRKB and synced project reference files were left untouched. Appendix provenance hashes identify exactly the files used, without assuming that an unavailable newer upload was reviewed.

**Exclusions:** The Trails4Soil practice list and programme crosswalk are omitted entirely. No interoperability edge or bibliography dependency to PBCKA or EIRKB is created. AMRKB references are limited to empirically assessable technical methods, inputs and management context; philosophical, cultural and historical classifications are outside this inventory. Existing quantitative human-pressure indicators remain in Domain 14.

## Reading and interpretation rules

Each entry has a definition, actual observations/calculation and units, a defensible inference with limits, and supporting EII IDs. A derived index measures its mathematical input contrast; an inference about physiology or ecosystem condition requires validation. Method choice can change whether a quantity is measured or modelled. DNA potential, RNA expression, protein detection, enzyme assays and realised process fluxes are distinct evidence layers.

Supporting indicators are **interpretive companions**, not automatically formula inputs, causal evidence or substitutes. Relations are directed recommendations and need not be reciprocal. Use the relevant component of a family record. Multiple observations strengthen an inference only when their methods, spatial support, timing and uncertainty are compatible.

No universal “higher is better” direction is assigned: high respiration, nutrient concentration, greenness or diversity can have different implications by ecosystem and context. Management-effect claims require controls, replication and attention to confounding. Composite scores must retain their components, weights, reference conditions and uncertainty.

### Stable IDs and compound records

Legacy local IDs and preferred labels are retained exactly; their namespaces are now explicit, e.g. `EII:VEG-001`. IDs do not encode the current domain: moving a record never renumbers it. New records use new unused IDs. IDs are never recycled; future merges/deprecations should retain an alias/redirect and a versioned reason.

Several legacy labels combine distinct variables. They remain **family records**, with machine-readable `variants` in their metadata. An observation must select a variant (e.g. `EII:SOI-005` plus `organic_C_stock` versus `organic_C_concentration`) and record method and unit. Never place pH, salinity, carbon stocks, concentrations, GPP and NPP into one interchangeable numeric series. Existing separate additions such as `ATM-001`/`ATM-002` can specialise `DIS-006`; they do not retire its family ID. Family member keys are stable within their EII ID.

### Four classification levels

| Level | Field | Meaning |
|---|---|---|
| Primary | `domain` | One of the original 15 domains; one home per record, with optional `related_domains`. |
| Secondary | `secondary` | Acquisition/epistemic type: `observed`, `measured`, `derived`, `proxy`, `inferred`, `modelled`, `composite`, `predictive`, `process`, `context`, `pressure`. Tags can coexist and are method-dependent. |
| Tertiary | `tertiary.spatial`, `tertiary.temporal` | Typical observation/application supports and intervals. These are applicability guides, never claims of native pixel resolution, minimum sampling frequency or validated extrapolation. |
| Quaternary | `quaternary` | Ecological/assessment role: state, condition, function, pressure, context, exposure, disturbance response, production assessment, restoration assessment, planning or threshold comparison. |

A molecular/sample profile remains a sample observation when mapped: interpolation to a landscape requires a separate model, validation and uncertainty. Station records, pixels, field plots and watersheds cannot be combined simply because their coordinates overlap. Aggregate by an explicit support/time transformation; do not silently resample into apparent precision.

### Compact interoperability

Each heading has a stable HTML anchor. Immediately below it is an HTML comment containing one JSON object prefixed by `eii:`. Comments remain unobtrusive in rendered Markdown and can be parsed from the raw download. Definition/direct/inference/support bullets have fixed labels. The JSON fields use full names; `routes` contains short **EII-local adapter keys**, resolved once in Appendix A. These keys are not IDs invented for other projects.

`GISDS:RS001` and similar source-system IDs preserve the existing catalogue IDs. A route is a **candidate** until an exact dataset/product/version is bound. Not every indicator can be derived from every source listed in a route: band coverage, geography, calibration and validation decide suitability. Provider/model estimates require their own methods and quality metadata.

AMRKB links express context or possible technical-method relationships, never claimed observed data provenance. IoT/bioinformatics routes have `namespace: null` and `dataset_id: null`: they are reserved integration channels, not existing databases. Scientific references in Appendix B are local EII bibliography keys, independent of the excluded knowledge bases. Acquisition possibilities and documentary references must never be confused with proof that an indicator has actually been computed.

## Domain index

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

## Master indicator register

<a id="d01"></a>

### 1. Atmosphere and climate

<a id="ter-004"></a>

#### EII:TER-004 — Solar radiation / insolation

<!-- eii:{"id":"EII:TER-004","domain":"D01","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","modelled"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["terrain","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Insolation is incoming solar energy at a surface over a specified interval.
- **Direct observations / derivation:** Radiometer measurements or terrain/atmosphere radiation models, W/m² or MJ/m²/day.
- **Inference and limits:** Supports energy-balance and microclimate assessment; potential terrain radiation differs from actual cloud-affected radiation.
- **Supporting indicators:** [EII:TER-003](#ter-003), [EII:ATM-004](#atm-004), [EII:HYD-012](#hyd-012).

<a id="hyd-003"></a>

#### EII:HYD-003 — Land Surface Temperature (LST)

<!-- eii:{"id":"EII:HYD-003","domain":"D01","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["thermal"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** LST is radiometric temperature of the observed land surface.
- **Direct observations / derivation:** Thermal radiance corrected for atmosphere and emissivity, K or °C; record acquisition time.
- **Inference and limits:** Supports surface-energy and heat-exposure analysis; it is neither air temperature nor uniquely a water-stress signal.
- **Supporting indicators:** [EII:DIS-006](#dis-006), [EII:VEG-012](#veg-012), [EII:HYD-012](#hyd-012).

<a id="dis-006"></a>

#### EII:DIS-006 — Air temperature / precipitation

<!-- eii:{"id":"EII:DIS-006","domain":"D01","related_domains":[],"record_type":"family","variants":["air_temperature","precipitation"],"secondary":["measured"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Air temperature and precipitation describe separate atmospheric variables.
- **Direct observations / derivation:** Shielded air thermometer, °C; gauge accumulation, mm per interval; record height/exposure and catch corrections.
- **Inference and limits:** Supports climate-baseline assessment; interpolated grids are estimates and short records do not define long-term climate.
- **Supporting indicators:** [EII:ATM-001](#atm-001), [EII:ATM-002](#atm-002), [EII:DIS-008](#dis-008).

<a id="dis-007"></a>

#### EII:DIS-007 — Drought index / aridity

<!-- eii:{"id":"EII:DIS-007","domain":"D01","related_domains":[],"record_type":"family","variants":["SPI","SPEI","aridity_ratio"],"secondary":["derived","modelled"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["drought","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Drought/aridity indices quantify distinct water-deficit or long-term dryness concepts.
- **Direct observations / derivation:** SPI from precipitation, SPEI from climatic water balance, or P/PET aridity; specify index, window and baseline.
- **Inference and limits:** Supports deficit comparison; meteorological, soil and hydrological drought may diverge and PET method affects results.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:HYD-006](#hyd-006), [EII:HYD-012](#hyd-012).

<a id="dis-008"></a>

#### EII:DIS-008 — Heatwave / frost frequency

<!-- eii:{"id":"EII:DIS-008","domain":"D01","related_domains":[],"record_type":"family","variants":["heatwave_frequency","frost_frequency"],"secondary":["derived"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Heatwave/frost frequency counts temperature events under stated thresholds/durations.
- **Direct observations / derivation:** Temperature series and event rule, events/year or days/year; distinguish air frost from plant-tissue exposure.
- **Inference and limits:** Supports thermal-extreme exposure assessment; biological injury depends on phenology, cultivar and duration.
- **Supporting indicators:** [EII:DIS-006](#dis-006), [EII:VEG-016](#veg-016), [EII:AGR-005](#agr-005).

<a id="atm-001"></a>

#### EII:ATM-001 — Air temperature

<!-- eii:{"id":"EII:ATM-001","domain":"D01","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Temperature of air at a specified height/exposure.
- **Direct observations / derivation:** Shielded calibrated sensor, °C; averages require declared interval.
- **Inference and limits:** Supports heat/cold exposure assessment; local microclimates and sensor shielding affect comparability.
- **Supporting indicators:** [EII:DIS-006](#dis-006), [EII:DIS-008](#dis-008), [EII:VEG-016](#veg-016).

<a id="atm-002"></a>

#### EII:ATM-002 — Precipitation amount/intensity

<!-- eii:{"id":"EII:ATM-002","domain":"D01","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Liquid-equivalent precipitation accumulated or received per time.
- **Direct observations / derivation:** Gauge/radar observations, mm and mm/h; snow and wind require corrections.
- **Inference and limits:** Supports water inputs and erosion forcing; spatial variability prevents assuming a point gauge represents a watershed.
- **Supporting indicators:** [EII:HYD-006](#hyd-006), [EII:HYD-001](#hyd-001), [EII:SOI-012](#soi-012).

<a id="atm-003"></a>

#### EII:ATM-003 — Relative humidity/vapour-pressure deficit

<!-- eii:{"id":"EII:ATM-003","domain":"D01","related_domains":[],"record_type":"family","variants":["relative_humidity","vapour_pressure_deficit"],"secondary":["measured","derived"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** RH is saturation-relative water vapour; VPD is saturation minus actual vapour pressure.
- **Direct observations / derivation:** Calibrated temperature/RH, %; calculate VPD, kPa, with stated temperature basis.
- **Inference and limits:** Supports atmospheric drying-demand assessment; VPD is not soil drought or actual transpiration.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:HYD-012](#hyd-012), [EII:VEG-015](#veg-015).

<a id="atm-004"></a>

#### EII:ATM-004 — Photosynthetically active radiation

<!-- eii:{"id":"EII:ATM-004","domain":"D01","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Photon flux in the declared photosynthetic wavelength range.
- **Direct observations / derivation:** Quantum sensor, µmol photons/m²/s, commonly 400–700 nm; integrate daily separately.
- **Inference and limits:** Supports light availability; intercepted/absorbed radiation and canopy physiology determine production.
- **Supporting indicators:** [EII:VEG-011](#veg-011), [EII:FUN-001](#fun-001), [EII:TER-004](#ter-004).

<a id="atm-005"></a>

#### EII:ATM-005 — Wind speed/direction

<!-- eii:{"id":"EII:ATM-005","domain":"D01","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Airflow magnitude and compass direction at a stated height.
- **Direct observations / derivation:** Calibrated anemometer, m/s and degrees, with averaging/gust convention.
- **Inference and limits:** Supports aerodynamic demand, dispersal and fire context; roughness and shelter affect local exposure.
- **Supporting indicators:** [EII:HYD-012](#hyd-012), [EII:DIS-002](#dis-002), [EII:BIO-008](#bio-008).

<a id="atm-006"></a>

#### EII:ATM-006 — Atmospheric CO₂ concentration

<!-- eii:{"id":"EII:ATM-006","domain":"D01","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** CO₂ mole fraction in a declared air sample.
- **Direct observations / derivation:** Calibrated gas analyser, µmol/mol or ppm, with dry-air convention.
- **Inference and limits:** Supports carbon-cycle context; local concentration changes are not ecosystem flux without transport analysis.
- **Supporting indicators:** [EII:CYC-001](#cyc-001), [EII:FUN-001](#fun-001), [EII:PB-001](#pb-001).

<a id="atm-007"></a>

#### EII:ATM-007 — Ozone exposure

<!-- eii:{"id":"EII:ATM-007","domain":"D01","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","derived","pressure"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["pressure"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Near-surface ozone concentration and separately computed cumulative exposure.
- **Direct observations / derivation:** Calibrated analyser, nmol/mol; dose/exposure metrics require declared threshold and time window.
- **Inference and limits:** Supports plant pollution-risk assessment; stomatal uptake, phenology and species determine injury.
- **Supporting indicators:** [EII:VEG-015](#veg-015), [EII:ATM-003](#atm-003), [EII:VEG-017](#veg-017).

<a id="atm-008"></a>

#### EII:ATM-008 — PM₂.₅/PM₁₀ concentration

<!-- eii:{"id":"EII:ATM-008","domain":"D01","related_domains":[],"record_type":"family","variants":["PM2_5","PM10"],"secondary":["measured","pressure"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["pressure"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Airborne particle mass within defined aerodynamic size fractions.
- **Direct observations / derivation:** Gravimetric/reference-calibrated sensor, µg/m³, with humidity and averaging metadata.
- **Inference and limits:** Supports particulate exposure assessment; optical sensors need calibration and mass does not identify composition/source.
- **Supporting indicators:** [EII:ATM-005](#atm-005), [EII:HUM-008](#hum-008), [EII:PB-009](#pb-009).

<a id="atm-009"></a>

#### EII:ATM-009 — Snow cover/snow water equivalent

<!-- eii:{"id":"EII:ATM-009","domain":"D01","related_domains":[],"record_type":"family","variants":["snow_cover","snow_water_equivalent"],"secondary":["measured","derived"],"tertiary":{"spatial":["site","landscape","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["opt","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Snow-covered fraction and stored liquid-equivalent water are separate quantities.
- **Direct observations / derivation:** Mapped snow fraction, %; snow depth/density survey or retrieval, mm water equivalent.
- **Inference and limits:** Supports meltwater-storage assessment; cover alone does not establish volume or melt rate.
- **Supporting indicators:** [EII:ATM-001](#atm-001), [EII:HYD-006](#hyd-006), [EII:HYD-001](#hyd-001).

<a id="d02"></a>

### 2. Hydrology

<a id="ter-005"></a>

#### EII:TER-005 — Topographic wetness index

<!-- eii:{"id":"EII:TER-005","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Topographic wetness index expresses terrain-driven accumulation potential.
- **Direct observations / derivation:** ln(a/tan β), where a is specific contributing area and β slope; dimensionless with declared algorithm.
- **Inference and limits:** Suggests relative topographic saturation propensity; not measured water content and unreliable without hydrological validation.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:TER-006](#ter-006), [EII:SOI-001](#soi-001).

<a id="ter-006"></a>

#### EII:TER-006 — Flow accumulation / drainage pathways

<!-- eii:{"id":"EII:TER-006","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","modelled"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Flow accumulation/drainage pathways describe terrain-routed contributing area.
- **Direct observations / derivation:** Hydrologically conditioned DTM and routing algorithm, cells or m²; declare sink handling.
- **Inference and limits:** Suggests runoff pathways; engineered drainage, infiltration and subsurface flow can alter routes.
- **Supporting indicators:** [EII:HYD-006](#hyd-006), [EII:HYD-008](#hyd-008), [EII:TER-009](#ter-009).

<a id="hyd-001"></a>

#### EII:HYD-001 — Surface / root-zone soil moisture

<!-- eii:{"id":"EII:HYD-001","domain":"D02","related_domains":[],"record_type":"family","variants":["surface_moisture","root_zone_moisture"],"secondary":["measured","modelled"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot","drought"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Soil moisture is water held in a defined soil layer.
- **Direct observations / derivation:** Gravimetric mass ratio or calibrated volumetric sensors, g/g or m³/m³; satellite retrievals estimate different depth/support.
- **Inference and limits:** Supports water-availability assessment; rooting depth, texture and matric potential govern plant access.
- **Supporting indicators:** [EII:HYD-005](#hyd-005), [EII:SOI-001](#soi-001), [EII:SOI-011](#soi-011).

<a id="hyd-006"></a>

#### EII:HYD-006 — Stream discharge / river flow

<!-- eii:{"id":"EII:HYD-006","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot","water"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Discharge is water volume crossing a channel section per time.
- **Direct observations / derivation:** Velocity–area gauging or calibrated stage–discharge relation, m³/s.
- **Inference and limits:** Supports flow availability and flood assessment; rating extrapolation, backwater and channel change affect estimates.
- **Supporting indicators:** [EII:HYD-008](#hyd-008), [EII:HYD-009](#hyd-009), [EII:DIS-006](#dis-006).

<a id="hyd-007"></a>

#### EII:HYD-007 — Groundwater level / recharge

<!-- eii:{"id":"EII:HYD-007","domain":"D02","related_domains":[],"record_type":"family","variants":["groundwater_level","recharge_rate"],"secondary":["measured","modelled"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Groundwater level and recharge are distinct aquifer state and flux quantities.
- **Direct observations / derivation:** Well water level, m relative to datum; recharge estimated with water-balance, tracer or hydraulic methods, mm/year.
- **Inference and limits:** Level change does not equal recharge; pumping, storage coefficients and lateral flow must be resolved.
- **Supporting indicators:** [EII:HYD-006](#hyd-006), [EII:HYD-001](#hyd-001), [EII:DIS-006](#dis-006).

<a id="hyd-008"></a>

#### EII:HYD-008 — Flood extent / frequency

<!-- eii:{"id":"EII:HYD-008","domain":"D02","related_domains":[],"record_type":"family","variants":["inundated_extent","observed_event_frequency","modelled_return_period"],"secondary":["derived","modelled"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["flood","water"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Flood extent/frequency describe inundated area and repeated occurrence.
- **Direct observations / derivation:** Validated event masks, km²; event counts or statistical recurrence, events/year or years.
- **Inference and limits:** Supports exposure and wetland-dynamics assessment; observed history does not alone provide a future return period.
- **Supporting indicators:** [EII:HYD-006](#hyd-006), [EII:TER-001](#ter-001), [EII:DIS-011](#dis-011).

<a id="hyd-009"></a>

#### EII:HYD-009 — Water turbidity / suspended sediment

<!-- eii:{"id":"EII:HYD-009","domain":"D02","related_domains":[],"record_type":"family","variants":["turbidity","suspended_sediment_concentration"],"secondary":["measured","proxy"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Turbidity and suspended sediment are separate optical and mass metrics.
- **Direct observations / derivation:** Nephelometer response, FNU/NTU; filtered dry sediment mass, mg/L; convert only with local calibration.
- **Inference and limits:** Supports sediment-transport interpretation; particle size, colour and organic matter affect optical response.
- **Supporting indicators:** [EII:HYD-006](#hyd-006), [EII:SOI-012](#soi-012), [EII:HYD-010](#hyd-010).

<a id="hyd-010"></a>

#### EII:HYD-010 — Water nutrient concentrations

<!-- eii:{"id":"EII:HYD-010","domain":"D02","related_domains":["D13"],"record_type":"family","variants":["nitrate_N","ammonium_N","total_N","orthophosphate_P","total_P"],"secondary":["measured","pressure"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["pressure"],"routes":["iot","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Water nutrients are concentrations of specified nutrient forms.
- **Direct observations / derivation:** Laboratory/sensor nitrate, ammonium, phosphate or total N/P, mg N/L or mg P/L; specify filtration and method.
- **Inference and limits:** Supports enrichment assessment; concentration is not load, source attribution or biological response.
- **Supporting indicators:** [EII:HYD-006](#hyd-006), [EII:HYD-014](#hyd-014), [EII:HYD-013](#hyd-013).

<a id="hyd-011"></a>

#### EII:HYD-011 — Water conductivity / salinity / pH

<!-- eii:{"id":"EII:HYD-011","domain":"D02","related_domains":[],"record_type":"family","variants":["conductivity","salinity","pH"],"secondary":["measured"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Water conductivity, salinity and pH describe distinct water-chemistry properties.
- **Direct observations / derivation:** Conductivity at reference temperature, µS/cm; salinity on declared scale; pH with calibrated electrode.
- **Inference and limits:** Supports ionic and acidity constraints; conductivity is not a universal salinity conversion or contaminant assay.
- **Supporting indicators:** [EII:HYD-010](#hyd-010), [EII:HYD-013](#hyd-013), [EII:HYD-015](#hyd-015).

<a id="hyd-012"></a>

#### EII:HYD-012 — Evapotranspiration

<!-- eii:{"id":"EII:HYD-012","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","modelled","process"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["function"],"routes":["veg","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Evapotranspiration combines water evaporation and plant transpiration.
- **Direct observations / derivation:** Lysimeter/flux observations or energy/water-balance model, mm/day; distinguish actual ET from reference ET.
- **Inference and limits:** Supports consumptive water-use assessment; models require meteorological and surface validation.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:VEG-011](#veg-011), [EII:ATM-005](#atm-005), [EII:DIS-006](#dis-006).

<a id="dis-011"></a>

#### EII:DIS-011 — SAR-derived inundation / surface change

<!-- eii:{"id":"EII:DIS-011","domain":"D02","related_domains":[],"record_type":"family","variants":["radar_inundation_mask","radar_change_metric"],"secondary":["derived","proxy"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["sar","flood"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** SAR inundation/surface change are radar-derived interpretations of backscatter/coherence.
- **Direct observations / derivation:** Calibrated radar backscatter, dB, and declared classification/change algorithm, area or index.
- **Inference and limits:** Supports cloud-independent change detection; roughness, vegetation, geometry and soil moisture produce ambiguous signals.
- **Supporting indicators:** [EII:HYD-008](#hyd-008), [EII:HYD-001](#hyd-001), [EII:DIS-004](#dis-004).

<a id="hyd-013"></a>

#### EII:HYD-013 — Dissolved oxygen

<!-- eii:{"id":"EII:HYD-013","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":["R10"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** Oxygen dissolved in water, on concentration or saturation basis.
- **Direct observations / derivation:** Calibrated optical/electrochemical probe or titration, mg/L and % saturation, with temperature/salinity.
- **Inference and limits:** Supports oxygen-habitat assessment; diurnal cycles and flow matter and low oxygen is not uniquely eutrophication.
- **Supporting indicators:** [EII:HYD-014](#hyd-014), [EII:HYD-015](#hyd-015), [EII:HYD-010](#hyd-010).

<a id="hyd-014"></a>

#### EII:HYD-014 — Water chlorophyll-a

<!-- eii:{"id":"EII:HYD-014","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","proxy"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["marine","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Chlorophyll-a pigment concentration in a water sample.
- **Direct observations / derivation:** Extracted pigment assay, µg/L; fluorescence/remote retrievals need calibration.
- **Inference and limits:** Supports phytoplankton-biomass assessment; pigment per cell, taxonomic composition and turbidity vary.
- **Supporting indicators:** [EII:HYD-010](#hyd-010), [EII:HYD-013](#hyd-013), [EII:HYD-009](#hyd-009).

<a id="hyd-015"></a>

#### EII:HYD-015 — Water temperature

<!-- eii:{"id":"EII:HYD-015","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["marine","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Temperature of water at specified depth/time.
- **Direct observations / derivation:** Calibrated profile/probe, °C.
- **Inference and limits:** Supports thermal habitat and oxygen-solubility assessment; surface estimates do not represent deep-water conditions.
- **Supporting indicators:** [EII:HYD-013](#hyd-013), [EII:HYD-006](#hyd-006), [EII:ATM-001](#atm-001).

<a id="hyd-016"></a>

#### EII:HYD-016 — Surface-water occurrence/hydroperiod

<!-- eii:{"id":"EII:HYD-016","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["water","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Frequency or duration of surface inundation.
- **Direct observations / derivation:** Valid water detections/valid observations, %; continuous gauge/time series for days inundated.
- **Inference and limits:** Supports wetland persistence assessment; cloud/sensor sampling biases fractions and groundwater saturation may be invisible.
- **Supporting indicators:** [EII:HYD-008](#hyd-008), [EII:HYD-007](#hyd-007), [EII:BIO-005](#bio-005).

<a id="hyd-017"></a>

#### EII:HYD-017 — Environmental-flow deficit

<!-- eii:{"id":"EII:HYD-017","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","pressure"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["pressure"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Deviation of actual flow from a specified ecological-flow requirement.
- **Direct observations / derivation:** Discharge series and justified seasonal reference, m³/s, deficit duration or volume.
- **Inference and limits:** Supports aquatic stress assessment; thresholds must be basin/species specific and flow quality also matters.
- **Supporting indicators:** [EII:HYD-006](#hyd-006), [EII:HYD-015](#hyd-015), [EII:BIO-002](#bio-002).

<a id="hyd-018"></a>

#### EII:HYD-018 — Water nutrient load

<!-- eii:{"id":"EII:HYD-018","domain":"D02","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["function"],"routes":["iot","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Mass of a specified nutrient transported per time.
- **Direct observations / derivation:** Time-resolved concentration × discharge, kg N/P/day; integrate with appropriate sampling.
- **Inference and limits:** Supports export assessment; sparse sampling misses storm pulses and does not establish source attribution.
- **Supporting indicators:** [EII:HYD-010](#hyd-010), [EII:HYD-006](#hyd-006), [EII:FUN-003](#fun-003).

<a id="hyd-019"></a>

#### EII:HYD-019 — Faecal indicator bacteria

<!-- eii:{"id":"EII:HYD-019","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","proxy"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Concentration of specified culturable or molecular faecal indicators.
- **Direct observations / derivation:** Validated assay, CFU/100 mL, MPN/100 mL or gene copies with method separated.
- **Inference and limits:** Supports contamination screening; indicators do not quantify every pathogen and molecular detections may include nonviable material.
- **Supporting indicators:** [EII:HYD-006](#hyd-006), [EII:HYD-015](#hyd-015), [EII:HYD-011](#hyd-011).

<a id="hyd-020"></a>

#### EII:HYD-020 — Water contaminant residues

<!-- eii:{"id":"EII:HYD-020","domain":"D02","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","pressure"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["pressure"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Concentration of named pesticides, pharmaceuticals or other chemicals in water.
- **Direct observations / derivation:** Validated chemical analysis, µg/L, with recovery and detection limits.
- **Inference and limits:** Supports chemical-exposure assessment; toxicity depends on mixtures, duration and organism and non-detects are censored observations.
- **Supporting indicators:** [EII:HYD-006](#hyd-006), [EII:FUN-007](#fun-007), [EII:HUM-005](#hum-005).

<a id="hyd-021"></a>

#### EII:HYD-021 — Water transparency/Secchi depth

<!-- eii:{"id":"EII:HYD-021","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","proxy"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Depth at which a standard disk becomes invisible under a declared protocol.
- **Direct observations / derivation:** Disk visibility depth, m, recording light and viewing conditions.
- **Inference and limits:** Supports optical habitat comparison; algae, sediment and dissolved colour contribute jointly.
- **Supporting indicators:** [EII:HYD-014](#hyd-014), [EII:HYD-009](#hyd-009), [EII:HYD-015](#hyd-015).

<a id="hyd-022"></a>

#### EII:HYD-022 — Ocean carbonate chemistry

<!-- eii:{"id":"EII:HYD-022","domain":"D02","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["site","watershed","region"],"temporal":["hour","day","season","year"]},"quaternary":["state"],"routes":["marine"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Dissolved inorganic carbon, alkalinity and associated carbonate speciation.
- **Direct observations / derivation:** Paired measured carbonate-system quantities, µmol/kg, with temperature/salinity; calculate pH or saturation consistently.
- **Inference and limits:** Supports acidification assessment; a single pH observation does not resolve the entire carbonate system.
- **Supporting indicators:** [EII:HYD-011](#hyd-011), [EII:HYD-015](#hyd-015), [EII:PB-008](#pb-008).

<a id="d03"></a>

### 3. Soil physics

<a id="ter-007"></a>

#### EII:TER-007 — Surface roughness

<!-- eii:{"id":"EII:TER-007","domain":"D03","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["terrain","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Surface roughness quantifies elevation variation over a stated support area.
- **Direct observations / derivation:** Survey heights and declared RMS, standard deviation or rugosity metric, m or ratio.
- **Inference and limits:** Supports runoff, seedbed and habitat interpretation; metric and measurement scale determine meaning.
- **Supporting indicators:** [EII:HYD-004](#hyd-004), [EII:SOI-003](#soi-003), [EII:TER-002](#ter-002).

<a id="ter-009"></a>

#### EII:TER-009 — Erosion rills / gullies / sediment pathways

<!-- eii:{"id":"EII:TER-009","domain":"D03","related_domains":[],"record_type":"indicator","variants":[],"secondary":["observed","derived"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Rill/gully geometry records concentrated erosion features and sediment routes.
- **Direct observations / derivation:** Mapped lengths, depths, areas or volumes, m, m² or m³, from repeat surveys.
- **Inference and limits:** Provides evidence of erosion morphology; a single feature map does not establish an annual mass-loss rate.
- **Supporting indicators:** [EII:SOI-012](#soi-012), [EII:TER-014](#ter-014), [EII:HYD-009](#hyd-009).

<a id="hyd-004"></a>

#### EII:HYD-004 — Infiltration rate

<!-- eii:{"id":"EII:HYD-004","domain":"D03","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Infiltration rate is water entry through the soil surface under stated conditions.
- **Direct observations / derivation:** Infiltrometer volume/time/area, mm/h; distinguish initial, steady and saturated regimes.
- **Inference and limits:** Supports runoff susceptibility assessment; antecedent moisture and imposed head affect results.
- **Supporting indicators:** [EII:SOI-003](#soi-003), [EII:SOI-002](#soi-002), [EII:HYD-001](#hyd-001).

<a id="hyd-005"></a>

#### EII:HYD-005 — Soil water-holding capacity

<!-- eii:{"id":"EII:HYD-005","domain":"D03","related_domains":["D13"],"record_type":"family","variants":["water_retention_at_potential","plant_available_water_capacity"],"secondary":["measured","derived"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Water-holding capacity describes a stated soil retention quantity.
- **Direct observations / derivation:** Water retained at declared matric potentials; available water often θfield-capacity−θwilting, m³/m³ or mm over depth.
- **Inference and limits:** Supports storage and rooting-zone drought assessment; conventional potentials are method-dependent and crop access varies.
- **Supporting indicators:** [EII:SOI-001](#soi-001), [EII:SOI-002](#soi-002), [EII:HYD-001](#hyd-001).

<a id="soi-001"></a>

#### EII:SOI-001 — Soil texture

<!-- eii:{"id":"EII:SOI-001","domain":"D03","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Texture is the particle-size distribution of the fine-earth fraction.
- **Direct observations / derivation:** Sand/silt/clay mass percentages by declared dispersion and size limits.
- **Inference and limits:** Supports hydraulic and substrate interpretation; structure and organic matter modify texture-based expectations.
- **Supporting indicators:** [EII:SOI-003](#soi-003), [EII:HYD-005](#hyd-005), [EII:HYD-004](#hyd-004).

<a id="soi-002"></a>

#### EII:SOI-002 — Bulk density / compaction

<!-- eii:{"id":"EII:SOI-002","domain":"D03","related_domains":["D13"],"record_type":"family","variants":["bulk_density","penetration_resistance"],"secondary":["measured"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Bulk density and compaction describe mass per volume and mechanical resistance respectively.
- **Direct observations / derivation:** Oven-dry soil mass/core volume, g/cm³; penetration resistance, MPa, at stated water content.
- **Inference and limits:** Supports pore/rooting assessment; density thresholds vary with texture and resistance varies with moisture.
- **Supporting indicators:** [EII:SOI-001](#soi-001), [EII:SOI-004](#soi-004), [EII:HYD-001](#hyd-001).

<a id="soi-003"></a>

#### EII:SOI-003 — Soil aggregate stability

<!-- eii:{"id":"EII:SOI-003","domain":"D03","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Aggregate stability is resistance of aggregates to specified disruptive forces.
- **Direct observations / derivation:** Wet-sieving stable fraction, % or mean-weight diameter, mm; declare pretreatment.
- **Inference and limits:** Supports erosion-resistance interpretation; assay conditions and soil type limit comparability.
- **Supporting indicators:** [EII:HYD-004](#hyd-004), [EII:SOI-005](#soi-005), [EII:SOI-012](#soi-012).

<a id="soi-004"></a>

#### EII:SOI-004 — Soil porosity

<!-- eii:{"id":"EII:SOI-004","domain":"D03","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Porosity is void volume divided by total soil volume.
- **Direct observations / derivation:** Measured pore volumes or 1−bulk-density/particle-density, fraction; record particle-density assumption.
- **Inference and limits:** Supports aeration/storage assessment; total porosity does not resolve connected macropores.
- **Supporting indicators:** [EII:SOI-002](#soi-002), [EII:HYD-004](#hyd-004), [EII:SOI-015](#soi-015).

<a id="soi-011"></a>

#### EII:SOI-011 — Soil temperature

<!-- eii:{"id":"EII:SOI-011","domain":"D03","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Soil temperature is temperature at a declared depth.
- **Direct observations / derivation:** Calibrated probe, °C, with depth and recording interval.
- **Inference and limits:** Supports biological/hydraulic-rate interpretation; surface temperature cannot substitute for a root-zone profile.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:SOI-010](#soi-010), [EII:DIS-006](#dis-006).

<a id="soi-012"></a>

#### EII:SOI-012 — Erosion rate / soil loss

<!-- eii:{"id":"EII:SOI-012","domain":"D03","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","modelled","process"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["function"],"routes":["terrain","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Erosion/soil loss is exported or redistributed soil mass per area/time.
- **Direct observations / derivation:** Runoff plots, sediment budgets or erosion models, Mg/ha/year; distinguish gross erosion from sediment delivery.
- **Inference and limits:** Supports soil-conservation assessment; modelled susceptibility and channel loads do not uniquely establish local soil loss.
- **Supporting indicators:** [EII:TER-009](#ter-009), [EII:HYD-009](#hyd-009), [EII:VEG-012](#veg-012).

<a id="soi-014"></a>

#### EII:SOI-014 — Coarse fragments/soil depth

<!-- eii:{"id":"EII:SOI-014","domain":"D03","related_domains":["D13"],"record_type":"family","variants":["coarse_fragment_volume_fraction","soil_depth"],"secondary":["measured"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Stone volume fraction and depth of the defined soil profile.
- **Direct observations / derivation:** Field cores/pits, %, cm; distinguish rock, roots and fine earth.
- **Inference and limits:** Supports rooting/storage and carbon-stock corrections; shallow sampling cannot establish whole-profile stocks.
- **Supporting indicators:** [EII:SOI-005](#soi-005), [EII:SOI-002](#soi-002), [EII:HYD-005](#hyd-005).

<a id="soi-015"></a>

#### EII:SOI-015 — Saturated hydraulic conductivity

<!-- eii:{"id":"EII:SOI-015","domain":"D03","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Water-transmission capacity under saturated conditions.
- **Direct observations / derivation:** Permeameter or field hydraulic test, mm/h or m/s with geometry specified.
- **Inference and limits:** Supports drainage assessment; preferential flow and small sample volume limit extrapolation.
- **Supporting indicators:** [EII:SOI-004](#soi-004), [EII:HYD-004](#hyd-004), [EII:HYD-001](#hyd-001).

<a id="soi-016"></a>

#### EII:SOI-016 — Soil matric potential

<!-- eii:{"id":"EII:SOI-016","domain":"D03","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Energy state of soil water relative to a reference.
- **Direct observations / derivation:** Tensiometer/validated sensor, kPa, at declared depth; specify sign convention.
- **Inference and limits:** Supports plant-water access assessment; texture and osmotic potential must also be considered.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:SOI-007](#soi-007), [EII:HYD-005](#hyd-005).

<a id="soi-017"></a>

#### EII:SOI-017 — Macropore abundance/connectivity

<!-- eii:{"id":"EII:SOI-017","domain":"D03","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["sample","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Large-pore fraction and spatial connectivity under a declared size threshold.
- **Direct observations / derivation:** Imaging, dye tracing or pore analysis, fraction and declared connectivity metric.
- **Inference and limits:** Supports preferential-flow hypotheses; static pore structure does not directly quantify solute transport.
- **Supporting indicators:** [EII:SOI-015](#soi-015), [EII:SOI-004](#soi-004), [EII:FUN-003](#fun-003).

<a id="d04"></a>

### 4. Soil chemistry

<a id="soi-005"></a>

#### EII:SOI-005 — Soil organic carbon stock / concentration

<!-- eii:{"id":"EII:SOI-005","domain":"D04","related_domains":["D13"],"record_type":"family","variants":["organic_C_concentration","organic_C_stock"],"secondary":["measured","derived"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["state"],"routes":["amr"],"refs":["R03"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** SOC concentration and stock quantify organic C per dry soil mass and per area/depth respectively.
- **Direct observations / derivation:** Organic C assay, g/kg; stock from C, compatible density, layer thickness and coarse fragments, Mg C/ha.
- **Inference and limits:** Supports carbon-pool assessment; repeat stock comparisons require consistent depth or equivalent soil mass and uncertainty; neither % nor one survey proves sequestration.
- **Supporting indicators:** [EII:SOI-002](#soi-002), [EII:SOI-014](#soi-014), [EII:FUN-002](#fun-002).

<a id="soi-006"></a>

#### EII:SOI-006 — Soil pH

<!-- eii:{"id":"EII:SOI-006","domain":"D04","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Soil pH is acidity measured in a specified suspension.
- **Direct observations / derivation:** Electrode response, pH units; declare water/salt extract and soil:solution ratio.
- **Inference and limits:** Supports nutrient and microbial-habitat interpretation; assays are not interchangeable and pH alone does not establish fertility.
- **Supporting indicators:** [EII:SOI-008](#soi-008), [EII:SOI-009](#soi-009), [EII:MIC-001](#mic-001).

<a id="soi-007"></a>

#### EII:SOI-007 — Electrical conductivity / soil salinity

<!-- eii:{"id":"EII:SOI-007","domain":"D04","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","proxy"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["state"],"routes":["amr","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Soil EC measures ionic conductance in a declared extract or in situ.
- **Direct observations / derivation:** Conductivity, dS/m, with temperature and extraction basis; distinguish ECe and bulk apparent EC.
- **Inference and limits:** Supports salinity screening; moisture, clay and ions affect readings, so thresholds require a compatible method.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:SOI-001](#soi-001), [EII:SOI-019](#soi-019).

<a id="soi-008"></a>

#### EII:SOI-008 — Available nitrogen / phosphorus / potassium

<!-- eii:{"id":"EII:SOI-008","domain":"D04","related_domains":["D13"],"record_type":"family","variants":["extractable_mineral_N","method_defined_available_P","exchangeable_K"],"secondary":["measured"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Available N/P/K are method-defined nutrient fractions rather than total pools.
- **Direct observations / derivation:** Specified mineral-N extraction, P test and exchangeable-K assay, mg/kg with nutrient basis declared.
- **Inference and limits:** Supports agronomic nutrient assessment; availability depends on extraction, soil, crop, season and mineralisation.
- **Supporting indicators:** [EII:SOI-006](#soi-006), [EII:MIC-023](#mic-023), [EII:AGR-001](#agr-001).

<a id="soi-009"></a>

#### EII:SOI-009 — Cation exchange capacity

<!-- eii:{"id":"EII:SOI-009","domain":"D04","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** CEC is exchangeable-cation capacity under stated chemical conditions.
- **Direct observations / derivation:** Displacement/exchange assay, cmolc/kg; distinguish effective and buffered potential CEC.
- **Inference and limits:** Supports nutrient-buffering interpretation; charge, pH and mineralogy affect capacity and actual occupancy.
- **Supporting indicators:** [EII:SOI-006](#soi-006), [EII:SOI-001](#soi-001), [EII:SOI-019](#soi-019).

<a id="soi-013"></a>

#### EII:SOI-013 — Soil contamination / heavy metals

<!-- eii:{"id":"EII:SOI-013","domain":"D04","related_domains":["D13"],"record_type":"family","variants":["named_total_contaminant","named_extractable_contaminant"],"secondary":["measured","pressure"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["pressure"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Contamination records concentration of specified metals or organic pollutants.
- **Direct observations / derivation:** Validated chemical assay, mg/kg dry soil; report analyte, fraction and detection limits.
- **Inference and limits:** Supports exposure screening; total concentration does not establish bioavailability or food-chain transfer.
- **Supporting indicators:** [EII:SOI-006](#soi-006), [EII:SOI-005](#soi-005), [EII:SOI-022](#soi-022).

<a id="soi-018"></a>

#### EII:SOI-018 — Total soil nitrogen/C:N ratio

<!-- eii:{"id":"EII:SOI-018","domain":"D04","related_domains":["D13"],"record_type":"family","variants":["total_N","C_to_N_ratio"],"secondary":["measured","derived"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Total N pool and organic-C to total-N mass ratio.
- **Direct observations / derivation:** Elemental assays, g N/kg and dimensionless C:N, with matching sample basis.
- **Inference and limits:** Supports substrate/stoichiometric comparison; total N does not equal mineral-N availability and ratio alone does not determine immobilisation.
- **Supporting indicators:** [EII:SOI-005](#soi-005), [EII:SOI-008](#soi-008), [EII:MIC-023](#mic-023).

<a id="soi-019"></a>

#### EII:SOI-019 — Exchangeable sodium percentage/SAR

<!-- eii:{"id":"EII:SOI-019","domain":"D04","related_domains":["D13"],"record_type":"family","variants":["ESP","SAR"],"secondary":["derived","pressure"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["pressure"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Method-defined indices of sodium dominance in exchange or solution chemistry.
- **Direct observations / derivation:** ESP=100 exchangeable Na/CEC; SAR=Na/√((Ca+Mg)/2) with standard concentration basis.
- **Inference and limits:** Supports sodicity screening; EC, mineralogy and compatible extraction are needed to infer dispersion risk.
- **Supporting indicators:** [EII:SOI-007](#soi-007), [EII:SOI-009](#soi-009), [EII:SOI-003](#soi-003).

<a id="soi-020"></a>

#### EII:SOI-020 — Soil inorganic carbon

<!-- eii:{"id":"EII:SOI-020","domain":"D04","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Carbon held in carbonates and other inorganic forms on a specified basis.
- **Direct observations / derivation:** Carbonate/inorganic C assay, g C/kg; stocks need depth/density/coarse fractions.
- **Inference and limits:** Supports carbonate and C-budget assessment; carbonate accumulation is not automatically net atmospheric sequestration.
- **Supporting indicators:** [EII:SOI-005](#soi-005), [EII:SOI-006](#soi-006), [EII:FUN-002](#fun-002).

<a id="soi-021"></a>

#### EII:SOI-021 — Labile/particulate/mineral-associated organic carbon

<!-- eii:{"id":"EII:SOI-021","domain":"D04","related_domains":["D13"],"record_type":"family","variants":["labile_C","particulate_organic_C","mineral_associated_organic_C"],"secondary":["measured"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Distinct operational fractions of soil organic carbon.
- **Direct observations / derivation:** Declared oxidation or physical fractionation, g C/kg; record size/density cut-offs and recoveries.
- **Inference and limits:** Supports carbon-pool comparison; operational pools do not uniquely represent turnover time or permanence.
- **Supporting indicators:** [EII:SOI-005](#soi-005), [EII:SOI-001](#soi-001), [EII:MIC-024](#mic-024).

<a id="soi-022"></a>

#### EII:SOI-022 — Bioavailable contaminant fraction

<!-- eii:{"id":"EII:SOI-022","domain":"D04","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","proxy"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["state"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Method-defined mobile/extractable fraction of a named contaminant.
- **Direct observations / derivation:** Specified extraction, porewater or organism assay, mg/kg or µg/L.
- **Inference and limits:** Supports exposure refinement; extraction is an approximation and organism-specific uptake requires validation.
- **Supporting indicators:** [EII:SOI-013](#soi-013), [EII:SOI-006](#soi-006), [EII:SOI-005](#soi-005).

<a id="soi-023"></a>

#### EII:SOI-023 — Soil redox potential

<!-- eii:{"id":"EII:SOI-023","domain":"D04","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","proxy"],"tertiary":{"spatial":["sample","plot"],"temporal":["season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Electrode potential indicating local oxidation–reduction conditions.
- **Direct observations / derivation:** Calibrated redox electrodes, mV with reference electrode, pH, depth and equilibration.
- **Inference and limits:** Supports anaerobic-process interpretation; mixed potentials and microsites prevent unique chemical speciation.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:MIC-012](#mic-012), [EII:CYC-003](#cyc-003).

<a id="d05"></a>

### 5. Soil biology

<a id="soi-010"></a>

#### EII:SOI-010 — Soil respiration / CO₂ efflux

<!-- eii:{"id":"EII:SOI-010","domain":"D05","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","plot","community"],"temporal":["event","season","year"]},"quaternary":["function"],"routes":["iot","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Soil respiration is CO₂ release from soil under field or incubation conditions.
- **Direct observations / derivation:** Chamber/infrared gas flux, µmol CO₂/m²/s, or incubation mass C/kg/time; identify roots and heterotrophs when possible.
- **Inference and limits:** Indicates carbon turnover; high respiration can reflect productivity, warming or C loss and is not inherently healthier.
- **Supporting indicators:** [EII:MIC-007](#mic-007), [EII:SOI-005](#soi-005), [EII:HYD-001](#hyd-001), [EII:SOI-011](#soi-011).

<a id="mic-001"></a>

#### EII:MIC-001 — Bacterial community composition

<!-- eii:{"id":"EII:MIC-001","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":["R04","R05"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** Bacterial composition describes taxonomic representation within a microbial sample.
- **Direct observations / derivation:** 16S/shotgun reads assigned to taxa, proportions; absolute cells/g require independent calibration.
- **Inference and limits:** Supports community comparisons; primer, extraction, copy-number and compositional biases prevent equating reads with cells or function.
- **Supporting indicators:** [EII:MIC-005](#mic-005), [EII:MIC-025](#mic-025), [EII:SOI-006](#soi-006).

<a id="mic-002"></a>

#### EII:MIC-002 — Archaeal community composition

<!-- eii:{"id":"EII:MIC-002","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":["R04"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** Archaeal composition describes sampled archaeal taxonomic representation.
- **Direct observations / derivation:** Archaeal marker or shotgun assignments, proportions/copies with method declared.
- **Inference and limits:** Supports archaeal habitat/pathway hypotheses; taxonomy does not prove ammonia oxidation or methane production.
- **Supporting indicators:** [EII:MIC-011](#mic-011), [EII:CYC-003](#cyc-003), [EII:MIC-025](#mic-025).

<a id="mic-003"></a>

#### EII:MIC-003 — Fungal community composition

<!-- eii:{"id":"EII:MIC-003","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":["R04"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** Fungal composition describes sampled fungal taxonomic representation.
- **Direct observations / derivation:** ITS/shotgun assignments and relative profiles; record reference release and guild assignment confidence.
- **Inference and limits:** Supports fungal-community comparisons; guild labels and reads do not prove realised decomposition, symbiosis or disease.
- **Supporting indicators:** [EII:MIC-014](#mic-014), [EII:MIC-024](#mic-024), [EII:MIC-016](#mic-016).

<a id="mic-004"></a>

#### EII:MIC-004 — Protist community composition

<!-- eii:{"id":"EII:MIC-004","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":["R04"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** Protist composition describes sampled protistan taxonomic representation.
- **Direct observations / derivation:** 18S/shotgun assignments, relative profiles under stated pipeline.
- **Inference and limits:** Supports microbial-food-web hypotheses; marker coverage and taxonomic assignment limit functional interpretation.
- **Supporting indicators:** [EII:MIC-005](#mic-005), [EII:BIO-013](#bio-013), [EII:MIC-025](#mic-025).

<a id="mic-005"></a>

#### EII:MIC-005 — Microbial alpha diversity

<!-- eii:{"id":"EII:MIC-005","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Microbial alpha diversity summarises within-sample richness/evenness.
- **Direct observations / derivation:** ASV/taxon table and specified richness, Shannon or Hill metric; standardise coverage and filtering.
- **Inference and limits:** Supports within-sample comparisons; increased diversity is not universally improved soil function.
- **Supporting indicators:** [EII:MIC-001](#mic-001), [EII:MIC-003](#mic-003), [EII:MIC-007](#mic-007).

<a id="mic-006"></a>

#### EII:MIC-006 — Microbial beta diversity

<!-- eii:{"id":"EII:MIC-006","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Microbial beta diversity describes compositional dissimilarity between samples.
- **Direct observations / derivation:** Taxon profiles and declared Bray–Curtis, Jaccard, UniFrac or compositional distance.
- **Inference and limits:** Supports community differentiation; dispersion, sequencing coverage and environmental confounding affect tests.
- **Supporting indicators:** [EII:MIC-005](#mic-005), [EII:MIC-020](#mic-020), [EII:SOI-006](#soi-006).

<a id="mic-007"></a>

#### EII:MIC-007 — Microbial biomass carbon / nitrogen

<!-- eii:{"id":"EII:MIC-007","domain":"D05","related_domains":["D13"],"record_type":"family","variants":["microbial_biomass_C","microbial_biomass_N"],"secondary":["measured"],"tertiary":{"spatial":["sample","plot","community"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Microbial biomass C/N estimates living microbial carbon/nitrogen pools.
- **Direct observations / derivation:** Fumigation-extraction or specified biomass assay, mg C or N/kg dry soil, with conversion factors.
- **Inference and limits:** Supports biomass-pool comparison; method recovery and soil moisture matter, and biomass is not process efficiency.
- **Supporting indicators:** [EII:SOI-005](#soi-005), [EII:SOI-010](#soi-010), [EII:MIC-019](#mic-019).

<a id="mic-008"></a>

#### EII:MIC-008 — Fungal:bacterial abundance ratio

<!-- eii:{"id":"EII:MIC-008","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":["R05"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** Fungal:bacterial ratio compares two method-defined microbial signals.
- **Direct observations / derivation:** PLFA biomarkers, calibrated qPCR or other declared abundance measures, ratio; avoid raw cross-marker read ratios.
- **Inference and limits:** Supports broad community comparison within a consistent assay; ratios do not establish health or functional dominance.
- **Supporting indicators:** [EII:MIC-007](#mic-007), [EII:MIC-003](#mic-003), [EII:MIC-001](#mic-001).

<a id="mic-019"></a>

#### EII:MIC-019 — Extracellular enzyme activity

<!-- eii:{"id":"EII:MIC-019","domain":"D05","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample"],"temporal":["assay_interval","sampling_event"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Extracellular enzyme activity is substrate conversion under a specified assay.
- **Direct observations / derivation:** Fluorometric/colorimetric product formation per dry soil mass/time, nmol/g/h; declare substrate, pH and temperature.
- **Inference and limits:** Measures assay activity; often potential activity at supplied substrate levels rather than in situ flux.
- **Supporting indicators:** [EII:SOI-011](#soi-011), [EII:SOI-006](#soi-006), [EII:MIC-024](#mic-024).

<a id="mic-020"></a>

#### EII:MIC-020 — Community turnover along land-use gradients

<!-- eii:{"id":"EII:MIC-020","domain":"D05","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio","land","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Land-use community turnover describes microbial differences along independently recorded management gradients.
- **Direct observations / derivation:** Matched taxon profiles and land-use data, dissimilarity/effect size with repeated or paired design.
- **Inference and limits:** Supports land-use associations; confounded soil, geography and season do not establish management causality.
- **Supporting indicators:** [EII:MIC-006](#mic-006), [EII:DIS-004](#dis-004), [EII:SOI-006](#soi-006).

<a id="mic-021"></a>

#### EII:MIC-021 — Spatial microbial community similarity / connectivity

<!-- eii:{"id":"EII:MIC-021","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","modelled"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Spatial similarity/connectivity describes community distance relationships or tested movement estimates.
- **Direct observations / derivation:** Taxon dissimilarity versus geographic/environmental distance; connectivity only with explicit model or tracing evidence.
- **Inference and limits:** Supports biogeographic pattern assessment; similarity or co-occurrence is not proof of dispersal or interaction.
- **Supporting indicators:** [EII:MIC-006](#mic-006), [EII:BIO-007](#bio-007), [EII:SOI-001](#soi-001).

<a id="mic-022"></a>

#### EII:MIC-022 — Metatranscriptomic expression of functional genes

<!-- eii:{"id":"EII:MIC-022","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":["R04"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** Metatranscriptomic expression describes sampled community RNA assigned to genes.
- **Direct observations / derivation:** RNA reads with stated normalisation and matched DNA abundance where possible; report preservation and controls.
- **Inference and limits:** Supports transcription-at-sampling interpretation; RNA quantity does not establish translated enzyme activity or process flux.
- **Supporting indicators:** [EII:MIC-009](#mic-009), [EII:MIC-019](#mic-019), [EII:MIC-023](#mic-023).

<a id="mic-025"></a>

#### EII:MIC-025 — Absolute microbial load

<!-- eii:{"id":"EII:MIC-025","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":["R05"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** Number or biomass of microbial cells in a defined soil/sample quantity.
- **Direct observations / derivation:** Calibrated flow counts, spike-in sequencing or validated qPCR, cells/g or copies/g; gene copies are not automatically cells.
- **Inference and limits:** Supports interpretation of relative profiles; extraction recovery, viability and copy number remain method-dependent.
- **Supporting indicators:** [EII:MIC-001](#mic-001), [EII:MIC-007](#mic-007), [EII:MIC-005](#mic-005).

<a id="mic-026"></a>

#### EII:MIC-026 — Soil fauna abundance/biomass

<!-- eii:{"id":"EII:MIC-026","domain":"D05","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["sample","plot","community"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Abundance or dry mass of defined soil-animal groups.
- **Direct observations / derivation:** Standardised cores/extraction/hand sorting, individuals/m² or g/m², with depth and season.
- **Inference and limits:** Supports below-ground community assessment; extraction efficiency varies and total abundance does not identify function.
- **Supporting indicators:** [EII:MIC-024](#mic-024), [EII:SOI-003](#soi-003), [EII:MIC-027](#mic-027).

<a id="mic-027"></a>

#### EII:MIC-027 — Nematode trophic composition

<!-- eii:{"id":"EII:MIC-027","domain":"D05","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Relative representation of identified nematode feeding guilds.
- **Direct observations / derivation:** Extracted counts and validated guild assignment, proportions; derived indices require stated rules.
- **Inference and limits:** Supports soil-food-web comparison; guild uncertainty, season and extraction bias affect inference.
- **Supporting indicators:** [EII:MIC-026](#mic-026), [EII:MIC-007](#mic-007), [EII:BIO-013](#bio-013).

<a id="mic-028"></a>

#### EII:MIC-028 — Metaproteomic functional profile

<!-- eii:{"id":"EII:MIC-028","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Proteins detected and assigned to functions in a sample.
- **Direct observations / derivation:** Mass-spectrometry peptide identifications/intensities with reference database and false-discovery control.
- **Inference and limits:** Supports protein-presence assessment; detection does not itself quantify catalytic flux or species-specific activity.
- **Supporting indicators:** [EII:MIC-022](#mic-022), [EII:MIC-019](#mic-019), [EII:MIC-023](#mic-023).

<a id="mic-029"></a>

#### EII:MIC-029 — Metabolomic profile

<!-- eii:{"id":"EII:MIC-029","domain":"D05","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Detected concentrations or relative signals of specified metabolites.
- **Direct observations / derivation:** Targeted/untargeted assays, molar concentration or normalised intensity; distinguish confirmed from putative identities.
- **Inference and limits:** Supports biochemical-state hypotheses; pools integrate production, consumption and transport rather than proving flux.
- **Supporting indicators:** [EII:MIC-028](#mic-028), [EII:MIC-023](#mic-023), [EII:SOI-010](#soi-010).

<a id="mic-030"></a>

#### EII:MIC-030 — Microbial carbon-use efficiency

<!-- eii:{"id":"EII:MIC-030","domain":"D05","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["function"],"routes":["bio","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fraction of assimilated carbon allocated to microbial growth under a defined method.
- **Direct observations / derivation:** Growth and respiration from matched tracer/assay, growth/(growth+respiration) where applicable, fraction.
- **Inference and limits:** Supports allocation-efficiency comparison; method, substrate and timescale alter estimates and field carbon persistence needs additional evidence.
- **Supporting indicators:** [EII:MIC-007](#mic-007), [EII:SOI-010](#soi-010), [EII:SOI-021](#soi-021).

<a id="d06"></a>

### 6. Biodiversity

<a id="bio-001"></a>

#### EII:BIO-001 — Species richness

<!-- eii:{"id":"EII:BIO-001","domain":"D06","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Species richness is the number of distinct taxa in a declared sampling unit.
- **Direct observations / derivation:** Standardised taxon detections and effort, species count; state coverage and taxonomic resolution.
- **Inference and limits:** Supports detected diversity comparison; incomplete detection and effort prevent treating counts as total richness.
- **Supporting indicators:** [EII:BIO-002](#bio-002), [EII:BIO-003](#bio-003), [EII:VEG-017](#veg-017).

<a id="bio-002"></a>

#### EII:BIO-002 — Species abundance / occupancy

<!-- eii:{"id":"EII:BIO-002","domain":"D06","related_domains":[],"record_type":"family","variants":["population_abundance","modelled_occupancy"],"secondary":["observed","modelled"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Abundance and occupancy are separate population quantities.
- **Direct observations / derivation:** Counts/density and repeated detection histories; occupancy estimated with an explicit detection model, individuals/area or probability.
- **Inference and limits:** Supports population status; detection/non-detection or sequence reads alone do not equal abundance or occupancy.
- **Supporting indicators:** [EII:BIO-001](#bio-001), [EII:BIO-014](#bio-014), [EII:BIO-011](#bio-011).

<a id="bio-003"></a>

#### EII:BIO-003 — Shannon / Simpson diversity

<!-- eii:{"id":"EII:BIO-003","domain":"D06","related_domains":[],"record_type":"family","variants":["Shannon_H","Simpson_concentration","Simpson_complement","inverse_Simpson"],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Shannon/Simpson indices summarise taxon abundance distribution.
- **Direct observations / derivation:** H=−Σp ln p; Simpson specify concentration Σp², complement or reciprocal; dimensionless.
- **Inference and limits:** Supports richness/evenness comparison; formulas and effort must match and one index does not establish integrity.
- **Supporting indicators:** [EII:BIO-001](#bio-001), [EII:BIO-002](#bio-002), [EII:BIO-004](#bio-004).

<a id="bio-004"></a>

#### EII:BIO-004 — Functional diversity

<!-- eii:{"id":"EII:BIO-004","domain":"D06","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Functional diversity describes variation in measured organism traits.
- **Direct observations / derivation:** Trait values, abundance weights and declared metric such as functional dispersion or Rao Q.
- **Inference and limits:** Supports functional-composition comparisons; trait gaps and redundancy prevent equating diversity with process rate.
- **Supporting indicators:** [EII:BIO-001](#bio-001), [EII:VEG-017](#veg-017), [EII:FUN-001](#fun-001).

<a id="bio-005"></a>

#### EII:BIO-005 — Habitat area / quality

<!-- eii:{"id":"EII:BIO-005","domain":"D06","related_domains":[],"record_type":"family","variants":["habitat_extent","reference_based_quality"],"secondary":["derived","modelled"],"tertiary":{"spatial":["organism","population","community","landscape"],"temporal":["season","year"]},"quaternary":["state"],"routes":["land"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Habitat area and quality describe extent and separately assessed condition for a target ecosystem/taxon.
- **Direct observations / derivation:** Validated habitat polygons, ha; quality from explicit field attributes/reference model, declared units.
- **Inference and limits:** Supports habitat assessment; class labels or area do not prove suitability or integrity for every species.
- **Supporting indicators:** [EII:BIO-002](#bio-002), [EII:TER-013](#ter-013), [EII:FUN-013](#fun-013).

<a id="bio-010"></a>

#### EII:BIO-010 — Invasive species presence / spread

<!-- eii:{"id":"EII:BIO-010","domain":"D06","related_domains":[],"record_type":"indicator","variants":[],"secondary":["observed","derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio","land"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Invasive occurrence/spread records detection and changing distribution of a declared invasive taxon.
- **Direct observations / derivation:** Verified occurrence/cover maps and repeat surveys, area or km/year; distinguish non-native from invasive.
- **Inference and limits:** Supports invasion surveillance; detections do not by themselves establish ecological impact or absence elsewhere.
- **Supporting indicators:** [EII:BIO-002](#bio-002), [EII:DIS-005](#dis-005), [EII:BIO-005](#bio-005).

<a id="bio-011"></a>

#### EII:BIO-011 — Indicator / threatened species occurrence

<!-- eii:{"id":"EII:BIO-011","domain":"D06","related_domains":[],"record_type":"indicator","variants":[],"secondary":["observed"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Indicator/threatened occurrence records verified presence of taxa with a declared status or association.
- **Direct observations / derivation:** Validated observations or eDNA detections with blanks, date, coordinates and status-list version.
- **Inference and limits:** Supports conservation screening; non-detection is not absence and indicator associations require local validation.
- **Supporting indicators:** [EII:BIO-002](#bio-002), [EII:BIO-005](#bio-005), [EII:BIO-014](#bio-014).

<a id="bio-012"></a>

#### EII:BIO-012 — Acoustic biodiversity / soundscape indices

<!-- eii:{"id":"EII:BIO-012","domain":"D06","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","population","community","landscape"],"temporal":["season","year"]},"quaternary":["state"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Soundscape indices summarise defined acoustic energy/complexity patterns.
- **Direct observations / derivation:** Calibrated recordings and a specified acoustic index, dimensionless; distinguish classified calls from generic sound metrics.
- **Inference and limits:** Supports acoustic-activity comparison; wind, rain and anthropogenic noise prevent treating an index as species richness.
- **Supporting indicators:** [EII:BIO-001](#bio-001), [EII:BIO-002](#bio-002), [EII:HUM-008](#hum-008).

<a id="bio-014"></a>

#### EII:BIO-014 — Environmental-DNA taxon detection

<!-- eii:{"id":"EII:BIO-014","domain":"D06","related_domains":[],"record_type":"indicator","variants":[],"secondary":["observed","derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Presence of taxon-associated DNA in a defined environmental sample.
- **Direct observations / derivation:** Validated sequence/qPCR detections with field/extraction blanks and replicates, detection or copies/volume.
- **Inference and limits:** Supports occurrence surveillance; DNA transport, persistence and contamination prevent assuming local living abundance.
- **Supporting indicators:** [EII:BIO-002](#bio-002), [EII:HYD-006](#hyd-006), [EII:BIO-011](#bio-011).

<a id="bio-015"></a>

#### EII:BIO-015 — Genetic diversity/population differentiation

<!-- eii:{"id":"EII:BIO-015","domain":"D06","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Variation within and among sampled populations at specified loci.
- **Direct observations / derivation:** Genotypes, heterozygosity, nucleotide diversity or FST with locus/sample design recorded.
- **Inference and limits:** Supports population genetic comparisons; demographic history, sampling and selection confound connectivity interpretations.
- **Supporting indicators:** [EII:BIO-007](#bio-007), [EII:BIO-002](#bio-002), [EII:BIO-016](#bio-016).

<a id="bio-016"></a>

#### EII:BIO-016 — Population growth/recruitment/survival

<!-- eii:{"id":"EII:BIO-016","domain":"D06","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","modelled","process"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["function"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Separate demographic rates for a focal species and interval.
- **Direct observations / derivation:** Repeated counts, marked individuals or age cohorts; λ, recruits/area/time and survival probability.
- **Inference and limits:** Supports population trajectory assessment; detection, migration and age structure require modelling.
- **Supporting indicators:** [EII:BIO-002](#bio-002), [EII:BIO-005](#bio-005), [EII:BIO-011](#bio-011).

<a id="bio-017"></a>

#### EII:BIO-017 — Community-weighted traits

<!-- eii:{"id":"EII:BIO-017","domain":"D06","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Abundance-weighted trait mean of a defined community.
- **Direct observations / derivation:** Species trait table and comparable abundance weights; units of the selected trait.
- **Inference and limits:** Supports trait-composition interpretation; database gaps and within-species variability affect accuracy.
- **Supporting indicators:** [EII:BIO-004](#bio-004), [EII:BIO-002](#bio-002), [EII:VEG-017](#veg-017).

<a id="bio-018"></a>

#### EII:BIO-018 — Freshwater macroinvertebrate composition

<!-- eii:{"id":"EII:BIO-018","domain":"D06","related_domains":[],"record_type":"indicator","variants":[],"secondary":["observed","derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Taxonomic/functional composition in standardised aquatic samples.
- **Direct observations / derivation:** Kick/core sampling and identification, abundance and declared region-specific index if used.
- **Inference and limits:** Supports aquatic-condition assessment; substrate, season and sampling method require reference-specific interpretation.
- **Supporting indicators:** [EII:HYD-013](#hyd-013), [EII:HYD-010](#hyd-010), [EII:HYD-006](#hyd-006).

<a id="bio-019"></a>

#### EII:BIO-019 — Live coral cover/bleaching prevalence

<!-- eii:{"id":"EII:BIO-019","domain":"D06","related_domains":[],"record_type":"family","variants":["live_coral_cover","bleaching_prevalence"],"secondary":["measured"],"tertiary":{"spatial":["organism","population","community","landscape"],"temporal":["season","year"]},"quaternary":["state"],"routes":["reef","marine"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Proportion of substrate with living coral and proportion of observed colonies bleached.
- **Direct observations / derivation:** Validated transect/photo observations, % with depth and denominator stated.
- **Inference and limits:** Supports reef-condition assessment; habitat class maps do not directly measure live cover, bleaching or mortality.
- **Supporting indicators:** [EII:HYD-015](#hyd-015), [EII:HYD-022](#hyd-022), [EII:BIO-005](#bio-005).

<a id="bio-020"></a>

#### EII:BIO-020 — Mangrove extent/condition

<!-- eii:{"id":"EII:BIO-020","domain":"D06","related_domains":[],"record_type":"family","variants":["mangrove_extent","specified_condition_attribute"],"secondary":["derived","measured"],"tertiary":{"spatial":["organism","population","community","landscape"],"temporal":["season","year"]},"quaternary":["state"],"routes":["mangrove"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Area of mangrove habitat and separately assessed structural/physiological condition.
- **Direct observations / derivation:** Validated maps, ha; field canopy, mortality or salinity observations in declared units.
- **Inference and limits:** Supports coastal habitat assessment; area stability does not imply unchanged condition or function.
- **Supporting indicators:** [EII:BIO-005](#bio-005), [EII:TER-013](#ter-013), [EII:HYD-011](#hyd-011).

<a id="d07"></a>

### 7. Vegetation

<a id="veg-001"></a>

#### EII:VEG-001 — Normalised Difference Vegetation Index (NDVI)

<!-- eii:{"id":"EII:VEG-001","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["opt"],"refs":["R12"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** NDVI is the normalised contrast between near-infrared and red reflectance.
- **Direct observations / derivation:** (NIR-red)/(NIR+red), dimensionless, from masked surface-reflectance bands.
- **Inference and limits:** Supports comparison of green vegetation and seasonal vigour; saturation, soil background and species prevent diagnosis of health or biomass alone.
- **Supporting indicators:** [EII:VEG-011](#veg-011), [EII:VEG-012](#veg-012), [EII:VEG-013](#veg-013), [EII:HYD-001](#hyd-001).

<a id="veg-002"></a>

#### EII:VEG-002 — Green Normalised Difference Vegetation Index (GNDVI)

<!-- eii:{"id":"EII:VEG-002","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["opt"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** GNDVI substitutes green for red in a normalised vegetation contrast.
- **Direct observations / derivation:** (NIR-green)/(NIR+green), dimensionless reflectance ratio.
- **Inference and limits:** Can track chlorophyll-related variation after crop-specific calibration; canopy structure and illumination confound interpretation.
- **Supporting indicators:** [EII:VEG-013](#veg-013), [EII:VEG-011](#veg-011), [EII:SOI-008](#soi-008).

<a id="veg-003"></a>

#### EII:VEG-003 — Normalised Difference Red Edge Index (NDRE)

<!-- eii:{"id":"EII:VEG-003","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["rededge"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** NDRE contrasts near-infrared with red-edge reflectance.
- **Direct observations / derivation:** (NIR-rededge)/(NIR+rededge), dimensionless; record exact band wavelengths.
- **Inference and limits:** Supports chlorophyll-related canopy comparisons; sensor band choice, leaf area and species affect response.
- **Supporting indicators:** [EII:VEG-013](#veg-013), [EII:VEG-011](#veg-011), [EII:VEG-017](#veg-017).

<a id="veg-004"></a>

#### EII:VEG-004 — Soil Adjusted Vegetation Index (SAVI)

<!-- eii:{"id":"EII:VEG-004","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["opt"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** SAVI adjusts a red–NIR vegetation contrast for soil background.
- **Direct observations / derivation:** (1+L)(NIR-red)/(NIR+red+L), dimensionless; declare L and reflectance scaling.
- **Inference and limits:** Improves comparison where vegetation is sparse; adjustment does not remove all soil or atmospheric effects.
- **Supporting indicators:** [EII:VEG-012](#veg-012), [EII:VEG-001](#veg-001), [EII:SOI-001](#soi-001).

<a id="veg-005"></a>

#### EII:VEG-005 — Enhanced Vegetation Index (EVI)

<!-- eii:{"id":"EII:VEG-005","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["opt"],"refs":["R01"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** EVI uses red, blue and NIR bands with background and atmospheric resistance terms.
- **Direct observations / derivation:** 2.5(NIR-red)/(NIR+6red-7.5blue+1), dimensionless, for the standard three-band form.
- **Inference and limits:** Supports greenness comparisons in dense vegetation; cloud, aerosols and processing still matter.
- **Supporting indicators:** [EII:VEG-001](#veg-001), [EII:VEG-011](#veg-011), [EII:VEG-012](#veg-012).

<a id="veg-006"></a>

#### EII:VEG-006 — Green–Red Vegetation Index (GRVI)

<!-- eii:{"id":"EII:VEG-006","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["rgb"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** GRVI is the normalised green–red contrast.
- **Direct observations / derivation:** (green-red)/(green+red), dimensionless; calibrated RGB preferred.
- **Inference and limits:** Indicates visible greenness, not photosynthesis directly; shade and camera colour processing confound comparisons.
- **Supporting indicators:** [EII:VEG-012](#veg-012), [EII:VEG-013](#veg-013), [EII:VEG-001](#veg-001).

<a id="veg-007"></a>

#### EII:VEG-007 — Excess Green (ExG)

<!-- eii:{"id":"EII:VEG-007","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["rgb"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** ExG enhances green relative to red and blue for vegetation segmentation.
- **Direct observations / derivation:** 2g-r-b using normalised RGB channels, dimensionless; record normalisation and threshold.
- **Inference and limits:** Supports green-cover segmentation; threshold accuracy depends on illumination and background.
- **Supporting indicators:** [EII:VEG-012](#veg-012), [EII:VEG-006](#veg-006), [EII:VEG-017](#veg-017).

<a id="veg-008"></a>

#### EII:VEG-008 — Visible Atmospherically Resistant Index (VARI)

<!-- eii:{"id":"EII:VEG-008","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["rgb"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** VARI uses a visible-band contrast with a blue-band correction.
- **Direct observations / derivation:** (green-red)/(green+red-blue), dimensionless; mask near-zero denominators.
- **Inference and limits:** Supports visible green-cover comparisons; atmospheric resistance is limited and does not guarantee radiometric comparability.
- **Supporting indicators:** [EII:VEG-012](#veg-012), [EII:VEG-006](#veg-006), [EII:VEG-001](#veg-001).

<a id="veg-009"></a>

#### EII:VEG-009 — Green Leaf Index (GLI)

<!-- eii:{"id":"EII:VEG-009","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["rgb"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** GLI enhances green relative to the other visible channels.
- **Direct observations / derivation:** (2green-red-blue)/(2green+red+blue), dimensionless.
- **Inference and limits:** Supports foliage segmentation; camera calibration and shadow determine accuracy.
- **Supporting indicators:** [EII:VEG-012](#veg-012), [EII:VEG-007](#veg-007), [EII:VEG-017](#veg-017).

<a id="veg-010"></a>

#### EII:VEG-010 — Red–Green–Blue Vegetation Index (RGBVI)

<!-- eii:{"id":"EII:VEG-010","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["rgb"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** RGBVI contrasts squared green against red–blue products.
- **Direct observations / derivation:** (green²-red×blue)/(green²+red×blue), dimensionless; record channel treatment.
- **Inference and limits:** Can distinguish vegetation from backgrounds; not a direct chlorophyll or productivity measurement.
- **Supporting indicators:** [EII:VEG-012](#veg-012), [EII:VEG-013](#veg-013), [EII:VEG-001](#veg-001).

<a id="veg-011"></a>

#### EII:VEG-011 — Leaf Area Index (LAI)

<!-- eii:{"id":"EII:VEG-011","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","modelled"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["veg"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** LAI is leaf area per unit ground area, with convention declared.
- **Direct observations / derivation:** Leaf area and ground area, m²/m²; destructive sampling, optical gap inversion or calibrated remote estimation.
- **Inference and limits:** Represents canopy development and potential light interception; clumping and woody material bias optical estimates.
- **Supporting indicators:** [EII:VEG-012](#veg-012), [EII:TER-013](#ter-013), [EII:VEG-014](#veg-014).

<a id="veg-012"></a>

#### EII:VEG-012 — Fractional vegetation / ground cover

<!-- eii:{"id":"EII:VEG-012","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["observed","derived"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["veg"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fractional cover is the proportion of a defined surface occupied by vegetation.
- **Direct observations / derivation:** Point-intercept counts or classified pixels, fraction or %; distinguish green, total, ground and crown cover.
- **Inference and limits:** Supports assessment of soil exposure and habitat structure; equal cover need not imply equal biomass or diversity.
- **Supporting indicators:** [EII:VEG-017](#veg-017), [EII:SOI-012](#soi-012), [EII:FUN-005](#fun-005).

<a id="veg-013"></a>

#### EII:VEG-013 — Canopy chlorophyll content

<!-- eii:{"id":"EII:VEG-013","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","modelled"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["veg"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Canopy chlorophyll content describes chlorophyll quantity on a declared leaf or ground-area basis.
- **Direct observations / derivation:** Pigment extraction, calibrated chlorophyll meters or spectral inversion, mg/m²; meter units require calibration.
- **Inference and limits:** Supports assessment of pigment status; nutrient limitation, age, stress and species can produce similar changes.
- **Supporting indicators:** [EII:VEG-011](#veg-011), [EII:SOI-008](#soi-008), [EII:VEG-015](#veg-015).

<a id="veg-014"></a>

#### EII:VEG-014 — Above-ground biomass

<!-- eii:{"id":"EII:VEG-014","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","modelled"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["veg"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Above-ground biomass is dry living plant mass above the soil surface.
- **Direct observations / derivation:** Harvest dry mass, kg/m² or Mg/ha; inventories and LiDAR require validated allometry.
- **Inference and limits:** Supports carbon-pool and fuel estimates; water content, dead biomass and allometric uncertainty must be separated.
- **Supporting indicators:** [EII:TER-010](#ter-010), [EII:TER-011](#ter-011), [EII:VEG-017](#veg-017), [EII:DIS-002](#dis-002).

<a id="veg-015"></a>

#### EII:VEG-015 — Plant water stress / canopy temperature anomaly

<!-- eii:{"id":"EII:VEG-015","domain":"D07","related_domains":[],"record_type":"family","variants":["canopy_temperature_anomaly","validated_water_stress_index"],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["thermal","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Canopy temperature anomaly compares canopy temperature with air or a reference canopy.
- **Direct observations / derivation:** Thermal radiance converted to temperature and reference temperature, °C difference; stress indices require stated wet/dry baselines.
- **Inference and limits:** May indicate reduced transpiration or heat exposure; radiation, wind and architecture also affect temperature.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:HYD-012](#hyd-012), [EII:ATM-003](#atm-003), [EII:ATM-005](#atm-005).

<a id="veg-016"></a>

#### EII:VEG-016 — Phenology / green-up / senescence dates

<!-- eii:{"id":"EII:VEG-016","domain":"D07","related_domains":[],"record_type":"family","variants":["green_up_date","senescence_date","season_duration"],"secondary":["observed","derived"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["veg"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Phenological dates locate seasonal events such as green-up and senescence.
- **Direct observations / derivation:** Repeated observations or fitted vegetation-index curves, day-of-year and duration in days; declare event threshold.
- **Inference and limits:** Reveals seasonal shifts; cloud gaps, mixed vegetation and crop calendars can mimic climatic responses.
- **Supporting indicators:** [EII:VEG-001](#veg-001), [EII:DIS-006](#dis-006), [EII:VEG-017](#veg-017).

<a id="veg-017"></a>

#### EII:VEG-017 — Species / cultivar composition

<!-- eii:{"id":"EII:VEG-017","domain":"D07","related_domains":["D13"],"record_type":"family","variants":["species_composition","cultivar_composition"],"secondary":["observed","derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["veg","bio","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Species/cultivar composition records plant identity and relative representation.
- **Direct observations / derivation:** Botanical counts, cover estimates or validated molecular assignments, taxa and proportions.
- **Inference and limits:** Supports community and crop comparisons; remote classes rarely resolve cultivars without validation.
- **Supporting indicators:** [EII:BIO-001](#bio-001), [EII:BIO-004](#bio-004), [EII:VEG-016](#veg-016).

<a id="ter-010"></a>

#### EII:TER-010 — Tree height

<!-- eii:{"id":"EII:TER-010","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["organism","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Tree height is vertical distance from ground to tree top.
- **Direct observations / derivation:** Field range measurements or canopy-minus-ground heights, m.
- **Inference and limits:** Supports stand development and biomass estimation; occlusion and ground errors propagate.
- **Supporting indicators:** [EII:VEG-014](#veg-014), [EII:TER-011](#ter-011), [EII:VEG-017](#veg-017).

<a id="ter-011"></a>

#### EII:TER-011 — Canopy volume

<!-- eii:{"id":"EII:TER-011","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot"],"temporal":["event","season","year"]},"quaternary":["state"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Canopy volume is a defined three-dimensional crown envelope.
- **Direct observations / derivation:** Point-cloud crown segmentation and volume algorithm, m³; declare convex hull/voxel method.
- **Inference and limits:** Supports crown architecture comparison; envelope volume is not woody mass or leaf area.
- **Supporting indicators:** [EII:TER-010](#ter-010), [EII:VEG-014](#veg-014), [EII:VEG-011](#veg-011).

<a id="ter-012"></a>

#### EII:TER-012 — Canopy gaps / crown cover

<!-- eii:{"id":"EII:TER-012","domain":"D07","related_domains":[],"record_type":"family","variants":["gap_fraction","crown_cover"],"secondary":["derived"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["terrain","veg"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Canopy gaps/crown cover quantify projected crowns and openings.
- **Direct observations / derivation:** Mapped crown/gap area divided by plot area, %, with minimum gap definition.
- **Inference and limits:** Supports light and regeneration interpretation; projected cover differs from leaf area and understory cover.
- **Supporting indicators:** [EII:VEG-011](#veg-011), [EII:TER-013](#ter-013), [EII:BIO-005](#bio-005).

<a id="ter-013"></a>

#### EII:TER-013 — Vertical vegetation complexity

<!-- eii:{"id":"EII:TER-013","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Vertical vegetation complexity describes vegetation distribution through height strata.
- **Direct observations / derivation:** Height-bin returns, foliage profiles or stated structural diversity index, proportions or index.
- **Inference and limits:** Supports habitat and vertical fuel interpretation; LiDAR sampling and sensor geometry affect profiles.
- **Supporting indicators:** [EII:TER-010](#ter-010), [EII:DIS-002](#dis-002), [EII:BIO-004](#bio-004).

<a id="hyd-002"></a>

#### EII:HYD-002 — Normalised Difference Moisture Index (NDMI)

<!-- eii:{"id":"EII:HYD-002","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["opt"],"refs":["R11"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** NDMI contrasts near-infrared with shortwave-infrared reflectance.
- **Direct observations / derivation:** (NIR-SWIR1)/(NIR+SWIR1), dimensionless; declare wavelengths and alias conventions.
- **Inference and limits:** Supports canopy moisture comparisons; leaf area, soil exposure and species confound water-status inference.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:VEG-011](#veg-011), [EII:VEG-015](#veg-015).

<a id="dis-012"></a>

#### EII:DIS-012 — Hyperspectral material / vegetation trait signatures

<!-- eii:{"id":"EII:DIS-012","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Hyperspectral signatures are densely sampled spectral observations used for trait/material retrieval.
- **Direct observations / derivation:** Spectral radiance/reflectance by wavelength; traits require calibrated inversion, declared trait units.
- **Inference and limits:** Supports material/trait hypotheses; spectra are not uniquely diagnostic without independent samples and validation.
- **Supporting indicators:** [EII:VEG-013](#veg-013), [EII:SOI-005](#soi-005), [EII:VEG-017](#veg-017).

<a id="veg-018"></a>

#### EII:VEG-018 — Fraction of absorbed PAR

<!-- eii:{"id":"EII:VEG-018","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","modelled"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["veg"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fraction of incoming photosynthetic radiation absorbed by vegetation.
- **Direct observations / derivation:** Above/below-canopy radiation measurements or validated retrieval, fraction; specify green versus total absorption.
- **Inference and limits:** Supports light-use production models; absorption is not conversion into fixed carbon.
- **Supporting indicators:** [EII:ATM-004](#atm-004), [EII:VEG-011](#veg-011), [EII:FUN-001](#fun-001).

<a id="veg-019"></a>

#### EII:VEG-019 — Solar-induced chlorophyll fluorescence

<!-- eii:{"id":"EII:VEG-019","domain":"D07","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Radiance emitted by chlorophyll following solar excitation.
- **Direct observations / derivation:** Spectrally resolved retrieval, mW/m²/sr/nm with wavelength/geometry specified.
- **Inference and limits:** Supports photosynthetic-state assessment; canopy escape probability and energy partitioning prevent a universal GPP conversion.
- **Supporting indicators:** [EII:FUN-001](#fun-001), [EII:ATM-004](#atm-004), [EII:VEG-013](#veg-013).

<a id="veg-020"></a>

#### EII:VEG-020 — Leaf water potential/stomatal conductance

<!-- eii:{"id":"EII:VEG-020","domain":"D07","related_domains":["D13"],"record_type":"family","variants":["leaf_water_potential","stomatal_conductance"],"secondary":["measured","process"],"tertiary":{"spatial":["organism","plot"],"temporal":["event","season","year"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Separate measures of plant water-energy state and leaf gas-exchange conductance.
- **Direct observations / derivation:** Pressure chamber, MPa; porometer/gas exchange, mol H₂O/m²/s, recording time and conditions.
- **Inference and limits:** Supports physiological water-stress assessment; species, leaf age and atmospheric demand affect response.
- **Supporting indicators:** [EII:SOI-016](#soi-016), [EII:ATM-003](#atm-003), [EII:VEG-015](#veg-015).

<a id="veg-021"></a>

#### EII:VEG-021 — Plant mortality/recruitment

<!-- eii:{"id":"EII:VEG-021","domain":"D07","related_domains":[],"record_type":"family","variants":["mortality_rate","recruitment_rate"],"secondary":["measured","process"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["function"],"routes":["veg"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Rates of death and establishment in a defined plant population.
- **Direct observations / derivation:** Repeated mapped stems/seedlings, %/year or individuals/ha/year.
- **Inference and limits:** Supports stand demographic assessment; delayed detection and seedling-to-adult transitions must be considered.
- **Supporting indicators:** [EII:VEG-017](#veg-017), [EII:BIO-016](#bio-016), [EII:DIS-009](#dis-009).

<a id="veg-022"></a>

#### EII:VEG-022 — Root biomass/depth distribution

<!-- eii:{"id":"EII:VEG-022","domain":"D07","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured"],"tertiary":{"spatial":["organism","plot","landscape"],"temporal":["day","season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Root dry mass and allocation through soil depth.
- **Direct observations / derivation:** Washed cores, ingrowth methods or calibrated imaging, g/m² by depth; distinguish live/dead and diameter classes.
- **Inference and limits:** Supports below-ground allocation/rooting assessment; sampling misses spatial heterogeneity and standing mass does not equal uptake.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:SOI-014](#soi-014), [EII:VEG-020](#veg-020).

<a id="d08"></a>

### 8. Ecological interactions

<a id="mic-014"></a>

#### EII:MIC-014 — Mycorrhizal community / colonisation

<!-- eii:{"id":"EII:MIC-014","domain":"D08","related_domains":["D13"],"record_type":"family","variants":["mycorrhizal_composition","root_colonisation"],"secondary":["measured","derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Mycorrhizal composition and root colonisation describe distinct symbiotic observations.
- **Direct observations / derivation:** Fungal assignments and microscopy of colonised root length, %; report structures and host.
- **Inference and limits:** Supports assessment of symbiotic association; DNA presence or colonisation does not quantify nutrient transfer or benefit.
- **Supporting indicators:** [EII:VEG-017](#veg-017), [EII:SOI-008](#soi-008), [EII:INT-006](#int-006).

<a id="mic-015"></a>

#### EII:MIC-015 — Rhizosphere-associated community structure

<!-- eii:{"id":"EII:MIC-015","domain":"D08","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Rhizosphere structure is community composition in root-associated soil relative to a defined comparator.
- **Direct observations / derivation:** Paired rhizosphere/bulk samples and taxon/function profiles, proportions or dissimilarity.
- **Inference and limits:** Supports plant-associated enrichment hypotheses; soil gradients and sampling separation confound causal host effects.
- **Supporting indicators:** [EII:MIC-001](#mic-001), [EII:MIC-003](#mic-003), [EII:VEG-017](#veg-017).

<a id="mic-016"></a>

#### EII:MIC-016 — Potential plant pathogens / beneficial taxa

<!-- eii:{"id":"EII:MIC-016","domain":"D08","related_domains":[],"record_type":"family","variants":["validated_pathogen_marker","candidate_beneficial_taxon"],"secondary":["derived","inferred"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Potential pathogens/beneficial taxa are organisms or markers associated with specified outcomes.
- **Direct observations / derivation:** Validated taxon/virulence assignments or qPCR, detection and copies/g; retain strain and reference uncertainty.
- **Inference and limits:** Supports targeted follow-up; species identity alone does not establish pathogenicity, viability or disease suppression.
- **Supporting indicators:** [EII:AGR-005](#agr-005), [EII:INT-009](#int-009), [EII:MIC-022](#mic-022).

<a id="bio-008"></a>

#### EII:BIO-008 — Pollinator abundance / visitation

<!-- eii:{"id":"EII:BIO-008","domain":"D08","related_domains":["D13"],"record_type":"family","variants":["pollinator_count","flower_visitation_rate"],"secondary":["measured","process"],"tertiary":{"spatial":["organism","community","plot"],"temporal":["event","season"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Pollinator abundance/visitation record insects and visits to defined flowers.
- **Direct observations / derivation:** Standardised counts per transect/time and visits/flower/hour, with weather and species recorded.
- **Inference and limits:** Supports pollination activity assessment; visitation alone does not prove pollen transfer or successful reproduction.
- **Supporting indicators:** [EII:INT-001](#int-001), [EII:INT-002](#int-002), [EII:VEG-016](#veg-016).

<a id="bio-009"></a>

#### EII:BIO-009 — Predation / natural pest-control rate

<!-- eii:{"id":"EII:BIO-009","domain":"D08","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["organism","community","plot"],"temporal":["event","season"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Predation/pest-control rate measures consumption or pest reduction in a stated experiment.
- **Direct observations / derivation:** Sentinel-prey loss/time and paired exclusion/open treatment effects, %/day or pest-density difference.
- **Inference and limits:** Supports biocontrol assessment; prey disappearance and experimental artefacts require predator verification.
- **Supporting indicators:** [EII:AGR-004](#agr-004), [EII:INT-003](#int-003), [EII:BIO-002](#bio-002).

<a id="bio-013"></a>

#### EII:BIO-013 — Food-web / interaction network structure

<!-- eii:{"id":"EII:BIO-013","domain":"D08","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","modelled"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Interaction-network structure describes links among organisms and associated network metrics.
- **Direct observations / derivation:** Observed/traced feeding or interaction events and link weights; calculate connectance/modularity with method declared.
- **Inference and limits:** Supports trophic/network comparison; co-occurrence alone is not a validated interaction and incomplete sampling biases metrics.
- **Supporting indicators:** [EII:INT-003](#int-003), [EII:INT-008](#int-008), [EII:BIO-002](#bio-002).

<a id="int-001"></a>

#### EII:INT-001 — Pollen deposition/pollen limitation

<!-- eii:{"id":"EII:INT-001","domain":"D08","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["organism","community","plot"],"temporal":["event","season"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Pollen delivered to stigmas and reproduction limited by pollen supply.
- **Direct observations / derivation:** Stigma pollen counts; supplemented-versus-control fruit/seed set, counts and effect size.
- **Inference and limits:** Supports pollination-function assessment; pollen quality and resource limitation require separate controls.
- **Supporting indicators:** [EII:BIO-008](#bio-008), [EII:INT-002](#int-002), [EII:VEG-016](#veg-016).

<a id="int-002"></a>

#### EII:INT-002 — Fruit/seed set

<!-- eii:{"id":"EII:INT-002","domain":"D08","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["organism","community","plot"],"temporal":["event","season"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fraction of flowers/ovules developing into fruits/seeds under stated conditions.
- **Direct observations / derivation:** Repeated reproductive counts, % with denominator and abortion timing declared.
- **Inference and limits:** Supports reproductive-success assessment; pollination, weather, nutrition and herbivory jointly determine outcomes.
- **Supporting indicators:** [EII:INT-001](#int-001), [EII:BIO-008](#bio-008), [EII:VEG-020](#veg-020).

<a id="int-003"></a>

#### EII:INT-003 — Herbivory rate

<!-- eii:{"id":"EII:INT-003","domain":"D08","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["organism","community","plot"],"temporal":["event","season"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Plant tissue consumed/damaged per area or interval.
- **Direct observations / derivation:** Repeated leaf-area loss or biomass removal, %/time; distinguish herbivore from disease damage.
- **Inference and limits:** Supports consumer-pressure assessment; standing damage is not automatically current feeding rate.
- **Supporting indicators:** [EII:AGR-004](#agr-004), [EII:BIO-009](#bio-009), [EII:VEG-014](#veg-014).

<a id="int-004"></a>

#### EII:INT-004 — Competition effect

<!-- eii:{"id":"EII:INT-004","domain":"D08","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["organism","community","plot"],"temporal":["event","season"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Performance difference attributable to competitor presence in a controlled comparison.
- **Direct observations / derivation:** Neighbour-removal/addition experiment, growth/reproduction effect size.
- **Inference and limits:** Supports competition inference within the tested context; observational co-occurrence cannot establish direction or mechanism.
- **Supporting indicators:** [EII:VEG-014](#veg-014), [EII:HYD-001](#hyd-001), [EII:SOI-008](#soi-008).

<a id="int-005"></a>

#### EII:INT-005 — Facilitation effect

<!-- eii:{"id":"EII:INT-005","domain":"D08","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["organism","community","plot"],"temporal":["event","season"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Performance benefit attributable to another organism under defined conditions.
- **Direct observations / derivation:** Controlled neighbour/nurse treatment comparisons, survival/growth effect size.
- **Inference and limits:** Supports facilitation inference; effects may reverse with resource conditions or life stage.
- **Supporting indicators:** [EII:BIO-016](#bio-016), [EII:VEG-020](#veg-020), [EII:HYD-001](#hyd-001).

<a id="int-006"></a>

#### EII:INT-006 — Mycorrhizal nutrient transfer

<!-- eii:{"id":"EII:INT-006","domain":"D08","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["function"],"routes":["bio","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Nutrient transfer associated with a defined fungal–plant pathway.
- **Direct observations / derivation:** Isotopic tracing/compartment controls and plant nutrient recovery, mass/time or fraction.
- **Inference and limits:** Supports demonstrated transfer under experiment; colonisation alone cannot establish mutual benefit or field-scale flux.
- **Supporting indicators:** [EII:MIC-014](#mic-014), [EII:SOI-008](#soi-008), [EII:AGR-001](#agr-001).

<a id="int-007"></a>

#### EII:INT-007 — Seed dispersal/removal

<!-- eii:{"id":"EII:INT-007","domain":"D08","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["function"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Movement or removal of seeds by specified processes.
- **Direct observations / derivation:** Tracked seeds, traps or validated molecular assignments, distance and fraction/time.
- **Inference and limits:** Supports dispersal-function assessment; seed disappearance may be predation and movement does not ensure establishment.
- **Supporting indicators:** [EII:BIO-016](#bio-016), [EII:VEG-021](#veg-021), [EII:BIO-007](#bio-007).

<a id="int-008"></a>

#### EII:INT-008 — Diet/trophic-link evidence

<!-- eii:{"id":"EII:INT-008","domain":"D08","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Observed consumption or traced dietary contribution between organisms.
- **Direct observations / derivation:** Gut/faecal metabarcoding, observation or isotopes, detections or estimated contribution with mixing assumptions.
- **Inference and limits:** Supports trophic linkage; secondary predation, DNA persistence and isotope baselines complicate quantification.
- **Supporting indicators:** [EII:BIO-013](#bio-013), [EII:BIO-002](#bio-002), [EII:MIC-024](#mic-024).

<a id="int-009"></a>

#### EII:INT-009 — Disease suppression in bioassays

<!-- eii:{"id":"EII:INT-009","domain":"D08","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["function"],"routes":["amr","bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Reduction in specified disease outcomes under a controlled soil/community treatment.
- **Direct observations / derivation:** Matched inoculation/control disease incidence or severity, % or effect size.
- **Inference and limits:** Supports suppression under tested conditions; marker/taxon detection alone does not demonstrate protection or field efficacy.
- **Supporting indicators:** [EII:MIC-016](#mic-016), [EII:AGR-005](#agr-005), [EII:MIC-007](#mic-007).

<a id="d09"></a>

### 9. Biogeochemical cycles

<a id="mic-009"></a>

#### EII:MIC-009 — Carbon-degradation gene/pathway potential

<!-- eii:{"id":"EII:MIC-009","domain":"D09","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","inferred"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":["R04"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** Carbon-degradation genetic potential describes annotated genes/pathways for organic-C processing.
- **Direct observations / derivation:** Shotgun/qPCR gene counts normalised to stated denominator; report annotation release and pathway completeness.
- **Inference and limits:** Indicates encoded potential; gene presence does not establish expression, substrate access or decomposition rate.
- **Supporting indicators:** [EII:MIC-022](#mic-022), [EII:MIC-019](#mic-019), [EII:MIC-024](#mic-024).

<a id="mic-010"></a>

#### EII:MIC-010 — Nitrogen-fixation genetic potential

<!-- eii:{"id":"EII:MIC-010","domain":"D09","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","inferred"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** N-fixation genetic potential describes markers of biological nitrogen fixation.
- **Direct observations / derivation:** nifH or validated pathway genes, copies/g or normalised abundance; evaluate homolog specificity.
- **Inference and limits:** Supports diazotrophic-potential hypotheses; presence does not quantify fixation and some homologs have other functions.
- **Supporting indicators:** [EII:CYC-004](#cyc-004), [EII:MIC-022](#mic-022), [EII:SOI-008](#soi-008).

<a id="mic-011"></a>

#### EII:MIC-011 — Nitrification genetic potential

<!-- eii:{"id":"EII:MIC-011","domain":"D09","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","inferred"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Nitrification genetic potential describes ammonia/nitrite oxidation capacity encoded in DNA.
- **Direct observations / derivation:** amoA and suitable pathway markers, copies/g or normalised abundance, with archaeal/bacterial/comammox coverage.
- **Inference and limits:** Supports nitrifier-potential assessment; marker abundance does not establish realised nitrification.
- **Supporting indicators:** [EII:MIC-023](#mic-023), [EII:MIC-022](#mic-022), [EII:SOI-008](#soi-008).

<a id="mic-012"></a>

#### EII:MIC-012 — Denitrification genetic potential

<!-- eii:{"id":"EII:MIC-012","domain":"D09","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","inferred"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Denitrification potential records encoded nitrate/nitrite reduction and N₂O reduction pathways.
- **Direct observations / derivation:** nirK/nirS, nor, nosZ and other stated genes, normalised abundance or copies/g; separate pathway steps.
- **Inference and limits:** Supports pathway-potential hypotheses; incomplete pathways and environment prevent prediction of N₂O flux from DNA alone.
- **Supporting indicators:** [EII:CYC-005](#cyc-005), [EII:CYC-002](#cyc-002), [EII:MIC-022](#mic-022), [EII:HYD-001](#hyd-001).

<a id="mic-013"></a>

#### EII:MIC-013 — Phosphorus solubilisation / acquisition potential

<!-- eii:{"id":"EII:MIC-013","domain":"D09","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","inferred"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** P-acquisition potential describes encoded P mobilisation, mineralisation or uptake functions.
- **Direct observations / derivation:** Annotated phosphatase, transport and other validated marker genes; distinguish mineralisation from solubilisation.
- **Inference and limits:** Supports P-processing hypotheses; annotated capacity does not quantify P release or plant uptake.
- **Supporting indicators:** [EII:MIC-019](#mic-019), [EII:SOI-008](#soi-008), [EII:CYC-006](#cyc-006).

<a id="mic-018"></a>

#### EII:MIC-018 — Pollutant degradation gene potential

<!-- eii:{"id":"EII:MIC-018","domain":"D09","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","inferred"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Pollutant-degradation potential describes encoded transformation pathways.
- **Direct observations / derivation:** Validated marker/pathway abundance, copies/g or normalised counts; specify chemical target.
- **Inference and limits:** Suggests biodegradation capacity; genes alone cannot establish removal rate, detoxification or complete mineralisation.
- **Supporting indicators:** [EII:SOI-013](#soi-013), [EII:CYC-009](#cyc-009), [EII:MIC-022](#mic-022).

<a id="mic-023"></a>

#### EII:MIC-023 — Nitrogen mineralisation / nitrification rate

<!-- eii:{"id":"EII:MIC-023","domain":"D09","related_domains":["D13"],"record_type":"family","variants":["net_N_mineralisation","gross_N_mineralisation","net_nitrification","gross_nitrification"],"secondary":["measured","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Mineralisation/nitrification rates quantify separate realised N transformations.
- **Direct observations / derivation:** Incubation changes in mineral-N, mg N/kg/day, or isotope-based gross rates; distinguish net and gross processes.
- **Inference and limits:** Supports N-transformation assessment under assay conditions; substrate additions and incubations alter field behaviour.
- **Supporting indicators:** [EII:SOI-008](#soi-008), [EII:HYD-001](#hyd-001), [EII:MIC-011](#mic-011).

<a id="mic-024"></a>

#### EII:MIC-024 — Decomposition / litter mass-loss rate

<!-- eii:{"id":"EII:MIC-024","domain":"D09","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","derived","process"],"tertiary":{"spatial":["sample","plot","ecosystem"],"temporal":["day","season","year"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Decomposition rate is loss or transformation of a defined organic substrate over time.
- **Direct observations / derivation:** Litter dry-mass loss, %, or fitted decay constant k, time⁻¹; correct handling losses and describe bags/substrate.
- **Inference and limits:** Supports realised decay assessment; leaching, fragmentation and fauna contribute, so mass loss is not solely microbial respiration.
- **Supporting indicators:** [EII:MIC-019](#mic-019), [EII:SOI-010](#soi-010), [EII:SOI-011](#soi-011).

<a id="fun-002"></a>

#### EII:FUN-002 — Carbon sequestration / stock change

<!-- eii:{"id":"EII:FUN-002","domain":"D09","related_domains":["D13"],"record_type":"family","variants":["specified_pool_stock_change","net_ecosystem_carbon_balance"],"secondary":["derived","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["amr","veg"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Carbon stock change is repeated pool difference; net sequestration requires a defined system carbon balance.
- **Direct observations / derivation:** Comparable stocks over time, Mg C/ha/year, with transfers and fluxes for net balance.
- **Inference and limits:** Supports storage-change assessment; redistribution, harvested export and off-site emissions prevent equating one pool gain with net climate benefit.
- **Supporting indicators:** [EII:SOI-005](#soi-005), [EII:VEG-014](#veg-014), [EII:CYC-001](#cyc-001), [EII:CYC-002](#cyc-002).

<a id="fun-003"></a>

#### EII:FUN-003 — Nutrient retention / leaching

<!-- eii:{"id":"EII:FUN-003","domain":"D09","related_domains":["D13"],"record_type":"family","variants":["nutrient_retention","nutrient_leaching"],"secondary":["measured","modelled","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["amr","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Nutrient retention/leaching quantify distinct retained and exported nutrient masses.
- **Direct observations / derivation:** Input/output water and nutrient mass balance, kg N/P/ha/year; drainage flux × concentration for leaching.
- **Inference and limits:** Supports nutrient-loss assessment; concentration decline alone is not retention and missing pathways bias budgets.
- **Supporting indicators:** [EII:HYD-010](#hyd-010), [EII:HYD-006](#hyd-006), [EII:CYC-007](#cyc-007).

<a id="cyc-001"></a>

#### EII:CYC-001 — Net ecosystem CO₂ exchange

<!-- eii:{"id":"EII:CYC-001","domain":"D09","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","derived","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Net CO₂ transfer between an ecosystem and atmosphere under an explicit sign convention.
- **Direct observations / derivation:** Eddy covariance/chambers and flux processing, µmol/m²/s or g C/m²/year.
- **Inference and limits:** Supports net carbon-exchange assessment; gap filling, storage and lateral/harvest exports are needed for a complete carbon balance.
- **Supporting indicators:** [EII:FUN-001](#fun-001), [EII:SOI-010](#soi-010), [EII:FUN-002](#fun-002).

<a id="cyc-002"></a>

#### EII:CYC-002 — N₂O flux

<!-- eii:{"id":"EII:CYC-002","domain":"D09","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["iot","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Net nitrous-oxide transfer across a stated surface.
- **Direct observations / derivation:** Chamber or micrometeorological flux, µg N/m²/h, with N versus N₂O mass convention explicit.
- **Inference and limits:** Supports emission assessment; pulses and pathway mixtures mean gene abundance cannot substitute for measurements.
- **Supporting indicators:** [EII:MIC-012](#mic-012), [EII:HYD-001](#hyd-001), [EII:SOI-008](#soi-008).

<a id="cyc-003"></a>

#### EII:CYC-003 — Methane flux

<!-- eii:{"id":"EII:CYC-003","domain":"D09","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Net methane production/oxidation expressed as surface exchange.
- **Direct observations / derivation:** Gas flux observations, mg CH₄/m²/day, with temporal coverage.
- **Inference and limits:** Supports methane-budget assessment; emission is net production, oxidation and transport and cannot be inferred solely from archaeal taxa.
- **Supporting indicators:** [EII:SOI-023](#soi-023), [EII:HYD-016](#hyd-016), [EII:MIC-002](#mic-002).

<a id="cyc-004"></a>

#### EII:CYC-004 — Biological nitrogen-fixation rate

<!-- eii:{"id":"EII:CYC-004","domain":"D09","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["function"],"routes":["amr","bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** N input through biological conversion of atmospheric N₂.
- **Direct observations / derivation:** Validated ¹⁵N₂ incorporation or calibrated alternative, mg N/kg/time or kg N/ha/year.
- **Inference and limits:** Supports realised fixation assessment; tracer availability and scaling assumptions matter and nifH is not a rate.
- **Supporting indicators:** [EII:MIC-010](#mic-010), [EII:SOI-008](#soi-008), [EII:VEG-017](#veg-017).

<a id="cyc-005"></a>

#### EII:CYC-005 — Denitrification rate

<!-- eii:{"id":"EII:CYC-005","domain":"D09","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Nitrate/nitrite reduction to gaseous N products under specified conditions.
- **Direct observations / derivation:** Isotope or validated gas assay, mass N/area/time; distinguish total N gases from N₂O alone.
- **Inference and limits:** Supports N-removal assessment; assay inhibition and oxygen/substrate manipulation can bias field estimates.
- **Supporting indicators:** [EII:MIC-012](#mic-012), [EII:CYC-002](#cyc-002), [EII:SOI-023](#soi-023).

<a id="cyc-006"></a>

#### EII:CYC-006 — Phosphorus mineralisation rate

<!-- eii:{"id":"EII:CYC-006","domain":"D09","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Release of inorganic P from organic substrates under a stated assay.
- **Direct observations / derivation:** Time-resolved P fractions/tracers, mg P/kg/time.
- **Inference and limits:** Supports P-transformation assessment; sorption, immobilisation and enzyme potential complicate net-rate interpretation.
- **Supporting indicators:** [EII:MIC-013](#mic-013), [EII:MIC-019](#mic-019), [EII:SOI-008](#soi-008).

<a id="cyc-007"></a>

#### EII:CYC-007 — Nitrogen/phosphorus balance

<!-- eii:{"id":"EII:CYC-007","domain":"D09","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Inputs minus outputs of each nutrient for a declared system and interval.
- **Direct observations / derivation:** Fertiliser, fixation, deposition, harvest, runoff/leaching and gas terms, kg N/P/ha/year.
- **Inference and limits:** Supports surplus/deficit assessment; incomplete budgets do not establish retained stocks or specific losses.
- **Supporting indicators:** [EII:FUN-007](#fun-007), [EII:FUN-004](#fun-004), [EII:FUN-003](#fun-003), [EII:CYC-004](#cyc-004).

<a id="cyc-008"></a>

#### EII:CYC-008 — Nutrient resorption efficiency

<!-- eii:{"id":"EII:CYC-008","domain":"D09","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fraction of a nutrient recovered from leaves before senescence.
- **Direct observations / derivation:** Matched green/senescent tissue nutrient assays, %, correcting for leaf mass loss.
- **Inference and limits:** Supports internal recycling assessment; species, timing and incomplete senescence affect estimates.
- **Supporting indicators:** [EII:VEG-016](#veg-016), [EII:SOI-008](#soi-008), [EII:MIC-024](#mic-024).

<a id="cyc-009"></a>

#### EII:CYC-009 — Measured contaminant transformation

<!-- eii:{"id":"EII:CYC-009","domain":"D09","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Change of a specified chemical attributable to a stated transformation pathway.
- **Direct observations / derivation:** Repeated parent/metabolite mass balance or isotope mineralisation, %/time or mass/time.
- **Inference and limits:** Supports transformation assessment; sorption/export are not degradation and products may remain toxic.
- **Supporting indicators:** [EII:MIC-018](#mic-018), [EII:SOI-013](#soi-013), [EII:SOI-022](#soi-022).

<a id="cyc-010"></a>

#### EII:CYC-010 — Dissolved organic carbon export

<!-- eii:{"id":"EII:CYC-010","domain":"D09","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["sample","plot","ecosystem","watershed"],"temporal":["hour","season","year"]},"quaternary":["function"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Organic carbon transported in the operationally dissolved water fraction.
- **Direct observations / derivation:** Filtered DOC assay × discharge, mg C/L and kg C/time, with filter definition.
- **Inference and limits:** Supports aquatic carbon-export assessment; concentration alone is not load or source attribution.
- **Supporting indicators:** [EII:HYD-006](#hyd-006), [EII:SOI-005](#soi-005), [EII:CYC-001](#cyc-001).

<a id="d10"></a>

### 10. Landscape ecology

<a id="ter-001"></a>

#### EII:TER-001 — Elevation / digital terrain model

<!-- eii:{"id":"EII:TER-001","domain":"D10","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["state"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Elevation/DTM represents ground-surface height relative to a vertical datum.
- **Direct observations / derivation:** Survey or ground-classified LiDAR heights, m; declare datum, grid size and ground classification.
- **Inference and limits:** Provides terrain context; a surface model containing canopy/buildings is not a ground model.
- **Supporting indicators:** [EII:TER-002](#ter-002), [EII:TER-003](#ter-003), [EII:TER-014](#ter-014).

<a id="ter-002"></a>

#### EII:TER-002 — Slope gradient

<!-- eii:{"id":"EII:TER-002","domain":"D10","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","context"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["context"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Slope is the local rate of elevation change.
- **Direct observations / derivation:** DTM derivatives, degrees or %; record neighbourhood and grid resolution.
- **Inference and limits:** Indicates gravitational runoff/erosion context; does not measure realised erosion.
- **Supporting indicators:** [EII:SOI-012](#soi-012), [EII:TER-009](#ter-009), [EII:VEG-012](#veg-012).

<a id="ter-003"></a>

#### EII:TER-003 — Aspect / slope orientation

<!-- eii:{"id":"EII:TER-003","domain":"D10","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","context"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["context"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Aspect is the compass direction of maximum downslope gradient.
- **Direct observations / derivation:** DTM orientation, degrees clockwise from north; undefined on flat terrain.
- **Inference and limits:** Supports radiation and exposure interpretation; local shading modifies actual microclimate.
- **Supporting indicators:** [EII:TER-004](#ter-004), [EII:HYD-001](#hyd-001), [EII:DIS-006](#dis-006).

<a id="ter-008"></a>

#### EII:TER-008 — Terrace geometry / terrace-wall condition

<!-- eii:{"id":"EII:TER-008","domain":"D10","related_domains":["D13"],"record_type":"family","variants":["terrace_geometry","wall_condition"],"secondary":["measured","context"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["context"],"routes":["terrain","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Terrace geometry/wall condition describes measured dimensions and damage.
- **Direct observations / derivation:** Surveyed terrace width, wall height, slope and damage frequency, m and %; retain component fields.
- **Inference and limits:** Supports stability and maintenance assessment; structural safety requires site investigation.
- **Supporting indicators:** [EII:TER-009](#ter-009), [EII:TER-002](#ter-002), [EII:HYD-006](#hyd-006).

<a id="ter-014"></a>

#### EII:TER-014 — Surface / canopy change between surveys

<!-- eii:{"id":"EII:TER-014","domain":"D10","related_domains":[],"record_type":"family","variants":["ground_height_change","canopy_height_change","volume_change"],"secondary":["derived"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["state"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Repeat surface/canopy change is the difference between co-registered surveys.
- **Direct observations / derivation:** Height or volume differences, m or m³, with a spatial level-of-detection threshold.
- **Inference and limits:** Can indicate growth, erosion or deposition; season, registration and occlusion can mimic change.
- **Supporting indicators:** [EII:TER-001](#ter-001), [EII:TER-009](#ter-009), [EII:VEG-014](#veg-014).

<a id="bio-006"></a>

#### EII:BIO-006 — Landscape fragmentation / patch size

<!-- eii:{"id":"EII:BIO-006","domain":"D10","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["state"],"routes":["land"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fragmentation/patch size describe spatial subdivision of a stated habitat class.
- **Direct observations / derivation:** Class map and patch metrics, ha, count or index; record grain, extent and adjacency.
- **Inference and limits:** Supports habitat-pattern interpretation; fragmentation depends on focal habitat and is not uniformly harmful across taxa.
- **Supporting indicators:** [EII:BIO-007](#bio-007), [EII:BIO-005](#bio-005), [EII:LAN-001](#lan-001).

<a id="bio-007"></a>

#### EII:BIO-007 — Habitat connectivity / corridor suitability

<!-- eii:{"id":"EII:BIO-007","domain":"D10","related_domains":[],"record_type":"family","variants":["structural_connectivity","modelled_functional_connectivity"],"secondary":["derived","modelled"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["state"],"routes":["land","bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Connectivity/corridor suitability describe structural connection or modelled movement opportunity.
- **Direct observations / derivation:** Habitat distances, resistance surfaces and declared graph/circuit model; validate with movement/genetic evidence.
- **Inference and limits:** Supports movement hypotheses; structural corridors do not prove functional use or gene flow.
- **Supporting indicators:** [EII:BIO-002](#bio-002), [EII:BIO-015](#bio-015), [EII:LAN-004](#lan-004).

<a id="dis-004"></a>

#### EII:DIS-004 — Land-cover / land-use class

<!-- eii:{"id":"EII:DIS-004","domain":"D10","related_domains":["D13"],"record_type":"family","variants":["land_cover","land_use"],"secondary":["derived","context"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["context"],"routes":["land","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Land cover and land use are distinct surface classes and activities.
- **Direct observations / derivation:** Validated imagery classes and independent management records, categorical with class probabilities/accuracy.
- **Inference and limits:** Supports context mapping; tree cover is not necessarily forest use and imagery rarely identifies practices uniquely.
- **Supporting indicators:** [EII:DIS-005](#dis-005), [EII:VEG-017](#veg-017), [EII:FUN-007](#fun-007).

<a id="dis-005"></a>

#### EII:DIS-005 — Land-cover transition rate

<!-- eii:{"id":"EII:DIS-005","domain":"D10","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","pressure"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["pressure"],"routes":["land"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Transition rate is area changing between harmonised land classes per time.
- **Direct observations / derivation:** Comparable validated class maps, ha/year or %/year; account for class and algorithm changes.
- **Inference and limits:** Supports conversion/abandonment assessment; map disagreement may be classification error rather than real change.
- **Supporting indicators:** [EII:DIS-004](#dis-004), [EII:BIO-005](#bio-005), [EII:FUN-009](#fun-009).

<a id="fun-008"></a>

#### EII:FUN-008 — Field-margin / hedgerow length and condition

<!-- eii:{"id":"EII:FUN-008","domain":"D10","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["observed","derived"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["state"],"routes":["terrain","land","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Field-margin/hedgerow structure records extent and separately measured condition.
- **Direct observations / derivation:** Mapped length/width, m, area, ha, and botanical/structural attributes.
- **Inference and limits:** Supports habitat and buffer assessment; length alone does not establish pollination or nutrient filtering.
- **Supporting indicators:** [EII:BIO-008](#bio-008), [EII:VEG-017](#veg-017), [EII:LAN-002](#lan-002).

<a id="lan-001"></a>

#### EII:LAN-001 — Edge density/core habitat area

<!-- eii:{"id":"EII:LAN-001","domain":"D10","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["state"],"routes":["land"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Habitat boundary per area and habitat interior beyond a stated edge distance.
- **Direct observations / derivation:** Validated patch polygons, m/ha and ha; declare focal class, grain and edge rule.
- **Inference and limits:** Supports edge-exposure assessment; species-specific edge responses and map resolution govern meaning.
- **Supporting indicators:** [EII:BIO-006](#bio-006), [EII:BIO-005](#bio-005), [EII:LAN-002](#lan-002).

<a id="lan-002"></a>

#### EII:LAN-002 — Landscape composition/diversity

<!-- eii:{"id":"EII:LAN-002","domain":"D10","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["state"],"routes":["land"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Area proportions and diversity of declared land/habitat classes.
- **Direct observations / derivation:** Harmonised classes and area weights, proportions and specified diversity index.
- **Inference and limits:** Supports mosaic comparison; class diversity does not itself imply species diversity or functional integrity.
- **Supporting indicators:** [EII:DIS-004](#dis-004), [EII:BIO-001](#bio-001), [EII:FUN-008](#fun-008).

<a id="lan-003"></a>

#### EII:LAN-003 — Riparian buffer extent/continuity

<!-- eii:{"id":"EII:LAN-003","domain":"D10","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["state"],"routes":["terrain","land","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Width, area and gaps in defined streamside vegetation.
- **Direct observations / derivation:** Stream/vegetation maps and field checks, m, ha and % continuity.
- **Inference and limits:** Supports buffering/habitat assessment; width alone does not quantify pollutant removal or flood protection.
- **Supporting indicators:** [EII:FUN-003](#fun-003), [EII:HYD-018](#hyd-018), [EII:BIO-007](#bio-007).

<a id="lan-004"></a>

#### EII:LAN-004 — Barrier density/permeability

<!-- eii:{"id":"EII:LAN-004","domain":"D10","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","modelled","pressure"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["pressure"],"routes":["settlement","terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Number/extent of obstacles and species-specific movement passability.
- **Direct observations / derivation:** Roads, dams/fences and verified passage data, barriers/km or crossing probability.
- **Inference and limits:** Supports movement constraint assessment; mapped barriers vary in permeability with species and flow/traffic.
- **Supporting indicators:** [EII:BIO-007](#bio-007), [EII:BIO-015](#bio-015), [EII:HYD-017](#hyd-017).

<a id="lan-005"></a>

#### EII:LAN-005 — Burned/converted area by habitat

<!-- eii:{"id":"EII:LAN-005","domain":"D10","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","pressure"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["pressure"],"routes":["fire","land"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Disturbance area intersected with harmonised habitat classes.
- **Direct observations / derivation:** Validated event/transition polygons over habitat maps, ha and % affected.
- **Inference and limits:** Supports habitat-specific exposure assessment; classification and event-boundary errors propagate.
- **Supporting indicators:** [EII:DIS-003](#dis-003), [EII:DIS-005](#dis-005), [EII:BIO-005](#bio-005).

<a id="lan-006"></a>

#### EII:LAN-006 — Topographic position/terrain curvature

<!-- eii:{"id":"EII:LAN-006","domain":"D10","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","context"],"tertiary":{"spatial":["landscape","watershed","region"],"temporal":["event","year","decade"]},"quaternary":["context"],"routes":["terrain"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Relative terrain position and curvature at a declared neighbourhood scale.
- **Direct observations / derivation:** DTM derivatives or local elevation contrast, m, index or curvature units as defined.
- **Inference and limits:** Supports drainage/exposure context; neighbourhood choice changes meaning and does not measure soil properties.
- **Supporting indicators:** [EII:TER-002](#ter-002), [EII:TER-005](#ter-005), [EII:HYD-001](#hyd-001).

<a id="d11"></a>

### 11. Ecosystem functioning

<a id="fun-001"></a>

#### EII:FUN-001 — Primary productivity (GPP/NPP)

<!-- eii:{"id":"EII:FUN-001","domain":"D11","related_domains":[],"record_type":"family","variants":["GPP","NPP"],"secondary":["modelled","process"],"tertiary":{"spatial":["plot","ecosystem","watershed"],"temporal":["season","year"]},"quaternary":["function"],"routes":["veg","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** GPP is gross carbon fixation; NPP is GPP minus autotrophic respiration.
- **Direct observations / derivation:** Carbon flux/biomass observations and partitioning/model, g C/m²/year; record whether GPP or NPP.
- **Inference and limits:** Supports production assessment; eddy-covariance net exchange needs partitioning and greenness is not direct productivity.
- **Supporting indicators:** [EII:VEG-011](#veg-011), [EII:VEG-014](#veg-014), [EII:SOI-010](#soi-010), [EII:CYC-001](#cyc-001).

<a id="fun-012"></a>

#### EII:FUN-012 — Composite soil-health index

<!-- eii:{"id":"EII:FUN-012","domain":"D11","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["composite"],"tertiary":{"spatial":["plot","ecosystem","watershed"],"temporal":["season","year"]},"quaternary":["condition","assessment"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** A composite soil-health index combines specified soil metrics against explicit reference conditions.
- **Direct observations / derivation:** Named variables, weights, transformations and missing-data rules, dimensionless declared score.
- **Inference and limits:** Supports within-framework condition screening; no universal score or threshold and opposing components can be hidden.
- **Supporting indicators:** [EII:SOI-003](#soi-003), [EII:SOI-005](#soi-005), [EII:MIC-007](#mic-007), [EII:SOI-013](#soi-013).

<a id="fun-013"></a>

#### EII:FUN-013 — Ecosystem condition / integrity index

<!-- eii:{"id":"EII:FUN-013","domain":"D11","related_domains":[],"record_type":"indicator","variants":[],"secondary":["composite","modelled"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["condition","assessment"],"routes":["land","bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Ecosystem condition/integrity index combines selected ecosystem properties relative to a declared reference.
- **Direct observations / derivation:** Explicit extent, composition, structure and function metrics with weights, score and uncertainty.
- **Inference and limits:** Supports reference-based condition comparison; sensitive to ecosystem type, baseline, weights and incomplete coverage.
- **Supporting indicators:** [EII:BIO-005](#bio-005), [EII:BIO-002](#bio-002), [EII:TER-013](#ter-013), [EII:FUN-001](#fun-001).

<a id="fun-015"></a>

#### EII:FUN-015 — Net ecosystem metabolism

<!-- eii:{"id":"EII:FUN-015","domain":"D11","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["plot","ecosystem","watershed"],"temporal":["season","year"]},"quaternary":["function"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Gross ecosystem production minus ecosystem respiration for a declared system.
- **Direct observations / derivation:** Aquatic oxygen/CO₂ time series with gas exchange, or validated flux balance, mass/area/time.
- **Inference and limits:** Supports autotrophic/heterotrophic balance assessment; transport and diel mixing must be modelled.
- **Supporting indicators:** [EII:HYD-013](#hyd-013), [EII:HYD-014](#hyd-014), [EII:CYC-001](#cyc-001).

<a id="fun-016"></a>

#### EII:FUN-016 — Trophic transfer efficiency

<!-- eii:{"id":"EII:FUN-016","domain":"D11","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["function"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Production passed between specified trophic levels relative to lower-level production.
- **Direct observations / derivation:** Comparable production/energy estimates, %, with food-web and spatial boundary.
- **Inference and limits:** Supports energy-transfer assessment; standing biomass ratios are not production efficiencies.
- **Supporting indicators:** [EII:BIO-013](#bio-013), [EII:INT-008](#int-008), [EII:FUN-001](#fun-001).

<a id="fun-017"></a>

#### EII:FUN-017 — Ecosystem multifunctionality

<!-- eii:{"id":"EII:FUN-017","domain":"D11","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["composite"],"tertiary":{"spatial":["plot","ecosystem","watershed"],"temporal":["season","year"]},"quaternary":["condition","assessment"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Joint performance of multiple specified ecosystem functions.
- **Direct observations / derivation:** Named function measurements and declared averaging/threshold/ordination method, score or number above threshold.
- **Inference and limits:** Supports multivariate function comparison; function selection, scaling and trade-offs control results.
- **Supporting indicators:** [EII:FUN-001](#fun-001), [EII:FUN-003](#fun-003), [EII:BIO-009](#bio-009), [EII:MIC-024](#mic-024).

<a id="fun-018"></a>

#### EII:FUN-018 — Water purification/removal efficiency

<!-- eii:{"id":"EII:FUN-018","domain":"D11","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["plot","ecosystem","watershed"],"temporal":["season","year"]},"quaternary":["function"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fraction or mass of specified pollutant removed across a defined system.
- **Direct observations / derivation:** Matched inflow/outflow concentration and flow, % and mass/time including retained/transformed fate.
- **Inference and limits:** Supports treatment-function assessment; dilution, storage and export must be separated from permanent removal.
- **Supporting indicators:** [EII:HYD-018](#hyd-018), [EII:FUN-003](#fun-003), [EII:CYC-009](#cyc-009).

<a id="fun-019"></a>

#### EII:FUN-019 — Thermal regulation effect

<!-- eii:{"id":"EII:FUN-019","domain":"D11","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["plot","ecosystem","watershed"],"temporal":["season","year"]},"quaternary":["function"],"routes":["thermal","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Temperature difference attributable to a specified vegetation/ecosystem feature.
- **Direct observations / derivation:** Matched shaded/open or intervention/control temperature observations, °C, with weather/time controls.
- **Inference and limits:** Supports cooling assessment; association alone does not isolate causal cooling and scales differ.
- **Supporting indicators:** [EII:HYD-003](#hyd-003), [EII:ATM-001](#atm-001), [EII:VEG-012](#veg-012).

<a id="fun-020"></a>

#### EII:FUN-020 — Soil-function deficit profile

<!-- eii:{"id":"EII:FUN-020","domain":"D11","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["plot","ecosystem","watershed"],"temporal":["season","year"]},"quaternary":["state"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Separate departures of stated soil functions from justified references.
- **Direct observations / derivation:** Function-specific measurements and uncertainty, native units or standardised differences, kept disaggregated.
- **Inference and limits:** Supports targeted assessment; reference choice and trade-offs preclude a universal soil-quality verdict.
- **Supporting indicators:** [EII:HYD-004](#hyd-004), [EII:MIC-023](#mic-023), [EII:SOI-005](#soi-005), [EII:SOI-013](#soi-013).

<a id="d12"></a>

### 12. Ecological resilience

<a id="mic-017"></a>

#### EII:MIC-017 — Drought / salinity stress-response gene potential

<!-- eii:{"id":"EII:MIC-017","domain":"D12","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","inferred"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Stress-response potential describes encoded responses to declared environmental stresses.
- **Direct observations / derivation:** Annotated osmotic, oxidative or drought-associated genes, normalised abundance.
- **Inference and limits:** Suggests possible response capacity; common multifunctional genes cannot prove community or ecosystem resilience.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:SOI-007](#soi-007), [EII:RES-001](#res-001).

<a id="dis-001"></a>

#### EII:DIS-001 — Normalised Burn Ratio (NBR)

<!-- eii:{"id":"EII:DIS-001","domain":"D12","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","proxy"],"tertiary":{"spatial":["plot","ecosystem","landscape"],"temporal":["event","year","decade"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":["opt","fire"],"refs":["R02"],"status":"curated_working_definition","review_scope":"specific_documentary_aspects_only"} -->

- **Definition:** NBR contrasts NIR with SWIR2 to characterise vegetation/char signals.
- **Direct observations / derivation:** (NIR-SWIR2)/(NIR+SWIR2), dimensionless; dNBR is pre-fire minus post-fire NBR.
- **Inference and limits:** Supports burn-impact mapping with field calibration; phenology, soil and initial vegetation alter severity relationships.
- **Supporting indicators:** [EII:DIS-003](#dis-003), [EII:VEG-014](#veg-014), [EII:RES-005](#res-005).

<a id="dis-002"></a>

#### EII:DIS-002 — Fire fuel load / vertical continuity

<!-- eii:{"id":"EII:DIS-002","domain":"D12","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","modelled"],"tertiary":{"spatial":["plot","ecosystem","landscape"],"temporal":["event","year","decade"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":["terrain","fire"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fuel load/continuity describe combustible biomass and its spatial arrangement.
- **Direct observations / derivation:** Dry live/dead fuel mass, Mg/ha; height/spacing and moisture observations, m and %.
- **Inference and limits:** Supports fire-behaviour assessment; fuel alone does not determine ignition, weather, exposure or damage.
- **Supporting indicators:** [EII:TER-013](#ter-013), [EII:ATM-005](#atm-005), [EII:DIS-007](#dis-007).

<a id="dis-003"></a>

#### EII:DIS-003 — Fire occurrence / recurrence

<!-- eii:{"id":"EII:DIS-003","domain":"D12","related_domains":[],"record_type":"indicator","variants":[],"secondary":["observed","derived"],"tertiary":{"spatial":["plot","ecosystem","landscape"],"temporal":["event","year","decade"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":["fire"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fire occurrence/recurrence describe confirmed events, affected area and intervals.
- **Direct observations / derivation:** Validated event records/burn perimeters, dates, ha and years between events.
- **Inference and limits:** Supports disturbance-history assessment; thermal hotspots are detections rather than perimeters or ignition counts.
- **Supporting indicators:** [EII:DIS-001](#dis-001), [EII:DIS-002](#dis-002), [EII:RES-005](#res-005).

<a id="dis-009"></a>

#### EII:DIS-009 — Soil/vegetation recovery after disturbance

<!-- eii:{"id":"EII:DIS-009","domain":"D12","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","modelled"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":["veg","bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Post-disturbance recovery describes a trajectory towards a stated baseline/reference.
- **Direct observations / derivation:** Repeat soil/vegetation measurements, baseline-normalised effect, slope or time to threshold.
- **Inference and limits:** Supports resilience assessment; regreening is not recovery of composition, soil carbon or all functions.
- **Supporting indicators:** [EII:RES-001](#res-001), [EII:RES-002](#res-002), [EII:VEG-017](#veg-017), [EII:FUN-001](#fun-001).

<a id="dis-010"></a>

#### EII:DIS-010 — Future climate exposure / suitability

<!-- eii:{"id":"EII:DIS-010","domain":"D12","related_domains":[],"record_type":"family","variants":["scenario_exposure","modelled_species_suitability"],"secondary":["modelled","predictive"],"tertiary":{"spatial":["plot","ecosystem","landscape"],"temporal":["event","year","decade"]},"quaternary":["exposure","planning"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Future exposure/suitability is a conditional climate/ecological model output.
- **Direct observations / derivation:** Scenario ensemble, downscaling and explicit suitability model, probability or change in relevant variable.
- **Inference and limits:** Supports conditional planning; projections are not observations and extrapolation/reference bias require validation.
- **Supporting indicators:** [EII:DIS-006](#dis-006), [EII:DIS-007](#dis-007), [EII:VEG-017](#veg-017), [EII:RES-007](#res-007).

<a id="res-001"></a>

#### EII:RES-001 — Disturbance resistance

<!-- eii:{"id":"EII:RES-001","domain":"D12","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["plot","ecosystem","landscape"],"temporal":["event","year","decade"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":["veg","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Magnitude of retained condition/function during a specified disturbance.
- **Direct observations / derivation:** Matched baseline/reference and disturbance observations, ratio or change with formula declared.
- **Inference and limits:** Supports resistance comparison for one response variable; unrelated variables may respond differently and controls are needed.
- **Supporting indicators:** [EII:DIS-009](#dis-009), [EII:FUN-001](#fun-001), [EII:HYD-001](#hyd-001).

<a id="res-002"></a>

#### EII:RES-002 — Recovery rate/time

<!-- eii:{"id":"EII:RES-002","domain":"D12","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","modelled"],"tertiary":{"spatial":["plot","ecosystem","landscape"],"temporal":["event","year","decade"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":["veg"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Speed of return towards a declared condition/function reference.
- **Direct observations / derivation:** Repeated response trajectory, change/time or time to threshold with censoring if unrecovered.
- **Inference and limits:** Supports recovery comparison; reference drift and sampling frequency affect estimated recovery.
- **Supporting indicators:** [EII:DIS-009](#dis-009), [EII:VEG-017](#veg-017), [EII:FUN-001](#fun-001).

<a id="res-003"></a>

#### EII:RES-003 — Temporal variability/stability

<!-- eii:{"id":"EII:RES-003","domain":"D12","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["plot","ecosystem","landscape"],"temporal":["event","year","decade"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":["veg","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Variation of a declared ecological variable across a stated period.
- **Direct observations / derivation:** Repeat data, variance, CV or mean/SD with sampling interval and trend treatment.
- **Inference and limits:** Supports temporal-stability comparison; low variability may reflect persistent degradation and mean dependence matters.
- **Supporting indicators:** [EII:FUN-004](#fun-004), [EII:DIS-006](#dis-006), [EII:RES-004](#res-004).

<a id="res-004"></a>

#### EII:RES-004 — Response diversity/asynchrony

<!-- eii:{"id":"EII:RES-004","domain":"D12","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":["bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Differences in component responses to the same environmental variation.
- **Direct observations / derivation:** Species/function time series and declared covariance/asynchrony metric.
- **Inference and limits:** Supports portfolio-buffering hypotheses; trait diversity alone does not demonstrate asynchronous realised responses.
- **Supporting indicators:** [EII:BIO-004](#bio-004), [EII:BIO-002](#bio-002), [EII:RES-003](#res-003).

<a id="res-005"></a>

#### EII:RES-005 — Post-fire compositional/function recovery

<!-- eii:{"id":"EII:RES-005","domain":"D12","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":["fire","veg","bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Recovery of specified taxonomic and process variables following confirmed fire.
- **Direct observations / derivation:** Repeat matched community/process measures against pre-fire/reference, distance or recovery time.
- **Inference and limits:** Supports multidimensional recovery assessment; satellite regreening does not establish full biodiversity/function recovery.
- **Supporting indicators:** [EII:DIS-001](#dis-001), [EII:DIS-003](#dis-003), [EII:VEG-017](#veg-017), [EII:MIC-024](#mic-024).

<a id="res-006"></a>

#### EII:RES-006 — Early-warning time-series signals

<!-- eii:{"id":"EII:RES-006","domain":"D12","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","predictive"],"tertiary":{"spatial":["plot","ecosystem","landscape"],"temporal":["event","year","decade"]},"quaternary":["exposure","planning"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Declared statistical signals hypothesised to precede state transitions.
- **Direct observations / derivation:** Long standardised series, lag autocorrelation/variance or other specified metric with detrending/null tests.
- **Inference and limits:** Supports exploratory transition surveillance; noise, forcing and sampling artefacts create false positives and no deterministic tipping forecast.
- **Supporting indicators:** [EII:RES-003](#res-003), [EII:DIS-006](#dis-006), [EII:HYD-001](#hyd-001).

<a id="res-007"></a>

#### EII:RES-007 — Scenario sensitivity/model uncertainty

<!-- eii:{"id":"EII:RES-007","domain":"D12","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","modelled"],"tertiary":{"spatial":["plot","ecosystem","landscape"],"temporal":["event","year","decade"]},"quaternary":["disturbance_response","restoration_assessment"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Response of a modelled ecological quantity to scenarios, parameters and model choice.
- **Direct observations / derivation:** Validated ensemble outputs, distributions and variance components in target-variable units.
- **Inference and limits:** Supports conditional confidence assessment; ensembles need not span all structural uncertainty and are not observed future outcomes.
- **Supporting indicators:** [EII:DIS-010](#dis-010), [EII:RES-001](#res-001), [EII:DIS-007](#dis-007).

<a id="d13"></a>

### 13. Agricultural ecology

<a id="fun-004"></a>

#### EII:FUN-004 — Crop yield / yield stability

<!-- eii:{"id":"EII:FUN-004","domain":"D13","related_domains":[],"record_type":"family","variants":["crop_yield","interannual_yield_stability"],"secondary":["measured","derived"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["state","production_assessment"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Yield and stability describe harvest mass and interannual variation respectively.
- **Direct observations / derivation:** Harvest dry/standard-moisture mass per area, Mg/ha; multi-year CV or specified stability metric.
- **Inference and limits:** Supports productivity and variability assessment; mean differences, weather, inputs and price do not imply ecological resilience alone.
- **Supporting indicators:** [EII:AGR-001](#agr-001), [EII:AGR-002](#agr-002), [EII:DIS-006](#dis-006).

<a id="fun-005"></a>

#### EII:FUN-005 — Groundcover persistence

<!-- eii:{"id":"EII:FUN-005","domain":"D13","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["state","production_assessment"],"routes":["veg","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Groundcover persistence describes duration/continuity of protective vegetation/residues.
- **Direct observations / derivation:** Repeated cover fractions and days above a stated cover threshold, days/year; distinguish green and residue cover.
- **Inference and limits:** Supports soil-exposure assessment; sufficient cover and water competition vary with site and crop.
- **Supporting indicators:** [EII:VEG-012](#veg-012), [EII:HYD-001](#hyd-001), [EII:SOI-012](#soi-012).

<a id="fun-006"></a>

#### EII:FUN-006 — Grazing pressure / stocking intensity

<!-- eii:{"id":"EII:FUN-006","domain":"D13","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","pressure"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["pressure"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Grazing/stocking intensity quantify animal pressure on a defined land area and period.
- **Direct observations / derivation:** Animal-unit days/ha plus forage removal/utilisation, %, with grazing season and feed imports.
- **Inference and limits:** Supports grazing-pressure assessment; stocking rate alone does not establish overgrazing without forage supply and vegetation response.
- **Supporting indicators:** [EII:VEG-014](#veg-014), [EII:SOI-002](#soi-002), [EII:AGR-009](#agr-009).

<a id="fun-007"></a>

#### EII:FUN-007 — Irrigation / fertiliser / pesticide input

<!-- eii:{"id":"EII:FUN-007","domain":"D13","related_domains":[],"record_type":"family","variants":["irrigation_input","fertiliser_input","pesticide_input"],"secondary":["measured","pressure"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["pressure"],"routes":["amr","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Input intensity records separate irrigation, fertiliser and pesticide applications.
- **Direct observations / derivation:** Metered water, m³/ha; nutrients, kg N/P/K/ha; active ingredients, kg/ha, with dates/formulations.
- **Inference and limits:** Supports resource/pressure assessment; quantities alone do not describe toxicity, losses or agronomic benefit.
- **Supporting indicators:** [EII:AGR-001](#agr-001), [EII:AGR-002](#agr-002), [EII:AGR-003](#agr-003), [EII:HUM-005](#hum-005).

<a id="agr-001"></a>

#### EII:AGR-001 — Agronomic nitrogen-use efficiency

<!-- eii:{"id":"EII:AGR-001","domain":"D13","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["state","production_assessment"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Declared crop production or uptake response per N input.
- **Direct observations / derivation:** Yield/N-input or fertilised-minus-control yield/N-input, kg product/kg N; label partial factor productivity versus agronomic efficiency.
- **Inference and limits:** Supports N-performance comparison; definitions differ and high yield/input does not establish low N loss.
- **Supporting indicators:** [EII:FUN-004](#fun-004), [EII:FUN-007](#fun-007), [EII:CYC-007](#cyc-007).

<a id="agr-002"></a>

#### EII:AGR-002 — Crop water productivity

<!-- eii:{"id":"EII:AGR-002","domain":"D13","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["state","production_assessment"],"routes":["amr","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Crop output per stated water input or consumptive use.
- **Direct observations / derivation:** Harvest mass divided by ET, irrigation or total supply, kg/m³ with denominator declared.
- **Inference and limits:** Supports water-performance comparison; irrigation efficiency and basin water savings require return-flow analysis.
- **Supporting indicators:** [EII:FUN-004](#fun-004), [EII:FUN-007](#fun-007), [EII:HYD-012](#hyd-012).

<a id="agr-003"></a>

#### EII:AGR-003 — Pesticide hazard/risk indicator

<!-- eii:{"id":"EII:AGR-003","domain":"D13","related_domains":[],"record_type":"indicator","variants":[],"secondary":["composite","modelled","pressure"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["condition","assessment"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Method-specific aggregation of chemical hazard and, for risk, exposure.
- **Direct observations / derivation:** Application records, active ingredients and named toxicity/exposure model, declared score.
- **Inference and limits:** Supports screening under a stated framework; kg applied alone is not ecological risk and species/mixtures matter.
- **Supporting indicators:** [EII:FUN-007](#fun-007), [EII:HYD-020](#hyd-020), [EII:BIO-008](#bio-008).

<a id="agr-004"></a>

#### EII:AGR-004 — Pest population/crop damage

<!-- eii:{"id":"EII:AGR-004","domain":"D13","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","pressure"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["pressure"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Abundance of named pests and separately measured plant injury.
- **Direct observations / derivation:** Standardised trap/scout counts and damaged tissue/production fraction, counts/area and %.
- **Inference and limits:** Supports pest-pressure assessment; trap counts require calibration and economic injury thresholds are context-specific.
- **Supporting indicators:** [EII:BIO-009](#bio-009), [EII:INT-003](#int-003), [EII:FUN-004](#fun-004).

<a id="agr-005"></a>

#### EII:AGR-005 — Crop disease incidence/severity

<!-- eii:{"id":"EII:AGR-005","domain":"D13","related_domains":[],"record_type":"family","variants":["disease_incidence","disease_severity"],"secondary":["measured","pressure"],"tertiary":{"spatial":["sample","community"],"temporal":["sampling_event","season","year"]},"quaternary":["pressure"],"routes":["amr","bio"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Proportion of plants diseased and amount of affected tissue are separate quantities.
- **Direct observations / derivation:** Confirmed diagnostics and field scoring, % plants and % tissue or declared scale.
- **Inference and limits:** Supports disease-burden assessment; symptoms may have abiotic causes and marker presence does not establish disease.
- **Supporting indicators:** [EII:MIC-016](#mic-016), [EII:INT-009](#int-009), [EII:VEG-015](#veg-015).

<a id="agr-006"></a>

#### EII:AGR-006 — Crop/rotation diversity

<!-- eii:{"id":"EII:AGR-006","domain":"D13","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","context"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["context","production_assessment"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Diversity of cultivated taxa and their sequence through time.
- **Direct observations / derivation:** Crop identities, area shares and rotation records, richness or declared diversity metric.
- **Inference and limits:** Supports diversification assessment; diversity alone does not prove reduced inputs, resilience or functional complementarity.
- **Supporting indicators:** [EII:VEG-017](#veg-017), [EII:FUN-004](#fun-004), [EII:BIO-004](#bio-004).

<a id="agr-007"></a>

#### EII:AGR-007 — Land equivalent ratio

<!-- eii:{"id":"EII:AGR-007","domain":"D13","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["state","production_assessment"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Relative land productivity of an intercrop compared with its specified monocultures.
- **Direct observations / derivation:** Σ(intercrop component yield/monocrop reference yield), dimensionless, using matched seasons and inputs.
- **Inference and limits:** Supports land-productivity comparison; reference choice and unequal inputs prevent universal superiority claims.
- **Supporting indicators:** [EII:FUN-004](#fun-004), [EII:AGR-006](#agr-006), [EII:AGR-001](#agr-001).

<a id="agr-008"></a>

#### EII:AGR-008 — Harvest nutrient removal

<!-- eii:{"id":"EII:AGR-008","domain":"D13","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","process"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["function","production_assessment"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Nutrient mass exported in harvested products.
- **Direct observations / derivation:** Harvest dry mass × nutrient concentration, kg N/P/K/ha/season.
- **Inference and limits:** Supports nutrient-budget assessment; residues, losses and harvested moisture require explicit accounting.
- **Supporting indicators:** [EII:FUN-004](#fun-004), [EII:CYC-007](#cyc-007), [EII:SOI-008](#soi-008).

<a id="agr-009"></a>

#### EII:AGR-009 — Forage utilisation/feed dependence

<!-- eii:{"id":"EII:AGR-009","domain":"D13","related_domains":[],"record_type":"family","variants":["forage_utilisation","imported_feed_share"],"secondary":["derived","pressure"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["pressure"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fraction of forage consumed and imported feed contribution are separate metrics.
- **Direct observations / derivation:** Before/after forage dry mass and feed accounts, % utilisation and % imported dry matter/nutrients.
- **Inference and limits:** Supports grazing/resource assessment; trampling/wastage must be separated from intake and imports shift impacts off-site.
- **Supporting indicators:** [EII:FUN-006](#fun-006), [EII:VEG-014](#veg-014), [EII:HUM-003](#hum-003).

<a id="agr-010"></a>

#### EII:AGR-010 — Tillage/traffic disturbance intensity

<!-- eii:{"id":"EII:AGR-010","domain":"D13","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","context","pressure"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["context"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Recorded mechanical soil disturbance rather than an agricultural philosophy label.
- **Direct observations / derivation:** Passes, implement depth, axle load, area and dates, declared component units.
- **Inference and limits:** Supports management-pressure comparison; index weighting is method-specific and physical outcome needs direct soil measurements.
- **Supporting indicators:** [EII:SOI-002](#soi-002), [EII:SOI-003](#soi-003), [EII:SOI-012](#soi-012).

<a id="agr-011"></a>

#### EII:AGR-011 — Farm nutrient/energy balance

<!-- eii:{"id":"EII:AGR-011","domain":"D13","related_domains":[],"record_type":"family","variants":["nutrient_balance","energy_balance"],"secondary":["derived"],"tertiary":{"spatial":["plot","farm","landscape"],"temporal":["season","year"]},"quaternary":["state","production_assessment"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Separate nutrient and energy flow accounts across a declared farm boundary.
- **Direct observations / derivation:** Inputs/outputs and inventory changes, kg N/P/year and MJ/year; document allocation/imports.
- **Inference and limits:** Supports resource-efficiency comparison; boundary omissions and unequal products can reverse comparisons.
- **Supporting indicators:** [EII:CYC-007](#cyc-007), [EII:HUM-004](#hum-004), [EII:HUM-003](#hum-003).

<a id="d14"></a>

### 14. Human–ecological systems

<a id="ter-015"></a>

#### EII:TER-015 — Built structures and landscape geometry

<!-- eii:{"id":"EII:TER-015","domain":"D14","related_domains":[],"record_type":"indicator","variants":[],"secondary":["observed","context"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["context"],"routes":["terrain","settlement"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Built geometry describes physical structures and engineered landscape features.
- **Direct observations / derivation:** Surveyed footprints, dimensions and volumes, m² and m³; classify feature type.
- **Inference and limits:** Provides land occupation/material context; geometry alone does not reveal resource consumption or social meaning.
- **Supporting indicators:** [EII:FUN-009](#fun-009), [EII:HUM-001](#hum-001), [EII:DIS-004](#dis-004).

<a id="fun-009"></a>

#### EII:FUN-009 — Human settlement / roads / infrastructure

<!-- eii:{"id":"EII:FUN-009","domain":"D14","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","pressure"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["pressure"],"routes":["settlement"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Settlement/roads/infrastructure quantify built extent and network occupation.
- **Direct observations / derivation:** Validated footprints and networks, ha, % built-up or km/km²; population products are modelled separately.
- **Inference and limits:** Supports land-pressure/accessibility assessment; mapped infrastructure does not establish actual usage or impacts.
- **Supporting indicators:** [EII:TER-015](#ter-015), [EII:BIO-006](#bio-006), [EII:HUM-001](#hum-001).

<a id="fun-010"></a>

#### EII:FUN-010 — Material / biomass availability

<!-- eii:{"id":"EII:FUN-010","domain":"D14","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","modelled"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["state"],"routes":["veg","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Material/biomass availability is an inventory of accessible resources under specified constraints.
- **Direct observations / derivation:** Measured stocks and replenishment/harvest models, Mg and Mg/year, with ownership/ecological/access exclusions.
- **Inference and limits:** Supports supply screening; standing biomass is not necessarily sustainably harvestable resource.
- **Supporting indicators:** [EII:VEG-014](#veg-014), [EII:FUN-004](#fun-004), [EII:HUM-003](#hum-003).

<a id="fun-011"></a>

#### EII:FUN-011 — Ecological footprint / resource demand

<!-- eii:{"id":"EII:FUN-011","domain":"D14","related_domains":["D13"],"record_type":"family","variants":["ecological_footprint","physical_resource_demand"],"secondary":["derived","modelled","pressure"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["pressure"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Ecological footprint/resource demand describe method-defined consumption pressures.
- **Direct observations / derivation:** Resource-flow accounts or footprint conversion, physical units or global hectares; declare accounting method and boundary.
- **Inference and limits:** Supports demand comparison; assumptions and trade allocation matter and footprint is not a direct local ecosystem measurement.
- **Supporting indicators:** [EII:HUM-003](#hum-003), [EII:HUM-004](#hum-004), [EII:HUM-005](#hum-005).

<a id="hum-001"></a>

#### EII:HUM-001 — Impervious surface fraction

<!-- eii:{"id":"EII:HUM-001","domain":"D14","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","pressure"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["pressure"],"routes":["settlement","land"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Proportion of ground covered by effectively water-impermeable surfaces.
- **Direct observations / derivation:** Validated land-surface classification/field verification, %, with distinction between built-up and sealed surfaces.
- **Inference and limits:** Supports runoff/heat-pressure assessment; drainage connectivity and permeable construction modify impacts.
- **Supporting indicators:** [EII:FUN-009](#fun-009), [EII:HYD-006](#hyd-006), [EII:HYD-003](#hyd-003).

<a id="hum-002"></a>

#### EII:HUM-002 — Land-use intensity

<!-- eii:{"id":"EII:HUM-002","domain":"D14","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["measured","derived","pressure"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["pressure"],"routes":["amr","land"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Measured physical activity/input density under a declared land-use system.
- **Direct observations / derivation:** Harvest frequency, stocking, input or traffic measures per area/time; retain separate components or name index.
- **Inference and limits:** Supports pressure comparison; land-use label alone does not quantify intensity or ecological effect.
- **Supporting indicators:** [EII:FUN-006](#fun-006), [EII:FUN-007](#fun-007), [EII:AGR-010](#agr-010).

<a id="hum-003"></a>

#### EII:HUM-003 — Material-flow account/circularity

<!-- eii:{"id":"EII:HUM-003","domain":"D14","related_domains":["D13"],"record_type":"family","variants":["material_flow","recycled_input_fraction"],"secondary":["derived","pressure"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["pressure"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Physical material inputs, outputs and recycled fractions across a declared system.
- **Direct observations / derivation:** Mass balance by material, Mg/year and recycled/input fraction, excluding double counting.
- **Inference and limits:** Supports resource-flow comparison; recycled fraction does not demonstrate low total demand or low ecological impact.
- **Supporting indicators:** [EII:FUN-010](#fun-010), [EII:HUM-004](#hum-004), [EII:HUM-006](#hum-006).

<a id="hum-004"></a>

#### EII:HUM-004 — Energy demand/return

<!-- eii:{"id":"EII:HUM-004","domain":"D14","related_domains":["D13"],"record_type":"family","variants":["energy_demand","energy_return_ratio"],"secondary":["measured","derived","pressure"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["pressure"],"routes":["amr","iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Energy consumed and useful energy output relative to a stated investment.
- **Direct observations / derivation:** Metered/embodied energy accounting, MJ/year and output/input ratio with system boundary.
- **Inference and limits:** Supports energetic comparison; fuel mix, service delivered and lifecycle allocation must be retained.
- **Supporting indicators:** [EII:AGR-011](#agr-011), [EII:HUM-003](#hum-003), [EII:HUM-006](#hum-006).

<a id="hum-005"></a>

#### EII:HUM-005 — Water withdrawal/consumption

<!-- eii:{"id":"EII:HUM-005","domain":"D14","related_domains":["D13"],"record_type":"family","variants":["water_withdrawal","water_consumption"],"secondary":["measured","derived","pressure"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["pressure"],"routes":["iot","amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Water abstracted and water not returned within the declared system are distinct flows.
- **Direct observations / derivation:** Meters and water balance, m³/year with source and return-flow timing.
- **Inference and limits:** Supports water-pressure assessment; withdrawal is not equivalent to basin consumption or scarcity impact.
- **Supporting indicators:** [EII:FUN-007](#fun-007), [EII:HYD-012](#hyd-012), [EII:HYD-017](#hyd-017).

<a id="hum-006"></a>

#### EII:HUM-006 — Lifecycle greenhouse-gas intensity

<!-- eii:{"id":"EII:HUM-006","domain":"D14","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived","modelled","pressure"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["pressure"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Method-defined greenhouse-gas emissions per functional unit over a declared lifecycle.
- **Direct observations / derivation:** Activity data × versioned emission factors and GWP horizon, kg CO₂e/unit service/product.
- **Inference and limits:** Supports climate-impact comparison; allocation, land-use change and omitted processes affect comparability.
- **Supporting indicators:** [EII:CYC-002](#cyc-002), [EII:CYC-003](#cyc-003), [EII:AGR-011](#agr-011), [EII:FUN-002](#fun-002).

<a id="hum-007"></a>

#### EII:HUM-007 — Artificial light at night

<!-- eii:{"id":"EII:HUM-007","domain":"D14","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","pressure"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["pressure"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Nighttime light exposure at the sensor or biological receptor.
- **Direct observations / derivation:** Calibrated radiance/illuminance and spectrum, W/m²/sr or lux; declare viewing and time.
- **Inference and limits:** Supports exposure assessment; satellite brightness does not directly represent organism-level dose or biological harm.
- **Supporting indicators:** [EII:BIO-012](#bio-012), [EII:BIO-002](#bio-002), [EII:FUN-009](#fun-009).

<a id="hum-008"></a>

#### EII:HUM-008 — Anthropogenic noise exposure

<!-- eii:{"id":"EII:HUM-008","domain":"D14","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","pressure"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["pressure"],"routes":["iot"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Acoustic pressure spectrum and level attributable to declared human sources.
- **Direct observations / derivation:** Calibrated sound records, dB referenced to stated medium/pressure; weighting and time interval explicit.
- **Inference and limits:** Supports disturbance-exposure assessment; hearing ranges, backgrounds and source attribution affect biological interpretation.
- **Supporting indicators:** [EII:BIO-012](#bio-012), [EII:BIO-002](#bio-002), [EII:FUN-009](#fun-009).

<a id="hum-009"></a>

#### EII:HUM-009 — Resource import dependence

<!-- eii:{"id":"EII:HUM-009","domain":"D14","related_domains":["D13"],"record_type":"indicator","variants":[],"secondary":["derived","context"],"tertiary":{"spatial":["farm","watershed","region"],"temporal":["year"]},"quaternary":["context"],"routes":["amr"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Fraction of specified resource demand supplied from outside a declared area/system.
- **Direct observations / derivation:** Physical supply and demand accounts, % or mass/year with trade origin.
- **Inference and limits:** Supports dependency assessment; imported-resource share alone does not determine environmental sustainability.
- **Supporting indicators:** [EII:HUM-003](#hum-003), [EII:HUM-005](#hum-005), [EII:AGR-009](#agr-009).

<a id="d15"></a>

### 15. Planetary and regional boundaries

<a id="fun-014"></a>

#### EII:FUN-014 — Planetary / regional boundary exceedance

<!-- eii:{"id":"EII:FUN-014","domain":"D15","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","modelled"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Boundary exceedance compares a specified control variable against a cited threshold and scale.
- **Direct observations / derivation:** Observed/modelled variable and versioned threshold; report signed difference or appropriate ratio with uncertainty.
- **Inference and limits:** Supports framework-specific pressure assessment; a global threshold cannot be allocated locally without an explicit scientifically justified method.
- **Supporting indicators:** [EII:PB-001](#pb-001), [EII:PB-002](#pb-002), [EII:PB-003](#pb-003), [EII:PB-004](#pb-004).

<a id="pb-001"></a>

#### EII:PB-001 — Atmospheric CO₂/radiative forcing control variables

<!-- eii:{"id":"EII:PB-001","domain":"D15","related_domains":[],"record_type":"family","variants":["CO2_concentration","radiative_forcing"],"secondary":["measured","modelled","pressure"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Version-specific climate control variables used by a cited boundary framework.
- **Direct observations / derivation:** Global CO₂ concentration, ppm, and/or forcing, W/m², with reference baseline and threshold source.
- **Inference and limits:** Supports framework-based climate-pressure comparison; do not treat local CO₂ or a farm footprint as a global boundary value.
- **Supporting indicators:** [EII:ATM-006](#atm-006), [EII:HUM-006](#hum-006), [EII:FUN-014](#fun-014).

<a id="pb-002"></a>

#### EII:PB-002 — Biosphere genetic/functional integrity controls

<!-- eii:{"id":"EII:PB-002","domain":"D15","related_domains":[],"record_type":"family","variants":["genetic_integrity_control","functional_integrity_control"],"secondary":["modelled","pressure"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Distinct framework-defined measures of genetic loss and functional alteration.
- **Direct observations / derivation:** Named extinction-rate estimate and framework-specific functional control variable; record version and uncertainty.
- **Inference and limits:** Supports global biosphere assessment; local richness cannot substitute for global extinction or functional alteration.
- **Supporting indicators:** [EII:BIO-016](#bio-016), [EII:FUN-001](#fun-001), [EII:FUN-014](#fun-014).

<a id="pb-003"></a>

#### EII:PB-003 — Biogeochemical N/P control variables

<!-- eii:{"id":"EII:PB-003","domain":"D15","related_domains":[],"record_type":"family","variants":["N_control","P_control"],"secondary":["derived","modelled","pressure"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Version-specific human alteration of large-scale nitrogen/phosphorus flows.
- **Direct observations / derivation:** Global/regional fixation, application or ocean-export budgets, mass/year, under cited framework.
- **Inference and limits:** Supports nutrient-pressure comparison; farm surplus is not interchangeable with a global boundary control variable.
- **Supporting indicators:** [EII:CYC-004](#cyc-004), [EII:CYC-007](#cyc-007), [EII:HYD-018](#hyd-018).

<a id="pb-004"></a>

#### EII:PB-004 — Freshwater blue/green change controls

<!-- eii:{"id":"EII:PB-004","domain":"D15","related_domains":[],"record_type":"family","variants":["blue_water_change","green_water_change"],"secondary":["derived","modelled","pressure"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":["drought"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Framework-specific departures of surface flow and root-zone moisture from reference variability.
- **Direct observations / derivation:** Spatially aggregated streamflow/soil-moisture anomalies under the cited version's procedure.
- **Inference and limits:** Supports freshwater-change assessment; withdrawal, drought index and anomaly controls represent different concepts.
- **Supporting indicators:** [EII:HYD-001](#hyd-001), [EII:HYD-006](#hyd-006), [EII:HUM-005](#hum-005).

<a id="pb-005"></a>

#### EII:PB-005 — Land-system change control variables

<!-- eii:{"id":"EII:PB-005","domain":"D15","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","pressure"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":["land"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Framework-specific remaining forest/biome extent relative to reference.
- **Direct observations / derivation:** Harmonised biome-specific land/forest maps and specified reference fractions.
- **Inference and limits:** Supports land-system-pressure comparison; tree cover alone does not establish native forest integrity or an allocated regional boundary.
- **Supporting indicators:** [EII:DIS-004](#dis-004), [EII:DIS-005](#dis-005), [EII:BIO-005](#bio-005).

<a id="pb-006"></a>

#### EII:PB-006 — Stratospheric ozone

<!-- eii:{"id":"EII:PB-006","domain":"D15","related_domains":[],"record_type":"indicator","variants":[],"secondary":["measured","derived"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Column ozone used with a specified global/reference comparison.
- **Direct observations / derivation:** Validated atmospheric column retrieval/observations, Dobson units, with latitude/season.
- **Inference and limits:** Supports stratospheric protection assessment; surface ozone is a distinct variable and local readings cannot substitute.
- **Supporting indicators:** [EII:ATM-007](#atm-007), [EII:FUN-014](#fun-014), [EII:PB-001](#pb-001).

<a id="pb-007"></a>

#### EII:PB-007 — Novel-entity releases/assessment coverage

<!-- eii:{"id":"EII:PB-007","domain":"D15","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","pressure"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Version-specific pollution pressure and capacity to assess/manage released substances.
- **Direct observations / derivation:** Chemical release inventories, mass/time and declared assessment/coverage metrics.
- **Inference and limits:** Supports pollution-governance screening based on empirical accounts; no universally interchangeable concentration threshold exists for all novel entities.
- **Supporting indicators:** [EII:SOI-013](#soi-013), [EII:HYD-020](#hyd-020), [EII:AGR-003](#agr-003).

<a id="pb-008"></a>

#### EII:PB-008 — Ocean acidification control variable

<!-- eii:{"id":"EII:PB-008","domain":"D15","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","pressure"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":["marine"],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Version-specific ocean carbonate saturation relative to a stated reference.
- **Direct observations / derivation:** Carbonate chemistry and computed aragonite saturation, dimensionless with reference fraction declared.
- **Inference and limits:** Supports acidification-pressure assessment; local pH alone does not establish the global control variable or all biological effects.
- **Supporting indicators:** [EII:HYD-022](#hyd-022), [EII:HYD-015](#hyd-015), [EII:BIO-019](#bio-019).

<a id="pb-009"></a>

#### EII:PB-009 — Atmospheric aerosol loading control variable

<!-- eii:{"id":"EII:PB-009","domain":"D15","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","pressure"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Version-specific aerosol optical loading/distribution measure.
- **Direct observations / derivation:** Validated aerosol optical depth or specified hemispheric contrast, dimensionless.
- **Inference and limits:** Supports framework-based aerosol assessment; PM mass, optical depth and regional climate effects are not interchangeable.
- **Supporting indicators:** [EII:ATM-008](#atm-008), [EII:ATM-005](#atm-005), [EII:FUN-014](#fun-014).

<a id="pb-010"></a>

#### EII:PB-010 — Regional ecological threshold departure

<!-- eii:{"id":"EII:PB-010","domain":"D15","related_domains":[],"record_type":"indicator","variants":[],"secondary":["derived","modelled"],"tertiary":{"spatial":["region","planet"],"temporal":["year","decade"]},"quaternary":["system_pressure","threshold_comparison"],"routes":[],"refs":[],"status":"curated_working_definition"} -->

- **Definition:** Departure of a measured ecological variable from a justified regional threshold.
- **Direct observations / derivation:** Named variable, reference, threshold derivation and uncertainty in compatible units; report sign/direction.
- **Inference and limits:** Supports regional assessment; thresholds require local evidence and are not automatic downscalings of planetary boundaries.
- **Supporting indicators:** [EII:FUN-014](#fun-014), [EII:HYD-017](#hyd-017), [EII:FUN-013](#fun-013).

## Appendix A — Source routes and interoperable observation schema

The following registry is machine-readable. It stores **route-level possibilities**, not completed dataset links. The GISDS register remains authoritative for provider names/access/coverage/licences. Computation/viewing services `RS020` and `RS022`, AI summaries `RS008`, and general discovery resources do not supply ecological observations merely by displaying or processing them. They can later be recorded as `processed_by` or discovery context, never substituted for original data provenance. Only relevant existing RS IDs are used below; unused catalogue IDs remain intact in GISDS.

Bind only the selected source(s) and product(s), not every candidate in a route. Unbound indicators with `routes: []` require an independently registered field/laboratory/model dataset or a future contributing catalogue. Empty routes mean “no suitable specific route established from reviewed catalogues”, not “no scientific acquisition method exists”. Even records with candidate routes commonly require complementary field or laboratory observations beyond GISDS.

```json
{
  "schema_version": "eii.inventory/1.0",
  "document_version": "0.2.0",
  "date": "2026-10-13",
  "namespace": "EII",
  "record_count": 235,
  "source_routes": {
    "opt": {
      "namespace": "GISDS",
      "external_ids": [
        "RS001",
        "RS002"
      ],
      "role": "candidate_input",
      "input": "Product-specific calibrated optical reflectance with suitable bands",
      "dataset_id": null,
      "status": "candidate_unbound"
    },
    "rededge": {
      "namespace": "GISDS",
      "external_ids": [
        "RS001"
      ],
      "role": "candidate_input",
      "input": "Selected Sentinel-2 red-edge/NIR bands with recorded wavelengths and matched spatial support",
      "dataset_id": null,
      "status": "candidate_unbound"
    },
    "rgb": {
      "namespace": "GISDS",
      "external_ids": [
        "RS021"
      ],
      "role": "candidate_input",
      "input": "Selected orthophoto with calibrated RGB; own cameras require separate acquisition records",
      "dataset_id": null,
      "status": "candidate_unbound"
    },
    "veg": {
      "namespace": "GISDS",
      "external_ids": [
        "RS004",
        "RS001",
        "RS002"
      ],
      "role": "candidate_input",
      "input": "Selected vegetation product or suitable reflectance; field validation required",
      "dataset_id": null,
      "status": "candidate_unbound"
    },
    "terrain": {
      "namespace": "GISDS",
      "external_ids": [
        "RS021"
      ],
      "role": "candidate_input",
      "input": "Selected DTM/LiDAR/orthophoto product; local field surveys remain separate",
      "dataset_id": null,
      "status": "candidate_unbound"
    },
    "thermal": {
      "namespace": "GISDS",
      "external_ids": [
        "RS002"
      ],
      "role": "candidate_input",
      "input": "Selected Landsat thermal product; local canopy thermography is a separate acquisition",
      "dataset_id": null,
      "status": "candidate_unbound"
    },
    "sar": {
      "namespace": "GISDS",
      "external_ids": [
        "RS001"
      ],
      "role": "candidate_input",
      "input": "Selected Sentinel radar product with declared processing",
      "dataset_id": null,
      "status": "candidate_unbound"
    },
    "land": {
      "namespace": "GISDS",
      "external_ids": [
        "RS004",
        "RS005",
        "RS006",
        "RS009"
      ],
      "role": "candidate_input",
      "input": "One or more geographically suitable land-classification products; harmonise taxonomy and versions",
      "dataset_id": null,
      "status": "candidate_unbound"
    },
    "water": {
      "namespace": "GISDS",
      "external_ids": [
        "RS013"
      ],
      "role": "candidate_input",
      "input": "Selected surface-water occurrence/seasonality product; not discharge observations",
      "dataset_id": null,
      "status": "candidate_unbound"
    },
    "flood": {
      "namespace": "GISDS",
      "external_ids": [
        "RS014"
      ],
      "role": "candidate_input",
      "input": "Selected observed inundation product; keep forecasts separate",
      "dataset_id": null,
      "status": "candidate_unbound"
    },
    "drought": {
      "namespace": "GISDS",
      "external_ids": [
        "RS015"
      ],
      "role": "candidate_input",
      "input": "Selected drought indicator and its underlying variable/method; not a universal moisture or future-climate source",
      "dataset_id": null,
      "status": "candidate_unbound"
    },
    "fire": {
      "namespace": "GISDS",
      "external_ids": [
        "RS016",
        "RS017"
      ],
      "role": "candidate_input",
      "input": "Selected event/burn-area/thermal-detection product with product-specific semantics",
      "dataset_id": null,
      "status": "candidate_unbound"
    },
    "marine": {
      "namespace": "GISDS",
      "external_ids": [
        "RS018"
      ],
      "role": "candidate_input",
      "input": "Selected marine variable, distinguishing observation from model and surface from depth",
      "dataset_id": null,
      "status": "candidate_unbound"
    },
    "settlement": {
      "namespace": "GISDS",
      "external_ids": [
        "RS019"
      ],
      "role": "candidate_input",
      "input": "Selected built-up/settlement product; roads and engineering detail need independent datasets",
      "dataset_id": null,
      "status": "candidate_unbound"
    },
    "reef": {
      "namespace": "GISDS",
      "external_ids": [
        "RS012"
      ],
      "role": "candidate_context",
      "input": "Mapped reef habitat; live coral/bleaching outcomes require field or specialised observations",
      "dataset_id": null,
      "status": "candidate_unbound"
    },
    "mangrove": {
      "namespace": "GISDS",
      "external_ids": [
        "RS011"
      ],
      "role": "candidate_input",
      "input": "Mangrove extent/change; condition requires additional observations",
      "dataset_id": null,
      "status": "candidate_unbound"
    },
    "amr": {
      "namespace": "AMRKB",
      "external_ids": [],
      "document": "README.md",
      "version": "0.1.0",
      "role": "method_or_management_context",
      "input": "Scientific/technical practices, input records and experimental context only; no observation dataset reviewed",
      "dataset_id": null,
      "status": "scope_only"
    },
    "iot": {
      "namespace": null,
      "planned_channel": "iot",
      "external_ids": [],
      "role": "future_input",
      "input": "Future calibrated, georeferenced sensor streams; project namespace and dataset IDs not assigned",
      "dataset_id": null,
      "status": "unresolved_future"
    },
    "bio": {
      "namespace": null,
      "planned_channel": "bioinformatics",
      "external_ids": [],
      "role": "future_input",
      "input": "Future biological observations and pipeline outputs; local project namespace and accessions not assigned",
      "dataset_id": null,
      "status": "unresolved_future"
    }
  },
  "provenance": [
    {
      "path": "/Users/jonathan/Github/ecological-information/EII/EII.md",
      "sha256": "47f7098f999cbb2570464d198793a11b0624386ee9b43fad0a2e9edd3451d547"
    },
    {
      "path": "/Users/jonathan/Github/ecological-information/EII/README.md",
      "sha256": "41429e550fc7fb4ccc313543f320a8e14df49bfcab5881e7137061ebf0bb0d92"
    },
    {
      "path": "/Users/jonathan/Github/ecological-information/GISDS/Cartography_Database_Sources.md",
      "sha256": "82cec11c4eb6706ac200db2986631c3e25831ae6424f3b955e4bcfa0813ec1b8"
    },
    {
      "path": "/Users/jonathan/Github/ecological-information/GISDS/README.md",
      "sha256": "84b225b53b0999c4d46144e7436f93560ddbf29d79e587ad7bbd38e9f2ab3a8c"
    },
    {
      "path": "/Users/jonathan/Github/ecological-information/AMRKB/README.md",
      "sha256": "4eb11eb8f9ead8d907007dc26d0c469d8dda78b1d250b9dab1b9205d10708ea1"
    }
  ]
}
```

### Binding observations without inflating the inventory

Keep actual measurements in contributing datasets. A future binding/observation record should include:

```json
{
  "eii_id": "EII:SOI-005",
  "variant": "organic_C_stock",
  "observation_id": null,
  "binding_status": "unbound",
  "source_namespace": null,
  "source_record_id": null,
  "dataset_id": null,
  "dataset_version": null,
  "relation": "derived_from",
  "method_id": null,
  "method_version": null,
  "observed_property": "soil organic carbon stock in a declared layer",
  "value": null,
  "unit": "Mg C/ha",
  "location_id": null,
  "geometry": null,
  "crs": null,
  "spatial_support": null,
  "depth_interval_cm": null,
  "time_start": null,
  "time_end": null,
  "input_observation_ids": [],
  "processing": null,
  "calibration": null,
  "uncertainty": null,
  "quality_flags": [],
  "detection_limit": null,
  "licence": null,
  "attribution": null,
  "retrieved_at": null
}
```

This is an unfilled schema example, not an actual measurement. `null` means unknown/unbound, never zero; missing values and non-detects must remain distinguishable. Use ISO 8601 timestamps with timezone, explicit dry/wet and element/compound mass bases, documented units and named uncertainty models. Add sensors/calibration/drift/gaps for IoT; add sample/depth/accessions, extraction/primers, controls, library size, normalisation, annotation/reference versions and pipeline version for bioinformatics. Store exact dataset URLs and product-specific rights at binding time.

Relations are controlled: `observed_in`, `derived_from`, `estimated_by`, `contextualised_by`, `processed_by`, `supported_by`. Source routes above remain candidates; AMRKB should normally bind as `contextualised_by` or a separately identified technical method, not `observed_in`, until actual observations exist. A future dataset's namespace must be registered deliberately, rather than inferring a new database identity from the labels “IoT” or “bioinformatics”.

For actual computational dependencies, store `input_observation_ids` and the formula/pipeline independently of the inventory's interpretive `support`. A field-validated NDVI biomass model should bind both reflectance and calibration observations and declare an `estimated_by` relation; it must not relabel NDVI itself as measured biomass.

### SOC stock calculation example

Using organic C concentration in g/kg, compatible fine-earth bulk density in g/cm³, layer thickness in cm and coarse-fragment volume fraction, a commonly used stock form is:

`SOC stock (Mg C/ha) = C (g/kg) × BD_fine (g/cm³) × thickness (cm) × (1 − coarse_fragment_volume_fraction) × 0.1`.

The density denominator and fragment correction must match: do not apply the correction twice if density already expresses dry fine-earth mass per total sample volume. Sum declared layers; use consistent/equivalent soil mass for repeated comparisons where density changes. Concentration, stock and stock-change rate remain separate variants/records. [FAO Annex 4](https://www.fao.org/fileadmin/user_upload/GSP/MRV/GSP_MRV_Protocol_A4_EN_002.pdf).

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

## Appendix C — Cross-domain interpretation examples

| Question | Indicator combination | Required qualification |
|---|---|---|
| Does a greener canopy indicate better water status? | VEG-001, VEG-011, VEG-013, HYD-001, VEG-020, ATM-003 | Separate leaf area, chlorophyll, water access and atmospheric demand; calibrate by species and season. |
| Is carbon actually accumulating? | SOI-005 stock variant, SOI-002, SOI-014, FUN-002, CYC-001 | Repeat compatible stocks with uncertainty, account for depth/mass, export and gas fluxes; SOC % alone is insufficient. |
| Are nitrogen-cycling genes expressing realised function? | MIC-010/011/012, MIC-022, MIC-023, CYC-004/005, CYC-002 | DNA → transcription → process are distinct observations; sample together and measure substrate/environment. |
| Does a technical agricultural intervention improve outcomes? | AMRKB method context; FUN-004, AGR-001/002, SOI-003/005, HYD-018, BIO-008 | Compare matched controls over time; retain trade-offs and confounders rather than presuming benefit from a method label. |
| Does mapped connectivity support biological movement? | BIO-007, LAN-004, BIO-015, INT-007, BIO-016 | Validate pathways with movement/genetic evidence and demographic context; spatial similarity is insufficient. |
| Has a disturbed ecosystem recovered? | DIS-009, RES-001/002/005, VEG-017, BIO-002, FUN-001, MIC-024 | Use explicit reference conditions and multiple responses; greenness recovery alone is narrow evidence. |

## Maintenance, validation and next review

New IDs are assigned once; edits preserve identity unless a concept changes enough to require a new record and explicit relation. Definitions and formulas must cite the selected convention; variant additions must not change old series meaning. New dataset links need actual source-system IDs and a resolved binding. Add new contributing scientific/technological catalogues to the route registry without duplicating their authoritative records or introducing excluded-project dependencies.

Before using an indicator operationally: select the variant and assay/product; confirm units and method version; validate context-specific inference; record uncertainty, spatial/temporal support and sampling design. For modelled/composite/predictive outputs, keep inputs, weights, baseline, validation and scenario explicit. Verify specialist entries against primary protocols during Stage B, prioritising molecular functions, composite indices, remote trait retrievals and threshold comparisons.

### Version history

- **0.2.0 — 13 October 2026:** Expanded the 120-record baseline into the 15-domain master register; retained every original ID and preferred label; added working definitions, observed inputs, units, qualified inferences, supporting-ID links and four-level classifications. Removed the excluded programme crosswalk and excluded interoperability dependencies. Added candidate GISDS source routes, scope-only AMRKB context, unresolved future channels, variant discipline, provenance hashes and schema validation.
- **0.1.0 — 10 October 2026:** Original consolidated inventory; retained as the reviewed provenance baseline, including sections intentionally removed from this edition.
