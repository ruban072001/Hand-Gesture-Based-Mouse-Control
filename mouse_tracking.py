import cv2   # Importing OpenCV module
import mediapipe as mp  # Importing Mediapipe module for hand tracking
import time  # Importing time module to calculate fps
import numpy as np
import Hand_tracking_module as htm
import pyautogui


# Capture webcam
vid = cv2.VideoCapture(0)

# Initialize frame timing
prev_time = 0

wcam = 500
hcam = 350

wscr, hscr = 1920, 1080
# Create hand tracking object
detector = htm.HandTracking()

# Smoothing parameters
alpha = 0.2  # Smoothing factor (0 < alpha < 1)
prev_x, prev_y = 0, 0  # Initialize previous mouse positions

while True:
    ret, frame = vid.read()  # Capture frame
    if not ret:
        break

    # Find hands and positions in the frame
    frame = detector.find_hands(frame)
    frame, positions = detector.find_position(frame, False, [3, 4, 6, 8, 10, 12, 14, 16, 18, 20])  # Track specific landmarks

       
    # print(wcam, hcam)
    cv2.rectangle(frame, (100, 50), (500, 350), (255, 0, 255), 2)
    finger = []
    if positions:
        if positions[0][0] <= positions[1][0]:
            finger.append(1)
        else:
            finger.append(0)
            
        tip = [3, 5, 7, 9]
        base = [2, 4, 6, 8]
        for i in range(4):
            if positions[tip[i]][1] < positions[base[i]][1]:
                finger.append(1)
            else:
                finger.append(0) 
    if len(finger) > 4:               
        
        if finger[1] == 1 and finger[2] == 0:
            x1 = positions[3][0]
            y1 = positions[3][1] 
            # Interpolate hand positions to screen positions
            x3 = np.interp(x1, (100, wcam), (0, wscr))
            y3 = np.interp(y1, (50, hcam), (0, hscr))
            
            # Apply exponential moving average for smoothness
            smooth_x = prev_x + alpha * (x3 - prev_x)
            smooth_y = prev_y + alpha * (y3 - prev_y)

            # Move mouse smoothly
            pyautogui.moveTo(smooth_x, smooth_y)

            # Update previous positions
            prev_x, prev_y = smooth_x, smooth_y

        if finger[0] != 1 and finger[3] != 1 and finger[2] == 1 and finger[1] == 1:
            x1 = positions[3][0]
            y1 = positions[3][1] 
            # Interpolate hand positions to screen positions
            x3 = np.interp(x1, (100, wcam), (0, wscr))
            y3 = np.interp(y1, (50, hcam), (0, hscr))
            
            # Apply exponential moving average for smoothness
            smooth_x = prev_x + alpha * (x3 - prev_x)
            smooth_y = prev_y + alpha * (y3 - prev_y)

            # Simulate click
            pyautogui.click(smooth_x, smooth_y)

            # Update previous positions
            prev_x, prev_y = smooth_x, smooth_y
            
        
    # Calculate FPS
    current_time = time.time()
    fps = 1 / max((current_time - prev_time), 1e-6)  # Avoid division by 0
    prev_time = current_time

    # Display FPS on frame
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the frame
    cv2.imshow('Hand Tracking', frame)

    # Break loop with 'q' key
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
vid.release()
cv2.destroyAllWindows()
