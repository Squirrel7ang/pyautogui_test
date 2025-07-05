import pyautogui
import cv2
import numpy as np
from datetime import datetime
import sys
import os

def screen_monitor():
    """
    Captures the screen continuously and displays it in a new window in real-time.
    Press 'q' to quit the stream.
    """
    try:
        # Set pyautogui to be faster by reducing delay
        pyautogui.PAUSE = 0
        
        # Get screen size
        screen_width, screen_height = pyautogui.size()
        
        # Create a window for display
        cv2.namedWindow("Screen Monitor", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Screen Monitor", screen_width // 2, screen_height // 2)  # Scale down for performance
        
        print("Starting screen monitoring... Press 'q' to quit.")
        
        while True:
            # Capture screenshot
            screenshot = pyautogui.screenshot()
            
            # Convert screenshot to numpy array for OpenCV
            frame = np.array(screenshot)
            
            # Convert RGB to BGR (OpenCV uses BGR)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            
            # Display the frame in the window
            cv2.imshow("Screen Monitor", frame)
            
            # Check for 'q' key press to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Stopping screen monitoring...")
                break
                
    except Exception as e:
        print(f"Error during screen monitoring: {str(e)}")
        return False
    finally:
        # Clean up
        cv2.destroyAllWindows()
        return True

def main():
    try:
        # Run the screen monitor
        if screen_monitor():
            print("Screen monitoring completed successfully.")
        else:
            print("Screen monitoring failed.")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        cv2.destroyAllWindows()
        sys.exit(0)

if __name__ == "__main__":
    main()
