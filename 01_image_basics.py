# Lesson 1: Image Basics

import cv2
import numpy as np

def main():
    # 1. Create a dummy digital image canvas (300x500 pixels, 3 color channels)
    # This ensures the code runs immediately without needing an external image file!
    height, width = 300, 500
    canvas = np.zeros((height, width, 3), dtype=np.uint8)
    
    # 2. Draw a visual element (simulating a target bounding box or lane marker)
    # OpenCV uses BGR color order (Blue, Green, Red) instead of RGB!
    start_point = (100, 50)   # (x, y)
    end_point = (400, 250)    # (x, y)
    color = (0, 255, 0)       # Vibrant Green
    thickness = 3
    cv2.rectangle(canvas, start_point, end_point, color, thickness)
    
    # 3. Add telemetry text overlay
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(canvas, 'Tesla AI Track: OpenCV OK', (20, 40), font, 0.8, (255, 255, 255), 2)
    
    # 4. Display the processed frame in a native window
    print("Opening display window. Press 'q' or 'ESC' to close...")
    cv2.imshow("Computer Vision Hub - Step 1", canvas)
    
    # 5. Wait safely for user input to gracefully close the window
    # Crucial for preventing VS Code from crashing when rendering windows
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:  # 'q' or ESC key
            break
            
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
