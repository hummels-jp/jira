# PLATEAU 调查笔记

> Jira: **WL-17**
> 创建日期: 2026-07-15
> 分类: 调查 / 基础资料
> 🌐 语言: **中文（本文档）** · [日本語](00_PLATEAU_ja.md) · [English](00_PLATEAU_en.md)

---

<a id="sec-1"></a>
## 1. PLATEAU 是什么

> 🌐 **中文** · [日本語](00_PLATEAU_ja.md#sec-1) · [English](00_PLATEAU_en.md#sec-1)

**PLATEAU（プラトー）** 是日本国土交通省主导的 **3D 城市模型建设、利用及开放数据化项目**。

- **启动年份**: 2020 年度
- **主管部门**: 国土交通省 都市局
- **官方网站**: <https://www.mlit.go.jp/plateau/>
- **目标**: 将日本全国城市 3D 数字孪生化，为城市规划、防灾、自动驾驶、仿真等提供通用基础设施。

---

<a id="sec-2"></a>
## 2. 数据规格

> 🌐 **中文** · [日本語](00_PLATEAU_ja.md#sec-2) · [English](00_PLATEAU_en.md#sec-2)

| 项目 | 内容 |
|---|---|
| **标准规格** | CityGML 2.0 / 3.0（OGC 标准） |
| **分发格式** | CityGML, 3D Tiles, MVT, FBX, OBJ, GeoJSON |
| **坐标系** | 平面直角坐标系 / JGD2011 |
| **许可协议** | 知识共享署名 4.0 (CC BY 4.0) |
| **覆盖范围** | 全国 200+ 城市（截至 2025 年） |

### 主要地物类别（LOD）

- **建筑物** (Building) — LOD1〜LOD4
- **道路** (Transportation) — LOD1〜LOD3
- **土地利用** (LandUse)
- **城市设施** (CityFurniture)
- **植被** (Vegetation)
- **灾害风险** (UrbanPlanning 扩展)

---

<a id="sec-3"></a>
## 3. 主要应用场景

> 🌐 **中文** · [日本語](00_PLATEAU_ja.md#sec-3) · [English](00_PLATEAU_en.md#sec-3)

1. **防灾仿真** — 洪水、海啸、泥石流灾害可视化
2. **自动驾驶 / MaaS** — HD 地图补充、仿真器地图
3. **城市规划** — 日照、景观、容积率仿真
4. **智慧城市 / 数字孪生** — 与 IoT 数据联动
5. **XR / 元宇宙** — 基于真实城市的空间体验

---

<a id="sec-4"></a>
## 4. 数据获取

> 🌐 **中文** · [日本語](00_PLATEAU_ja.md#sec-4) · [English](00_PLATEAU_en.md#sec-4)

- **G 空间信息中心**: <https://www.geospatial.jp/ckan/dataset?q=plateau>
- **PLATEAU VIEW**: <https://plateauview.mlit.go.jp/>
- **GitHub 官方**: <https://github.com/Project-PLATEAU>

---

<a id="sec-5"></a>
## 5. 相关工具 / SDK

> 🌐 **中文** · [日本語](00_PLATEAU_ja.md#sec-5) · [English](00_PLATEAU_en.md#sec-5)

| 工具 | 用途 |
|---|---|
| **PLATEAU SDK for Unity** | 在 Unity 中导入 CityGML |
| **PLATEAU SDK for Unreal** | Unreal Engine 版本 |
| **plateau-py** | 用 Python 读写 CityGML |
| **FME / QGIS 插件** | 与 GIS 联动 |
| **Cesium / deck.gl** | Web 3D 可视化 |

---

<a id="sec-6"></a>
## 6. 与自动驾驶（CARLA / Autoware）的联动要点

> 🌐 **中文** · [日本語](00_PLATEAU_ja.md#sec-6) · [English](00_PLATEAU_en.md#sec-6)

- **HD 地图生成**: CityGML 道路 LOD3 → Lanelet2 / OpenDRIVE 转换
- **建筑几何**: 为 CARLA 仿真器输出 FBX
- **交叉口、信号**: 从 CityFurniture 提取
- **互操作性**: 与 OSM / DGM 混合运用较为现实

---

<a id="sec-7"></a>
## 7. 后续行动 (TODO)

> 🌐 **中文** · [日本語](00_PLATEAU_ja.md#sec-7) · [English](00_PLATEAU_en.md#sec-7)

- [ ] 下载目标城市的 PLATEAU 数据
- [ ] CityGML → OpenDRIVE 转换 PoC
- [ ] 确认 Autoware 用 Lanelet2 地图生成流程
- [ ] CARLA 上的可视化测试

---

<a id="sec-8"></a>
## 8. HD 地图生成详情: CityGML LOD3 → Lanelet2 / OpenDRIVE

> 🌐 **中文** · [日本語](00_PLATEAU_ja.md#sec-8) · [English](00_PLATEAU_en.md#sec-8)

---

<a id="sec-8-1"></a>
### 8.1 CityGML 道路数据（Transportation Module）按 LOD 分级

> 🌐 **中文** · [日本語](00_PLATEAU_ja.md#sec-8-1) · [English](00_PLATEAU_en.md#sec-8-1)

| LOD | 表现 | 内容 | HD Map 用途 |
|---|---|---|---|
| LOD0 | 中心线（1D linestring） | 道路网络、拓扑 | ❌ 仅导航级 |
| LOD1 | 面（2D polygon） | 道路总面积、无车道区分 | ❌ |
| LOD2 | 表面（含辅助区） | 车道 / 人行道 / 中央分离带分离 | △ 半自动 |
| **LOD3** | **车道级 3D 几何** | **各车道独立面 + 附属物** | ✅ **HD Map 数据源** |
| LOD4 | 室内 | 隧道内部等 | 特殊场景 |

---

<a id="sec-8-2"></a>
### 8.2 LOD3 道路数据的构成要素

> 🌐 **中文** · [日本語](00_PLATEAU_ja.md#sec-8-2) · [English](00_PLATEAU_en.md#sec-8-2)

#### (1) 几何要素（Geometry）

- **TrafficArea（通行区域）**
  - 车行道 (driving lane) / 自行车道 (cycle lane) / 人行道 (sidewalk)
  - 停车带 (parking) / 公交专用道 (bus lane)
- **AuxiliaryTrafficArea（辅助区域）**
  - 中央分离带、路肩、绿化带、导流岛
- 每个 area 都是独立的 **3D 多边形（含 Z 值）**

#### (2) 车道属性（Lane Attributes）

| 属性 | 说明 |
|---|---|
| `function` | 用途（driving / cycle / pedestrian…） |
| `usage` | 通行方式（单向 / 双向 等） |
| `surfaceMaterial` | 路面材质（asphalt / concrete） |
| `numberOfLanes` | 车道数 |
| `width` | 车道宽度 |
| `slope` / `gradient` | 坡度 |

#### (3) 道路附属物（CityFurniture / Road Markings）

- **标线**: 车道分界线、停止线、斑马线、导流线
- **标志**: 限速、指示、警告
- **信号灯**: 交通信号灯、行人信号灯
- **护栏 / 中央隔离带**
- **路缘石（curb）**
- **井盖 / 排水沟**

#### (4) 拓扑关系（Topology）

- **Intersection（交叉点）**: 车道连接关系
- **Section（路段）**: 分段管理
- **Connectivity**: predecessor / successor 关系

#### (5) 语义信息（Semantics）

CityGML 3.0 强化了 **SpaceBoundary** 语义标注：
- 车道边界类型（实线 / 虚线 / 双黄线）
- 路面颜色
- 通行规则

---

<a id="sec-8-3"></a>
### 8.3 转换映射: CityGML LOD3 → **Lanelet2**（Autoware 使用）

> 🌐 **中文** · [日本語](00_PLATEAU_ja.md#sec-8-3) · [English](00_PLATEAU_en.md#sec-8-3)

| CityGML | Lanelet2 |
|---|---|
| TrafficArea (driving) | `Lanelet`（车道原语） |
| 车道左右边界线 | `LineString`（bound） |
| Intersection | `Lanelet` 组 + `RegulatoryElement` |
| 停止线 / 斑马线 | `RegulatoryElement`（stop_line, crosswalk） |
| 信号灯 | `RegulatoryElement`（traffic_light） |
| 拓扑连接 | Lanelet 的 relation 关系 |

**输出**: `.osm` 格式（Lanelet2 使用 OSM XML 扩展）

---

<a id="sec-8-4"></a>
### 8.4 转换映射: CityGML LOD3 → **OpenDRIVE**（CARLA 使用）

> 🌐 **中文** · [日本語](00_PLATEAU_ja.md#sec-8-4) · [English](00_PLATEAU_en.md#sec-8-4)

| CityGML | OpenDRIVE (.xodr) |
|---|---|
| 道路中心线 | `<road>` + `<planView>`（geometry: line/arc/spiral） |
| 车道面 | `<lanes>` + `<laneSection>` + `<lane>` |
| 高程 | `<elevationProfile>` |
| 超高 / 横坡 | `<lateralProfile>` |
| 交叉口 | `<junction>` + `<connection>` |
| 标线 | `<roadMark>` |
| 信号 | `<signals>` / `<signal>` |
| 物体（护栏等） | `<objects>` / `<object>` |

**输出**: `.xodr` 文件（与 CARLA-90 中 `NOA_CITYWAY_V3.0.xodr` 同格式）

---

<a id="sec-8-5"></a>
### 8.5 转换难点

> 🌐 **中文** · [日本語](00_PLATEAU_ja.md#sec-8-5) · [English](00_PLATEAU_en.md#sec-8-5)

1. **中心线提取**: CityGML LOD3 是**面**表达 → 需 skeleton 算法提取中心线
2. **几何拟合**: OpenDRIVE 要求参数化曲线（line/arc/spiral/poly3） → 需曲线拟合
3. **拓扑重建**: LOD3 的连接信息不完整 → 需重建交叉口
4. **标线关联**: CityFurniture 的标线需匹配到对应车道
5. **信号绑定**: 交通信号需绑定到 controlled lane

---

<a id="sec-8-6"></a>
### 8.6 工具链

> 🌐 **中文** · [日本語](00_PLATEAU_ja.md#sec-8-6) · [English](00_PLATEAU_en.md#sec-8-6)

| 工具 | 方向 | 说明 |
|---|---|---|
| **plateau-py** | 读取 | Python 解析 CityGML |
| **PLATEAU SDK for Unity** | 可视化 | Unity 内浏览 |
| **CityGML2OBJs** | 3D | Mesh 转换 |
| **FME / QGIS 插件** | ETL | 商业 GIS 转换 |
| **lanelet2 (C++/Py)** | 生成 | Autoware 官方 API |
| **esmini / CommonRoad** | OpenDRIVE | 验证与编辑 |
| **carla-map-editor** | CARLA | .xodr 微调 |

---

<a id="sec-ref"></a>
## 参考链接

> 🌐 **中文** · [日本語](00_PLATEAU_ja.md#sec-ref) · [English](00_PLATEAU_en.md#sec-ref)

- 国交省 PLATEAU 官方: <https://www.mlit.go.jp/plateau/>
- PLATEAU VIEW: <https://plateauview.mlit.go.jp/>
- GitHub: <https://github.com/Project-PLATEAU>
- OGC CityGML: <https://www.ogc.org/standards/citygml>

---
