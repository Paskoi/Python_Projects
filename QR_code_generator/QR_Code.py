import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk
import qrcode

class QRCodeGenerator:
    def __init__(self, root):
        # Main window
        self.root = root
        self.root.title("QR Code Generator")

        # Label for URL entry
        self.label = tk.Label(root, text="Enter URL:")
        self.label.pack(pady=10)

        # Entry widget for URL input
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=10)

        # Button to generate QR code (initially disabled)
        self.generate_button = tk.Button(root, text="Generate QR Code", command=self.generate_qr_code, state=tk.DISABLED)
        self.generate_button.pack(pady=20)

        # Bind the URL entry widget to key release event
        self.url_entry.bind("<KeyRelease>", self.on_key_release)

    def on_key_release(self, event):
        # Enable the generate button if URL entry is not empty
        url = self.url_entry.get()
        if url:
            self.generate_button.config(state=tk.NORMAL)
        else:
            self.generate_button.config(state=tk.DISABLED)

    def generate_qr_code(self):
        # Generate a QR code from the entered URL
        url = self.url_entry.get()
        if url:
            # QR code object
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)

            # Image from the QR code
            img = qr.make_image(fill='black', back_color='white')
            self.display_qr_code(img)

    def display_qr_code(self, img):
        # Window for generated QR code
        qr_window = tk.Toplevel(self.root)
        qr_window.title("Generated QR Code")

        # Convert image to RGB mode for saving as JPEG
        img = img.convert("RGB")
        self.qr_img = ImageTk.PhotoImage(img)
        
        # Display the QR code image
        qr_label = tk.Label(qr_window, image=self.qr_img)
        qr_label.pack(pady=10)

        # Save button
        save_button = tk.Button(qr_window, text="Save", command=lambda: self.save_qr_code(img))
        save_button.pack(pady=10)

    def save_qr_code(self, img):
        # Open a file dialog to save the QR code image as a JPEG file
        file_path = filedialog.asksaveasfilename(defaultextension=".jpeg", filetypes=[("JPEG files", "*.jpeg"), ("All files", "*.*")])
        if file_path:
            # Save the image
            img.save(file_path)
            # Success message
            messagebox.showinfo("Success", f"QR code saved as {file_path}")

if __name__ == "__main__":
    # Make main window and run the application
    root = tk.Tk()
    app = QRCodeGenerator(root)
    root.mainloop()
