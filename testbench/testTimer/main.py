import os
from pathlib import Path
import sys

import random

from PySide6 import QtCharts
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import Qt, QObject, Slot, QPointF, Property


class DataModel(QObject):
    textChanged = Slot(str)

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self.m_text = ""

    @Property(str, notify=textChanged)
    def text(self):
        return self.m_text

    @text.setter
    def setText(self, text):
        if self.m_text == text:
            return
        self.m_text = text
        self.textChanged.emit(self.m_text)

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

    @Slot()
    def change(self, item):
        width = 300
        item = width


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