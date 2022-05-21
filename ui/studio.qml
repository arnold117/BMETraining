import QtQuick 2.11
import QtQuick.Window 2.11
import QtQuick.Controls 2.4
import QtCharts 2.0
// TODO: Add GUI!

ApplicationWindow {
    id:root
    title:qsTr("Arnold's ParamMonitor")
    visible: true
    width: 850
    height: 480

    //property int timer: 0

    background: Rectangle{
        color: "#4d4747"
    }

     menuBar: MenuBar{
        Menu {
            title: "File";
            MenuItem{
                text: "Open CSV File";
                onTriggered: _Control.open_file();
            }
            MenuItem{
                text: "Save File";
                onTriggered: _Control.save_file();
            }
            MenuItem{
                text: "Exit";
                onTriggered: Qt.exit(0);
            }
        }
        Menu {
            title: "Help";
            MenuItem{
                text: "Website";
                onTriggered: Qt.openUrlExternally("https://dotponder.github.io/");
            }
        }
    }

    Rectangle {
        id: rectangle5
        x: 37
        y: 30
        width: 591
        height: 87
        color: "#ffffff"

        ChartView {
            id: waveChartView1
            anchors.fill: parent
            antialiasing: true
            backgroundColor: "#9917719b"
            animationOptions: ChartView.SeriesAnimations
            legend{
                visible: false
            }

            ValueAxis {
                id: myAxisX1
                min: 0
                max: 10
                tickCount: 11
                labelsColor: "#ffffff"
                labelsFont.pointSize: 13
                labelsFont.bold: true
                labelFormat: '%d'
                }
            ValueAxis{
                id:myAxisY1
                min:0
                max:300
                tickCount: 6
                labelsColor: "#ffffff"
                labelsFont.pointSize: 13
                labelsFont.bold: true
                labelFormat: '%d'
            }

            LineSeries {
                id:lineSeries1
                axisX: myAxisX1
                axisY: myAxisY1
                name: "LineSeries"
                color: "#00ffff"
                width: 3
            }
        }
    }

    Rectangle {
        id: rectangle6
        x: 37
        y: 145
        width: 591
        height: 87
        color: "#ffffff"

        ChartView {
            id: waveChartView
            anchors.fill: parent
            antialiasing: true
            backgroundColor: "#9917719b"
            animationOptions: ChartView.SeriesAnimations
            legend{
                visible: false
            }

            ValueAxis {
                id: myAxisX
                min: 0
                max: 10
                tickCount: 11
                labelsColor: "#ffffff"
                labelsFont.pointSize: 13
                labelsFont.bold: true
                labelFormat: '%d'
                }
            ValueAxis{
                id:myAxisY
                min:0
                max:300
                tickCount: 6
                labelsColor: "#ffffff"
                labelsFont.pointSize: 13
                labelsFont.bold: true
                labelFormat: '%d'
            }

            LineSeries {
                id:lineSeries
                axisX: myAxisX
                axisY: myAxisY
                name: "LineSeries"
                color: "#00ffff"
                width: 3
            }
        }
    }
    Rectangle {
        id: rectangle7
        x: 37
        y: 250
        width: 591
        height: 87
        color: "#ffffff"

        ChartView {
            id: waveChartView2
            anchors.fill: parent
            antialiasing: true
            backgroundColor: "#9917719b"
            animationOptions: ChartView.SeriesAnimations
            legend{
                visible: false
            }

            ValueAxis {
                id: myAxisX2
                min: 0
                max: 10
                tickCount: 11
                labelsColor: "#ffffff"
                labelsFont.pointSize: 13
                labelsFont.bold: true
                labelFormat: '%d'
                }
            ValueAxis{
                id:myAxisY2
                min:0
                max:300
                tickCount: 6
                labelsColor: "#ffffff"
                labelsFont.pointSize: 13
                labelsFont.bold: true
                labelFormat: '%d'
            }

            LineSeries {
                id:lineSeries2
                axisX: myAxisX2
                axisY: myAxisY2
                name: "LineSeries"
                color: "#00ffff"
                width: 3
            }
        }
    }

    Rectangle {
        id: rectangle8
        x: 37
        y: 355
        width: 591
        height: 87
        color: "#ffffff"

        ChartView {
            id: waveChartView3
            anchors.fill: parent
            antialiasing: true
            backgroundColor: "#9917719b"
            animationOptions: ChartView.SeriesAnimations
            legend{
                visible: false
            }

            ValueAxis {
                id: myAxisX3
                min: 0
                max: 10
                tickCount: 11
                labelsColor: "#ffffff"
                labelsFont.pointSize: 13
                labelsFont.bold: true
                labelFormat: '%d'
                }
            ValueAxis{
                id:myAxisY3
                min:0
                max:300
                tickCount: 6
                labelsColor: "#ffffff"
                labelsFont.pointSize: 13
                labelsFont.bold: true
                labelFormat: '%d'
            }

            LineSeries {
                id:lineSeries3
                axisX: myAxisX3
                axisY: myAxisY3
                name: "LineSeries"
                color: "#00ffff"
                width: 3
            }
        }
    }

    Rectangle {
        id: rectangle
        x: 656
        y: 27
        width: 120
        height: 87
        color: "#ffffff"

        Text {
            id: element
            x: 0
            y: 0
            text: qsTr("心率")
            font.pixelSize: 12
        }

        Text {
            id: element1
            x: 82
            y: 0
            text: qsTr("bgm")
            font.pixelSize: 12
        }

        Text {
            id: element2
            x: 0
            y: 18
            text: qsTr("RA")
            font.pixelSize: 12
        }

        Text {
            id: element3
            x: 0
            y: 38
            text: qsTr("LA")
            font.pixelSize: 12
        }

        Text {
            id: element5
            x: 32
            y: 58
            text: qsTr("V")
            font.pixelSize: 12
        }

        TextEdit {
            id: textEdit
            x: 76
            y: 18
            width: 24
            height: 20
            text: "Edit"
            font.pixelSize: 12
        }
    }
    Rectangle {
        id: rectangle1
        x: 656
        y: 140
        width: 120
        height: 87
        color: "#ffffff"

        TextEdit {
            id: textEdit2
            x: 70
            y: 17
            width: 30
            height: 20
            text: qsTr("Edit")
            font.pixelSize: 12
        }

        Text {
            id: element8
            x: 0
            y: 75
            text: qsTr("手动")
            font.pixelSize: 12

            TextEdit {
                id: textEdit4
                x: 26
                y: 0
                width: 45
                height: 12
                text: qsTr("Edit")
                font.pixelSize: 12
            }
        }

        Text {
            id: element9
            x: 73
            y: 75
            text: qsTr("bgm")
            font.pixelSize: 12
        }
    }
    Rectangle {
        id: rectangle2
        x: 656
        y: 246
        width: 120
        height: 87
        color: "#ffffff"

        Text {
            id: element10
            x: 0
            y: 0
            text: qsTr("血氧")
            font.pixelSize: 12
        }

        TextEdit {
            id: textEdit6
            x: 46
            y: 23
            width: 24
            height: 20
            text: qsTr("Edit")
            font.pixelSize: 12
        }

        Text {
            id: element12
            x: 0
            y: 67
            text: qsTr("手指链接")
            font.pixelSize: 12
        }

        Text {
            id: element13
            x: 54
            y: 67
            text: qsTr("探头链接")
            font.pixelSize: 12
        }

        Text {
            id: element14
            x: 76
            y: 23
            text: qsTr("bgm")
            font.pixelSize: 12
        }
    }
    Rectangle {
        id: rectangle3
        x: 656
        y: 351
        width: 120
        height: 87
        color: "#ffffff"

        Text {
            id: element15
            x: 0
            y: 0
            text: qsTr("呼吸 bpm")
            font.pixelSize: 12
        }

        TextEdit {
            id: textEdit7
            x: 0
            y: 34
            width: 48
            height: 20
            text: qsTr("Edit")
            font.pixelSize: 12
        }

        Text {
            id: element16
            x: 54
            y: 0
            text: qsTr("体温 ℃")
            font.pixelSize: 12
        }

        Text {
            id: element17
            x: 54
            y: 18
            width: 18
            height: 12
            text: qsTr("T1:")
            font.pixelSize: 12
        }

        TextEdit {
            id: textEdit8
            x: 72
            y: 18
            width: 28
            height: 12
            text: qsTr("Edit")
            font.pixelSize: 12
        }

        Text {
            id: element18
            x: 54
            y: 34
            width: 18
            height: 12
            text: qsTr("T2:")
            font.pixelSize: 12

            TextEdit {
                id: textEdit9
                x: 17
                y: 0
                width: 29
                height: 12
                text: qsTr("Edit")
                font.pixelSize: 12
            }
        }

        Text {
            id: element19
            x: 54
            y: 52
            text: qsTr("T1导联")
            font.pixelSize: 12
        }

        Text {
            id: element20
            x: 54
            y: 70
            text: qsTr("T2导联")
            font.pixelSize: 12
        }
    }

    Text {
        id: element4
        x: 656
        y: 85
        text: qsTr("LL")
        font.pixelSize: 12
    }

    Text {
        id: element6
        x: 656
        y: 140
        text: qsTr("无创血压")
        font.pixelSize: 12
    }

    Text {
        id: element7
        x: 732
        y: 140
        text: qsTr("mmhg")
        font.pixelSize: 12
    }

    TextEdit {
        id: textEdit1
        x: 656
        y: 158
        width: 48
        height: 20
        text: "Edit"
        font.pixelSize: 12

        TextEdit {
            id: textEdit3
            x: 8
            y: 20
            width: 80
            height: 20
            text: qsTr("Text Edit")
            font.pixelSize: 12
        }
    }

    Text {
        id: element11
        x: 711
        y: 246
        text: qsTr("脉率")
        font.pixelSize: 12
    }

    TextEdit {
        id: textEdit5
        x: 656
        y: 269
        width: 29
        height: 20
        text: qsTr("Edit")
        font.pixelSize: 12
    }

    Text {
        id: element21
        x: 37
        y: 14
        text: qsTr("ECG1")
        font.pixelSize: 12
    }

    Text {
        id: element22
        x: 37
        y: 129
        text: qsTr("ECG2")
        font.pixelSize: 12
    }

    Text {
        id: element23
        x: 37
        y: 234
        font.pixelSize: 12
    }

    Text {
        id: element24
        x: 37
        y: 234
        text: qsTr("SPO2")
        font.pixelSize: 12
    }

    Text {
        id: element25
        x: 37
        y: 339
        text: qsTr("Res2")
        font.pixelSize: 12
    }

    Text {
        id: element26
        x: 0
        y: 468
        text: qsTr("串口未配置")
        font.pixelSize: 12
    }
}
