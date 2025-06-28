# <strong>06</strong> - <i class="fa-solid fa-disease"></i> Ilastik for Object Classification

In this section, we will explore how to use **Ilastik** for [**object classification**](https://www.ilastik.org/documentation/objects/objects). This process is very similar to what we have done in the [*pixel classification*](../05_segmentation/machine_learning/pixel_classification_with_ilastik.md) section and still involves training a machine learning model. However, instead of classifying pixels, we will **classify entire objects** based on **instance segmentation** images.

In this exercise, we will use the **instance segmentation** data from the nuclei dataset that we generated from the [*Form Ilastik Masks to Labels*](../05_segmentation/machine_learning/from_ilastik_masks_to_labels.ipynb) exercise and train a model to separate cells in *mitotic* vs *non-mitotic* states.

<div class="alert alert-info">
    <strong>NOTE:</strong> Ilastik supports a variety of <a href="https://www.ilastik.org/documentation/basics/dataselection#formats" target="_blank">data formats</a>. For simplicity and ease of use during this course, we will use images saved as <strong>.tif</strong> files. However, Ilastik recommends using files saved as <strong>.h5</strong> for [optimal performance](https://www.ilastik.org/documentation/basics/performance_tips). If you wish to use your own dataset and need to convert your files to <strong>.h5</strong>, Ilastik provides tools such as a <a href="https://www.ilastik.org/documentation/fiji_export/plugin" target="_blank">Fiji plugin</a> or a <a href="https://github.com/ilastik/ilastik/tree/main/notebooks/h5convert" target="_blank">Jupyter Notebook</a> with instructions.
</div>

## Ilastik Object Classification Workflow

For a detailed workflow instruction, you can refer to the [Ilastik Object Classification Documentation](https://www.ilastik.org/documentation/objects/objects).

### 1. Select the Workflow

When you open **Ilastik**, you will see the [Startup Screen](https://www.ilastik.org/documentation/basics/startup) with various workflows. Select the ***Object Classification*** workflow by clicking on it. You will be automatically brought to the **Input Data** step.