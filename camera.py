# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2

cap = cv2.VideoCapture(0) # series of image

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # floating point number
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

# print(frame_count)

width = int(width)
height = int(height)


# windows -- DIVX
# macos -- XVID

# put filepath of video, the pass video coder that actually writes in mp4 - it is platform dependent. DIVX changes depending on platform
    # then third parameter is how many frames captured by camera (more frames captured, larger is the file)
    # fourth parameter is width and height
# writer = cv2.VideoWriter('mysupervideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

print("Press 'q' for exiting the program")
while True:

    ret, frame = cap.read()
    # writer.write(frame)
    
    # gray = cv2.cvtColor(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()

