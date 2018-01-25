import numpy
import cv2

print(cv2.__version__)
vidcap = cv2.VideoCapture('lectest1.mp4')
success,image = vidcap.read()
print(success)
outcount = 0
#framerate = vidcap.get(cv2, cv2.CV_CAP_PROP_FPS)
#print(framerate)
count = 0
# while(True):
#     # Capture frame-by-frame
#     success, image = vidcap.read()
#     count += 1
#
#     # Check if this is the frame closest to 10 seconds
#     if count == (framerate*10):
#       count = 0
#       cv2.imshow('image',image)
#
#     # Check end of video
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()



success = True
while success:
    success,image = vidcap.read()
    outcount = outcount+100
    if outcount % 50000 == 0:
      cv2.imwrite('frame%d.jpg' % count, image)
      print('success')
      count += 1