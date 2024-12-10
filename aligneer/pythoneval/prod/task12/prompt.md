I need some help here. I've got this function that's part of our real-time image and video processing pipeline using OpenCV, and we're integrating with cloud services for scalability.

import cv2

def process_frame(frame):
    # Apply advanced processing
    blurred = cv2.GaussianBlur(frame, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    return edges
Could you write some unit tests for this function using pytest? Make sure to cover all edge cases, including invalid inputs like None or corrupt frames, and test how it handles very large images. Also, consider any potential issues that might arise when processing videos in real-time streaming scenarios.