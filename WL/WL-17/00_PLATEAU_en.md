# PLATEAU Research Notes

> Jira: **WL-17**
> Created: 2026-07-15
> Category: Research / Reference
> Language: [中文](00_PLATEAU.md) / [日本語](00_PLATEAU_ja.md) / **English (this document)**

---

## 1. What is PLATEAU

**PLATEAU** is a **3D city model development, utilization, and open data initiative** led by Japan's Ministry of Land, Infrastructure, Transport and Tourism (MLIT).

- **Launched**: FY 2020
- **Managed by**: MLIT City Bureau
- **Official site**: <https://www.mlit.go.jp/plateau/>
- **Goal**: Create 3D digital twins of Japanese cities as a common infrastructure for urban planning, disaster prevention, autonomous driving, and simulation.

---

## 2. Data Specifications

| Item | Content |
|---|---|
| **Standard** | CityGML 2.0 / 3.0 (OGC standard) |
| **Distribution formats** | CityGML, 3D Tiles, MVT, FBX, OBJ, GeoJSON |
| **Coordinate system** | Plane Rectangular Coordinate System / JGD2011 |
| **License** | Creative Commons Attribution 4.0 (CC BY 4.0) |
| **Coverage** | 200+ cities nationwide (as of 2025) |

### Main Feature Classes (LOD)

- **Building** — LOD1 to LOD4
- **Transportation (Road)** — LOD1 to LOD3
- **LandUse**
- **CityFurniture**
- **Vegetation**
- **Disaster Risk** (UrbanPlanning extension)

---

## 3. Main Use Cases

1. **Disaster simulation** — Flood, tsunami, landslide visualization
2. **Autonomous driving / MaaS** — HD map augmentation, simulator maps
3. **Urban planning** — Sunlight, landscape, floor-area-ratio simulation
4. **Smart city / Digital twin** — IoT data integration
5. **XR / Metaverse** — Real-city-based spatial experience

---

## 4. Data Acquisition

- **G-Spatial Information Center**: <https://www.geospatial.jp/ckan/dataset?q=plateau>
- **PLATEAU VIEW**: <https://plateauview.mlit.go.jp/>
- **GitHub (official)**: <https://github.com/Project-PLATEAU>

---

## 5. Related Tools / SDKs

| Tool | Purpose |
|---|---|
| **PLATEAU SDK for Unity** | Import CityGML into Unity |
| **PLATEAU SDK for Unreal** | Unreal Engine version |
| **plateau-py** | Read/write CityGML with Python |
| **FME / QGIS plugins** | GIS integration |
| **Cesium / deck.gl** | Web 3D visualization |

---

## 6. Integration with Autonomous Driving (CARLA / Autoware)

- **HD map generation**: CityGML road LOD3 → Lanelet2 / OpenDRIVE conversion
- **Building geometry**: FBX export for CARLA simulator
- **Intersections / signals**: Extract from CityFurniture
- **Interoperability**: Hybrid use with OSM / DGM is practical

---

## 7. Next Actions (TODO)

- [ ] Download PLATEAU data for target cities
- [ ] PoC for CityGML → OpenDRIVE conversion
- [ ] Confirm Lanelet2 map generation workflow for Autoware
- [ ] Visualization test in CARLA

---

## 8. HD Map Generation Details: CityGML LOD3 → Lanelet2 / OpenDRIVE

### 8.1 CityGML Road Data (Transportation Module) by LOD

| LOD | Representation | Content | HD Map use |
|---|---|---|---|
| LOD0 | Centerline (1D linestring) | Road network, topology | ❌ Navigation-level only |
| LOD1 | Surface (2D polygon) | Total road area, no lane separation | ❌ |
| LOD2 | Surface (with auxiliary) | Roadway / sidewalk / median separated | △ Semi-automated |
| **LOD3** | **Lane-level 3D geometry** | **Each lane as independent surface + attachments** | ✅ **HD Map source** |
| LOD4 | Interior | Tunnel interior, etc. | Special scenes |

### 8.2 Components of LOD3 Road Data

#### (1) Geometry

- **TrafficArea**
  - Driving lane / cycle lane / sidewalk
  - Parking / bus lane
- **AuxiliaryTrafficArea**
  - Median, shoulder, greenbelt, traffic island
- Each area is an independent **3D polygon with Z values**

#### (2) Lane Attributes

| Attribute | Description |
|---|---|
| `function` | Purpose (driving / cycle / pedestrian…) |
| `usage` | Direction (one-way / two-way, etc.) |
| `surfaceMaterial` | Pavement material (asphalt / concrete) |
| `numberOfLanes` | Lane count |
| `width` | Lane width |
| `slope` / `gradient` | Slope |

#### (3) Road Attachments (CityFurniture / Road Markings)

- **Markings**: Lane boundaries, stop lines, crosswalks, channelization
- **Signs**: Speed limits, directional, warning
- **Signals**: Traffic lights, pedestrian signals
- **Guardrails / medians**
- **Curbs**
- **Manholes / drainage**

#### (4) Topology

- **Intersection**: Lane connectivity
- **Section**: Segment management
- **Connectivity**: predecessor / successor relations

#### (5) Semantics

CityGML 3.0 strengthens **SpaceBoundary** semantic tagging:
- Lane boundary type (solid / dashed / double yellow)
- Pavement color
- Traffic rules

### 8.3 Mapping: CityGML LOD3 → **Lanelet2** (Autoware)

| CityGML | Lanelet2 |
|---|---|
| TrafficArea (driving) | `Lanelet` (lane primitive) |
| Left/right lane boundaries | `LineString` (bound) |
| Intersection | `Lanelet` group + `RegulatoryElement` |
| Stop line / crosswalk | `RegulatoryElement` (stop_line, crosswalk) |
| Traffic light | `RegulatoryElement` (traffic_light) |
| Topological connection | Lanelet relation |

**Output**: `.osm` format (Lanelet2 uses OSM XML extension)

### 8.4 Mapping: CityGML LOD3 → **OpenDRIVE** (CARLA)

| CityGML | OpenDRIVE (.xodr) |
|---|---|
| Road centerline | `<road>` + `<planView>` (geometry: line/arc/spiral) |
| Lane surface | `<lanes>` + `<laneSection>` + `<lane>` |
| Elevation | `<elevationProfile>` |
| Superelevation / cross-slope | `<lateralProfile>` |
| Intersection | `<junction>` + `<connection>` |
| Markings | `<roadMark>` |
| Signals | `<signals>` / `<signal>` |
| Objects (guardrails, etc.) | `<objects>` / `<object>` |

**Output**: `.xodr` file (same format as `NOA_CITYWAY_V3.0.xodr` in CARLA-90)

### 8.5 Conversion Challenges

1. **Centerline extraction**: CityGML LOD3 is **surface**-based → need skeleton algorithm
2. **Geometry fitting**: OpenDRIVE requires parametric curves (line/arc/spiral/poly3) → curve fitting
3. **Topology reconstruction**: LOD3 connectivity info is incomplete → rebuild intersections
4. **Marking association**: Match CityFurniture markings to corresponding lanes
5. **Signal binding**: Bind traffic signals to controlled lanes

### 8.6 Toolchain

| Tool | Direction | Description |
|---|---|---|
| **plateau-py** | Read | Parse CityGML with Python |
| **PLATEAU SDK for Unity** | Visualize | Browse in Unity |
| **CityGML2OBJs** | 3D | Convert to Mesh |
| **FME / QGIS plugins** | ETL | Commercial GIS conversion |
| **lanelet2 (C++/Py)** | Generate | Autoware official API |
| **esmini / CommonRoad** | OpenDRIVE | Validation & editing |
| **carla-map-editor** | CARLA | .xodr fine-tuning |

---

## References

- MLIT PLATEAU official: <https://www.mlit.go.jp/plateau/>
- PLATEAU VIEW: <https://plateauview.mlit.go.jp/>
- GitHub: <https://github.com/Project-PLATEAU>
- OGC CityGML: <https://www.ogc.org/standards/citygml>
