

import time
import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from setting.setting import *
from src.scanner import Scanner
from src.log_saving import FileSaving


def choose_folder():
    return filedialog.askdirectory()

class AppGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(TITLE)
        self.geometry(f"{WSIZE[0]}x{WSIZE[1]}")
        self.configure(bg=COLOR["Background_Mint"])
        self.iconbitmap("assets/icon.ico")
        self.resizable(False, False)

        # 2-column layout: Sidebar (20%) and Main Area (80%)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)
        self.grid_rowconfigure(0, weight=1)

        self.create_sidebar()
        self.create_main_area()

        # Initialize scanner and file saving logic
        self.scanner = Scanner()
        self.log_saving = FileSaving()

    def create_sidebar(self):
        sidebar = tk.Frame(self, bg=COLOR["Ligth_Green"], bd=2, relief="ridge")
        sidebar.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        tk.Label(sidebar, text="🔍 File Scanner", font=FONT_SIZE["Small"], bg=COLOR["Cream_Beige_Box"]).pack(pady=15)

        tk.Button(sidebar, 
                  text="📂 Choose Folder", 
                  command=self.select_folder, 
                  bg=COLOR["Cream_Beige_Box"], 
                  width=20).pack(pady=10, padx=5)

        self.scan_btn = tk.Button(sidebar, 
                                  text="▶️ Start Scan", 
                                  command=self.run_scan, 
                                  bg=COLOR["Primary_Green"], 
                                  width=20,
                                  state="disabled")
        self.scan_btn.pack(pady=10, padx=5)

        self.save_csv_btn = tk.Button(sidebar, 
                                  text="▶️ Save as CSV", 
                                  command=self.run_save_csv, 
                                  bg=COLOR["Ligth_Green"], 
                                  width=20,
                                  state="disabled")
        self.save_csv_btn.pack(pady=10, padx=5)

        self.save_pkl_btn = tk.Button(sidebar, 
                                  text="▶️ Save as PKL", 
                                  command=self.save_pkl_logs, 
                                  bg=COLOR["Ligth_Green"], 
                                  width=20,
                                  state="disabled")
        self.save_pkl_btn.pack(pady=10, padx=5)

        self.save_txt_btn = tk.Button(sidebar, 
                                  text="▶️ Save File Info", 
                                  command=self.save_file_infotxt, 
                                  bg=COLOR["Ligth_Green"], 
                                  width=20,
                                  state="disabled")
        self.save_txt_btn.pack(pady=10, padx=5)

        # Close button
        self.close_btn = tk.Button(sidebar, 
                                  text="▶️ Close", 
                                  command=self.close_app, 
                                  bg=COLOR["Ligth_Green"], 
                                  width=20,
                                  state="normal")
        self.close_btn.pack(pady=10, padx=5)

    def create_main_area(self):
        main_area = tk.Frame(self, bg=COLOR["Background_Mint"])
        main_area.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        main_area.grid_rowconfigure(0, weight=1)
        main_area.grid_columnconfigure(0, weight=1)

        # Logs / Output area
        self.log_box = scrolledtext.ScrolledText(main_area, 
                                                 wrap=tk.WORD, 
                                                 bg=COLOR["Entry_Background"], 
                                                 fg=COLOR["Text_Normal"], 
                                                 font=("Consolas", 10))
        self.log_box.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.log_box.insert(tk.END, "✅ Welcome to File Scanner!\n")

    def select_folder(self):
        folder = choose_folder()
        if folder:
            # Reset old scan data
            self.scanner.reset()
            self.log_box.delete(1.0, tk.END)
            self.source = folder # Store the selected folder path
            self.log_box.insert(tk.END, f"📂 Selected folder: {folder}\n")
            self.scan_btn.config(state="normal")
        else:
            messagebox.showwarning("Warning", "No folder selected.")

        self.save_csv_btn.config(state="disabled")
        self.save_pkl_btn.config(state="disabled")
        self.save_txt_btn.config(state="disabled")


    def run_scan(self):
        self.scanner.reset()  # Reset scanner logs before starting a new scan
        self.log_box.delete(1.0, tk.END)
        self.log_box.insert(tk.END, "🔍 Scanning started...\n")
        self.update_idletasks()  # Update the GUI to show the log box
        # print(f"calling scan: {self.source}")
        # Example logic call:

        # bb = self.scanner.get_file_paths()
        # self.log_box.insert(tk.END, f"Files found: {bb}\n")

        start_time = time.time()  # Start timer
        num = 0
        for root, dirs, files in os.walk(self.source):
            for file_name in files:
                scanning_path = Path(root) / file_name
                num += 1
                log = f"{num}. 📁 Scanning: {scanning_path}"
                self.log_box.insert(tk.END, log + "\n")
                self.log_box.see(tk.END)
                self.update_idletasks()
                self.log_box.delete(1.0, tk.END)
                # time.sleep(0.01)  # Simulate some delay for scanning
        time_taken = time.time() - start_time
        self.log_box.insert(tk.END, f"✅ Scan completed in {time_taken:.2f} seconds.\n")
        self.log_box.insert(tk.END, "------------------Scan End------------------------\n")

        self.scanner.scan(self.source, self.log_box)

        for ftype, data in self.scanner.get_file_stats().items():
            self.log_box.insert(tk.END, f"{ftype}: {data['count']} files, {data['size']} MB \n")
        # self.log_box.insert(tk.END, f"📊 File statistics: {self.scanner.get_file_stats()}\n")

        # self.log_box.insert(tk.END, f"✅ Scan completed. {num} files scanned.\n")
        self.log_box.insert(tk.END, "💾 You can now save the logs as CSV or PKL and Files Info in Text file.\n")
        self.log_box.see(tk.END)
        self.save_csv_btn.config(state="normal")
        self.save_pkl_btn.config(state="normal")
        self.save_txt_btn.config(state="normal")

    def run_save_csv(self):
        self.log_box.insert(tk.END, "💾 Saving logs as CSV...\n")
        # Example logic for saving CSV
        self.log_saving.csv_logs_save(self.scanner.get_file_paths())
        self.log_box.insert(tk.END, "✅ CSV logs saved successfully.\n")
        self.save_csv_btn.config(state="disabled")
        
    def save_pkl_logs(self):
        self.log_box.insert(tk.END, "💾 Saving logs as PKL...\n")
        # Example logic for saving PKL
        self.log_saving.pkl_logs_save(self.scanner.get_logs())
        self.log_box.insert(tk.END, "✅ PKL logs saved successfully.\n")
        self.save_pkl_btn.config(state="disabled")

    def save_file_infotxt(self):
        self.log_box.insert(tk.END, "💾 Saving file info...\n")
        # Example logic for saving file info in Text File
        self.log_saving.save_file_info(self.scanner.get_file_stats().items())
        self.log_box.insert(tk.END, "✅ File info saved successfully in Text file.\n")
        self.save_txt_btn.config(state="disabled")

    def close_app(self):
        self.scanner.reset()
        self.log_box.insert(tk.END, "❌ Closing application...\n")
        self.destroy()