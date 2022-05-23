import QtQuick 2.11
import QtQuick.Window 2.11
import QtQuick.Controls 2.4
import QtCharts 2.0

ApplicationWindow {
    id:root
    title:qsTr("Arnold's ParamMonitor")
    visible: true
    width: 1280
    height: 740

    property int count : 0

    menuBar: MenuBar{
        Menu {
            title: "File";
            MenuItem{
                text: "Open CSV File"
                onTriggered: {
                    _Control.open_file();
                }
            }
            MenuItem{
                text: "Save File"
                onTriggered: _Control.save_file()
            }
            MenuItem{
                text: "Exit"
                onTriggered: Qt.exit(0)
            }
        }
        Menu {
            title: "Serial";
            MenuItem {
                text: "Open Serial Configuration"
                onTriggered: root.openSerialConfig()
            }
        }
        Menu {
            title: "Help";
            MenuItem{
                text: "About";
                onTriggered: _Control.about_page()
            }
            MenuItem{
                text: "Website";
                onTriggered: Qt.openUrlExternally("https://dotponder.github.io/");
            }
        }
    }



    Connections {
        target: _Control

        // Signal Handler
        onEcg1WaveRes: {
            _Control.update_ecg1_series(ecg1Series)
        }

        onEcg2WaveRes: {
            _Control.update_ecg2_series(ecg2Series)
        }

        onRaStatusRes: {
            raStauts.text = getRaStatus
        }

        onLaStatusRes: {
            laStauts.text = getLaStatus
        }

        onLlStatusRes: {
            llStauts.text = getLlStatus
        }

        onVStatusRes: {
            vStauts.text = getVStatus
        }

        onHeartRateRes: {
            heartRate.text = getHeartRate
        }


        onRespirationWaveRes: {
            _Control.update_respiration_series(respSeries)
        }

        onRespirationRateRes: {
            respRate.text = getRespirationRate
        }


        onTempSen1Res: {
            tempSen1.text = getTempSen1
        }

        onTempSen2Res: {
            tempSen2.text = getTempSen2
        }

        onTemp1Res: {
            tempC1.text = getT1
        }

        onTemp2Res: {
            tempC2.text = getT2
        }


        onSpo2WaveRes: {
            _Control.update_spo2_series(spo2Series)
        }

        onFingerInfoRes: {
            fingerInfo.text = getFingerInfo
        }

        onProbeInfoRes: {
            probeInfo.text = getProbeInfo
        }

        onSpo2RateRes: {
            spo2Rate.text = getSpo2Rate
        }

        onSpo2DataRes: {
            spo2Data.text = getSpo2Data
        }


        onCuffPressureRes: {
            cuffPreasure.text = getCuffPressure
        }

        onNbpMethodRes: {
            nbpMethod.text = getNbpMethod
        }

        onPressureRes: {
            pressure.text = getPressure
        }

        onMeanPressureRes: {
            meanPressure.text = getMeanPressure
        }

        onNbpRateRes: {
            nbpRate.text = getNbpRate
        }
    }

    Rectangle {
        id: ecgRect1
        x: 37
        y: 30
        width: 951
        height: 145
        color: "#ffffff"

        ChartView {
            id: ecgChart1
            anchors.fill: parent
            antialiasing: true
            backgroundColor: "#9917719b"
            legend{
                visible: false
            }

            ValueAxis {
                id: ecg1AxisX
                min: 0
                max: 1000
                tickCount: 11
                labelsColor: "#ffffff"
                labelsFont.pointSize: 13
                labelsFont.bold: true
                labelFormat: '%d'
                }
            ValueAxis{
                id: ecg1AxisY
                min: 1500
                max: 3000
                tickCount: 6
                labelsColor: "#ffffff"
                labelsFont.pointSize: 13
                labelsFont.bold: true
                labelFormat: '%d'
            }

            LineSeries {
                id: ecg1Series
                axisX: ecg1AxisX
                axisY: ecg1AxisY
                name: "LineSeries"
                color: "#00ffff"
                width: 3
            }
        }
    }

    Rectangle {
        id: ecgRect2
        x: 37
        y: 202
        width: 951
        height: 145
        color: "#ffffff"

        ChartView {
            id: ecgChart2
            anchors.fill: parent
            antialiasing: true
            backgroundColor: "#9917719b"
            legend{
                visible: false
            }

            ValueAxis {
                id: ecg2AxisX
                min: 0
                max: 1000
                tickCount: 11
                labelsColor: "#ffffff"
                labelsFont.pointSize: 13
                labelsFont.bold: true
                labelFormat: '%d'
                }
            ValueAxis{
                id: ecg2AxisY
                min: 1500
                max: 3000
                tickCount: 6
                labelsColor: "#ffffff"
                labelsFont.pointSize: 13
                labelsFont.bold: true
                labelFormat: '%d'
            }

            LineSeries {
                id: ecg2Series
                axisX: ecg2AxisX
                axisY: ecg2AxisY
                name: "LineSeries"
                color: "#00ffff"
                width: 3
            }
        }
    }

    Rectangle {
        id: spo2Rect
        x: 40
        y: 375
        width: 948
        height: 155
        color: "#ffffff"

        ChartView {
            id: spo2Chart
            anchors.fill: parent
            antialiasing: true
            backgroundColor: "#9917719b"
            legend{
                visible: false
            }

            ValueAxis {
                id: spo2AxisX
                min: 0
                max: 1000
                tickCount: 11
                labelsColor: "#ffffff"
                labelsFont.pointSize: 13
                labelsFont.bold: true
                labelFormat: '%d'
                }
            ValueAxis{
                id: spo2AxisY
                min:45
                max:200
                tickCount: 6
                labelsColor: "#ffffff"
                labelsFont.pointSize: 13
                labelsFont.bold: true
                labelFormat: '%d'
            }

            LineSeries {
                id: spo2Series
                axisX: spo2AxisX
                axisY: spo2AxisY
                name: "LineSeries"
                color: "#00ffff"
                width: 3
            }
        }
    }

    Rectangle {
        id: respRect
        x: 37
        y: 549
        width: 951
        height: 155
        color: "#ffffff"

        ChartView {
            id: respChart
            anchors.fill: parent
            antialiasing: true
            backgroundColor: "#9917719b"
            legend{
                visible: false
            }

            ValueAxis {
                id: respAxisX
                min: 0
                max: 1000
                tickCount: 11
                labelsColor: "#ffffff"
                labelsFont.pointSize: 13
                labelsFont.bold: true
                labelFormat: '%d'
                }
            ValueAxis{
                id: respAxisY
                min: 50
                max: 200
                tickCount: 6
                labelsColor: "#ffffff"
                labelsFont.pointSize: 13
                labelsFont.bold: true
                labelFormat: '%d'
            }

            LineSeries {
                id: respSeries
                axisX: respAxisX
                axisY: respAxisY
                name: "LineSeries"
                color: "#00ffff"
                width: 3
            }
        }
    }

    Rectangle {
        id: ecgArea
        x: 1028
        y: 30
        width: 212
        height: 165
        color: "#ffffff"

        Text {
            id: element
            x: 0
            y: 0
            width: 64
            height: 38
            text: qsTr("Heart Rate")
            font.pixelSize: 12
        }

        Text {
            id: element1
            x: 152
            y: 0
            width: 60
            height: 38
            text: qsTr("bpm")
            font.pixelSize: 12
        }

        Text {
            id: raStauts
            x: 0
            y: 38
            width: 35
            height: 23
            text: qsTr("Offline")
            font.pixelSize: 12
        }

        Text {
            id: laStatus
            x: 0
            y: 77
            width: 35
            height: 29
            text: qsTr("Offline")
            font.pixelSize: 12
        }

        Text {
            id: vStatus
            x: 70
            y: 120
            width: 38
            height: 29
            text: qsTr("Offline")
            font.pixelSize: 12
        }

        Text {
            id: heartRate
            x: 152
            y: 44
            width: 52
            height: 27
            text: "--"
            font.pixelSize: 12
        }
        Text {
            id: llStatus
            x: 0
            y: 120
            width: 35
            height: 33
            text: qsTr("Offline")
            font.pixelSize: 12
        }
    }

    Rectangle {
        id: nbpArea
        x: 1028
        y: 202
        width: 212
        height: 165
        color: "#ffffff"

        Text {
            id: nbpRate
            x: 72
            y: 130
            width: 82
            height: 35
            text: qsTr("--")
            font.pixelSize: 12
        }

        Text {
            id: pressure
            x: 3
            y: 88
            width: 209
            height: 30
            text: qsTr("--/--")
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: 12
        }

        Text {
            id: meanPressure
            x: 118
            y: 41
            width: 86
            height: 41
            text: qsTr("--")
            horizontalAlignment: Text.AlignRight
            font.pixelSize: 12
        }

        Text {
            id: element6
            x: 3
            y: 0
            width: 209
            height: 35
            text: qsTr("Non-Invasive Blood Pressure  mmgh")
            font.pixelSize: 12
        }

        Text {
            id: nbpMethod
            x: 5
            y: 130
            width: 63
            height: 35
            text: qsTr("Manual")
            font.pixelSize: 12
        }

        Text {
            id: element9
            x: 165
            y: 133
            width: 47
            height: 32
            text: qsTr("bpm")
            font.pixelSize: 12
        }
        Text {
            id: cuffPreasure
            x: 3
            y: 41
            width: 95
            height: 41
            text: "--"
            font.pixelSize: 12
        }
    }

    Rectangle {
        id: spo2Area
        x: 1028
        y: 373
        width: 212
        height: 165
        color: "#ffffff"

        Text {
            id: spo2Rate
            x: 77
            y: 52
            width: 77
            height: 48
            text: qsTr("--")
            font.pixelSize: 12
        }

        Text {
            id: element11
            x: 100
            y: 1
            width: 112
            height: 45
            text: qsTr("Pulse Rate")
            font.pixelSize: 12
        }

        Text {
            id: element10
            x: 0
            y: 0
            width: 94
            height: 46
            text: qsTr("SpO2")
            font.pixelSize: 12
        }

        Text {
            id: spo2Data
            x: 0
            y: 52
            width: 64
            height: 48
            text: qsTr("--")
            font.pixelSize: 12
        }

        Text {
            id: fingerInfo
            x: 0
            y: 120
            width: 94
            height: 45
            text: qsTr("Finger Offline")
            font.pixelSize: 12
        }

        Text {
            id: probeInfo
            x: 100
            y: 120
            width: 112
            height: 45
            text: qsTr("Probe Offline")
            font.pixelSize: 12
        }

        Text {
            id: element14
            x: 153
            y: 52
            width: 59
            height: 48
            text: qsTr("bpm")
            font.pixelSize: 12
        }

        Text {
            id: element19
            x: 35
            y: 52
            width: 29
            height: 19
            text: qsTr("%")
            font.pixelSize: 12
        }
    }
    Rectangle {
        id: respTempArea
        x: 1028
        y: 544
        width: 212
        height: 165
        color: "#ffffff"

        Text {
            id: element15
            x: 0
            y: 0
            width: 87
            height: 28
            text: qsTr("Respiration")
            font.pixelSize: 12
        }

        Text {
            id: respRate
            x: 0
            y: 43
            width: 34
            height: 73
            text: qsTr("--")
            horizontalAlignment: Text.AlignLeft
            verticalAlignment: Text.AlignVCenter
            font.pixelSize: 12
        }

        Text {
            id: element16
            x: 93
            y: 0
            width: 111
            height: 28
            text: qsTr("Temperature ℃")
            font.pixelSize: 12
        }

        Text {
            id: element17
            x: 93
            y: 34
            width: 56
            height: 24
            text: qsTr("T1:")
            font.pixelSize: 12
        }

        Text {
            id: tempC1
            x: 155
            y: 34
            width: 57
            height: 24
            text: qsTr("--")
            font.pixelSize: 12
        }

        Text {
            id: element18
            x: 93
            y: 64
            width: 56
            height: 24
            text: qsTr("T2:")
            font.pixelSize: 12
        }

        Text {
            id: tempC2
            x: 155
            y: 64
            width: 58
            height: 24
            text: qsTr("--")
            font.pixelSize: 12
        }

        Text {
            id: tempSen1
            x: 98
            y: 92
            width: 66
            height: 29
            text: qsTr("T1 Disconnected")
            font.pixelSize: 12
        }

        Text {
            id: tempSen2
            x: 98
            y: 119
            width: 66
            height: 38
            text: qsTr("T2 Disconnected")
            font.pixelSize: 12
        }

        Text {
            id: element7
            x: 40
            y: 73
            width: 40
            height: 25
            text: qsTr("bpm")
            font.pixelSize: 12
        }
    }

    Text {
        id: element21
        x: 37
        y: 12
        width: 36
        height: 14
        text: qsTr("ECG1")
        font.pixelSize: 12
    }

    Text {
        id: element22
        x: 36
        y: 185
        width: 43
        height: 16
        text: qsTr("ECG2")
        font.pixelSize: 12
    }

    Text {
        id: element24
        x: 39
        y: 356
        width: 34
        height: 18
        text: qsTr("SPO2")
        font.pixelSize: 12
    }

    Text {
        id: element25
        x: 36
        y: 534
        width: 67
        height: 14
        text: qsTr("Res2")
        font.pixelSize: 12
    }
}
