import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk
import qrcode

class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")

        self.label = tk.Label(root, text="Enter URL:")
        self.label.pack(pady=10)

        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=10)

        self.generate_button = tk.Button(root, text="Generate QR Code", command=self.generate_qr_code, state=tk.DISABLED)
        self.generate_button.pack(pady=20)

        self.url_entry.bind("<KeyRelease>", self.on_key_release)

    def on_key_release(self, event):
        url = self.url_entry.get()
        if url:
            self.generate_button.config(state=tk.NORMAL)
        else:
            self.generate_button.config(state=tk.DISABLED)

    def generate_qr_code(self):
        url = self.url_entry.get()
        if url:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)

            img = qr.make_image(fill='black', back_color='white')
            self.display_qr_code(img)

    def display_qr_code(self, img):
        qr_window = tk.Toplevel(self.root)
        qr_window.title("Generated QR Code")

        img = img.convert("RGB")
        self.qr_img = ImageTk.PhotoImage(img)

        qr_label = tk.Label(qr_window, image=self.qr_img)
        qr_label.pack(pady=10)

        save_button = tk.Button(qr_window, text="Save", command=lambda: self.save_qr_code(img))
        save_button.pack(pady=10)

    def save_qr_code(self, img):
        file_path = filedialog.asksaveasfilename(defaultextension=".jpeg", filetypes=[("JPEG files", "*.jpeg"), ("All files", "*.*")])
        if file_path:
            img.save(file_path)
            messagebox.showinfo("Success", f"QR code saved as {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGenerator(root)
    root.mainloop()
