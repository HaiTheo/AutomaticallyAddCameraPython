import pyautogui
import time

# ======================
# CẤU HÌNH
# ======================
password = "Mh@818304"
delay_between_devices = 8  # Giây chờ giữa mỗi thiết bị
start_ip_suffix = 100
number_of_devices = 50
scroll_every = 3  # Mỗi lần scroll cuộn 3 dòng
row_y = 154
click_row_1_y = 154  # Y tọa độ của dòng đầu tiên trong danh sách
device_spacing = 33  # Khoảng cách giữa các dòng camera
ip_box = (1784, 292)
gateway_box = (1797, 405)
password_box = (1766, 822)
modify_btn = (1720, 863)
clear_box = (23, 123)
clear_boxAgain = (24, 124)

ip_suffixes = [
    166, 167, 168, 169, 170, 171, 172, 174, 180, 181, 182, 183
]

row_x = 25  # X tọa độ click vào dòng camera

# ======================
# BẮT ĐẦU THỰC HIỆN
# ======================
start_device = 58

pyautogui.alert("Đặt cửa sổ SADP sẵn sàng. Nhấn OK để bắt đầu thay IP hàng loạt.")

for i in range(len(ip_suffixes)):
    print(f"▶ Đang xử lý thiết bị thứ {i+1}")

    # 1. Tính vị trí dòng
    # row_y = click_row_1_y + (i % scroll_every) * device_spacing
    pyautogui.click(row_x, row_y)
    time.sleep(0.5)



    # Bước 1: Click vào ô IP
    pyautogui.click(*ip_box)
    time.sleep(0.2)

    # Bước 2: Di chuyển con trỏ đến phần số cuối (sau dấu chấm thứ 3)
    # pyautogui.hotkey('ctrl', 'left')  # nhảy từ cuối về phần cuối IP
    # time.sleep(0.1)

    # pyautogui.hotkey('ctrl', 'shift' , 'right')  # nhảy tiếp về phần .1
    time.sleep(0.1)
    pyautogui.hotkey('backspace')

    # Bước 3: Bôi đen toàn bộ phần ".1", ".25", ".101", v.v.
    pyautogui.hotkey('backspace')
    time.sleep(0.1)
    new_suffix =  ip_suffixes[i]
    # Bước 5: Ghi lại đúng IP mới (VD: 100.101)
    pyautogui.write(str(new_suffix))
  



    time.sleep(0.2)

    # # 3. Sửa Gateway
    # pyautogui.click(*gateway_box)
    # time.sleep(0.2)
    # pyautogui.press(['left'] * 2)
    # pyautogui.write('00')
    # time.sleep(0.2)

    # 4. Nhập mật khẩu
    pyautogui.click(*password_box)
    time.sleep(0.2)
    pyautogui.write(password)
    time.sleep(0.2)

    # 5. Click Modify
    pyautogui.click(*modify_btn)
    time.sleep(delay_between_devices)

    pyautogui.click(*clear_box)
    pyautogui.click(*clear_boxAgain)

    # row_y = click_row_1_y + (i % scroll_every) * device_spacing
    # pyautogui.click(row_x + 1, row_y + 1)
    # time.sleep(0.3)


    # 6. Scroll mỗi khi hết nhóm 3 dòng
    # if (i + 1) % scroll_every == 0:
    #     pyautogui.scroll(-300)
    #     time.sleep(0.8)

pyautogui.alert("🎉 Đã hoàn tất thay đổi IP cho toàn bộ camera.")