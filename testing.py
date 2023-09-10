import cv2
from PIL import Image
import torch
import time

model = torch.hub.load('C:\\Users\\Asus\\OneDrive\\Documents\\!!!SKRIPSIJEES\\PROGRAM\\yolov5', 'custom', path='C:\\Users\\Asus\\OneDrive\\Documents\\!!!SKRIPSIJEES\\HASIL\\32500\\best.pt', source='local')

class Yolo():

    def run(self):
        # Set the confidence threshold
        confidence_threshold = 0.6
        
        # define a video capture object
        vid = cv2.VideoCapture(1)

        if not vid.isOpened():
            print("Tidak dapat membuka kamera, coba lagi")
            exit()

        while True:
            start_time = time.time()
            
            # Capture a frame
            ret, frame = vid.read()

            # # Grayscalling cam            
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Check if the frame was successfully read
            if not ret:
                print("Tidak bisa membaca frame")
                break
            
            # Convert the frame to a PIL image
            img = Image.fromarray(frame)

            # Perform inference
            results = model(img)

            
            # Get the bounding box coordinates, class labels
            boxes = results.xyxy[0].cpu().numpy()
            labels = results.names
            

            # If there's no object detected
            if (len(boxes) < 1):
                cv2.putText(frame, 'Objek Tidak terdeteksi', (0, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                
            # Iterate over the detections
            for box in boxes:

                # Get the bounding box, predicted class name, and confidence score
                x1, y1, x2, y2, confidence, class_index = box
                predicted_class = labels[class_index]

                # Ensure the detected object is on the threshold range
                if confidence > confidence_threshold:
                    # Convert the coordinates to integers
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                    # Draw the bounding box and label on the frame
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f'{predicted_class} {confidence:.2f}', (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            
                    # Calculate the response time
                    response_time = time.time() - start_time
                    # print(response_time)
            
                    # Draw the Response time to the screen
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f'Response Time: {round(response_time, 4)} s', (0, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        
            # Display the resulting frame
            cv2.imshow('Pengenalan Kata dalam Bahasa Isyarat Indonesia (BISINDO)', frame)
            
            # set 'q' button as quit button
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        # After the loop release the cap object
        vid.release()
        # Destroy all the windows
        cv2.destroyAllWindows()