# <strong>06</strong> - <i class="fa-solid fa-shapes"></i> Object Classification (Machine Learning)

**Object Classification** is a technique that can be used in image analysis to **identify and categorize objects within an image based on their features**, such as shape, color, texture, and size. In this context, an **object** can be defined as a **set of pixels that belongs to a specific area within the image**, such as a cell, tissue region, or any other structure of interest.

This approach is particularly useful in biological applications where you want to distinguish between different types of cells in a tissue, identify different cell cycle stages, classify various tissue areas, categorize different cellular structures based on their morphological characteristics and more. It is evident that to implement this approach, **you need to have image segmentation** already performed, as the classification process requires pre-defined objects (segmented regions) to analyze and classify.

<div align="center"> <img src="../../../_static/images/ilastik_obj_classification/8a.png" alt="Ilastik" width="700"> </div>

In this section, similarly to what we did for [**Pixel Classification**](../05_segmentation/machine_learning/machine_learning_with_ilastik.md), we will use the open-source software [**Ilastik**](https://www.ilastik.org) to perform [**Object Classification**](https://www.ilastik.org/documentation/objects/objects) using **Machine Learning**. In this case, instead of classifying individual pixels, we will **classify entire objects** based on their extracted features.
