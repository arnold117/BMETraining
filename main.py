import os
from pathlib import Path
import sys

import tkinter as tk
import tkinter.filedialog

from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import Qt, QObject, Slot

import PCT


class Control(QObject):
    @Slot()
    def ledOn(self):
        print("led on")

    @Slot()
    def ledOff(self):
        print("led off")

    @Slot()
    def openFile(self):
        f_path = tk.filedialog.askopenfilename()
        print('\n获取的文件地址：', f_path)

    @Slot()
    def saveFile(self):
        path_save = tkinter.filedialog.asksaveasfilename(initialfile='saved_data.csv', filetypes=[("CSV Files", ".csv")])
        print(path_save)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    engine = QQmlApplicationEngine()

    root = tk.Tk()
    root.withdraw()

    context = engine.rootContext()
    controler = Control()
    context.setContextProperty("_Control", controler)

    engine.load(os.fspath(Path(__file__).resolve().parent / "./ui/draw.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
