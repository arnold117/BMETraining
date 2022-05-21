import QtQuick 2.11
import QtQuick.Window 2.11
import QtQuick.Controls 2.4
import QtCharts 2.0

ApplicationWindow {
    id:root
    title:qsTr("Arnold's ParamMonitor")
    visible: true
    width: 800
    height: 480

    property int timer: 0

    background: Rectangle{
        color: "#4d4747"
        anchors.fill: parent
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

    Text {
        id: info
        color: "#cfcdcd"
        text: qsTr("LED Control")
        anchors{
            horizontalCenter: parent.horizontalCenter
            top: parent.top
            topMargin: 40
        }

        font.bold: true
        font.pointSize: 26
    }

    Item {
        id: contains
        anchors{
            left: parent.left
            top:parent.top
            leftMargin: 260
            topMargin: 150
        }

        Rectangle{
            id:  ledOn
            color: "#3061e0"
            radius: 20
            width: 140
            height: 40
            Text {
                id:txOn
                color: "#dbdbdb"
                text: qsTr("On")
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 32
                font.bold: true
                anchors.horizontalCenter: parent.horizontalCenter

            }
            anchors{
                top: stateOn.bottom
                topMargin: 30
                horizontalCenter: stateOn.horizontalCenter
            }

            MouseArea{
                anchors.fill: parent
                onPressed: {
                    ledOn.color = "#f0f0f0"
                }
                onReleased: {
                    ledOn.color = "#3061e0"
                }
                onClicked: {
                    _Control.ledOn();
                }
            }
        }

    }

    ChartView {
        id: waveChartView
        x: 22
        y: 36
        width: 591
        height: 264
        antialiasing: true
        backgroundColor: "#9917719b"
        animationOptions: ChartView.SeriesAnimations
        legend.visible:false

        ValueAxis {
             id: myAxisX
             min: 0
             max: 10>timer? 10:timer+1
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

    Timer{
        interval: 100
        running: true
        repeat: true
        onTriggered: {
            lineSeries.append(timer,Math.random()*50)
            timer = timer+1
        }
    }
}
