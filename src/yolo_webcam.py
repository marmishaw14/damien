import cv2
from ultralytics import YOLO


def main():
    model = YOLO("yolo11n.pt")
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        raise RuntimeError("Could not open webcam.")

    while True:
        success, frame = camera.read()

        if not success:
            break

        results = model(frame, verbose=False)
        annotated_frame = results[0].plot()

        cv2.imshow("YOLO Webcam Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()