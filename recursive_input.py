import cv2
import os

#get the inputs from the user
input_directory=input('Enter the directory path: ')

top=int(input("Enter the percentage of top to be cropped: "))
bottom=int(input("Enter the percentage of bottom to be cropped: "))
left=int(input("Enter the percentage of left to be cropped: "))
right=int(input("Enter the percentage of right to be cropped: "))

def crop_pic(image_path):
    print(image_path)
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
        x=int(x-w*left/100)
        y=int(y-h*top/100)
        w=int(w+2*w*right/100)
        h=int(h+2*h*bottom/100)
        # Crop the face region from the image
        cropped_face = image[y:y + h, x:x + w]

        # Chech if there are multiple faces in the image
        if i<1:
            # replace the picture with the cropped face
            cv2.imwrite(image_path, cropped_face)
        else:
            # Save the cropped face as a separate image

            # separate the file name and extension
            ext=image_path.split('.')[-1]
            image_path=image_path.split('.')[0]

            cv2.imwrite(f'{image_path}_{i}.{ext}', cropped_face)

def process_directory(directory_path):
    # Iterate over all files and subdirectories in the given directory
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        
        if os.path.isfile(item_path):
            # If it's a file, process it
            crop_pic(item_path)
        elif os.path.isdir(item_path):
            # If it's a directory, recursively process it
            process_directory(item_path)

process_directory(input_directory)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

