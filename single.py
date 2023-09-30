import cv2

# get the inputs from the user
top=int(input("Enter the percentage of top to be cropped: "))
bottom=int(input("Enter the percentage of bottom to be cropped: "))
left=int(input("Enter the percentage of left to be cropped: "))
right=int(input("Enter the percentage of right to be cropped: "))

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

# Iterate over the detected faces and crop them
for i, (x, y, w, h) in enumerate(faces):
    x=int(x-x*left/100)
    y=int(y-y*top/100)
    w=int(w+w*right/100)
    h=int(h+h*bottom/100)
    # Crop the face region from the image
    cropped_face = image[y:y + h, x:x + w]

    # Save or display the cropped face
    cv2.imwrite(f'face_{i}.jpg', cropped_face)  # Save the cropped face as a separate image
    cv2.imshow(f'Face {i}', cropped_face)


# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

