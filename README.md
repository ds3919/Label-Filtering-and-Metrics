# image_filtering
Filter images from an image dataset based on a set of criteria based on image labels.

Criteria 1
    Images with only 1 labeled object.
      --Primarily to benchmark the model's ability to identify singular object images.
        
Criteria 2
    Find the dominant labeled object in each image.
      --Done by checking which labeled object has the largest bounding box, according to the assumption that any object recognition model chooses the largest object in the image.

Reads XML files mapped to each image. Each XML holds image filename, object names, and bounding box specifications (xmin, xmax, ymin, ymax). According to the selected criteria, it will create a CSV file holding filenames, and object names. The part 2 file will auto copy all images from the original directory to the new directory based on the selected CSV file. This allows for the creation of two new datasets from the original one.
