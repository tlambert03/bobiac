# Ilastik for Pixel Classification

In this section, we will explore how to use **Ilastik** for **semantic segmentation** through [**pixel classification**](https://www.ilastik.org/documentation/pixelclassification/pixelclassification). This process involves training a machine learning model to classify pixels in an image based on user-defined labels.

In particular, we will...

We will be using the [pixel classification dataset]() TODO: update the link.

## Slides

<a
    class="custom-button custom-download-button" href="../../../pdfs/05_segmentation/machine_learning/templates.pdf" download> <i class="fas fa-download"></i> Download this Slides
</a>

<div align="center"> <iframe class="custom-pdf-frame" src="../../../pdfs/05_segmentation/machine_learning/templates.pdf"> </iframe> </div>

## What is Pixel Classification?

**Pixel classification** is a fundamental image analysis technique that involves **assigning a specific category or class to each pixel** in an image based on its unique features, such as color, intensity, or texture. This approach is particularly valuable in tasks like **semantic segmentation**, where the objective is to **divide an image into meaningful regions** by categorizing pixels into predefined classes, such as background, foreground, or distinct objects.

## Ilastik Pixel Classification Workflow

### 1. Select the Workflow

When you open **Ilastik**, you will see the [Startup Screen](https://www.ilastik.org/documentation/basics/startup) with various workflows. Select the **Pixel Classification** workflow by clicking on it. You will be automaticaly brought to the **Input Data** step.

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/1a.png" alt="Ilastik Logo" width="800"> </div>

### 2. Load the Image Data

Next, you will need to [load the image data](https://www.ilastik.org/documentation/basics/dataselection) you want to use to train the classifier. Select the **Raw Data** tab and either *Drag and drop* your image files into the **Add New...** field of the data table or click on it to select your images. To create a robust classifier, you should load multiple images from the dataset. For this exercise, you can load 3 random images from the [pixel classification dataset]().

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/1b.png" alt="Ilastik Logo" width="800"> </div>

Once loaded, you can view the images by clicking on the image name in the data table. The corresponding image will be displayed in the window viewer.

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/1d.png" alt="Ilastik Logo" width="800"> </div>

### 3. Select the Features

To continue, click on the **Feature Selection** step (on the left side of the GUI) and then on the **Select Features...** button. Here, you can select the [features](https://www.ilastik.org/documentation/pixelclassification/pixelclassification#selecting-good-features) that will be used for classification. **Ilastik** provides a variety of features, including intensity, texture, and shape descriptors.

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/2a.png" alt="Ilastik Logo" width="800"> </div>