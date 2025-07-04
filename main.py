#بسم الله
import cv2

#img = cv2.imread('person.png')

#camera sittings
#740    580
cam = cv2.VideoCapture(1)

cam.set(3, 600)
cam.set(4, 350)

#variables

classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
   classNames = f.read().rstrip('\n').split('\n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,230)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)
while True:
   success, img = cam.read()
   classIds, confs, bbox = net.detect(img, confThreshold=0.5)
   print(classIds, bbox)

   if len(classIds)  !=0:
      for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
         cv2.rectangle(img, box, color=(0, 255,0), thickness=2)
         cv2.putText(img, classNames[classId-1],(box[0]+10, box[1]+20),
                     cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0, 255), thickness=2)



   cv2.imshow('Output', img)
   cv2.waitKey(1)

   #الحمد لله


#[AHMED AL SHIHABI]
