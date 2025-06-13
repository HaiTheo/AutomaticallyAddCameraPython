import pyautogui
import time

# ======================
# CẤU HÌNH
# ======================
delay_between_devices = 8  # Giây chờ giữa mỗi thiết bị
start_ip_suffix = 100
number_of_devices = 20
# scroll_every = 3  # Mỗi lần scroll cuộn 3 dòng


row_x = 694 # X tọa độ click vào dòng camera
row_y = 238

ip_box = (516, 480)


password = "Mh@818304"
password_box = (472, 602)
repassword_box = (470, 630)
enter_box = (560, 707)

ip_full_list = [
    "192.168.100.180", "192.168.100.174", "192.168.100.172", "192.168.100.103",
    "192.168.100.162", "192.168.100.182", "192.168.100.171", "192.168.100.113",
    "192.168.100.160", "192.168.100.181", "192.168.100.107", "192.168.100.128",
    "192.168.100.127", "192.168.100.159", "192.168.100.152", "192.168.1.100",
    "192.168.100.118", "192.168.100.120", "192.168.100.130"
]

# ======================
# BẮT ĐẦU THỰC HIỆN
# ======================

pyautogui.alert("Đặt cửa sổ SADP sẵn sàng. Nhấn OK để bắt đầu thay IP hàng loạt.")

for i in range(len(ip_full_list)):
    print(f"▶ Đang xử lý camera thứ {i+1}")

    # 1. Tính vị trí dòng
    # row_y = click_row_1_y + (i % scroll_every) * device_spacing
    pyautogui.click(row_x, row_y)
    time.sleep(0.5)


    # Bước 1: Click vào ô IP
    pyautogui.click(*ip_box)
    time.sleep(0.2)
    time.sleep(0.2)
    pyautogui.write(ip_full_list[i])


    pyautogui.click(*password_box)
    time.sleep(0.2)
    pyautogui.write(password)
    time.sleep(0.2)

    pyautogui.click(*repassword_box)
    time.sleep(0.2)
    pyautogui.write(password)
    time.sleep(0.2)


    pyautogui.click(*enter_box)

    # 5. Click Modify

    # row_y = click_row_1_y + (i % scroll_every) * device_spacing
    # pyautogui.click(row_x + 1, row_y + 1)
    time.sleep(5)


    # 6. Scroll mỗi khi hết nhóm 3 dòng
    # if (i + 1) % scroll_every == 0:
    #     pyautogui.scroll(-300)
    #     time.sleep(0.8)

pyautogui.alert("🎉 Đã hoàn tất thay đổi IP cho toàn bộ camera.")