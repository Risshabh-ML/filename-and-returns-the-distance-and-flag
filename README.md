# filename-and-returns-the-distance-and-flag
Read an image find the contours and  compute the midpoint between the top-left and top-right points, followed by the midpoint between the top-right and bottom-right


Takes in a filename and returns the distance and flag.
It is very difficult for getting a perfect distance between gaps and objects, Here using OpenCV, some possibilities can be made

Main file -
Python file : exp.py

Actually there are certain requirements
1.	Scipy
2.	imutils
3.	numpy
4.	OpenCV
5.	Matplotlib



So, Steps involved
•	Read an image

•	perform edge detection

•	then perform a dilation + erosion to close gaps in between object edges

•	find contours in the edge map

•	sort the contours from left-to-right and initialize the 'pixels per metric' calibration variable

•	order the points in the contour such that they appear in top-left, top-right, bottom-right, and bottom-left order

•	compute the midpoint between the top-left and top-right points, followed by the midpoint between the top-right and bottom-right

.compute the distace and flag

1.	In my code (exp.py)  enter  choose 1 to enter image file .
2.	Enter file name 

Output:---
3.	Get visual of image
4.	Get edge img
5.	Get file name ,distance and flag




##--I build also a jupyter file to take the distance diff way.

--Distance_of_cont.ipynb




