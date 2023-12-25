import tkinter as tk
from tkinter import ttk
import threading
import time
import bcrypt
import subprocess

def dang_nhap():
    ten_nguoi_dung = entry_ten_nguoi_dung.get()
    mat_khau = entry_mat_khau.get()

    # Kiểm tra điều kiện đăng nhập
    if kiem_tra_dang_nhap(ten_nguoi_dung, mat_khau):
        # Nếu đăng nhập thành công, ẩn cửa sổ đăng nhập và hiển thị cửa sổ chính
        cua_so_dang_nhap.withdraw()
        cua_so_chinh.deiconify()
        bat_dau_luong_thread()
    else:
        label_trang_thai.config(text="Tên người dùng hoặc mật khẩu không hợp lệ")

def kiem_tra_dang_nhap(ten_nguoi_dung, mat_khau):
    # Kiểm tra điều kiện đăng nhập
    if ten_nguoi_dung.lower() == "tri" and mat_khau == "HOA":
        return True

    # Nếu không phải tài khoản "tri", kiểm tra từ tệp tin
    nguoi_dung_tu_tep = doc_nguoi_dung_tu_tep()
    for user in nguoi_dung_tu_tep:
        if user['ten_nguoi_dung'] == ten_nguoi_dung and bcrypt.checkpw(mat_khau.encode('utf-8'), user['mat_khau']):
            return True

    return False

def doc_nguoi_dung_tu_tep():
    try:
        with open("DO_NOT_CLICK(passcode)/ten_nguoi_dung.txt", "r", encoding="utf-8") as tep:
            dong = tep.readlines()
            nguoi_dung = [{"ten_nguoi_dung": line.split(",")[0], "mat_khau": line.split(",")[1].strip()} for line in dong]
        return nguoi_dung
    except FileNotFoundError:
        return []

def bat_dau_luong_thread():
    luong_thread = threading.Thread(target=luong_thread_chuc_nang)
    luong_thread.start()

def luong_thread_chuc_nang():
    for i in range(1, 101):
        time.sleep(0.1)  # Giả sử mỗi bước mất 0.1 giây
        bien_tien_do.set(i)
        label_tien_do.config(text=f"Đang tải chạy phân mềm kết nối....{i}%")
    label_tien_do.config(text="Tải thành công!")

    # Sau khi loading hoàn tất, mở file Python mới
    mo_file_python_moi()

def mo_file_python_moi():
    # Thực hiện các thao tác cần thiết khi muốn mở file Python mới
    subprocess.run(["python", "ungdungmoi.py"])

# Tạo cửa sổ đăng nhập
cua_so_dang_nhap = tk.Tk()
cua_so_dang_nhap.title("Đăng nhập For flie")

label_ten_nguoi_dung = tk.Label(cua_so_dang_nhap, text="Tên Người Dùng:")
label_mat_khau = tk.Label(cua_so_dang_nhap, text="Mật Khẩu:")
entry_ten_nguoi_dung = tk.Entry(cua_so_dang_nhap)
entry_mat_khau = tk.Entry(cua_so_dang_nhap, show="*")
button_dang_nhap = tk.Button(cua_so_dang_nhap, text="Đăng Nhập", command=dang_nhap)
label_trang_thai = tk.Label(cua_so_dang_nhap, text="")
button_dang_nhap.grid(row=2, column=1, pady=10)
label_trang_thai.grid(row=3, column=0, columnspan=2, pady=5)
label_ten_nguoi_dung.grid(row=0, column=0, padx=10, pady=5, sticky="e")
label_mat_khau.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_ten_nguoi_dung.grid(row=0, column=1, padx=10, pady=5, sticky="w")
entry_mat_khau.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Tạo cửa sổ chính
cua_so_chinh = tk.Toplevel()
cua_so_chinh.title("Cửa Sổ Chính")
cua_so_chinh.geometry("400x200")
cua_so_chinh.protocol("WM_DELETE_WINDOW", cua_so_dang_nhap.destroy)  # Đóng cả hai cửa sổ khi đóng cửa sổ chính

bien_tien_do = tk.IntVar()
thanh_tien_do = ttk.Progressbar(cua_so_chinh, variable=bien_tien_do, maximum=100)
thanh_tien_do.pack(pady=10)
label_tien_do = tk.Label(cua_so_chinh, text="")
label_tien_do.pack()

# Ẩn cửa sổ chính khi bắt đầu
cua_so_chinh.withdraw()

# Chạy vòng lặp chính của ứng dụng
cua_so_dang_nhap.mainloop()
