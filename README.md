# 🖼️ Image Compressor (GUI App)

A simple and user-friendly **desktop image compression tool** built using Python, Tkinter, and Pillow.

This application allows you to select an image, adjust compression quality using a slider, and save a compressed version while viewing size reduction statistics.

---

## ✨ Features

* 🖱️ Easy-to-use graphical interface (Tkinter)
* 🎚️ Adjustable compression quality (1–95)
* 🖼️ Supports common image formats (JPG, PNG, etc.)
* 💾 Save compressed image to custom location
* 📊 Displays:

  * Original file size
  * Compressed file size
  * Compression ratio
* ⚡ Fast and lightweight

---

## 📸 Application Preview

> GUI window with slider, button, and compression results

---

## 📂 Project Structure

```id="pj7m2p"
image-compressor/
│── compressor.py
│── requirements.txt
│── README.md
│── LICENSE
│── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash id="6o2i1v"
git clone https://github.com/Moseskenny/image-compressor.git
cd image-compressor
```

### 2. Create a virtual environment (recommended)

```bash id="ts6k61"
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash id="k0x9n2"
pip install -r requirements.txt
```

---

## 🚀 How to Use

Run the application:

```bash id="1g8zfh"
python compressor.py
```

### Steps:

1. Click **"Select and Compress Image"**
2. Choose your image file
3. Choose where to save the compressed image
4. Adjust compression quality using the slider
5. View compression results instantly

---

## 🎚️ Compression Quality Guide

| Quality Value | Result                             |
| ------------- | ---------------------------------- |
| 90–95         | High quality, larger file          |
| 70–85         | Balanced compression               |
| 40–60         | Smaller size, some quality loss    |
| 1–30          | Maximum compression, lower quality |

---

## 📊 Example Output

```

Original size: 2048.00 KB  
Compressed size: 620.00 KB  
Compression ratio: 30.27%

```

---

## 🧰 Technologies Used

* Python
* Tkinter (GUI)
* Pillow (PIL)

---

## 📦 Requirements

```id="9pmgrl"
Pillow
```

---

## 📜 License

This project is licensed under the MIT License.

---

## 👤 Author

**Moses Kenny**
GitHub: https://github.com/Moseskenny

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a Pull Request

---

## ⭐ Support

If you like this project, please ⭐ the repository and share it!
