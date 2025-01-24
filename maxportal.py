import os
import json
import ctypes
from ctypes import wintypes
import tkinter as tk
from tkinter import colorchooser, filedialog

class MaxPortal:
    def __init__(self):
        self.theme = {
            'background': '#ffffff',
            'foreground': '#000000',
            'accent': '#0078d7'
        }
        self.theme_file = 'theme.json'
        self.load_theme()

    def load_theme(self):
        if os.path.exists(self.theme_file):
            with open(self.theme_file, 'r') as f:
                self.theme = json.load(f)

    def save_theme(self):
        with open(self.theme_file, 'w') as f:
            json.dump(self.theme, f, indent=4)

    def set_theme(self):
        # Applying theme to Windows (using ctypes for demonstration purposes)
        SPI_SETDESKWALLPAPER = 20
        user32 = ctypes.WinDLL('user32', use_last_error=True)
        user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, self.theme.get('background'), 3)

    def choose_color(self, color_type):
        color_code = colorchooser.askcolor(title=f"Choose {color_type} color")
        if color_code:
            self.theme[color_type] = color_code[1]

    def run(self):
        self.app = tk.Tk()
        self.app.title("MaxPortal - Custom Themes")

        bg_button = tk.Button(self.app, text="Background Color", command=lambda: self.choose_color('background'))
        bg_button.pack(pady=10)
        
        fg_button = tk.Button(self.app, text="Foreground Color", command=lambda: self.choose_color('foreground'))
        fg_button.pack(pady=10)
        
        accent_button = tk.Button(self.app, text="Accent Color", command=lambda: self.choose_color('accent'))
        accent_button.pack(pady=10)

        apply_button = tk.Button(self.app, text="Apply Theme", command=self.set_theme)
        apply_button.pack(pady=20)

        save_button = tk.Button(self.app, text="Save Theme", command=self.save_theme)
        save_button.pack(pady=20)

        self.app.mainloop()

if __name__ == "__main__":
    mp = MaxPortal()
    mp.run()