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

---

## 💻 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/Face-Recognition-Attendance.git
cd Face-Recognition-Attendance
````

### 2️⃣ Create and Activate Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On macOS/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt` yet, create one with:

```
streamlit
pandas
opencv-python
scikit-learn
numpy
pywin32
```

---

## 🧾 Usage

### ▶️ Step 1: Run the Face Recognition Script

```bash
python test.py
```

* Press **`O`** to mark attendance for recognized faces.
* Press **`Q`** to quit the application.

Attendance will be saved automatically to:

```
Attendance/Attendance_<current-date>.csv
```

---

### ▶️ Step 2: View Attendance with Streamlit

Run the following command:

```bash
streamlit run app.py
```

This will open a local web interface where you can see all attendance records for the day.

---

## 🗣️ Voice Feedback (Windows Only)

The program uses **Windows Speech API (SAPI)** to provide audio confirmation (“Attendance Taken”) when attendance is marked.

---

## 🧩 Technologies Used

* **Python 3.8+**
* **OpenCV**
* **scikit-learn**
* **pandas**
* **NumPy**
* **Streamlit**
* **pywin32** (for voice feedback)

---

## 📊 Example Output

**Streamlit Dashboard:**

* Displays current attendance in a styled table.
* Automatically reads from the latest CSV file.

**Terminal / OpenCV Window:**

* Shows real-time webcam feed with detected faces.
* Recognized names displayed with rectangles around faces.

---

## 🧰 Troubleshooting

* Ensure your webcam is connected and working.
* If the `Attendance/` folder doesn’t exist, create it manually.
* If `haarcascade_frontalface_default.xml` is missing, download it from OpenCV’s GitHub:
  👉 [https://github.com/opencv/opencv/tree/master/data/haarcascades](https://github.com/opencv/opencv/tree/master/data/haarcascades)

---

## 🧑‍💻 Author

**Your Name**
📧 [your.email@example.com](mailto:your.email@example.com)
🔗 [GitHub Profile](https://github.com/<your-username>)

---

## 📜 License

This project is licensed under the **MIT License** – feel free to modify and use it.


---

Would you like me to also generate a **`requirements.txt`** file for this project (based on your imports)?
```
