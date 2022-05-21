import os
from pathlib import Path
import sys

import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox

from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import Qt, QObject, Slot

import PCT

class Control(QObject):
    def __init__(self):
        super().__init__()

        self.pct_data_read = False
        self.pct_data = None
        self.path_open = None
        self.path_save = None
        self.pct = PCT.PCT()

    @Slot()
    def about_page(self):
        tkinter.messagebox.showinfo('About', 'Copyright (c) 2022 Arnold Chow, All rights reserved')

    @Slot()
    def open_file(self):
        self.path_open = tk.filedialog.askopenfilename(filetypes=(("csv files", "*.csv"),))
        print(self.path_open)
        self.pct_data = self.pct.read_packed_csv(self.path_open)
        try:
            if self.pct_data == [0, 0, 0, 0, 0, 0, 0, 0]:
                self.pct_data = self.pct.read_unpacked_csv(self.path_open)
            if self.pct_data == [0, 0, 0, 0, 0, 0, 0, 0]:
                tkinter.messagebox.showerror('Error', 'This is neither a packed PCT CSV nor'
                                                      'an unpacked PCT CSV!')
        except ValueError:
            self.pct_data_read = True
            self.data_process()

    @Slot()
    def save_file(self):
        self.path_save = tkinter.filedialog.asksaveasfilename(initialfile='saved_data.csv',
                                                              filetypes=[("CSV Files", ".csv")])
        print(self.path_save)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    engine = QQmlApplicationEngine()

    root = tk.Tk()
    root.withdraw()

    context = engine.rootContext()
    control = Control()
    context.setContextProperty("_Control", control)

    engine.load(os.fspath(Path(__file__).resolve().parent / "./ui/main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
