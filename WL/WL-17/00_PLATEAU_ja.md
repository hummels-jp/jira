# PLATEAU（プラトー）調査ノート

> Jira: **WL-17**
> 作成日: 2026-07-15
> 分類: 調査 / 基礎資料
> 言語版: [中文](00_PLATEAU.md) / **日本語（本文書）** / [English](00_PLATEAU_en.md)

---

## 1. PLATEAU とは

**PLATEAU（プラトー）** は、日本の国土交通省が主導する **3D 都市モデル整備・活用・オープンデータ化プロジェクト**。

- **開始年**: 2020 年度
- **主管**: 国土交通省 都市局
- **公式サイト**: <https://www.mlit.go.jp/plateau/>
- **目的**: 全国の都市を 3D デジタルツイン化し、まちづくり・防災・自動運転・シミュレーション等に活用できる共通基盤を提供する。

---

## 2. データ規格

| 項目 | 内容 |
|---|---|
| **標準規格** | CityGML 2.0 / 3.0（OGC 標準） |
| **配布形式** | CityGML, 3D Tiles, MVT, FBX, OBJ, GeoJSON |
| **座標系** | 平面直角座標系 / JGD2011 |
| **ライセンス** | クリエイティブ・コモンズ 表示 4.0 (CC BY 4.0) |
| **カバー範囲** | 全国 200 以上の都市（2025 年時点） |

### 主な地物クラス（LOD）

- **建築物** (Building) — LOD1〜LOD4
- **道路** (Transportation) — LOD1〜LOD3
- **土地利用** (LandUse)
- **都市設備** (CityFurniture)
- **植生** (Vegetation)
- **災害リスク** (UrbanPlanning 拡張)

---

## 3. 主要ユースケース

1. **防災シミュレーション** — 洪水・津波・土砂災害の可視化
2. **自動運転 / MaaS** — HD マップ補完、シミュレータ地図
3. **都市計画** — 日照・景観・容積率シミュレーション
4. **スマートシティ / デジタルツイン** — IoT データとの連携
5. **XR / メタバース** — 実都市ベースの空間体験

---

## 4. データ入手

- **G 空間情報センター**: <https://www.geospatial.jp/ckan/dataset?q=plateau>
- **PLATEAU VIEW**: <https://plateauview.mlit.go.jp/>
- **GitHub (公式)**: <https://github.com/Project-PLATEAU>

---

## 5. 関連ツール / SDK

| ツール | 用途 |
|---|---|
| **PLATEAU SDK for Unity** | Unity 上で CityGML をインポート |
| **PLATEAU SDK for Unreal** | Unreal Engine 版 |
| **plateau-py** | Python から CityGML を読み書き |
| **FME / QGIS プラグイン** | GIS 連携 |
| **Cesium / deck.gl** | Web 3D ビジュアライズ |

---

## 6. 自動運転（CARLA / Autoware）との連携ポイント

- **HD マップ生成**: CityGML の道路 LOD3 → Lanelet2 / OpenDRIVE 変換
- **建物ジオメトリ**: CARLA のシミュレータ用 FBX 出力
- **交差点・信号**: CityFurniture から抽出
- **相互運用**: OSM / DGM とのハイブリッド運用が現実的

---

## 7. 次のアクション（TODO）

- [ ] 対象都市の PLATEAU データダウンロード
- [ ] CityGML → OpenDRIVE 変換 PoC
- [ ] Autoware 用 Lanelet2 マップ生成フロー確認
- [ ] CARLA 上での可視化テスト

---

## 8. HD マップ生成詳細: CityGML LOD3 → Lanelet2 / OpenDRIVE

### 8.1 CityGML 道路データ（Transportation Module）の LOD 別内容

| LOD | 表現 | 内容 | HD Map 用途 |
|---|---|---|---|
| LOD0 | 中心線（1D linestring） | 道路ネットワーク・トポロジー | ❌ ナビ級のみ |
| LOD1 | 面（2D polygon） | 道路総面積、車線区分なし | ❌ |
| LOD2 | 表面（補助区含む） | 車道 / 歩道 / 中央帯を分離 | △ 半自動 |
| **LOD3** | **車線レベル 3D ジオメトリ** | **各車線独立面 + 附属物** | ✅ **HD Map ソース** |
| LOD4 | 屋内 | トンネル内部等 | 特殊シーン |

### 8.2 LOD3 道路データの構成要素

#### (1) ジオメトリ要素（Geometry）

- **TrafficArea（通行区域）**
  - 車道 (driving lane) / 自転車道 (cycle lane) / 歩道 (sidewalk)
  - 駐車帯 (parking) / バス専用道 (bus lane)
- **AuxiliaryTrafficArea（補助区域）**
  - 中央分離帯・路肩・緑化帯・導流島
- 各 area は独立した **3D ポリゴン（Z 値付き）**

#### (2) 車線属性（Lane Attributes）

| 属性 | 説明 |
|---|---|
| `function` | 用途（driving / cycle / pedestrian…） |
| `usage` | 通行方式（一方通行 / 双方向 等） |
| `surfaceMaterial` | 路面材質（asphalt / concrete） |
| `numberOfLanes` | 車線数 |
| `width` | 車線幅 |
| `slope` / `gradient` | 勾配 |

#### (3) 道路附属物（CityFurniture / Road Markings）

- **標示（マーキング）**: 車線境界線・停止線・横断歩道・導流線
- **標識**: 制限速度・指示・警告
- **信号機**: 交通信号機・歩行者信号
- **ガードレール / 中央分離帯**
- **縁石（curb）**
- **マンホール / 排水溝**

#### (4) トポロジー関係（Topology）

- **Intersection（交差点）**: 車線接続関係
- **Section（路段）**: セグメント管理
- **Connectivity**: predecessor / successor 関係

#### (5) セマンティクス（Semantics）

CityGML 3.0 では **SpaceBoundary** による意味付けが強化：
- 車線境界タイプ（実線 / 破線 / 二重黄線）
- 路面色
- 通行規則

### 8.3 変換マッピング: CityGML LOD3 → **Lanelet2**（Autoware）

| CityGML | Lanelet2 |
|---|---|
| TrafficArea (driving) | `Lanelet`（車線プリミティブ） |
| 車線左右境界線 | `LineString`（bound） |
| Intersection | `Lanelet` グループ + `RegulatoryElement` |
| 停止線 / 横断歩道 | `RegulatoryElement`（stop_line, crosswalk） |
| 信号機 | `RegulatoryElement`（traffic_light） |
| トポロジー接続 | Lanelet の relation 関係 |

**出力**: `.osm` 形式（Lanelet2 は OSM XML 拡張を使用）

### 8.4 変換マッピング: CityGML LOD3 → **OpenDRIVE**（CARLA）

| CityGML | OpenDRIVE (.xodr) |
|---|---|
| 道路中心線 | `<road>` + `<planView>`（geometry: line/arc/spiral） |
| 車線面 | `<lanes>` + `<laneSection>` + `<lane>` |
| 高さ | `<elevationProfile>` |
| 超高 / 横断勾配 | `<lateralProfile>` |
| 交差点 | `<junction>` + `<connection>` |
| 標示 | `<roadMark>` |
| 信号 | `<signals>` / `<signal>` |
| オブジェクト（ガードレール等） | `<objects>` / `<object>` |

**出力**: `.xodr` ファイル（CARLA-90 の `NOA_CITYWAY_V3.0.xodr` と同形式）

### 8.5 変換の難所（Challenges）

1. **中心線抽出**: CityGML LOD3 は**面**表現 → skeleton アルゴリズムで中心線算出
2. **幾何フィッティング**: OpenDRIVE はパラメトリック曲線（line/arc/spiral/poly3）必須 → 曲線フィッティング
3. **トポロジー再構築**: LOD3 の接続情報は不完全 → 交差点を再構築
4. **標示の紐付け**: CityFurniture の標示を対応車線にマッチング
5. **信号バインド**: 交通信号を controlled lane に紐付け

### 8.6 ツールチェーン

| ツール | 方向 | 説明 |
|---|---|---|
| **plateau-py** | 読取 | Python で CityGML パース |
| **PLATEAU SDK for Unity** | 可視化 | Unity 内で閲覧 |
| **CityGML2OBJs** | 3D | Mesh 変換 |
| **FME / QGIS プラグイン** | ETL | 商用 GIS 変換 |
| **lanelet2 (C++/Py)** | 生成 | Autoware 公式 API |
| **esmini / CommonRoad** | OpenDRIVE | 検証・編集 |
| **carla-map-editor** | CARLA | .xodr 微調整 |

---

## 参考リンク

- 国交省 PLATEAU 公式: <https://www.mlit.go.jp/plateau/>
- PLATEAU VIEW: <https://plateauview.mlit.go.jp/>
- GitHub: <https://github.com/Project-PLATEAU>
- OGC CityGML: <https://www.ogc.org/standards/citygml>
