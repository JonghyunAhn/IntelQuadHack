import numpy as np
import cv2

def findFaces(picFile):
  face_cascades = []
  face_cascades.append(cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml'))
#  face_cascades.append(cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'))
#  face_cascades.append(cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt_tree.xml'))
#  face_cascades.append(cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml'))
#  face_cascades.append(cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_profileface.xml'))
#  
#  body_cascades = []
#  body_cascades.append(cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_fullbody.xml'))
#  body_cascades.append(cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_lowerbody.xml'))
#  body_cascades.append(cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_upperbody.xml'))
  img = picFile.copy()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#  antigray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#  for i in xrange(gray.shape[0]):
#    for j in xrange(gray.shape[1]):
#      antigray[i][j] = 255-gray[i][j]
  
  faces = []
  for face_cascade in face_cascades:
    faces.append(face_cascade.detectMultiScale(gray, 1.13, 10))
#    faces.append(face_cascade.detectMultiScale(antigray, 1.13, 10))
#  bodies = []
#  for body_cascade in body_cascades:
#    bodies.append(body_cascade.detectMultiScale(gray, 1.08, 10))
#    bodies.append(body_cascade.detectMultiScale(antigray, 1.08, 10))
  for stuff in faces:
    for (x,y,w,h) in stuff:
      cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
      roi_gray = gray[y:y+h, x:x+w]
      roi_color = img[y:y+h, x:x+w]
  
#  for stuff in bodies:
#    for (x,y,w,h) in stuff:
#      cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
#      roi_gray = gray[y:y+h, x:x+w]
#      roi_color = img[y:y+h, x:x+w]

  return img
  
if __name__ == "__main__":
  import sys
  print findFaces(sys.argv[1])
