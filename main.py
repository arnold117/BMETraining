import os
from pathlib import Path
import sys

import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox

from PySide6 import QtCharts
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, QPointF, Signal, QTimer

import PCT


class Control(QObject):
    ecg1WaveRes = Signal(str)
    ecg2WaveRes = Signal(str)
    raStatusRes = Signal(str, arguments=['getRaStatus'])
    laStatusRes = Signal(str, arguments=['getLaStatus'])
    llStatusRes = Signal(str, arguments=['getLlStatus'])
    vStatusRes = Signal(str, arguments=['getVStatus'])
    heartRateRes = Signal(str, arguments=['getHeartRate'])

    tempSen1Res = Signal(str, arguments=['getTempSen1'])
    tempSen2Res = Signal(str, arguments=['getTempSen2'])
    temp1Res = Signal(str, arguments=['getT1'])
    temp2Res = Signal(str, arguments=['getT2'])

    respirationWaveRes = Signal(str)
    respirationRateRes = Signal(str, arguments=['getRespirationRate'])

    spo2WaveRes = Signal(str)
    fingerInfoRes = Signal(str, arguments=['getFingerInfo'])
    probeInfoRes = Signal(str, arguments=['getProbeInfo'])
    spo2RateRes = Signal(str, arguments=['getSpo2Rate'])
    spo2DataRes = Signal(str, arguments=['getSpo2Data'])

    cuffPressureRes = Signal(str, arguments=['getCuffPressure'])
    nbpMethodRes = Signal(str, arguments=['getNbpMethod'])
    pressureRes = Signal(str, arguments=['getPressure'])
    meanPressureRes = Signal(str, arguments=['getMeanPressure'])
    nbpRateRes = Signal(str, arguments=['getNbpRate'])

    def __init__(self):
        super().__init__()

        self.data_count = 0
        self.timer = QTimer(self)
        self.pct_data = None
        self.path_open = None
        self.path_save = None
        self.data_array = []
        self.count = 0
        self.pct = PCT.PCT()

        self.timer.timeout.connect(self.data_process)
        self.ecg1_wave = []
        self.ecg1_wave_x = 0
        self.ecg2_wave = []
        self.ecg2_wave_x = 0
        self.respiration_wave = []
        self.respiration_wave_x = 0
        self.spo2_wave = []
        self.spo2_wave_x = 0

    @Slot()
    def join_hex(self, data_high, data_low):
        return (data_high << 8) | data_low

    @Slot()
    def about_page(self):
        tkinter.messagebox.showinfo('About', 'Copyright (c) 2022 Arnold Chow, All rights reserved')

    @Slot(str)
    def set_ecg1_wave(self):
        self.ecg1WaveRes.emit("Triggered")

    @Slot(QtCharts.QXYSeries)
    def update_ecg1_series(self, series):
        series.replace(self.ecg1_wave)

    @Slot(str)
    def set_ecg2_wave(self):
        self.ecg2WaveRes.emit("Triggered")

    @Slot(QtCharts.QXYSeries)
    def update_ecg2_series(self, series):
        series.replace(self.ecg2_wave)

    @Slot(str)
    def set_ra_status(self, arg):
        self.raStatusRes.emit(arg)

    @Slot(str)
    def set_la_status(self, arg):
        self.laStatusRes.emit(arg)

    @Slot(str)
    def set_ll_status(self, arg):
        self.llStatusRes.emit(arg)

    @Slot(str)
    def set_v_status(self, arg):
        self.vStatusRes.emit(arg)

    @Slot(str)
    def set_heart_rate(self, arg):
        self.heartRateRes.emit(arg)

    @Slot(str)
    def set_respiration_wave(self):
        self.respirationWaveRes.emit("Triggered")

    @Slot(QtCharts.QXYSeries)
    def update_respiration_series(self, series):
        series.replace(self.respiration_wave)

    @Slot(str)
    def set_respiration_rate(self, arg):
        self.respirationRateRes.emit(arg)

    @Slot(str)
    def set_temperature_sensor1(self, arg):
        self.tempSen1Res.emit(arg)

    @Slot(str)
    def set_temperature_sensor2(self, arg):
        self.tempSen2Res.emit(arg)

    @Slot(str)
    def set_t1(self, arg):
        self.temp1Res.emit(arg)

    @Slot(str)
    def set_t2(self, arg):
        self.temp2Res.emit(arg)

    @Slot(str)
    def set_spo2_wave(self):
        self.spo2WaveRes.emit("Triggered")

    @Slot(QtCharts.QXYSeries)
    def update_spo2_series(self, series):
        series.replace(self.spo2_wave)

    @Slot(str)
    def set_finger_info(self, arg):
        self.fingerInfoRes.emit(arg)

    @Slot(str)
    def set_probe_info(self, arg):
        self.probeInfoRes.emit(arg)

    @Slot(str)
    def set_spo2_rate(self, arg):
        self.spo2RateRes.emit(arg)

    @Slot(str)
    def set_spo2_data(self, arg):
        self.spo2DataRes.emit(arg)

    @Slot(str)
    def set_cuff_pressure(self, arg):
        self.cuffPressureRes.emit(arg)

    @Slot(str)
    def set_nbp_method(self, arg):
        self.nbpMethodRes.emit(arg)

    @Slot(str)
    def set_pressure(self, arg):
        self.pressureRes.emit(arg)

    @Slot(str)
    def set_mean_pressure(self, arg):
        self.meanPressureRes.emit(arg)

    @Slot(str)
    def set_nbp_rate(self, arg):
        self.nbpRateRes.emit(arg)

    @Slot()
    def data_process(self):
        arr = self.data_array[self.count]

        if arr[0] == 0x10:
            if arr[1] == 0x02:
                data_type = "DAT_EEG_WAVE"
                ECG1_wave = self.join_hex(arr[2], arr[3])
                ECG2_wave = self.join_hex(arr[4], arr[5])
                ECG_status = arr[6]

                if self.ecg1_wave_x < 1000:
                    point = QPointF(self.ecg1_wave_x, ECG1_wave)
                    self.ecg1_wave.append(point)
                    self.ecg1_wave_x += 1
                else:
                    self.ecg1_wave_x = 0
                    self.ecg1_wave = []
                self.set_ecg1_wave()

                if self.ecg2_wave_x < 1000:
                    point = QPointF(self.ecg2_wave_x, ECG2_wave)
                    self.ecg2_wave.append(point)
                    self.ecg2_wave_x += 1
                else:
                    self.ecg2_wave_x = 0
                    self.ecg2_wave = []
                self.set_ecg2_wave()

            if arr[1] == 0x03:
                data_type = "DAT_EEG_LEAD"
                lead_info = arr[2]
                overload_warning = arr[3]
                if lead_info == 0x0:
                    self.set_ra_status("RA")
                    self.set_la_status("LA")
                    self.set_ll_status("LL")
                    self.set_v_status("V")

            if arr[1] == 0x04:
                data_type = "DAT_EEG_HR"
                heart_rate = self.join_hex(arr[2], arr[3])

                self.set_heart_rate(str(heart_rate))

        if arr[0] == 0x11:
            if arr[1] == 0x02:
                data_type = "DAT_RESP_WAVE"
                respiration_wave_data = []
                i = 2
                while i < 7:
                    respiration_wave_data.append(arr[i])
                    point = QPointF(self.respiration_wave_x, arr[i])
                    self.respiration_wave.append(point)
                    i += 1
                    self.respiration_wave_x += 1
                self.set_respiration_wave()

                if self.respiration_wave_x >= 1000:
                    self.respiration_wave_x = 0
                    self.respiration_wave = []

            if arr[1] == 0x03:
                data_type = "DAT_RESP_RR"
                respiration_rate = self.join_hex(arr[2], arr[3])

                self.set_respiration_rate(str(respiration_rate))

        if arr[0] == 0x12:
            if arr[1] == 0x02:
                data_type = "DAT_TEMP_DATA"
                temperature_sensor_status = arr[2]
                temperature_channel1 = self.join_hex(arr[3], arr[4]) / 10.0
                temperature_channel2 = self.join_hex(arr[5], arr[6]) / 10.0

                if temperature_sensor_status == 0x0:
                    self.set_temperature_sensor1("T1 Connected")
                    self.set_temperature_sensor2("T2 Connected")
                self.set_t1(str(temperature_channel1))
                self.set_t2(str(temperature_channel2))

        if arr[0] == 0x13:
            if arr[1] == 0x02:
                data_type = "DAT_SPO2_WAVE"
                o2_measure_status = arr[7]
                o2_wave_data = []
                i = 2
                while i < 7:
                    o2_wave_data.append(arr[i])
                    point = QPointF(self.spo2_wave_x, arr[i])
                    self.spo2_wave.append(point)
                    i += 1
                    self.spo2_wave_x += 1
                self.set_spo2_wave()

                if self.spo2_wave_x >= 1000:
                    self.spo2_wave_x = 0
                    self.spo2_wave = []

                if not (o2_measure_status & 0b10000) and (not (o2_measure_status & 0b10000000)):
                    self.set_finger_info("Finger Online")
                    self.set_probe_info("Probe Online")

            if arr[1] == 0x03:
                data_type = "DAT_SPO2_DATA"
                o2_saturate_info = arr[2]
                pulse_rate = self.join_hex(arr[3], arr[4])
                o2_saturate_data = arr[5]

                self.set_spo2_rate(str(pulse_rate))
                self.set_spo2_data(str(o2_saturate_data))

        if arr[0] == 0x14:
            if arr[1] == 0x02:
                data_type = "DAT_NBP_CUFPRE"
                cuff_pressure = self.join_hex(arr[2], arr[3])
                cuff_type_error = arr[4]
                measure_type = arr[5]

                self.set_cuff_pressure(str(cuff_pressure))
                if measure_type == 0x01:
                    self.set_nbp_method("Manual")

            if arr[1] == 0x03:
                data_type = "DAT_NBP_END"
                measure_type = arr[2]

                if measure_type == 0x01:
                    self.set_nbp_method("Manual")

            if arr[1] == 0x04:
                data_type = "DAT_NBP_RSLT1"
                systolic_pressure = self.join_hex(arr[2], arr[3])
                diastolic_pressure = self.join_hex(arr[4], arr[5])
                mean_pressure = self.join_hex(arr[6], arr[7])

                pressure = str(systolic_pressure) + r"/" + str(diastolic_pressure)
                self.set_pressure(pressure)
                self.set_mean_pressure(str(mean_pressure))

            if arr[1] == 0x05:
                data_type = "DAT_NBP_RSLT2"
                pulse_rate = self.join_hex(arr[2], arr[3])

                self.set_nbp_rate(str(pulse_rate))

        self.count += 1
        if self.count >= self.data_count:
            self.timer.stop()
            self.count = 0
            tk.messagebox.showinfo('Message', "Data Processing Complete!")

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
            self.data_count = len(self.pct_data)
            self.timer.start(10)

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
