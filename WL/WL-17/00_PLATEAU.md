# PLATEAU（プラトー）調査ノート

> Jira: **WL-17**
> 作成日: 2026-07-15
> 分類: 調査 / 基礎資料

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

## 参考リンク

- 国交省 PLATEAU 公式: <https://www.mlit.go.jp/plateau/>
- PLATEAU VIEW: <https://plateauview.mlit.go.jp/>
- GitHub: <https://github.com/Project-PLATEAU>
- OGC CityGML: <https://www.ogc.org/standards/citygml>
