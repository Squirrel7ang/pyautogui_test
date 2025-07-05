import pyautogui
import cv2
import numpy as np
import time

pyautogui.FAILSAFE = False

def mouse_callback(event, x, y, flags, param):
    global mouse_window_x, mouse_window_y
    mouse_window_x, mouse_window_y = x, y
    
    if event == cv2.EVENT_MOUSEMOVE:
        print(f"Window coords: ({x}, {y}), System coords: {pyautogui.position()}")
    elif event == cv2.EVENT_LBUTTONDOWN:
        print(f"Left click at Window: ({x}, {y}), System: {pyautogui.position()}")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(f"Right click at Window: ({x}, {y}), System: {pyautogui.position()}")
    elif event == cv2.EVENT_MBUTTONDOWN:
        print(f"Middle click at Window: ({x}, {y}), System: {pyautogui.position()}")
    elif event == cv2.EVENT_MOUSEWHEEL:
        direction = "up" if flags > 0 else "down"
        print(f"Mouse wheel scrolled {direction} at Window: ({x}, {y}), System: {pyautogui.position()}")

def main():
    global mouse_window_x, mouse_window_y
    mouse_window_x, mouse_window_y = 0, 0

    cv2.namedWindow("Screen Display", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("Screen Display", mouse_callback)

    FPS = 15
    frame_duration = 1.0 / FPS

    try:
        while True:
            start_time = time.time()

            # 捕获屏幕
            screenshot = pyautogui.screenshot()
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            # 获取系统鼠标坐标
            system_x, system_y = pyautogui.position()

            # 在窗口上绘制坐标
            cv2.putText(frame, f"Window: ({mouse_window_x}, {mouse_window_y})", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(frame, f"System: ({system_x}, {system_y})", (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            # 压缩图像
            _, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
            frame = cv2.imdecode(buffer, cv2.IMREAD_COLOR)

            # 显示图像
            cv2.imshow("Screen Display", frame)

            # 捕获键盘事件
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                print("Quit key pressed (q)")
                break
            elif key != 0xFF:
                print(f"Key pressed: {chr(key)} (ASCII: {key})")

            # 控制帧率
            elapsed = time.time() - start_time
            time.sleep(max(0, frame_duration - elapsed))

    except KeyboardInterrupt:
        print("Program terminated by user")
    
    finally:
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()