**Hand Gesture-Based Mouse Control 🖱️🤚**

This project uses hand gestures to control the mouse cursor and simulate mouse clicks without any physical contact. By tracking hand landmarks using MediaPipe and OpenCV, this application allows you to move the mouse and perform click operations using simple finger gestures.

**Features ✨**

**Move the cursor:** Control the mouse by moving your hand.

**Click actions:** Simulate mouse clicks by performing specific gestures.

**Smooth cursor movement:** Exponential moving average is applied to ensure smooth cursor movement.

**FPS display:** Track the application's performance in real-time.

**How It Works 🔍**

1.The webcam captures the video feed, and MediaPipe identifies key hand landmarks.

2.By raising your index finger, you can control the mouse cursor on your screen.

3.When you make a pinching motion (thumb and index finger together), a mouse click is simulated at the current cursor position.

4.The mouse movements are smoothed using an exponential moving average for fluid movement.

**Technologies Used 🛠️**

**Python:** Core programming language.
**OpenCV:** For video capture and processing.
**MediaPipe:** For hand landmark detection.
**PyAutoGUI:** For controlling the mouse programmatically.
**NumPy:** For smooth interpolation of hand movements.

**Installation ⚙️**

**Clone the repository:**
git clone https://github.com/yourusername/Hand-Gesture-Mouse-Control.git

**Navigate to the project directory:**
cd Hand-Gesture-Mouse-Control

**Install dependencies:**
pip install -r requirements.txt

Here's a **sample requirements.txt:**
opencv-python,
mediapipe,
numpy,
pyautogui.

**Run the project:**
python gesture_mouse_control.py

**Usage 🎮**

1.Ensure your webcam is connected.

2.Run the project and use your index finger to control the mouse.

3.Pinch your thumb and index finger to perform a mouse click.

4.Press q to exit the application.

**Project Structure 📂**

Hand-Gesture-Mouse-Control/

│

├── Hand_tracking_module.py    # Hand tracking utility module

├── mouse_tracking.py          # Main script to run the project

├── requirements.txt           # Project dependencies

└── README.md                  # Project documentation

**Future Improvements 🛠️**

1.Add gesture support for double-clicking and right-clicking.

2.Enhance hand detection for better accuracy in different lighting conditions.

3.Extend functionality to perform additional tasks like scrolling or zooming.
