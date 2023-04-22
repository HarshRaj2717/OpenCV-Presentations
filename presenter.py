import os
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

# Variables
slides = []
cur_slide = 0
allow_slide_change = True


def start_presenting(Slide_directory_name: str) -> None:
    global slides
    global cur_slide
    global allow_slide_change

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
        cur_video_img = cv2.flip(cur_video_img, 1)

        # Showing current slide
        cur_slide_image = cv2.imread(slides[cur_slide])

        # Finding hands
        hands, cur_video_img = hand_detector.findHands(
            cur_video_img)

        # Drawing a gesture threshold line
        cv2.line(cur_video_img, (0, threshold_height := int(cur_video_img.shape[0] / 2)),
                 (int(cur_video_img.shape[1]), int(threshold_height)), (0, 0, 255), 15)

        # Finding number of fingers up
        if hands:
            hands = hands[0]

            # Finding center of hand for setting gesture threshold
            cur_hands_pos_y = hands["center"][1]

            # Finding landmarks of the hand
            landmarks_list = hands["lmList"]

            # Finding index finger and constraining it to half of the slides
            index_finger_x = int(np.interp(landmarks_list[8][0], [int(
                cur_video_img.shape[1]) // 2, int(cur_video_img.shape[1])], [0, int(cur_video_img.shape[1])]))
            index_finger_y = int(np.interp(landmarks_list[8][1], [
                                 50, int(cur_video_img.shape[0])-50], [0, int(cur_video_img.shape[0])]))

            # Finding currently up fingers
            fingers = hand_detector.fingersUp(hands)

            # Checking for threshold height and hand position
            if cur_hands_pos_y < threshold_height:
                # Adding slide change gesture
                if fingers == [1, 0, 0, 0, 0]:
                    if cur_slide > 0 and allow_slide_change:
                        cur_slide -= 1
                        allow_slide_change = False
                elif fingers == [0, 0, 0, 0, 1]:
                    if cur_slide < len(slides) - 1 and allow_slide_change:
                        cur_slide += 1
                        allow_slide_change = False
                else:
                    allow_slide_change = True

            # Adding pointer gesture
            if fingers == [0, 1, 1, 0, 0]:
                cv2.circle(cur_slide_image, (index_finger_x,
                           index_finger_y), 15, (0, 0, 255), cv2.FILLED)

        # Placing presenter's video on top of slide
        presentation_slide_height, presentation_slide_width, _ = cur_slide_image.shape
        presenter_video_cur_img = cv2.resize(cur_video_img, (200, 113))
        cur_slide_image[presentation_slide_height - 113:presentation_slide_height,
                        presentation_slide_width - 200: presentation_slide_width] = presenter_video_cur_img

        # Showing the cur_slide_image
        cv2.imshow("Presentation", cur_slide_image)

        # Setting a key to stop video capture
        key = cv2.waitKey(1)
        if key == ord("q") or not success:
            break

    # Destroying all windows
    cv2.destroyAllWindows()


def main():
    start_presenting("sample_slides")


if __name__ == "__main__":
    main()
