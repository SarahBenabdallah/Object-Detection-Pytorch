import torchvision
import cv2
import torch
import argparse
import time
import utils
import json
import extract
import datetime


def main():
    # construct the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input',
                        help='path to input video')
    parser.add_argument('-o', '--output',
                        help='path to the output folder of the screenshots')
    # FasterRCNN network resizes all the images to 800×800 pixels by default.
    # Resizing the frames to min_size less than 300 makes the detection worse.
    parser.add_argument('-m', '--min-size', dest='min_size', default=800,
                        help='minimum input size for the FasterRCNN network')
    parser.add_argument('-c', '--colors',
                        help='path to input boxes colors')
    parser.add_argument('-z', '--zones',
                        help='path to input area of interest coordinates')
    args = vars(parser.parse_args())

    # Download or load the model from disk
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(
                                                    pretrained=True,
                                                    min_size=args['min_size']
                                                    )
    # Choose the device cpu if there is no gpu
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    # Extract the colors of labels
    with open(args['colors']) as json_data:
        boxcolors = json.load(json_data)
    # Extract the coordinates of the area of interest
    with open(args['zones']) as json_data:
        zones = json.load(json_data)
    # Get the highway information (index and hour)
    highwayindex = extract.extract_index(args['input'])
    highwayhour = extract.extract_hour(args['input'])
    highway = "highway_" + highwayindex
    # Get the coords of the area of interest
    area = zones[highway][0]
    xmin, xmax, ymin, ymax = extract.get_area_coord(zones, highway)
    # Open the video
    cap = cv2.VideoCapture(args['input'])
    if (cap.isOpened() is False):
        print('Error while trying to read video. Please check path again')
    # To count total frames
    frame_count = 0
    # To get the final frames per second
    total_fps = 0
    # Load the model into the computation device
    model = model.eval().to(device)
    # Read until end of video
    while (cap.isOpened()):
        # Capture each frame of the video
        ret, frame = cap.read()
        if ret is True:
            # Get the start time
            start_time = time.time()
            # Draw the area of interest
            overlay = frame.copy()
            output = frame.copy()
            cv2.rectangle(overlay, (xmin, ymin), (xmax, ymax), (250, 0, 0), -1)
            cv2.addWeighted(overlay, 0.5, output, 0.5, 0, output)
            frame = output
            # Get predictions for the current frame
            with torch.no_grad():
                boxes, classes, labels = utils.predict(
                    frame, model, device, 0.8)
            # Make screenshots of the detected objects
            # with the following name pattern:
            # “output_folder_path/highway_{i}/{hour}h/{timestamp}.png”
            # Draw boxes and show current frame on screen
            timestamp = datetime.datetime.now().astimezone().replace(
                        microsecond=0).isoformat().replace(":", "-")
            output_path = (
                            f"{args['output']}/highway_{str(highwayindex)}/"
                            f"{str(highwayhour)}h/{timestamp}UTC.png")
            image = utils.draw_and_capture(
                boxes, classes, labels,
                frame, boxcolors, area, output_path)
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
            if cv2.waitKey(wait_time) & 0xFF == ord('q'):
                break
        else:
            break
    # Release VideoCapture()
    cap.release()
    # Close all frames and video windows
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
