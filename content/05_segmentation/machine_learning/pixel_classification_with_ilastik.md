# Ilastik for Pixel Classification

In this section, we will explore how to use **Ilastik** for **semantic segmentation** through [**pixel classification**](https://www.ilastik.org/documentation/pixelclassification/pixelclassification). This process involves training a machine learning model to classify pixels in an image based on user-defined labels.

In this exercise, we will use the <a href="../../../_static/data/05_segmentation_ilastik.zip" download> <i class="fas fa-download"></i> pixel classification dataset</a> of nuclei images, and the goal is to train a classifier to distinguish between **nuclei** and **background**.

<div class="alert alert-info">
    <strong>NOTE:</strong> Ilastik supports a variety of <a href="https://www.ilastik.org/documentation/basics/dataselection#formats" target="_blank">data formats</a>. For simplicity and ease of use during this course, we will use images saved as <strong>.tif</strong> files. However, Ilastik recommends using files saved as <strong>.h5</strong> for optimal performance. If you wish to use your own dataset and need to convert your files to <strong>.h5</strong>, Ilastik provides tools such as a <a href="https://www.ilastik.org/documentation/fiji_export/plugin" target="_blank">Fiji plugin</a> or a <a href="https://github.com/ilastik/ilastik/tree/main/notebooks/h5convert" target="_blank">Jupyter Notebook</a> with instructions.
</div>

## What is Pixel Classification?

**Pixel classification** is a fundamental image analysis technique that involves **assigning a specific category or class to each pixel** in an image based on its unique features, such as color, intensity, or texture. This approach is particularly valuable in tasks like **semantic segmentation**, where the objective is to **divide an image into meaningful regions** by categorizing pixels into predefined classes, such as background, foreground, or distinct objects.

## Ilastik Pixel Classification Workflow

For a detailed workflow instruction, you can refer to the [Ilastik Pixel Classification Documentation](https://www.ilastik.org/documentation/pixelclassification/pixelclassification).

### 1. Select the Workflow

When you open **Ilastik**, you will see the [Startup Screen](https://www.ilastik.org/documentation/basics/startup) with various workflows. Select the ***Pixel Classification*** workflow by clicking on it. You will be automaticaly brought to the **Input Data** step.

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/1a.png" alt="Ilastik Logo" width="800"> </div>

<div class="alert alert-info">
    <strong>NOTE:</strong> Remember to save your project regularly using <strong>Cmd+S</strong> (macOS) or <strong>Ctrl+S</strong> (Windows), or via <strong>Project → Save Project</strong>.
</div>

### 2. Load the Image Data

Next, you will need to [load the image data](https://www.ilastik.org/documentation/basics/dataselection) you want to use to train the classifier. Select the ***Raw Data*** tab and either *Drag and drop* your image files into the ***Add New...*** field of the data table or click on it to select your images. To create a robust classifier, you should load multiple images from the dataset. For this exercise, you can load 3 random images from the <a href="../../../_static/data/05_segmentation_ilastik.zip" download> <i class="fas fa-download"></i> pixel classification dataset</a>.

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/1b.png" alt="Ilastik Logo" width="800"> </div>

Once loaded, you can view the images by clicking on the image name in the data table. The corresponding image will be displayed in the window viewer.

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/1d.png" alt="Ilastik Logo" width="800"> </div>

### 3. Select the Features

To continue, click on the ***Feature Selection*** step (on the left side of the GUI) and then on the ***Select Features...*** button. Here, you can select the [features](https://www.ilastik.org/documentation/pixelclassification/pixelclassification#selecting-good-features) and their scales (how much) that will be used to discriminate between the different classes of pixels.

For pixel classification, **Ilastik** provides a list of features types, divided by ***Color/Intensity***, ***Edge***, and ***Texture***:

- ***Color/Intensity***: these features should be selected if the color or brightness can be used to discern objects
- ***Edge***: should be selected if brightness or color gradients can be used to discern objects.
- ***Texture***: this might be an important feature if the objects in the image have a special textural appearance.

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/2a.png" alt="Ilastik Logo" width="730"> </div>

<br>

For each of the feature you can also choose the ***scale***. The scales correspond to the *sigma of the Gaussian* which is used to smooth the image before application of the filter. Filters with larger sigmas can thus pull in information from larger neighborhoods, but average out the fine details.

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/2b.png" alt="Ilastik Logo" width="730"> </div>

<br>

After clicking on ***Ok***, you can **visualize the effect of the selected features** by clicking on one of the options in the **Features** list in the bottom left part of the GUI. This will help you understand if the selected features are suitable for your dataset. You can always go back to the ***Feature Selection*** step to change the features and their scales.

<div class="alert alert-info">
    <strong>NOTE:</strong> In the next step, you will be able to also use the <a href="https://www.ilastik.org/documentation/pixelclassification/pixelclassification#suggest" target="_blank"><strong><i>Suggest Features</i></strong></a> functionality that could help you to select the most suitable features for your dataset.
</div>

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/2c.png" alt="Ilastik Logo" width="800"> </div>

### 4. Train the Classifier

The next step is to <a href="https://www.ilastik.org/documentation/pixelclassification/pixelclassification#training-the-classifier" target="_blank"><strong>train the classifier</strong></a> based on the features you selected. This is an iteractive process where you will need to **label a few pixels** in the image to provide the classifier with examples of the different classes.

In the ***Training*** step (on the left side of the GUI) you can **add**, **remove** or **edit** the classes (labels) that you want to use for the classification. For this exercise, we will use two classes: ***nuclei*** and ***background***. To rename the dafault classes, *Label 1* and *Label 2*, double-click on each class and type the new name (You can also change the class color by double-clicking on the color box next to the class name).

Now you can start by chosing few pixels in the image that correspond to the ***nuclei*** class; select the ***nuclei*** class, select the *Brush* tool (should be the default) and draw a short line over some pixel inside one nucleus. Next repeat the process for the ***background*** class, selecting some pixels that correspond to the background.

<div class="alert alert-info">
    <strong>NOTE:</strong> few interactive tips:
    <br>
    Use <strong>cmd+z</strong> (macOS) or <strong>ctrl+z</strong> (Windows) to <strong>undo</strong> the last action.
    <br>
    Use the <strong>Erase</strong> tool to <strong>remove</strong> the annotations.
    <br>
    If required, increase the <strong>Brush Size</strong> using the <strong>Size</strong> control.
    <br>
    To navigate the image viewer, <strong>zoom in and out</strong> using the <strong>mouse wheel</strong> (or the trackpad) together <strong>with</strong> the <strong>cmd (macOS) or ctrl (Windows) key</strong>, and <strong>pan</strong> the image with the <strong>mouse left button</strong> while holding the <strong>shift</strong> key.
</div>

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/3a.png" alt="Ilastik Logo" width="800"> </div>

To train the classifier and see the predictions, press the ***Live Update*** button. This will update the predictions in real-time as you label more pixels.
<br>
The predictions will be displayed as an overlay on the image and colored according to the class colors you defined. **Prediction overlay** can be **toggled on and off** by pressing the **p** key on your keyboard.

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/3b.png" alt="Ilastik Logo" width="800"> </div>

In a similar way, you can visualize and toggle on and off the resulting **semantic segmentation** by pressing the **s** key on your keyboard.

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/3c.png" alt="Ilastik Logo" width="800"> </div>

Examine the results for errors and add (or remove) annotations to correct.

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/4a.png" alt="Ilastik Logo" width="800"> </div>

Once you are satisfied with the results, you now need to check if the classifier is robust enough to be applied to the rest of the images that you loaded at the beginning. To do this, you can switch to another image by clicking on the ***Current View*** drop-down menu on the left side of the GUI. Now activate again the ***Live Update*** to see the predictions for the new image. If the results are not satisfactory, you can keep ***Training*** the classifier add more annotations.

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/4b.png" alt="Ilastik Logo" width="800"> </div>

### 5. Export the Results

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/5a.png" alt="Ilastik Logo" width="800"> </div>

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/5b.png" alt="Ilastik Logo" width="800"> </div>

### 6. Batch Mode

<div align="center"> <img class="custom-image" src="../../../_static/images/ilastik/6b.png" alt="Ilastik Logo" width="800"> </div>