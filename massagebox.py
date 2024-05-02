import tkinter as tk
from tkinter import messagebox

# Membuat instance Tkinter
root = tk.Tk()
root.title("Contoh MessageBox")

# Fungsi untuk menampilkan messagebox
def show_message_box():
    messagebox.showinfo("Pesan", "Ini adalah contoh pesan menggunakan Tkinter!")

# Membuat tombol untuk menampilkan messagebox
button = tk.Button(root, text="Tampilkan MessageBox", command=show_message_box)
button.pack(pady=20)

# Menjalankan loop Tkinter
root.mainloop()
