# 🖼️ Image Compressor

A simple and efficient Python-based image compression tool that reduces image file size while preserving quality.

---

## ✨ Features

* Compress images with adjustable quality
* Supports JPEG and PNG formats
* Batch compression support
* Lightweight and fast
* Easy to use CLI

---

## 📂 Project Structure

```
image-compressor/
│── compressor.py
│── requirements.txt
│── README.md
│── .gitignore
│── LICENSE
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Moseskenny/image-compressor.git
cd image-compressor
```

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### Basic compression

```bash
python compressor.py input.jpg output.jpg --quality 70
```

### Batch compression

```bash
python compressor.py ./input_folder ./output_folder --quality 60
```

---

## 🔧 Configuration

| Parameter   | Description                 |
| ----------- | --------------------------- |
| `--quality` | Compression quality (1–100) |
| `input`     | Input image/folder          |
| `output`    | Output image/folder         |

---

## 🧠 How it works

The script uses the Pillow library to:

1. Load image
2. Optimize encoding
3. Adjust compression quality
4. Save reduced file size image

---

## 📦 Dependencies

* Python 3.x
* Pillow

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the project
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👤 Author

**Moses Kenny**
GitHub: https://github.com/Moseskenny

---

## ⭐ Support

If you like this project, please ⭐ the repo!
