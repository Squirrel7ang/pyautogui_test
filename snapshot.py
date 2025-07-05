import pyautogui
import os
from datetime import datetime
import sys

def take_screenshot(save_path="screenshot.png"):
    """
    Takes a screenshot of the current screen and saves it to the specified path.
    
    Args:
        save_path (str): Path where the screenshot will be saved
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Generate timestamp for unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}.png"
        full_path = os.path.join(save_path, filename) if save_path else filename

        # Take screenshot
        screenshot = pyautogui.screenshot()

        # Save screenshot to file
        screenshot.save(full_path)
        print(f"Screenshot saved successfully as {full_path}")
        return True

    except Exception as e:
        print(f"Error taking screenshot: {str(e)}")
        return False

def main():
    # Default save directory (current working directory)
    save_dir = os.getcwd()
    
    # Create screenshots directory if it doesn't exist
    screenshot_dir = os.path.join(save_dir, "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)
    
    # Take screenshot
    if take_screenshot(screenshot_dir):
        print("Screenshot captured successfully!")
    else:
        print("Failed to capture screenshot.")
        sys.exit(1)

if __name__ == "__main__":
    main()
