import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():  # Cek apakah karakter adalah huruf
            shift_base = ord('A') if char.isupper() else ord('a')
            # Geser karakter dan pastikan tetap dalam rentang huruf
            result += chr((ord(char) + shift - shift_base) % 26 + shift_base)
        else:
            result += char  # Jika bukan huruf, tetap tambahkan karakter asli

    return result

def encrypt():
    text = input_text.get("1.0", tk.END).strip()
    shift = int(shift_entry.get())
    encrypted_text = caesar_cipher(text, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_text)

def decrypt():
    text = input_text.get("1.0", tk.END).strip()
    shift = int(shift_entry.get())
    decrypted_text = caesar_cipher(text, -shift)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_text)

# Membuat jendela utama
root = tk.Tk()
root.title("Caesar Cipher")

# Input teks
tk.Label(root, text="Teks:").pack()
input_text = tk.Text(root, height=10, width=40)
input_text.pack()

# Input shift
tk.Label(root, text="Shift:").pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

# Tombol Encrypt dan Decrypt
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.pack(pady=5)

# Output teks
tk.Label(root, text="Hasil:").pack()
output_text = tk.Text(root, height=10, width=40)
output_text.pack()

# Menjalankan aplikasi
root.mainloop()