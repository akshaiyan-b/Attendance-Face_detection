# Attendance-Face_detection

Here’s a **professional README.md** file you can use for your GitHub repository for this **Face Recognition Attendance System** built with **OpenCV, scikit-learn, and Streamlit**.

---

```markdown
# 🎯 Face Recognition Attendance System

A real-time **Face Recognition Attendance System** built using **Python, OpenCV, scikit-learn (KNN)**, and **Streamlit**.  
The system detects faces using a webcam, recognizes them with a trained model, and automatically records attendance in a CSV file for the current date.

---

## 🚀 Features

✅ Real-time face detection using OpenCV  
✅ Face recognition using K-Nearest Neighbors (KNN)  
✅ Automated attendance logging in a CSV file  
✅ Daily attendance reports saved by date  
✅ Interactive data view using Streamlit  
✅ Voice feedback for attendance confirmation (Windows only)

---

## 🧠 How It Works

1. **Face Data Collection**  
   Collect face samples and save them in `data/faces_data.pkl` with corresponding names in `data/names.pkl`.

2. **Model Training**  
   The KNN model is trained using the collected face data.

3. **Real-Time Recognition**  
   The system detects and recognizes faces through your webcam using the trained KNN model.

4. **Attendance Logging**  
   When a recognized face is confirmed (by pressing the `O` key), their name and timestamp are saved in a CSV file under the `Attendance/` folder.

5. **View Attendance**  
   Use the Streamlit interface to view the recorded attendance in a clean, tabular format.

---

## 📂 Project Structure

```

├── Attendance/
│   ├── Attendance_09-11-2025.csv     # Daily attendance files
│
├── data/
│   ├── faces_data.pkl                # Stored face embeddings
│   ├── names.pkl                     # Corresponding names
│   ├── haarcascade_frontalface_default.xml
│
├── background2.png                   # Background for OpenCV UI
│
├── app.py                            # Streamlit dashboard
├── test.py                           # Main face recognition script
├── requirements.txt                  # Dependencies
└── README.md                         # Project documentation

````


