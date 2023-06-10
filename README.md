# Patuli Model
This repository contains the code and resources for building a real-time Indonesian sign language (Bisindo) object detection model specifically designed for a mobile app. The model utilizes transfer learning techniques with SSD MobileNet V2 FPNLite architecture to accurately detect and localize sign language gestures in real-time video streams.

---

## Model Description
The real-time sign language object detection model is built using transfer learning, leveraging the pre-trained weights of SSD MobileNet V2 FPNLite 320x320 on a large-scale image recognition dataset. By fine-tuning the model on a custom dataset of sign language images, it has been trained to recognize and classify sign language gestures in real-time.

More information for the model: [here](#)

The model consists of three seperate model, each trained to detect specific categories:
- Abjad (Alphabet): Detects and classifies various alphabet signs ([26 classes](#))
- Angka (Number): Detects and classifies various number signs. ([11 classes](#))
- Kata (Word): Detects and classifies various word signs. ([23 classes](#))

The trained models have been converted into optimized .tflite format for efficient deployment on mobile devices. The model is also quantized to reduce the model size while maintaining accuracy.

## Dataset
The training dataset used for this project consists of a large collection of annotated sign language images. The dataset includes diverse samples of different sign language gestures, captured under various lighting conditions, backgrounds, and hand orientations. The annotations provide bounding box coordinates and corresponding labels for each sign language gesture

Link to the dataset: [here](#)

## Tensorboard
[V1] 
- Abjad:
- Angka:
- Kata:

[V2]
- Abjad:
- Angka:
- Kata:

[V3]
- Abjad:
- Angka:
- Kata: