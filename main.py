import os
from pathlib import Path
import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import Qt, QObject, Slot


class Control(QObject):
    @Slot()
    def ledOn(self):
        print("led on")

    @Slot()
    def ledOff(self):
        print("led off")


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()

    context = engine.rootContext()
    controler = Control()
    context.setContextProperty("_Control",controler)

    engine.load(os.fspath(Path(__file__).resolve().parent / "./ui/led.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
