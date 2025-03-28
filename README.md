# Label Filtering and Metrics
### Filtering XMLS metadata
Filter images from an image dataset based on a set of criteria based on image labels.

Criteria 1 (_1Objects_)
    Images with only 1 labeled object.
      --Primarily to benchmark the model's ability to identify singular object images.
        
Criteria 2 (_DominantObjects_)
    Find the dominant labeled object in each image.
      --Done by checking which labeled object has the largest bounding box, according to the assumption that any object recognition model chooses the largest object in the image.

Reads XML files mapped to each image. Each XML holds image filename, object names, and bounding box specifications (xmin, xmax, ymin, ymax). According to the selected criteria, it will create a CSV file holding filenames, and object names.


### Filtering by Classes

Filter results and the labels using _Merge_, only leaving predictions/labels that are a subset of a list of included classes.

Simply iterate through list of labels and find wherever the label is not part of the set of classes input, and based on the file associated to that row, erase any occurence of the same file in the prediction list.


### Calculating Performance

Using _CalculateMetrics_, cross check every prediction for each file with the label list. 

**Only meant for datasets where each image has at least one label, making TrueNegatives impossible.
