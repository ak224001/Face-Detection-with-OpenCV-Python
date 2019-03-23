# Face-Detection-with-OpenCV-Python

OpenCV library to detect faces in an image

1.Load the necessary Libraries

2.Loading the image 

3.convert the image to grayscale

4.Since we know that OpenCV loads an image in BGR format, so we need to convert it into RBG format to be able to display its true colors.

5.Load the classifier for frontal face

5.using detectMultiscale get the co-ordinate of face.This function will return a rectangle with coordinates(x,y,w,h) around the detected face

6.loop over all the coordinates it returned and draw rectangles around them using Open CV.

7.convert image to RGB and show image

thank you
