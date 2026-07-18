import cv2
import numpy as np

def main():
    # 1. Create a simulated highway scene with road lines
    # This generates a custom road image on the fly so you don't need external data
    img = np.zeros((400, 600, 3), dtype=np.uint8)
    
    # Draw a simulated gray asphalt highway trapezoid
    road_points = np.array([[100, 400], [250, 200], [350, 200], [500, 400]], dtype=np.int32) 
    cv2.fillPoly(img, [road_points], (50, 50, 50)) # (50, 50, 50) represent a specific shade of dark gray using the BGR (Blue, Green, Red) color system.
    
    # Draw a simulated solid white lane marker on the left
    cv2.line(img, (150, 360), (260, 210), (255, 255, 255), 5)
    
    # Draw a simulated dashed yellow lane marker on the right
    cv2.line(img, (450, 360), (340, 210), (0, 255, 255), 5)

    # 2. Convert to Grayscale
    # Drops the color channels to make processing mathematical transitions much faster
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 3. Apply Gaussian Blur
    # Smooths out small pixel grains so they aren't accidentally detected as edges
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # 4. Canny Edge Detection
    # Finds areas where pixel intensity changes rapidly (the edges of the lane lines)
    edges = cv2.Canny(blurred, 50, 150)
    
    # 5. Stack original and processed views side-by-side for comparison
    # We convert edges back to 3 channels so we can combine it horizontally with img
    edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    comparison = np.hstack((img, edges_colored))
    
    # 6. Runtime Display
    print("Opening split display. Original Highway (Left) vs. Canny Edges (Right)")
    print("Press 'q' while focusing on the image window to close it.")
    cv2.imshow("Lane Detection Pipeline - Step 2", comparison)
    
    while True:
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
            
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
