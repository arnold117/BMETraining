import os
from pathlib import Path
import sys

import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox

from threading import Timer

from PySide6 import QtCharts
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import Qt, QObject, Slot, QPointF, Signal

import PCT


class Control(QObject):
    tempSen1Res = Signal(str, arguments=['temperatureSensor1'])
    tempSen2Res = Signal(str, arguments=['temperatureSensor2'])

    def __init__(self):
        super().__init__()

        self.timer = None
        self.pct_data = None
        self.path_open = None
        self.path_save = None
        self.data_array = []
        self.count = 0
        self.pct = PCT.PCT()
        self.split_data = PCT.PCTData()

    # @Slot()
    # def get_ECG1_wave(self):
    #     return self.split_data.ECG1_wave

    @Slot()
    def join_hex(self, data_high, data_low):
        return (data_high << 8) | data_low

    @Slot()
    def about_page(self):
        tkinter.messagebox.showinfo('About', 'Copyright (c) 2022 Arnold Chow, All rights reserved')

    @Slot(QtCharts.QXYSeries)
    def update_series(self, series, dat):
        series.replace(dat)

    @Slot(str)
    def set_temperature_sensor1(self, arg):
        self.tempSen1Res.emit(arg)

    @Slot(str)
    def set_temperature_sensor2(self, arg):
        self.tempSen2Res.emit(arg)

    @Slot()
    def data_process(self):
        arr = self.data_array[self.count]

        if arr[0] == 0x10:
            if arr[1] == 0x02:
                data_type = "DAT_EEG_WAVE"
                ECG1_wave = self.join_hex(arr[2], arr[3])
                ECG2_wave = self.join_hex(arr[4], arr[5])
                ECG_status = arr[6]

                # self.split_data.ecg.ECG1_wave.append(ECG1_wave)
                # self.split_data.ecg.ECG2_wave.append(ECG2_wave)
                # self.split_data.ecg.ECG_status.append(ECG_status)
            if arr[1] == 0x03:
                data_type = "DAT_EEG_LEAD"
                lead_info = arr[2]
                overload_warning = arr[3]

                # self.split_data.ecg.lead_info.append(lead_info)
                # self.split_data.ecg.overload_warning.append(overload_warning)
            if arr[1] == 0x04:
                data_type = "DAT_EEG_HR"
                heart_rate = self.join_hex(arr[2], arr[3])

                # self.split_data.ecg.heart_rate.append(heart_rate)

        if arr[0] == 0x11:
            if arr[1] == 0x02:
                data_type = "DAT_RESP_WAVE"
                respiration_wave_data1 = arr[2]
                respiration_wave_data2 = arr[3]
                respiration_wave_data3 = arr[4]
                respiration_wave_data4 = arr[5]
                respiration_wave_data5 = arr[6]

                # i = 2
                # while i < 7:
                #     self.split_data.resp.respiration_wave_data.append(arr[i])
                #     i += 1
            if arr[1] == 0x03:
                data_type = "DAT_RESP_LEAD"
                respiration_rate = self.join_hex(arr[2], arr[3])

                # self.split_data.resp.respiration_rate.append(respiration_rate)

        if arr[0] == 0x12:
            if arr[1] == 0x02:
                data_type = "DAT_TEMP_DATA"
                temperature_sensor_status = arr[2]
                temperature_channel1 = self.join_hex(arr[3], arr[4])
                temperature_channel2 = self.join_hex(arr[5], arr[6])

                # self.split_data.temp.temperature_sensor_status.append(temperature_sensor_status)
                # self.split_data.temp.temperature_channel1.append(temperature_channel1)
                # self.split_data.temp.temperature_channel2.append(temperature_channel2)

                self.set_temperature_sensor1("T1 Connected")
                self.set_temperature_sensor2("T2 Connected")

        if arr[0] == 0x13:
            if arr[1] == 0x02:
                data_type = "DAT_SPO2_WAVE"
                o2_wave_data1 = arr[2]
                o2_wave_data2 = arr[3]
                o2_wave_data3 = arr[4]
                o2_wave_data4 = arr[5]
                o2_wave_data5 = arr[6]
                o2_measure_status = arr[7]

                # i = 2
                # while i < 7:
                #     self.split_data.spo2.o2_wave_data.append(arr[i])
                #     i += 1
                # self.split_data.spo2.o2_measure_status.append(o2_measure_status)
            if arr[1] == 0x03:
                data_type = "DAT_SPO2_DATA"
                o2_saturate_info = arr[2]
                pulse_rate = self.join_hex(arr[3], arr[4])
                o2_saturate_data = arr[5]

                # self.split_data.spo2.o2_saturate_info.append(o2_saturate_info)
                # self.split_data.spo2.pulse_rate.append(pulse_rate)
                # self.split_data.spo2.o2_saturate_data.append(o2_saturate_data)

        if arr[0] == 0x14:
            if arr[1] == 0x02:
                data_type = "DAT_NBP_CUFPRE"
                cuff_pressure = self.join_hex(arr[2], arr[3])
                cuff_type_error = arr[4]
                measure_type = arr[5]

                # self.split_data.nbp.cuff_pressure.append(cuff_pressure)
                # self.split_data.nbp.cuff_type_error.append(cuff_type_error)
                # self.split_data.nbp.measure_type.append(measure_type)
            if arr[1] == 0x03:
                data_type = "DAT_NBP_END"
                measure_type = arr[2]

                # self.split_data.nbp.measure_type.append(measure_type)
            if arr[1] == 0x04:
                data_type = "DAT_NBP_RSLT1"
                systolic_pressure = self.join_hex(arr[2], arr[3])
                diastolic_pressure = self.join_hex(arr[4], arr[5])
                mean_artery_pressure = self.join_hex(arr[6], arr[7])

                # self.split_data.nbp.systolic_pressure.append(systolic_pressure)
                # self.split_data.nbp.diastolic_pressure.append(diastolic_pressure)
                # self.split_data.nbp.mean_artery_pressure.append(mean_artery_pressure)
            if arr[1] == 0x05:
                data_type = "DAT_NBP_RSLT2"
                pulse_rate = self.join_hex(arr[2], arr[3])

                # self.split_data.nbp.pulse_rate.append(pulse_rate)
        self.count += 1

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
            for index, row in self.pct_data.iterrows():
                arr = self.pct_data.loc[index].values
                arr = list(map(int, arr))
                self.data_array.append(arr)
            self.timer.start()

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
    t = Timer(0.1, control.data_process)
    control.timer = t

    engine.load(os.fspath(Path(__file__).resolve().parent / "./ui/main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
