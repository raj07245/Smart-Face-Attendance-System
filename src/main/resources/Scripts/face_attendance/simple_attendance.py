import cv2
import numpy as np
import face_recognition
import os
import mysql.connector
from datetime import datetime
import tkinter as tk
import pickle

# 📌 MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",       
    password="Raj07245@",  
    database="attendance_db"
)
cursor = db.cursor()

pickle_file = "encodings.pickle"
dataset_path = "dataset"

# 📌 Load existing encodings
if os.path.exists(pickle_file):
    with open(pickle_file, "rb") as f:
        encodeListKnown, classNames = pickle.load(f)
    print("Encodings Loaded ✅")
else:
    encodeListKnown, classNames = [], []
    print("No encodings found, starting fresh...")

# 📌 Check for new images
for file in os.listdir(dataset_path):
    name = os.path.splitext(file)[0]
    if name.upper() not in [c.upper() for c in classNames]:  
        print(f"Encoding new face: {name}")
        img = cv2.imread(os.path.join(dataset_path, file))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img_rgb)[0]
        encodeListKnown.append(encode)
        classNames.append(name)

# 📌 Save updated encodings (if any new found)
with open(pickle_file, "wb") as f:
    pickle.dump((encodeListKnown, classNames), f)

print("Encodings Ready ✅ | Total Students:", len(classNames))

# 📌 Mark Attendance in DB
def markAttendance(name):
    now = datetime.now()
    date = now.date()
    time = now.strftime('%I:%M:%S %p')   

    cursor.execute("SELECT * FROM attendance WHERE name=%s AND date=%s", (name, date))
    result = cursor.fetchone()

    if not result:  
        cursor.execute("INSERT INTO attendance (name, date, time) VALUES (%s, %s, %s)", (name, date, time))
        db.commit()

# 📌 Webcam for Real-time Recognition
cap = cv2.VideoCapture(0)
name = "unknown"

# --- Get screen size for centering ---
root = tk.Tk()
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
root.destroy()

win_name = "Webcam"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(win_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

desired_w, desired_h = 800, 600
cv2.resizeWindow(win_name, desired_w, desired_h)

x = (screen_w - desired_w) // 2
y = (screen_h - desired_h) // 2
cv2.moveWindow(win_name, x, y)

while True:
    success, img = cap.read()
    if not success:
        print("Camera not detected!")
        break

    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
            markAttendance(name)

    cv2.putText(img, f"{name} Attendance Marked ", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow(win_name, img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cursor.close()
db.close()
