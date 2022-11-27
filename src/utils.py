#importing torchvision.transforms to convert the input image or video frame to a tensor.
import torchvision.transforms as transforms
import cv2
import numpy
import numpy as np
import in_polygon
import datetime
#From coco_names script, we are importing the COCO_INSTANCE_CATEGORY_NAMES list as coco_names. 
# This gives us access to all the instance category names
from coco_names import COCO_INSTANCE_CATEGORY_NAMES as coco_names

# define the torchvision image transforms
transform = transforms.Compose([
    transforms.ToTensor(),
])

def predict(image, model, device, detection_threshold):
    # transform the image to tensor
    image = transform(image).to(device)
    image = image.unsqueeze(0) # add a batch dimension
    outputs = model(image) # get the predictions on the image
    # print the results individually
    # print(f"BOXES: {outputs[0]['boxes']}")
    # print(f"LABELS: {outputs[0]['labels']}")
    # print(f"SCORES: {outputs[0]['scores']}")
    # get all the predicited class names
    pred_classes = [coco_names[i] for i in outputs[0]['labels'].cpu().numpy()]
    # get score for all the predicted objects
    pred_scores = outputs[0]['scores'].detach().cpu().numpy()
    # get all the predicted bounding boxes
    pred_bboxes = outputs[0]['boxes'].detach().cpu().numpy()
    # get boxes above the threshold score
    boxes = pred_bboxes[pred_scores >= detection_threshold].astype(np.int32)
    return boxes, pred_classes, outputs[0]['labels']

#They are the bounding boxes (coordinates), the class names, the label indices, and the image.
def draw_boxes(boxes, classes, labels, image, boxcolors, area, output_path):
    labels = labels.numpy()
    # read the image with OpenCV
    #image = cv2.cvtColor(np.asarray(image), cv2.COLOR_BGR2RGB)
    #print("COLORS", boxcolors)
    for i, box in enumerate(boxes):
        #  The center of a bounding box is the reference point to determine the location of an object.
        xcenter, ycenter = int((int(box[0])+int(box[2]))/2) , int((int(box[1])+int(box[3]))/2)
        # print("XCEEEENTEEEER",xcenter)
        # print("YCEEEENTEEEER",ycenter)
        # if the object is in  {car, truck, motorcycle, bus} and if the center of the object is inside the area of interest then draw rectangle and make screenshot 
        if (str(labels[i])) in boxcolors and in_polygon.in_polygon(area, (xcenter,ycenter)):
            print("TRUUUEEE", labels[i])
            color = boxcolors[str(labels[i])]
            cv2.rectangle(
                image,
                (int(box[0]), int(box[1])),
                (int(box[2]), int(box[3])),
                color, 2
            )
            #DRAW THE CENTER OF THE RECTANGLE
            #xcenter, ycenter = int((int(box[0])+int(box[2]))/2) , int((int(box[1])+int(box[3]))/2)
            #cv2.circle(image, (xcenter,ycenter), radius=0, color= color, thickness=10)
            cv2.putText(image, classes[i], (int(box[0]), int(box[1]-5)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2, 
                        lineType=cv2.LINE_AA)
            print("TEEEEEEEEEEST", output_path)
            cv2.imwrite(output_path,image)
    return image

####extract hour of the video from the input
def extracthour(s):
    hour = ""
    ##if hour is composed from one number : 1-9
    if s[len(s) - 7]=='_':
        hour = (s[len(s) - 6])
    ##if hour is composed from two numbers : 10-00
    else: 
        hour = (s[len(s) - 7 : len(s) - 5])
    return(hour)
####extract index of the highway video from the input
def extractindex(s):
    i = len(s)-1
    index = ""
    while i!=0 and s[i]!='_':
        i -= 1
    if s[i] == '_':
        index = s[i-1]
    return(index)

