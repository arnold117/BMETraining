import os
from pathlib import Path
import sys

import random

from PySide6 import QtCharts
from PySide6.QtWidgets import QApplication, QTextEdit
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import Qt, QObject, Slot, QPointF, Property, Signal


class DataModel(QObject):
    textRes = Signal(str, arguments=['textLabel'])
    serRes = Signal(str, arguments=['ser'])

    def __init__(self, parent=None):
        QObject.__init__(self, parent)

    @Slot(QtCharts.QXYSeries)
    def update_serie(self, serie):
        # generate points
        points = []
        x = 0
        while x < 10:
            x += 0.1
            y = random.uniform(-100, 100)
            point = QPointF(x, y)
            points.append(point)
        # replace points
        serie.replace(points)
        self.serRes.emit(points)

    @Slot(str)
    def change_text(self, arg1):
        # do something with the text and emit a signal
        # arg1 = arg1.upper()
        self.textRes.emit(arg1)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    engine = QQmlApplicationEngine()

    context = engine.rootContext()
    dataModel = DataModel()
    context.setContextProperty("dataModel", dataModel)

    engine.load(os.fspath(Path(__file__).resolve().parent / "./main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
