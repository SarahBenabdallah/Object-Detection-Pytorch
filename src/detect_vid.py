import torchvision
import cv2
import torch
import argparse
import time
import utils
from PIL import Image
import json
import numpy as np
import in_polygon
#construct the argument parser
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='path to input video')
parser.add_argument('-m', '--min-size', dest='min_size', default=800, 
                    help='minimum input size for the FasterRCNN network')
#color argument
parser.add_argument('-c', '--colors', help='path to input boxes colors')
#zone argument
parser.add_argument('-z', '--zones', help='path to input area of interest coordinates')
args = vars(parser.parse_args())

# download or load the model from disk
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True, 
                                                    min_size=args['min_size'])


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


with open(args['colors']) as json_data:
    boxcolors = json.load(json_data)
    print("*****COLORS*********",boxcolors)
###### Get coordinates of the area of interest ##########""
with open(args['zones']) as json_data:
    zones = json.load(json_data)
highways = list(zones.keys())
highwayindex = args['input'][23]
highway = "highway_"+highwayindex
area = zones[highway][0]
print("*********", highway)
i = 0
while i < len(highways):
    if highway == highways[i]:
        xmin = min(zones[highway][0])[0]
        xmax = max(zones[highway][0])[0]
        ymin = min(zones[highway][0])[1]
        ymax = max(zones[highway][0])[1]
        break
    i +=1
if i == len(highways):
    print("the interest area of this video is not available")  


cap = cv2.VideoCapture(args['input'])

if (cap.isOpened() == False):
    print('Error while trying to read video. Please check path again')
# get the frame width and height
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
save_name = f"{args['input'].split('/')[-1].split('.')[0]}_{args['min_size']}"
# define codec and create VideoWriter object 
out = cv2.VideoWriter(f"../output/{save_name}.mp4", 
                      cv2.VideoWriter_fourcc(*'mp4v'), 30, 
                      (frame_width, frame_height))

frame_count = 0 # to count total frames
total_fps = 0 # to get the final frames per second
# load the model onto the computation device
model = model.eval().to(device)

# read until end of video
while(cap.isOpened()):
    # capture each frame of the video
    ret, frame = cap.read()
    if ret == True:
        # get the start time
        start_time = time.time()
        #######################AREA OF INTEREST########################
        overlay = frame.copy()
        output = frame.copy()
        cv2.rectangle(overlay, (xmin, ymin), (xmax, ymax), (250,0,0), -1)
        res = cv2.addWeighted(overlay, 0.5, output, 0.5, 0, output)
        frame = output
        
        with torch.no_grad():
            # get predictions for the current frame
            boxes, classes, labels = utils.predict(frame, model, device, 0.8)

        # draw boxes and show current frame on screen
        image = utils.draw_boxes(boxes, classes, labels, frame, boxcolors, area)
        # get the end time
        end_time = time.time()
        # get the fps
        fps = 1 / (end_time - start_time)
        # add fps to total fps
        total_fps += fps
        # increment frame count
        frame_count += 1
        # press `q` to exit
        wait_time = max(1, int(fps/4))
        cv2.imshow('image', image)
        out.write(image)
        if cv2.waitKey(wait_time) & 0xFF == ord('q'):
            break
    else:
        break

# release VideoCapture()
cap.release()
# close all frames and video windows
cv2.destroyAllWindows()
# calculate and print the average FPS
avg_fps = total_fps / frame_count
print(f"Average FPS: {avg_fps:.3f}")