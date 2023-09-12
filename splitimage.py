# Importing all necessary libraries
import cv2
import os
import datetime
# Read the video from specified path
cam = cv2.VideoCapture("C:\\Users\\Asus\\Videos\\datasettiga\\tolong.mp4")

# count the number of frames
frames = cam.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cam.get(cv2.CAP_PROP_FPS)
  
# calculate duration of the video
seconds = round(frames / fps)
video_time = datetime.timedelta(seconds=seconds)
print(f"duration in seconds: {seconds}")
print(f"video time: {video_time}")

try:
	
	# creating a folder named data
	if not os.path.exists('data'):
		os.makedirs('data')

# if not created then raise error
except OSError:
	print ('Error: Creating directory of data')

# frame
currentframe = 0
while(True):
	
	# reading from frame
	ret,frame = cam.read()

	if ret:
		
		if currentframe %6== 0:
			# if video is still left continue creating images
			name = './data/frame' + str(currentframe) + '.jpg'
			print ('Creating...' + name)

			# writing the extracted images
			cv2.imwrite(name, frame)

		# increasing counter so that it will
		# show how many frames are created
		currentframe += 1
	else:
		break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
