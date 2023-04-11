import cv2
import time

# Set up video capture object
cap = cv2.VideoCapture(0)

# Set up image file name and index variables
img_file_prefix = "image_"
img_index = 0
img_shown_index = 0

# Set up variable to store time when last picture was taken
last_picture_time = time.time()
last_pressed_time = time.time()

# Loop indefinitely
while True:
    # Get current time
    current_time = time.time()

    # Check if 5 seconds have passed since last picture was taken
    if current_time - last_picture_time >= 5:
        # Capture frame from webcam
        ret, frame = cap.read()

        # Check if frame was successfully captured
        if ret:
            # Increment image index and update last picture time
            img_index += 1
            # Save frame as image file
            img_filename = "pictures/" + \
                img_file_prefix + str(img_index) + ".jpg"
            cv2.imwrite(img_filename, frame)
            last_picture_time = current_time
            # Display current image
            if current_time - last_pressed_time >= 5:
                img_shown_index = img_index
                cv2.imshow("Live Stream", frame)

    # Check for key presses
    key = cv2.waitKey(1)

    # Scroll back one picture if left arrow key is pressed
    if key == ord('a'):  # left arrow key
        img_shown_index -= 1
        if img_shown_index < 0:
            img_shown_index = 0
        img_filename = "pictures/" + img_file_prefix + \
            str(img_shown_index) + ".jpg"
        frame = cv2.imread(img_filename)
        cv2.imshow("Live Stream", frame)
        last_pressed_time = current_time
    elif key == ord('s'):  # left arrow key
        img_shown_index += 1
        if img_shown_index > img_index:
            img_shown_index = img_index
        img_filename = "pictures/" + img_file_prefix + \
            str(img_shown_index) + ".jpg"
        frame = cv2.imread(img_filename)
        cv2.imshow("Live Stream", frame)
        last_pressed_time = current_time

    # Wait for key press to exit
    elif key == ord('q'):
        break

# Release video capture object and close window
cap.release()
cv2.destroyAllWindows()
