# Automotive Project - Data Annotation Management

> This document is for AI annotation team leads / project managers, systematically covering the core concepts, tools, formats, and management essentials required for automotive data annotation projects.

---

## 1. Computer Vision (CV) Fundamentals
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)

### 1.1 Image Classification
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Definition**: Assign a single category label to the entire image; answers "what is in this image?"
- **Automotive scenarios**: Recognize vehicle brand, model, color; determine weather/lighting conditions (sunny / rainy / nighttime).
- **Annotation form**: No bounding required; only a label for the whole image.
- **Common models**: ResNet, EfficientNet, VGG.

### 1.2 Object Detection
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Definition**: Locate objects in an image and draw a Bounding Box around them, along with the class label.
- **Automotive scenarios**: Detect vehicles, pedestrians, traffic signs, traffic lights, lane-line obstacles, etc.
- **Annotation form**: BBox + class label.
- **Common models**: YOLO series, Faster R-CNN, SSD.
- **Key metrics**: mAP (mean Average Precision), IoU (Intersection over Union).

### 1.3 Semantic Segmentation
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Definition**: Assign every pixel in the image to a class; does not distinguish individual instances.
- **Automotive scenarios**: Distinguish drivable areas (road), non-drivable areas (sidewalk, building), sky, vegetation, etc.
- **Annotation form**: Pixel-level Mask; all pixels of the same category belong to one class.
- **Common models**: U-Net, DeepLab, SegFormer.
- **Note**: Two closely adjacent vehicles will be colored the same; it does not tell "car A vs car B".

### 1.4 Instance Segmentation
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Definition**: On top of semantic segmentation, further distinguish different individuals within the same class.
- **Automotive scenarios**: Not only know "this is a car", but also "this is car 1, this is car 2", each with an independent contour.
- **Annotation form**: Pixel-level Mask + instance ID.
- **Common models**: Mask R-CNN, SOLO, YOLO-Seg.
- **Difference from semantic segmentation**: Instance segmentation generates a separate Mask for each target object.

### 1.5 Keypoint Annotation
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Definition**: Mark semantically meaningful feature points on the target object.
- **Automotive scenarios**: Driver pose estimation (eyes, nose, shoulders, hands); vehicle keypoints (headlights, wheel centers, side mirrors).
- **Annotation form**: Coordinate point (x, y) + visibility flag (visible / occluded / not labeled).
- **Common models**: OpenPose, HRNet.
- **Remarks**: May not be immediately needed in current automotive projects, but belongs to fundamental CV capability reserves.

---

## 2. Annotation Tools
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)

### 2.1 CVAT (Computer Vision Annotation Tool)
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Developer**: Intel OpenVINO team.
- **Features**: Open-source, free, Web-based collaboration, comprehensive functionality.
- **Supported formats**: Image classification, object detection (BBox), segmentation (Polygon / Mask), keypoints, video tracking, 3D annotation.
- **Applicable scenarios**: Medium-to-large team projects; supports multi-user collaboration, task assignment, quality review.
- **Advantages**: Supports automated annotation (AI-assisted pre-labeling), semi-automatic tracking, integration with model training pipelines.

### 2.2 LabelMe
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Developer**: MIT.
- **Features**: Lightweight open-source tool, available in desktop and online versions.
- **Supported formats**: Primarily Polygon annotation; BBox also supported.
- **Applicable scenarios**: Small-scale projects, rapid prototyping, academic research.
- **Output format**: Default JSON, containing polygon vertex coordinates.
- **Advantages**: Simple and easy to use, low learning curve; downside is weak collaboration features.

### 2.3 Label Studio
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Developer**: Heartex (now Human Signal).
- **Features**: Open-source, highly configurable, supports multiple data types (image, text, audio, video, time series).
- **Applicable scenarios**: Projects requiring flexible annotation interface configurations or multi-modal mixed annotation.
- **Advantages**: Powerful template system; can integrate with ML models for Active Learning.
- **Automotive applications**: In addition to images, it can also be used for voice command annotation, in-vehicle sensor time-series annotation.

### 2.4 Scale AI
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Nature**: Commercial annotation platform (not open-source), providing "Annotation as a Service".
- **Features**: Has its own annotator workforce; clients upload data and Scale completes annotation and delivery.
- **Applicable scenarios**: Projects with sufficient budget, tight timelines, and a need for high-quality rapid delivery.
- **Advantages**: Strict quality control (multi-round QA, golden standard set), supports 3D point cloud annotation (LiDAR).
- **Note**: High cost, usually billed by annotation volume; suitable for autonomous driving 3D annotation needs in the automotive industry.

---

## 3. Annotation Types in Detail
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)

### 3.1 BBox (Bounding Box)
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Form**: Rectangle defined by top-left and bottom-right coordinates, or (center x, y + width w + height h).
- **Format examples**: `(x_min, y_min, x_max, y_max)` or `(cx, cy, w, h)` (normalized or pixel values).
- **Applicable tasks**: Object detection.
- **Pros & cons**: Fast and low-cost to annotate; but includes background noise inside the box, and is less precise for occluded or rotated targets.

### 3.2 Polygon
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Form**: Closed polygon made of a series of connected vertices, fitting any shape.
- **Format example**: `[(x1,y1), (x2,y2), ..., (xn,yn)]`.
- **Applicable tasks**: Precise object detection, instance segmentation, semantic segmentation.
- **Pros & cons**: More accurate than BBox, reduces background interference; but takes longer to annotate.
- **Automotive scenarios**: Precisely outline vehicle contours, road boundaries, irregular obstacles.

### 3.3 Mask (Pixel Mask)
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Form**: Binary matrix of the same size as the image; target region is 1 (or 255), background is 0.
- **Format examples**: PNG mask images, RLE (Run-Length Encoding).
- **Applicable tasks**: Semantic segmentation, instance segmentation.
- **Pros & cons**: Pixel-level precision; large file size, highest annotation workload.
- **Generation methods**: Can be drawn manually, converted from Polygon fill, or generated by models and then manually corrected.

### 3.4 Keypoint
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Form**: Mark predefined feature point coordinates on the target object.
- **Format example**: `{"point_id": 1, "x": 120, "y": 80, "visibility": 2}`.
- **Visibility flags**: Typically 0 = not labeled, 1 = visible, 2 = occluded (but position is inferable).
- **Applicable tasks**: Pose estimation, facial keypoints, vehicle part localization.
- **Automotive scenarios**: DMS (Driver Monitoring System) eye tracking, head pose estimation.

### 3.5 Image Classification and Grouping / Labeling
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Classification**: Assign a primary label to the entire image, e.g., `scene: highway`, `weather: rainy`.
- **Grouping**: Group images from the same batch or scene together for easier management and training sampling.
- **Labeling / Indexing**:
  - Define the label taxonomy according to client needs, e.g., vehicle types `[sedan, suv, truck, bus, motorcycle]`.
  - Build label hierarchies: Level 1 (vehicle / pedestrian / traffic facility) → Level 2 (vehicle → sedan / truck / bus).
  - Note mutual exclusivity vs multi-label: some scenarios allow only one primary class per image (single-label), while others allow multiple (multi-label).

---

## 4. Dataset Management Formats
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)

### 4.1 COCO Format (Common Objects in Context)
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Origin**: Standard dataset format introduced by Microsoft; now an industry-wide common standard.
- **File structure**: Single JSON file containing five top-level fields: `info`, `licenses`, `images`, `annotations`, `categories`.
- **Key field descriptions**:
  - `images`: Image ID, filename, width, height.
  - `annotations`: Annotation ID, image ID, category ID, BBox (`[x, y, width, height]`), Area, Segmentation (Polygon or RLE), Keypoints.
  - `categories`: Category ID, name, supercategory, keypoint definitions (if any).
- **Applicable scenarios**: Object detection, instance segmentation, keypoint detection, panoptic segmentation.
- **Automotive value**: If the client requires COCO format, it can be directly used to train mainstream frameworks such as Detectron2 and MMDetection.

### 4.2 YOLO Format (You Only Look Once)
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Origin**: Concise format introduced by Ultralytics along with the YOLO detector.
- **File structure**: One `.txt` file per image, with the same filename as the image.
- **Content format**: Each line represents one object, format is `<class_id> <x_center> <y_center> <width> <height>` (all normalized relative to image width/height, between 0 and 1).
- **Example**: `0 0.5 0.5 0.3 0.4` means class 0 object centered in the image, width 30%, height 40%.
- **Characteristics**: Extremely concise, one line per box, no extra nested structure.
- **Applicable scenarios**: YOLO series model training (YOLOv5 / v8 / v9 / v10, etc.).
- **Automotive value**: Many mass-production embedded deployments (e.g., NVIDIA Jetson) run YOLO directly; clients often request this format.

### 4.3 VOC Format (PASCAL VOC)
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Origin**: Early standard defined by the PASCAL VOC Challenge (2005–2012).
- **File structure**: XML files (Annotations), one XML per image.
- **Key fields**: `filename`, `size` (width/height/depth), `object` (name, pose, truncated, difficult, bndbox with xmin/ymin/xmax/ymax).
- **Directory structure**: `Annotations/` (XML), `JPEGImages/` (images), `ImageSets/Main/` (train/val/test split txts).
- **Applicable scenarios**: Classic object detection tasks; some legacy systems or European clients may still require this format.
- **Automotive value**: Legacy project migration, compatibility with existing data pipelines.

### 4.4 JSON Format (General Structured)
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Nature**: Not a specific standard, but refers to the flexible array/dictionary style.
- **Common variants**:
  - **LabelMe JSON**: `{"shapes": [{"label": "car", "points": [[x1,y1], ...], "shape_type": "polygon"}]}`.
  - **Custom JSON**: Define fields according to project needs, such as adding `attributes` (color, brand, pose).
- **Advantages**: Flexible and extensible, easy for programmatic parsing, suitable for front-end/back-end transmission.
- **Automotive scenarios**: When clients have custom needs (e.g., additionally annotating vehicle color, angle, occlusion rate), JSON is the most convenient to extend.

### 4.5 XML Format (Extensible Markup Language)
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Nature**: Similar to JSON, a general structured data format using tag nesting.
- **Common variants**:
  - **PASCAL VOC XML**: As described above.
  - **CVAT XML**: CVAT-exported XML contains richer metadata (image attributes, label attributes, tracking information).
- **Advantages**: Strict Schema validation, suitable for enterprise-level system exchange; good human readability (clear hierarchy).
- **Disadvantages**: File size usually larger than JSON, parsing slightly slower.
- **Conversion relationships**: In practice, frequent conversions between COCO ↔ YOLO ↔ VOC ↔ JSON are needed; conversion scripts must be written or reused.

### 4.6 Format Selection Strategy
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Client requirements first**: Confirm what input format the client's model training framework expects.
- **Storage strategy**: It is recommended to store data in the "richest format" (such as COCO or custom JSON) as the "master format", and convert to YOLO / VOC upon export.
- **Version management**: When iterating the dataset, annotation files should be managed separately from image files, using Git-LFS or DVC for version control.

---

## 5. Project Management Essentials
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)

### 5.1 Project Background Description (for interviews / negotiations)
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Project type**: Clarify the annotation type (2D image detection, 3D point cloud, semantic segmentation, multi-sensor fusion).
- **Industry domain**: Emphasize automotive / autonomous driving / intelligent cockpit background to highlight domain expertise.
- **Data scale**:
  - Total images (e.g., 50,000).
  - Total annotation targets (e.g., 200,000 BBoxes).
  - Number of categories (e.g., 12 classes: vehicle, pedestrian, cyclist, traffic signs, etc.).

### 5.2 Team and Process Management
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Annotation modes**:
  - **Single annotator**: Fast, low cost, suitable for simple tasks.
  - **Double annotation (two independent annotators)**: Two people annotate the same image separately; differences are compared via IoU or pixel overlap, and disagreements are arbitrated; suitable for high-precision requirements.
  - **Consensus (multi-person voting)**: Pass if two out of three agree; suitable for complex scenes.
- **QA workflow**:
  - **Sampling inspection**: Randomly extract 10%–20% of data for full manual inspection.
  - **Golden Set**: Reserve a set of "standard answers" annotated by experts; periodically use it to assess annotators.
  - **Automated QA**: Write scripts to check whether bounding boxes are out of bounds, whether categories are empty, whether there are missed targets.
- **Communication mechanisms**:
  - Confirm the label taxonomy and edge cases with the client.
  - Establish regular sync meetings (Weekly Sync) to report progress and blockers.
  - All QA issues and specification changes must be documented in writing (Email / Confluence / Notion).

### 5.3 Budget and Delivery
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Budget composition**:
  - Labor cost (annotators × working hours).
  - Tool / platform fees (e.g., Scale AI billed per image, or CVAT server costs).
  - QA and project management overhead (usually 15%–20%).
- **Delivery cycle estimation**:
  - First conduct a small pilot batch to measure average time per image (e.g., 2 minutes per image).
  - Formula: `Total hours = Number of images × Time per image ÷ Number of parallel annotators`.
  - Reserve a 20% buffer for rework and QA.
- **Quality metrics**:
  - **Accuracy**: Compared against client standards; BBox IoU > 0.85 is considered qualified.
  - **Recall**: Miss rate < 2%.
  - **Consistency**: Consistent within the same annotator over time, and controllable variance between different annotators.

### 5.4 Deliverables
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Data package structure**:
  ```
  project_delivery/
  ├── images/              # Raw images
  ├── annotations/         # Annotation files (by format)
  │   ├── coco/
  │   ├── yolo/
  │   └── voc/
  ├── metadata.json        # Dataset metadata (category list, image count, annotation count)
  ├── split/               # Train / validation / test split files
  └── qa_report.pdf        # QA report
  ```
- **Delivery standards**: Standardized file naming, clear directory structure, correct formats, consistent with contract requirements.

---

## 6. Supplementary Notes (Roles and Requirements)
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)

### 6.1 Client Interview and Negotiation
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **First client contact**: The AI lead participates to demonstrate professionalism.
- **Preparation content**:
  - Understand the client's business scenario (ADAS, parking, cockpit monitoring?).
  - Propose an annotation plan (tool selection, label taxonomy, delivery format, timeline).
  - Prepare similar cases (after de-identification) as proof of capability.
- **Common Q&A**:
  - "How do you guarantee quality?" → Double annotation + Golden Set + multi-level QA.
  - "What formats are supported?" → COCO / YOLO / VOC / JSON are all supported; custom conversion available.
  - "What if progress is delayed?" → Buffer reserved, additional manpower can be deployed, daily progress tracking.

### 6.2 Final Quality Gate
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Role positioning**: The AI lead is the final gatekeeper of quality.
- **Gate actions**:
  - Perform final sampling inspection (Final QA) before delivery.
  - Confirm all client-specific requirements are met (e.g., specific occlusion handling rules).
  - Sign the delivery confirmation or send the delivery email.
- **Responsibility**: Once delivered, quality issues are primarily borne by the lead; therefore, strictness is essential.

### 6.3 QA Issues and Client Communication
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Issue collection**: Annotators encounter ambiguous cases during work (e.g., "Should this pedestrian half-blocked by a tree be labeled?"), summarized to the lead.
- **Escalation mechanism**:
  - Level 1: Internal discussion, refer to the Annotation Guideline for resolution.
  - Level 2: If the guideline does not cover, the lead compiles a unified summary and confirms with the client.
  - Level 3: After the client responds, update the guideline and synchronize with all members.
- **Communication principles**:
  - Batch summarize issues to avoid frequent interruptions to the client.
  - Attach example images and current team disagreements for each issue, facilitating rapid client decisions.

### 6.4 Language and Attendance Requirements
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)
- **Japanese proficiency**: Business-level fluent Japanese (N1 or equivalent) required; capable of independent technical discussions and email correspondence.
- **Attendance arrangement**:
  - "0.4 person-month" ≈ approximately 8 days per month (calculated as 20 working days/month × 0.4).
  - Likely a hybrid model of on-site (client office) + remote.
  - Need to confirm that core meeting days require on-site presence; other times can be supported remotely.
- **Other languages**: If the client is a multinational automotive company, English reading and writing skills may also be required.

---

## Appendix: Quick Reference Table
> [中文](data_label.md) | [English](data_label_en.md) | [日本語](data_label_ja.md)

| Capability | Core Points | Interview Must-Knows |
|------------|-------------|----------------------|
| CV Basics | Differences between classification / detection / segmentation / keypoints | Semantic vs. Instance Segmentation |
| Tools | Features of CVAT / LabelMe / LabelStudio / Scale AI | Which to choose for team collaboration |
| Annotation Types | BBox / Polygon / Mask / Keypoint | When to use Polygon instead of BBox |
| Data Formats | COCO / JSON / YOLO / VOC / XML | Familiarity with mutual conversion |
| Project Management | Workflow / QA / Budget / Delivery | How to guarantee 99% accuracy |
| Client Communication | Requirement confirmation / QA escalation / Japanese communication | How to handle ambiguous cases |
