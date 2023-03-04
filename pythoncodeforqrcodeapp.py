import qrcode
import tkinter as tk
from PIL import ImageTk, Image

# Define the GUI window
root = tk.Tk()
root.title("QR Code Generator")

# Define the input label and entry
input_label = tk.Label(root, text="Enter URL:")
input_label.pack()
input_entry = tk.Entry(root)
input_entry.pack()

# Define the function to generate the QR code
def generate_qr_code():
    url = input_entry.get()
    qr_code = qrcode.QRCode(version=1, box_size=10, border=5)
    qr_code.add_data(url)
    qr_code.make(fit=True)
    qr_code_image = qr_code.make_image(fill_color="black", back_color="white")
    qr_code_image = qr_code_image.resize((250, 250), Image.ANTIALIAS)
    qr_code_image = ImageTk.PhotoImage(qr_code_image)
    qr_code_label.config(image=qr_code_image)
    qr_code_label.image = qr_code_image

# Define the generate button
generate_button = tk.Button(root, text="Generate", command=generate_qr_code)
generate_button.pack()

# Define the QR code label
qr_code_label = tk.Label(root)
qr_code_label.pack()

# Start the GUI
root.mainloop()
