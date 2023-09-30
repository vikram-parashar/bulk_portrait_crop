import cv2
import os

# input goes here
top=50
bottom=50
left=50
right=50

input_directory='/home/vikram/img/test/'

def crop_pic(image_path):
    # import sample picture
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
        cv2.imwrite(image_path, cropped_face)  # Save the cropped face as a separate image

def process_directory(directory_path):
    # Iterate over all files and subdirectories in the given directory
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        
        if os.path.isfile(item_path):
            # If it's a file, process it
            crop_pic(item_path)
            print(item_path)
        elif os.path.isdir(item_path):
            # If it's a directory, recursively process it
            process_directory(item_path)

process_directory(input_directory)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

