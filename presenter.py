import os
import cv2
from cvzone.HandTrackingModule import HandDetector

# Variables
slides = []
cur_slide = 0


def start_presenting(Slide_directory_name: str) -> None:
    global slides
    global cur_slide

    # Collecting the slides in the slide directory
    # and sorting based on length also to prevent "10.*" coming after "1.*" instead of "2.*"
    slides = sorted(os.listdir(Slide_directory_name), key=len)
    # Saving all slides with thier names
    slides = list(
        map(os.path.join, [Slide_directory_name] * len(slides), slides))
    # Keeping only files with a known image extension
    slides = [_ for _ in slides if _.split(
        '.')[-1] in ['jpeg', 'png', 'jpg', 'svg', 'webp']]

    # Starting up presenter's video capture
    presenter_video_capture = cv2.VideoCapture(0)

    # Setting up hand detector
    hand_detector = HandDetector(detectionCon=0.8, maxHands=1)

    while True:
        # Showing presenter's video
        success, cur_video_img = presenter_video_capture.read()

        # Showing current slide
        cur_slide_image = cv2.imread(slides[cur_slide])

        # Finding hands
        hands, cur_video_img = hand_detector.findHands(cur_video_img)

        # Placing presenter's video on top of slide
        presentation_slide_height, presentation_slide_width, _ = cur_slide_image.shape
        presenter_video_cur_img = cv2.resize(cur_video_img, (200, 113))
        cur_slide_image[presentation_slide_height - 113:presentation_slide_height,
                        presentation_slide_width - 200: presentation_slide_width] = presenter_video_cur_img

        cv2.imshow("Presentation", cur_slide_image)
        cv2.imshow("Video Capture", cur_video_img)

        # Setting a key to stop video capture
        key = cv2.waitKey(1)
        if key == ord("q") or not success:
            break

    # Destroying all windows
    cv2.destroyAllWindows()


def main():
    slides_directory_name = input("Enter slides directory location : ")
    start_presenting(slides_directory_name)


if __name__ == "__main__":
    main()
