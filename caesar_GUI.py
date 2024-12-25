import tkinter as tk
from tkinter import messagebox, ttk

def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():  # Cek apakah karakter adalah huruf
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) + shift - shift_base) % 26 + shift_base)
        else:
            result += char  # Jika bukan huruf, tetap tambahkan karakter asli

    return result

def encrypt():
    text = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
        encrypted_text = caesar_cipher(text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encrypted_text)
    except ValueError:
        messagebox.showerror("Error", "Shift harus berupa angka!")

def decrypt():
    text = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
        decrypted_text = caesar_cipher(text, -shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted_text)
    except ValueError:
        messagebox.showerror("Error", "Shift harus berupa angka!")

# Membuat jendela utama
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

# Judul
title_label = tk.Label(root, text="Caesar Cipher", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=20)

# Input teks
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Teks:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w")
input_text = tk.Text(input_frame, height=5, width=40, font=("Helvetica", 12))
input_text.grid(row=1, column=0, padx=10)

# Input shift
tk.Label(input_frame, text="Shift:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w")
shift_entry = tk.Entry(input_frame, font=("Helvetica", 12))
shift_entry.grid(row=3, column=0, padx=10, pady=5)

# Tombol Encrypt dan Decrypt
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

encrypt_button = tk.Button(button_frame, text="Encrypt", command=encrypt, bg="#4CAF50", fg="white", font=("Helvetica", 12))
encrypt_button.grid(row=0, column=0, padx=10)

decrypt_button = tk.Button(button_frame, text="Decrypt", command=decrypt, bg="#F44336", fg="white", font=("Helvetica", 12))
decrypt_button.grid(row=0, column=1, padx=10)

# Output teks
tk.Label(root, text="Hasil:", bg="#f0f0f0", font=("Helvetica", 12)).pack(pady=10)
output_text = tk.Text(root, height=5, width=40, font=("Helvetica", 12))
output_text.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()