import pyautogui

# 设置 pyautogui 配置
pyautogui.FAILSAFE = True  # 鼠标移到屏幕左上角可终止程序
pyautogui.PAUSE = 0.1  # 每次操作后暂停 0.1 秒

def simulate_key(key):
    """模拟按下单个键"""
    try:
        pyautogui.press(key)
        print(f"Pressed key: {key}")
    except Exception as e:
        print(f"Error pressing key {key}: {e}")

def simulate_combo(keys):
    """模拟按下组合键（如 'ctrl+c'）"""
    try:
        key_list = keys.split('+')
        pyautogui.hotkey(*key_list)
        print(f"Pressed combo: {keys}")
    except Exception as e:
        print(f"Error pressing combo {keys}: {e}")

def move_mouse_direction(direction, distance):
    """向指定方向移动鼠标"""
    try:
        x, y = 0, 0
        if direction.lower() == 'up':
            y = -distance
        elif direction.lower() == 'down':
            y = distance
        elif direction.lower() == 'left':
            x = -distance
        elif direction.lower() == 'right':
            x = distance
        else:
            print(f"Invalid direction: {direction}")
            return
        pyautogui.moveRel(x, y)
        print(f"Moved mouse {direction} by {distance} pixels")
    except Exception as e:
        print(f"Error moving mouse: {e}")

def move_mouse_to(x, y):
    """移动鼠标到指定坐标"""
    try:
        pyautogui.moveTo(x, y)
        print(f"Moved mouse to: ({x}, {y})")
    except Exception as e:
        print(f"Error moving mouse to ({x}, {y}): {e}")

def click_mouse(button):
    """模拟鼠标点击"""
    try:
        button = button.lower()
        if button in ['left', 'right', 'middle']:
            pyautogui.click(button=button)
            print(f"Clicked {button} button")
        else:
            print(f"Invalid button: {button}")
    except Exception as e:
        print(f"Error clicking {button}: {e}")

def main():
    print("Input Simulator: Enter commands (type 'exit' to quit)")
    print("Commands:")
    print("  key <key> (e.g., key a, key enter)")
    print("  combo <key1+key2> (e.g., combo ctrl+c)")
    print("  move <direction> <distance> (e.g., move up 100)")
    print("  moveto <x> <y> (e.g., moveto 500 500)")
    print("  click <button> (e.g., click left, click right)")

    while True:
        try:
            command = input("> ").strip().lower()
            if command == 'exit':
                print("Exiting program")
                break

            parts = command.split()
            if not parts:
                print("Empty command")
                continue

            action = parts[0]
            if action == 'key' and len(parts) == 2:
                simulate_key(parts[1])
            elif action == 'combo' and len(parts) == 2:
                simulate_combo(parts[1])
            elif action == 'move' and len(parts) == 3:
                move_mouse_direction(parts[1], int(parts[2]))
            elif action == 'moveto' and len(parts) == 3:
                move_mouse_to(int(parts[1]), int(parts[2]))
            elif action == 'click' and len(parts) == 2:
                click_mouse(parts[1])
            else:
                print("Invalid command format")

        except ValueError:
            print("Invalid number format")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()