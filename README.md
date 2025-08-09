
# 📂 File Scanner with Tkinter GUI

A Python-based **File Scanner** that allows you to quickly scan folders, count files by type, display real-time scanning logs, and measure scan duration. The tool features a **Tkinter GUI** with an intuitive sidebar for easy navigation, and supports exporting results as **CSV, PKL, and TXT** files.

---

## 🚀 Features

* **📂 Choose Folder** – Select the folder to scan.
* **🔍 File Scanning** – Detects and logs files with real-time updates.
* **📊 File Type Statistics** – Counts files by type and calculates total size.
* **⏱ Scan Duration** – Displays time taken to complete the scan.
* **💾 Save Results** – Export scan results as:

  * CSV file of scanned file paths
  * PKL file of scan logs
  * TXT file containing file statistics
* **🖥 User-Friendly Interface** – Sidebar menu with one-click actions.

---

## 📸 Screenshot

*(Add your app screenshot here)*

---

## 📦 Installation

### 1️⃣ Clone this repository

```bash
git clone https://github.com/Alexashok99/FileScanner.git
cd FileScanner
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

*(If you don’t have a requirements.txt, manually install Tkinter and other dependencies.)*

```bash
pip install pillow
```

---

## ▶️ Usage

Run the app with:

```bash
python main.py
```

1. Click **📂 Choose Folder** to select a directory.
2. Click **▶️ Start Scan** to begin scanning.
3. View real-time logs and file statistics.
4. Save results using CSV, PKL, or TXT options.
5. Close the app with the **▶️ Close** button.

---

## 📂 File Types Supported

Includes detection for **PDF, images, videos, audio, archives, code files, documents**, and more:

```
.pdf, .jpeg, .png, .docx, .xlsx, .txt, .zip, .rar, .mp3, .mp4, .html, .js, .css,
.json, .xml, .csv, .yaml, .tar, .gz, .apk, .exe, .bat, .sh, .py, .java, .cpp, .c,
.php, .go, .r, .swift, .kt, .ts
```

---

## 🛠 Project Structure

```
project/
│── main.py              # GUI entry point
│── src/
│    ├── scanner.py       # File scanning logic
│    ├── log_saving.py    # Saving logs in different formats
│── setting/
│    ├── setting.py       # App settings, colors, fonts
│    │──constant.py
│── assets/
│    ├── icon.ico         # App icon
```

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ✨ Author

Developed by **[Bijay Mahto](https://github.com/Alexashok99)**

---
