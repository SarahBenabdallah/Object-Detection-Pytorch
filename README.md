# Object-Detection-Pytorch
## Introduction
Implementing a tool which can take screenshots when the objects {car, truck, motorcycle, bus} are detected inside the area of interest. 
The center of a bounding box is the reference point to determine the location of an object.
All detections inside the area of interest need to appear on the screenshot with a bounding box respecting the color convention you are given.
Those screenshots will have to respect the following name pattern: “folder_path/screenshots/highway_{i}/{hour}h/{timestamp}.png”
## Table of Contents 
$ ./tree-md .
.
 * [input](./input)
    * [params](./dir2/file22.ext)
      * [labels_to_colors.json](./dir2/file22.ext)
      * [zones.json](./dir2/file22.ext)
    * [videos](./dir2/file23.ext)
      * [highway_1_9h.mp4](./dir2/file22.ext)
      * [highway_1_18h.mp4](./dir2/file22.ext)
      * [highway_2_9h.mp4](./dir2/file22.ext)
      * [highway_2_18h.mp4](./dir2/file22.ext)
 * [output](./output)
    * [screenshots](./dir2/file21.ext)
       * [highway_1](./dir2/file22.ext)
          * [9h](./dir2/file22.ext)
          * [18h](./dir2/file22.ext)
      * [highway_2](./dir2/file23.ext)
          * [9h](./dir2/file22.ext)
          * [18h](./dir2/file22.ext)
 * [src](./src)
   * [coco_names.py](./dir1/file11.ext)
   * [detect_vid.py](./dir1/file12.ext)
   * [extract.py](./dir1/file12.ext)
   * [in_polygon.py](./dir1/file12.ext)
   * [utils.py](./dir1/file12.ext)
 * [test](./test)
   * [test_extract.py](./dir1/file11.ext)
   * [test_in_polygon.py](./dir1/file12.ext)
 * [requirements.txt](./requirements.txt)
 * [README.md](./README.md)
