import tkinter as tk
from tkinter import messagebox

# Simulasi rotor Enigma sederhana
class EnigmaMachine:
    def __init__(self):
        self.rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"  # Rotor I
        self.rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"  # Rotor II
        self.rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"  # Rotor III
        self.reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"  # Reflector B
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def rotate_rotor(self, rotor):
        return rotor[1:] + rotor[0]

    def encrypt_character(self, char, rotor1, rotor2, rotor3):
        if char not in self.alphabet:
            return char

        # Rotor transformations
        idx = self.alphabet.index(char)
        char = rotor1[idx]
        idx = self.alphabet.index(char)
        char = rotor2[idx]
        idx = self.alphabet.index(char)
        char = rotor3[idx]

        # Reflector
        idx = self.alphabet.index(char)
        char = self.reflector[idx]

        # Back through rotors (reversed)
        idx = rotor3.index(char)
        char = self.alphabet[idx]
        idx = rotor2.index(char)
        char = self.alphabet[idx]
        idx = rotor1.index(char)
        char = self.alphabet[idx]

        return char

    def encrypt_message(self, message):
        encrypted_message = ""
        for char in message.upper():
            encrypted_message += self.encrypt_character(char, self.rotor1, self.rotor2, self.rotor3)
            self.rotor1 = self.rotate_rotor(self.rotor1)
        return encrypted_message

# GUI untuk aplikasi Enigma
class EnigmaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enigma Cipher")
        self.enigma = EnigmaMachine()

        # Label dan input pesan
        self.label_input = tk.Label(root, text="Masukkan Pesan:")
        self.label_input.pack(pady=5)
        self.entry_input = tk.Entry(root, width=50)
        self.entry_input.pack(pady=5)

        # Tombol enkripsi
        self.button_encrypt = tk.Button(root, text="Enkripsi", command=self.encrypt_message)
        self.button_encrypt.pack(pady=5)

        # Label hasil
        self.label_output = tk.Label(root, text="Hasil Enkripsi:")
        self.label_output.pack(pady=5)
        self.entry_output = tk.Entry(root, width=50, state="readonly")
        self.entry_output.pack(pady=5)

    def encrypt_message(self):
        message = self.entry_input.get()
        if not message:
            messagebox.showwarning("Peringatan", "Pesan tidak boleh kosong!")
            return

        encrypted_message = self.enigma.encrypt_message(message)
        self.entry_output.config(state="normal")
        self.entry_output.delete(0, tk.END)
        self.entry_output.insert(0, encrypted_message)
        self.entry_output.config(state="readonly")

if __name__ == "__main__":
    root = tk.Tk()
    app = EnigmaApp(root)
    root.mainloop()
