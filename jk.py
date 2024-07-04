import cv2
import tkinter as tk
from tkinter import filedialog

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Ask the user to select an image file
file_path = filedialog.askopenfilename()

# Check if the user selected a file
if file_path:
    # Load the selected image
    image = cv2.imread(file_path)

    # Load the eye detection classifier
    eye_data = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")

    # Convert the image to grayscale
    gray_scale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect eyes in the image
    eyes = eye_data.detectMultiScale(gray_scale_image)

    # Draw rectangles around the detected eyes
    for x, y, width, height in eyes:
        cv2.rectangle(image, (x, y), (x + width, y + height), (0, 0, 255), 2)

    # Save the result
    cv2.imwrite("detect/Eye_detected_image.jpg", image)

    # Display the result
    cv2.imshow("Eye Detection Result", image)
    cv2.waitKey(0)
else:
    print("No file selected.")