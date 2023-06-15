<p align="center">
    <img src="preview.png?raw=true" alt="Preview">
</p>

<h1 align="center">Patuli Bisindo Sign Language Model</h1>

This repository contains the code and resources for building a real-time Indonesian sign language (Bisindo) object detection model specifically designed for a mobile app. The model utilizes transfer learning techniques with SSD MobileNet V2 FPNLite architecture to accurately detect and localize sign language gestures in real-time video streams.

---

## Description

This real-time Bisindo sign language object detection model is built using transfer learning, leveraging the pre-trained weights of SSD MobileNet V2 FPNLite 320x320 on a large-scale image recognition dataset. By fine-tuning the model on a custom dataset of sign language images, it has been trained to recognize and classify sign language gestures in real-time.

More information for the model: [here](https://arxiv.org/abs/1801.04381v4)

The model consists of three seperate model, each trained to detect specific categories:

- Abjad (Alphabet): Detects and classifies various alphabet signs ([26 classes](Training/V2/Abjad/classes.txt))
- Angka (Number): Detects and classifies various number signs. ([11 classes](Training/V2/Angka/classes.txt))
- Kata (Word): Detects and classifies various word signs. ([23 classes](Training/V2/Kata/classes.txt))

The trained models have been converted into optimized `.tflite` format for efficient deployment on mobile devices. The model is also quantized to reduce the model size while maintaining accuracy.

## Model Performance

We have trained the models three time with each version having improved dataset and different training parameters. The following show the links for the Tensorboard visualization of the training process for each model:

- <details>
  <summary>Model V1</summary>

  [V1](Models/V1) is our experimental model, trained with varying steps and still not optimized datasets.

  - [Abjad](https://tensorboard.dev/experiment/IVQTyqHVQ3mquX9DeMozUg/#scalars&runSelectionState=eyJ2MS90cmFpbmluZy90cmFpbiI6dHJ1ZSwidjIvdHJhaW5pbmcvdHJhaW4iOmZhbHNlLCJ2My90cmFpbmluZy90cmFpbiI6ZmFsc2V9)
  - [Angka](https://tensorboard.dev/experiment/c8dWKgsRRTKj6xeob6ZBLg/#scalars&runSelectionState=eyJ2MS90cmFpbmluZy90cmFpbiI6dHJ1ZSwidjIvdHJhaW5pbmcvdHJhaW4iOmZhbHNlLCJ2My90cmFpbmluZy90cmFpbiI6ZmFsc2V9)
  - [Kata](https://tensorboard.dev/experiment/wtLb1cerQMOk1ayoQHw6YA/)

</details>

- <details>
  <summary>Model V2 (We use this in the application)</summary>

  [V2](Models/V2) is our first production model, trained with optimized dataset and 40k steps of training.

  - [Abjad](https://tensorboard.dev/experiment/IVQTyqHVQ3mquX9DeMozUg/#scalars&runSelectionState=eyJ2MS90cmFpbmluZy90cmFpbiI6ZmFsc2UsInYyL3RyYWluaW5nL3RyYWluIjp0cnVlLCJ2My90cmFpbmluZy90cmFpbiI6ZmFsc2V9)
  - [Angka](https://tensorboard.dev/experiment/c8dWKgsRRTKj6xeob6ZBLg/#scalars&runSelectionState=eyJ2MS90cmFpbmluZy90cmFpbiI6ZmFsc2UsInYyL3RyYWluaW5nL3RyYWluIjp0cnVlLCJ2My90cmFpbmluZy90cmFpbiI6ZmFsc2V9)
  - [Kata](https://tensorboard.dev/experiment/AIAlog5kSk2KRXJuyZjGxQ/)

</details>

- <details>
  <summary>Model V3</summary>

  [V3](Models/V3) is our second production model, trained with the same dataset as V2 and this time with less steps of training (20k steps).

  - [Abjad](https://tensorboard.dev/experiment/IVQTyqHVQ3mquX9DeMozUg/#scalars&runSelectionState=eyJ2MS90cmFpbmluZy90cmFpbiI6ZmFsc2UsInYyL3RyYWluaW5nL3RyYWluIjpmYWxzZSwidjMvdHJhaW5pbmcvdHJhaW4iOnRydWV9)
  - [Angka](https://tensorboard.dev/experiment/c8dWKgsRRTKj6xeob6ZBLg/#scalars&runSelectionState=eyJ2MS90cmFpbmluZy90cmFpbiI6ZmFsc2UsInYyL3RyYWluaW5nL3RyYWluIjpmYWxzZSwidjMvdHJhaW5pbmcvdHJhaW4iOnRydWV9)
  - [Kata](https://tensorboard.dev/experiment/m476V1CKQZy0HDaA2rkcMw/)

</details>

## Our Dataset

The training dataset used for this project consists of a large collection of annotated sign language images. The dataset includes diverse samples of different sign language gestures, captured under various lighting conditions, backgrounds, and hand orientations. The annotations provide bounding box coordinates and corresponding labels for each sign language gesture.

Link to the dataset:

- [**Abjad**](https://universe.roboflow.com/patuli-fbumd/patuli-alphabetical-dataset)
- [**Angka**](https://universe.roboflow.com/patuli-fbumd/patuli-numbers-dataset)
- [**Kata**](https://universe.roboflow.com/patuli-fbumd/patuli-words-dataset)

## Training the Model

To train the model, you can do it locally or on Google Colab. For our case, we trained the model locally on a machine with CUDA enabled GPU in a linux environment using WSL2 (Ubuntu 20 LTS). You need to train the model in a linux environment because some of the commands used in the training process are linux specific.

To train the model locally, you can follow the steps below:

1. Ensure that you have installed CUDA and cuDNN on your machine. You can follow the steps [here](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html) to install CUDA and [here](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html) to install cuDNN. We follow [this guide](https://gist.github.com/adwellj/2769957e7fc8c7e9372e5f4b06f72b80) to install CUDA on our WSL2 Ubuntu.
2. Install the WSL extension on your VSCode.
3. Prepare a virtual environment to train your model. You can follow the steps [here](https://docs.python.org/3/tutorial/venv.html) to create a virtual environment.
4. Visit our dataset links above and download the dataset in `code` format **to get your own API Key**. You can also just download it manually, move it to your project directory, and skip the downloading process of the dataset in the notebook, make sure that you download it in VOC format.
5. Clone the repository, open the notebooks in its own directory or as a root directory.
6. Follow the steps in the notebook to train the model.

To train the model on Google Colab, you will need to set the python version to 3.8.10, you can follow the steps below:

1. Create a new notebook on Google Colab.
2. Import the notebook from this repository.
3. Follow the steps in the notebook to train the model.
4. After you have finished training the model, you can download the model from the notebook.