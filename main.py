import cv2

# import sample picture
image_path = './sample.jpeg'
image = cv2.imread(image_path)

# Load the Haar Cascade for face detection from the local file path
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

# Convert the image to grayscale (required for face detection)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the grayscale image
faces = face_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
)

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    # You can change the color and thickness of the rectangle
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

# Display the image with detected faces
cv2.imshow('Face Detection', image)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

