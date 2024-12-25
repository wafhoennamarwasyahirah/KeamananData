import os
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
from stegano import lsb

def select_image(entry):
    filepath = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]
    )
    if filepath:
        entry.delete(0, "end")
        entry.insert(0, filepath)

def save_image(entry):
    filepath = filedialog.asksaveasfilename(
        defaultextension=".png", filetypes=[("PNG files", "*.png")]
    )
    if filepath:
        entry.delete(0, "end")
        entry.insert(0, filepath)

def hide_message():
    img_path = image_path_entry.get()
    save_path = save_path_entry.get()
    message = message_entry.get()

    if not os.path.exists(img_path) or not img_path.lower().endswith((".png", ".jpg", ".jpeg")):
        messagebox.showerror("Error", "Invalid image path. Please select a valid image.")
        return

    if not save_path:
        messagebox.showerror("Error", "Please specify where to save the encoded image.")
        return

    try:
        secret = lsb.hide(img_path, message)
        secret.save(save_path)
        messagebox.showinfo("Success", f"Message hidden successfully! Image saved at {save_path}.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to hide message: {e}")

def reveal_message():
    img_path = image_path_entry.get()

    if not os.path.exists(img_path) or not img_path.lower().endswith((".png", ".jpg", ".jpeg")):
        messagebox.showerror("Error", "Invalid image path. Please select a valid image.")
        return

    try:
        hidden_message = lsb.reveal(img_path)
        if hidden_message:
            messagebox.showinfo("Hidden Message", hidden_message)
        else:
            messagebox.showinfo("Hidden Message", "No hidden message found in the image.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to reveal message: {e}")

# GUI Setup
app = Tk()
app.title("Steganography Tool")
app.geometry("500x400")
app.resizable(False, False)

# Labels and Inputs
Label(app, text="Select Image:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
image_path_entry = Entry(app, width=50)
image_path_entry.grid(row=0, column=1, padx=10, pady=10)
Button(app, text="Browse", command=lambda: select_image(image_path_entry)).grid(row=0, column=2, padx=10, pady=10)

Label(app, text="Save As:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
save_path_entry = Entry(app, width=50)
save_path_entry.grid(row=1, column=1, padx=10, pady=10)
Button(app, text="Browse", command=lambda: save_image(save_path_entry)).grid(row=1, column=2, padx=10, pady=10)

Label(app, text="Message:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
message_entry = Entry(app, width=50)
message_entry.grid(row=2, column=1, padx=10, pady=10)

# Buttons
Button(app, text="Hide Message", width=15, command=hide_message).grid(row=3, column=1, pady=20)
Button(app, text="Reveal Message", width=15, command=reveal_message).grid(row=4, column=1, pady=10)

# Run the app
app.mainloop()
