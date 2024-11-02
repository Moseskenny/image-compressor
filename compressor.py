import PIL
from PIL import Image
from tkinter import Tk, Scale, Button, Label, filedialog, StringVar, ttk
import os
import tkinter as tk

def compress_image():
    global quality
    file_path = filedialog.askopenfilename(title="Select an image file")
    if not file_path:
        result_var.set("No file selected. Operation cancelled.")
        return

    img = Image.open(file_path)

    save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
    if not save_path:
        result_var.set("No save location selected. Operation cancelled.")
        return

    img.save(save_path, "JPEG", quality=quality, optimize=True)

    original_size = os.path.getsize(file_path)
    compressed_size = os.path.getsize(save_path)

    result_text = f"Image compressed and saved to: {save_path}\n\n"
    result_text += f"Original size: {original_size/1024:.2f} KB\n"
    result_text += f"Compressed size: {compressed_size/1024:.2f} KB\n"
    result_text += f"Compression ratio: {compressed_size/original_size:.2%}"

    result_var.set(result_text)

def update_quality(val):
    global quality
    quality = int(float(val))
    quality_var.set(f"{quality}")


root = Tk()
root.title("Image Compressor")
root.geometry("500x400")
root.configure(bg='#2c3e50')

style = ttk.Style()
style.theme_use('clam')
style.configure('TFrame', background='#2c3e50')
style.configure('TButton', font=('Arial', 12), padding=10, background='#3498db', foreground='white')
style.map('TButton', background=[('active', '#2980b9')])
style.configure('TLabel', font=('Arial', 12), background='#2c3e50', foreground='white')
style.configure('Horizontal.TScale', background='#2c3e50', troughcolor='#34495e', slidercolor='#3498db', sliderrelief='flat')


main_frame = ttk.Frame(root, padding="20 20 20 20")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

quality = 85


quality_var = StringVar()
quality_var.set(f"{quality}")
quality_label = ttk.Label(main_frame, text="Compression Quality:")
quality_label.grid(row=0, column=0, pady=(0, 5), sticky='w')
quality_value_label = ttk.Label(main_frame, textvariable=quality_var, width=3)
quality_value_label.grid(row=0, column=1, pady=(0, 5), sticky='e')

quality_slider = ttk.Scale(main_frame, from_=1, to=95, orient="horizontal", command=update_quality, length=300)
quality_slider.set(quality)
quality_slider.grid(row=1, column=0, columnspan=2, pady=(0, 20), sticky='ew')

compress_button = ttk.Button(main_frame, text="Select and Compress Image", command=compress_image)
compress_button.grid(row=2, column=0, columnspan=2, pady=(0, 20), sticky='ew')


result_var = StringVar()
result_var.set("Compression results will appear here.")
result_label = ttk.Label(main_frame, textvariable=result_var, wraplength=460, justify="left")
result_label.grid(row=3, column=0, columnspan=2, pady=(0, 10), sticky='w')


main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)


root.mainloop()

