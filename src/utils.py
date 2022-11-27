import torchvision.transforms as transforms
import cv2
import numpy
import numpy as np
import in_polygon
# This gives us access to all the instance category names
from coco_names import COCO_INSTANCE_CATEGORY_NAMES as coco_names

# Define the torchvision image transforms
transform = transforms.Compose([
    transforms.ToTensor(),
])


def predict(image, model, device, detection_threshold):
    # Transform the image to tensor
    image = transform(image).to(device)
    # Add a batch dimension torch.
    # unsqueeze adds an additional dimension to the tensor.
    image = image.unsqueeze(0)
    # Get the predictions on the image
    outputs = model(image)
    # print the results individually
    # print(f"BOXES: {outputs[0]['boxes']}")
    # print(f"LABELS: {outputs[0]['labels']}")
    # print(f"SCORES: {outputs[0]['scores']}")
    # Get all the predicited class names
    pred_classes = [coco_names[i] for i in outputs[0]['labels'].cpu().numpy()]
    # Get score for all the predicted objects
    pred_scores = outputs[0]['scores'].detach().cpu().numpy()
    # get all the predicted bounding boxes
    pred_bboxes = outputs[0]['boxes'].detach().cpu().numpy()
    # get boxes above the threshold score
    boxes = pred_bboxes[pred_scores >= detection_threshold].astype(np.int32)
    return boxes, pred_classes, outputs[0]['labels']


def draw_and_capture(
                    boxes, classes, labels, image,
                    boxcolors, area, output_path):
    """
        if the object is in  {car, truck, motorcycle, bus}
        and if the center of the object is inside the area of interest
        then draw bounding box and make screenshot
    """
    labels = labels.numpy()
    for i, box in enumerate(boxes):
        # The center of a bounding box is the reference point
        # to determine the location of an object.
        xcenter = int((int(box[0]) + int(box[2]))/2)
        ycenter = int((int(box[1]) + int(box[3]))/2)

        if (str(labels[i]) in boxcolors and
                in_polygon.in_polygon(area, (xcenter, ycenter))):
            # Define the color of the bounding box depending on the object
            color = boxcolors[str(labels[i])]
            cv2.rectangle(
                image,
                (int(box[0]), int(box[1])),
                (int(box[2]), int(box[3])),
                color, 2
            )
            # Write the name of the detected object
            cv2.putText(image, classes[i], (int(box[0]), int(box[1]-5)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2,
                        lineType=cv2.LINE_AA)
            # Save the frame in the output_path
            cv2.imwrite(output_path, image)
    return image
