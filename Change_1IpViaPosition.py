# Sau khi reset môi trường, ta ghi lại file Python theo yêu cầu trước đó

import pyautogui
import time

print("Chuyển sang cửa sổ SADP trong 3 giây...")
time.sleep(3)

pyautogui.alert("Rê chuột vào đúng cửa sổ SADP đang cần thao tác. Bấm OK khi sẵn sàng.")

# pyautogui.moveTo(27, 153)
# pyautogui.click()
# time.sleep(0.5)

# pyautogui.alert("Vừa click xong. Bạn thấy con trỏ nhảy đúng chỗ chưa?")

# 1. Click chọn thiết bị đầu tiên
pyautogui.click(27 , 153 )
print( "Đã click chọn thiết bị đầu tiên.")
time.sleep(1)

# 2. Sửa IP Address
pyautogui.click(1784, 292)  # Click vào ô IP
time.sleep(0.2)
pyautogui.press(['left'] * 4)  # Lùi sang số 1
pyautogui.write('00')  # Thêm '00' trước số 1 → thành 100
time.sleep(0.2)

# 3. Sửa Gateway
pyautogui.click(1797 , 405)  # Click vào ô Gateway
time.sleep(0.2)
pyautogui.press(['left'] * 2)  # Lùi sang số 1 (ở cuối)
pyautogui.write('00')  # Thêm '00' → thành 100
time.sleep(0.2)

# 4. Nhập mật khẩu
pyautogui.click(1766 , 822)  # Click vào ô Password
time.sleep(0.2)
pyautogui.write('Mh@818304')
time.sleep(0.2)

# 5. Click Modify
pyautogui.click(1720 , 863)
print("Đã gửi lệnh Modify theo định dạng chỉnh sửa thủ công.")
