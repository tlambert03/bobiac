# Ilastik for Pixel Classification

In this section, we will explore how to use **Ilastik** for **semantic segmentation** through [**pixel classification**](https://www.ilastik.org/documentation/pixelclassification/pixelclassification). This process involves training a machine learning model to classify pixels in an image based on user-defined labels.

TODO: add image ML + link to dataset

In this exercise, we will use a <a href="../../../_static/data/05_segmentation_ilastik.zip" download> <i class="fas fa-download"></i> dataset of nuclei images</a>, and the goal is to train a classifier to distinguish between **nuclei** and **background**.

<div class="alert alert-info">
    <strong>NOTE:</strong> Ilastik supports a variety of <a href="https://www.ilastik.org/documentation/basics/dataselection#formats" target="_blank">data formats</a>. For simplicity and ease of use during this course, we will use images saved as <strong>.tif</strong> files. However, Ilastik recommends using files saved as <strong>.h5</strong> for optimal performance. If you wish to use your own dataset and need to convert your files to <strong>.h5</strong>, Ilastik provides tools such as a <a href="https://www.ilastik.org/documentation/fiji_export/plugin" target="_blank">Fiji plugin</a> or a <a href="https://github.com/ilastik/ilastik/tree/main/notebooks/h5convert" target="_blank">Jupyter Notebook</a> with instructions.
</div>

## Slides

<a
    class="custom-button custom-download-button" href="../../../pdfs/05_segmentation/machine_learning/templates.pdf" download> <i class="fas fa-download"></i> Download this Slides
</a>

<div align="center"> <iframe class="custom-pdf-frame" src="../../../pdfs/05_segmentation/machine_learning/templates.pdf"> </iframe> </div>

## What is Pixel Classification?

**Pixel classification** is a fundamental image analysis technique that involves **assigning a specific category or class to each pixel** in an image based on its unique features, such as color, intensity, or texture. This approach is particularly valuable in tasks like **semantic segmentation**, where the objective is to **divide an image into meaningful regions** by categorizing pixels into predefined classes, such as background, foreground, or distinct objects.

## Ilastik Pixel Classification Workflow

For a detailed workflow instruction, you can refer to the [Ilastik documentation](https://www.ilastik.org/documentation/pixelclassification/pixelclassification).

### 1. Select the Workflow

When you open **Ilastik**, you will see the [Startup Screen](https://www.ilastik.org/documentation/basics/startup) with various workflows. Select the **Pixel Classification** workflow by clicking on it. You will be automaticaly brought to the **Input Data** step.

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/1a.png" alt="Ilastik Logo" width="800"> </div>

### 2. Load the Image Data

Next, you will need to [load the image data](https://www.ilastik.org/documentation/basics/dataselection) you want to use to train the classifier. Select the **Raw Data** tab and either *Drag and drop* your image files into the **Add New...** field of the data table or click on it to select your images. To create a robust classifier, you should load multiple images from the dataset. For this exercise, you can load 3 random images from the [pixel classification dataset]().

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/1b.png" alt="Ilastik Logo" width="800"> </div>

Once loaded, you can view the images by clicking on the image name in the data table. The corresponding image will be displayed in the window viewer.

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/1d.png" alt="Ilastik Logo" width="800"> </div>

### 3. Select the Features

To continue, click on the **Feature Selection** step (on the left side of the GUI) and then on the **Select Features...** button. Here, you can select the [features](https://www.ilastik.org/documentation/pixelclassification/pixelclassification#selecting-good-features) and their scales (how much) that will be used to discriminate between the different classes of pixels.

For pixel classification, **Ilastik** provides a list of features types, divided by **Color/Intensity**, **Edge**, and **Texture**:

- **Color/Intensity**: these features should be selected if the color or brightness can be used to discern objects
- **Edge**: should be selected if brightness or color gradients can be used to discern objects.
- **Texture**: this might be an important feature if the objects in the image have a special textural appearance.

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/2a.png" alt="Ilastik Logo" width="730"> </div>

<br>

For each of the feature you can also choose the **scale**. The scales correspond to the *sigma of the Gaussian* which is used to smooth the image before application of the filter. Filters with larger sigmas can thus pull in information from larger neighborhoods, but average out the fine details.

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/2b.png" alt="Ilastik Logo" width="730"> </div>

<br>

After clicking on **Ok**, you can **visualize the effect of the selected features** by clicking on one of the options in the **Features** list in the bottom left part of the GUI. This will help you understand if the selected features are suitable for your dataset. You can always go back to the **Feature Selection** step to change the features and their scales.

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/2c.png" alt="Ilastik Logo" width="800"> </div>

### 4. Annotate the Images

