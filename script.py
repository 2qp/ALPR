import numpy as np
import cv2
from openalpr import Alpr
import sys
import serial




RTSP_SOURCE  = 'rtsp://video_feed_ip:8080/h264_ulaw.sdp'
WINDOW_NAME  = 'openalpr'
FRAME_SKIP   = 1


def open_cam_rtsp(uri):
    gst_str = ('rtspsrc location={} ! rtph264depay ! h264parse ! avdec_h264 ! '
               'videoconvert ! appsink').format(uri)
    return cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)


def main():
    alpr = Alpr('country', 'country.conf', '/usr/local/share/openalpr/runtime_data')
    if not alpr.is_loaded():
        print('Error loading OpenALPR')
        sys.exit(1)
    alpr.set_top_n(3)
    #alpr.set_default_region('new')

    cap = open_cam_rtsp(RTSP_SOURCE)
    if not cap.isOpened():
        alpr.unload()
        sys.exit('Failed to open video file!')
    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
    cv2.setWindowTitle(WINDOW_NAME, 'Gate Camera test')

    _frame_number = 0
    while True:
        ret_val, frame = cap.read()
        if not ret_val:
            print('VidepCapture.read() failed. Exiting...')
            break

        _frame_number += 1
        if _frame_number % FRAME_SKIP != 0:
            continue
        cv2.imshow(WINDOW_NAME, frame)



        results = alpr.recognize_ndarray(frame)
        for i, plate in enumerate(results['results']):
            best_candidate = plate['candidates'][0]
	    with open('output.txt', 'w') as x:

		J = ('{:7s}'.format(best_candidate['plate'].upper(),best_candidate))
		print >> x, str(J)

	    with open("allowed.txt") as f, open ("output.txt") as d:
		for line in d:
			list_of_lists =[]
			inner_list = [elt.strip() for elt in line.split(',')]
			list_of_lists.append(inner_list)


		for line in f:
			allowed =[]
		        inner_list2 = [elt.strip() for elt in line.split(',')]
        		allowed.append(inner_list2)



            	if list_of_lists == allowed:
                 	print (True)
			        arduino = serial.Serial('/dev/ttyACM0', 9600)
			        command = str(85)
			        arduino.write(command)  
			        reachedPos = str(arduino.readline())

	        else:
        	        print (False)


        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    cap.release()
    alpr.unload()








if __name__ == "__main__":
    main()
