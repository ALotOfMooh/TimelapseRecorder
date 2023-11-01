import cv2
import time

# Set up video capture object
cap = cv2.VideoCapture(0)

# Set up image file name and index variables
img_file_prefix = "image_"
img_index = 0
img_shown_index = 0

isTimelapse = False

# Set up variable to store time when last picture was taken
last_picture_time = time.time()
last_pressed_time = time.time()
program_start_time = time.time()

# Create named window and make it resizable
cv2.namedWindow("Live Stream", cv2.WINDOW_NORMAL)

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
            timestamp = int((current_time - last_picture_time) / 60)
            # Add text to image
            elapsed_time = int(current_time - program_start_time)
            hours = elapsed_time // 3600
            minutes = (elapsed_time % 3600) // 60
            seconds = elapsed_time % 60
            text = "Elapsed Time: {:02d}:{:02d}:{:02d}".format(
                hours, minutes, seconds)
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.5
            font_thickness = 1
            text_color = (255, 255, 255)
            text_bg_color = (0, 0, 0)
            (text_width, text_height) = cv2.getTextSize(
                text, font, font_scale, font_thickness)[0]
            img = cv2.rectangle(
                frame, (0, 0), (text_width + 10, text_height + 10), text_bg_color, -1)
            org = (5, text_height + 5)
            img = cv2.putText(img, text, org, font, font_scale,
                              text_color, font_thickness, cv2.LINE_AA)

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
        if img_shown_index < 1:
            img_shown_index = 1
        img_filename = "pictures/" + img_file_prefix + \
            str(img_shown_index) + ".jpg"
        frame = cv2.imread(img_filename)
        cv2.imshow("Live Stream", frame)
        last_pressed_time = current_time
    elif key == ord('s'):  # lefat arrow key
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
