# Smart-Face-Attendance-System
Smart Face Attendance System is a facial recognition-based attendance app built with Spring Boot and Python (OpenCV). It automatically marks attendance through webcam detection and stores records in a MySQL database via Spring Boot APIs. Simple, fast, and intelligent!

🧠 Smart Face Attendance System

🚀 Project Overview

Smart Face Attendance System is an intelligent attendance management solution that combines Python (Face Recognition) with Spring Boot (Backend APIs) to automate and simplify the process of marking attendance.

The system detects faces in real-time using the webcam, recognizes registered users, and automatically updates attendance records in the backend database through REST APIs.

⸻

💡 Key Features

✅ Face Detection & Recognition — Uses OpenCV and face_recognition libraries to identify students or employees.
✅ Spring Boot Backend Integration — All attendance data is managed and stored via Spring Boot APIs.
✅ Real-time Processing — Attendance is marked instantly upon recognizing the face.
✅ Cross-Technology Integration — Python handles AI/ML logic, while Java Spring Boot ensures secure data management.
✅ Web Interface — Beautiful dashboard to mark attendance and view attendance records.

⸻

🧩 Tech Stack

Frontend: HTML, CSS, JavaScript (for UI buttons like “Mark Attendance” & “View Records”)
Backend: Spring Boot (Java)
AI/ML Processing: Python (OpenCV, face_recognition)
Database: MySQL (or any JPA-supported DB)

⸻

⚙️ How It Works
	1.	User clicks “Mark Attendance” on the web dashboard.
	2.	Spring Boot runs the Python script (face_attendance.py) located in /src/main/resources/Scripts/.
	3.	Python script captures face via webcam and identifies the user.
	4.	The recognized user data is sent back to Spring Boot through REST API.
	5.	Attendance is saved in the database and can be viewed anytime.

⸻

📸 Output Example
	•	✅ Encoding Complete (Face model generated)
	•	✅ Attendance successfully marked for recognized user
	•	⚠️ Error handled if unknown face detected

⸻

🌟 Future Enhancements

🔹 Add cloud storage for attendance logs
🔹 Deploy on a real-time server
🔹 Add mobile app integration
🔹 Implement voice-based login and notifications
