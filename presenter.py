import cv2

# Variables
width = 300
height = 250


def start_presenting() -> None:
    # Starting up video capture
    capture = cv2.VideoCapture(0)
    capture.set(3, width)
    capture.set(3, height)

    while True:
        success, img = capture.read()
        cv2.imshow("Camera", img)
        key = cv2.waitKey(1)
        # Setting a key to stop video capture
        if key == ord("q") or not success:
            break

    # Destroying all windows
    cv2.destroyAllWindows()
