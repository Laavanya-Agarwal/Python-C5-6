import cv2

def takeSnapshot():
    # starting the camera
    startingCam = cv2.VideoCapture(0)
    result = True
    
    while (result):
        # taking one picture saved as newPicture1.png if result is true
        ret, frame = startingCam.read()
        cv2.imwrite('newPicture1.png', frame)
        result = False
    # closing the camera
    startingCam.release()
    # destroying all windows
    cv2.destroyAllWindows()
takeSnapshot()

# cv2.VideoCapture( ) - gets a video capture object for the camera.
# while(True) - Sets up an infinite loop
# read( ) - reads the frames using the above created object.
# cv2.imshow( ) - shows the frames in the video.