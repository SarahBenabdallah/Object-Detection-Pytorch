# Object-Detection-Pytorch
## Introduction
Implementing a tool which can take screenshots when the objects {car, truck, motorcycle, bus} are detected inside the area of interest. 
The center of a bounding box is the reference point to determine the location of an object.
All detections inside the area of interest need to appear on the screenshot with a bounding box respecting the color convention you are given.
Those screenshots will have to respect the following name pattern: “folder_path/screenshots/highway_{i}/{hour}h/{timestamp}.png”
## Table of Contents 

 * [input](./input)
    * [params](./input/params)
      * [labels_to_colors.json](./input/params/labels_to_colors.json)
      * [zones.json](./input/params/zones.json)
    * [videos](./input/videos)
      * [highway_1_9h.mp4](./input/videos/highway_1_9h.mp4)
      * [highway_1_18h.mp4](./input/videos/highway_1_18h.mp4)
      * [highway_2_9h.mp4](./input/videos/highway_2_9h.mp4)
      * [highway_2_18h.mp4](./input/videos/highway_2_18h.mp4)
 * [output](./output)
    * [screenshots](./output/screenshots)
       * [highway_1](./output/screenshots/highway_1)
          * [9h](./output/screenshots/highway_1/9h)
          * [18h](./output/screenshots/highway_1/18h)
      * [highway_2](./output/screenshots/highway_2)
          * [9h](./output/screenshots/highway_2/9h)
          * [18h](./output/screenshots/highway_2/18h)
 * [src](./src)
   * [coco_names.py](./src/coco_names.py)
   * [detect_vid.py](./src/detect_vid.py)
   * [extract.py](./src/extract.py)
   * [in_polygon.py](./src/in_polygon.py)
   * [utils.py](./src/utils.py)
 * [test](./test)
   * [test_extract.py](./test/test_extract.py)
   * [test_in_polygon.py](./test/test_in_polygon.py)
 * [requirements.txt](./requirements.txt)
 * [README.md](./README.md)
 
 ## How to Install and Run the Project
 run the following commands:
 ```python
$ pip install -r requirements.txt
```
```python
$ python .\src\detect_vid.py --input .\input\videos\highway_2_9h.mp4  --colors .\input\params\labels_to_color.json --zones .\input\params\zones.json --output .\output\screenshots\
```
avec: 

| Arguments        | Explanation           | 
| ------------- |:-------------:|
| --input or -i     | path to the input video | 
| --output or -o    | path to the output folder of the screenshots      |  
| --zones or -z| path to input the coordinates of the area of interest depending on the highway       |  
| --colors or -c | path to input the colors of bounding boxes depending on the detected object      |  
| --min_size or -m| FasterRCNN network resizes all the images to 800×800 pixels by default   |    

## Example of Illustration
![Screenshot of a detected car][logo]

[logo]: https://github.com/SarahBenabdallah/Object-Detection-Pytorch/blob/master/output/screenshots/highway_2/9h/2022-11-27T18-59-18%2B01-00UTC.png "Screenshot of a detected car"
## Test
To run unit test of some functions :
 ```python
$ python -m unittest discover -s .\test\
```

