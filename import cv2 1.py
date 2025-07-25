import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"D:\CODES\tesseract\tesseract.exe"
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Start video capture
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video stream from camera.")
else:
    print("Press 'Space' to capture an image, or 'Q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    cv2.imshow("Camera", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord(' '):  # Press space to capture
        # Process captured frame
        cv2.imshow("Captured Image", frame)
        cap.release()
        cv2.destroyAllWindows()
        
        # Convert image to grayscale for better OCR accuracy
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # OCR to extract text
        text = pytesseract.image_to_string(gray_image)
        print("Extracted Text:", text)
        
        if text.strip():
            # Convert extracted text to speech
            engine.say(text)
            engine.runAndWait()
        else:
            print("No text detected in the image.")
        break
    elif key == ord('q'):  # Press Q to quit
        break

cap.release()
cv2.destroyAllWindows()
