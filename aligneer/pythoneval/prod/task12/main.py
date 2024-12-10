import cv2

def process_frame(frame):
    # Apply advanced processing
    blurred = cv2.GaussianBlur(frame, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    return edges