import cv2
import pickle
import numpy as np
import os

# Initialize video capture
video = cv2.VideoCapture(0)

# Load Haar cascade for face detection
facedetect = cv2.CascadeClassifier('data\haarcascade_frontalface_default.xml')

# List to store face data
faces_data = []

# Counter for capturing frames
i = 0

# Input name of the person
name = input("Enter Your Name: ")

# Loop to capture frames
while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    
    # Draw rectangle around detected face
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w, :]
        resized_img = cv2.resize(crop_img, (50, 50))
        if len(faces_data) <= 100 and i % 10 == 0:
            faces_data.append(resized_img)
        i += 1
        cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Green rectangle around face
    
    # Show frame
    cv2.imshow("Frame", frame)
    
    # Check for key press to exit or stop after capturing 50 frames
    k = cv2.waitKey(1)
    if k == ord('q') or len(faces_data) == 100:
        break

# Release video capture and close windows
video.release()
cv2.destroyAllWindows()

# Convert face data to numpy array
faces_data = np.asarray(faces_data)
faces_data = faces_data.reshape(100, -1)

# Save face data and names
if 'names.pkl' not in os.listdir('data/'):
    names = [name] * 100
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)
else:
    with open('data/names.pkl', 'rb') as f:
        names = pickle.load(f)
    names += [name] * 100
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)

if 'faces_data.pkl' not in os.listdir('data/'):
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(faces_data, f)
else:
    with open('data/faces_data.pkl', 'rb') as f:
        faces = pickle.load(f)
    faces = np.append(faces, faces_data, axis=0)
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(faces, f)
