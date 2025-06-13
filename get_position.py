import pyautogui
import time

print("Di chuột đến vị trí cần kiểm tra, nhấn Ctrl+C để dừng.")
try:
    while True:
        x, y = pyautogui.position()
        print(f"Toạ độ hiện tại: ({x}, {y})", end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nKết thúc.")
