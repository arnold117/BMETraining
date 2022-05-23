import QtQuick 2.12
import QtQuick.Controls 2.12
import QtCharts 2.2

ApplicationWindow {
    id: root
    visible: true
    width: 640
    height: 500
    menuBar: MenuBar {
        Menu {
            title: "File"
            MenuItem {
                text: "Start"
                onTriggered: {
                    timer.running = true
                }
            }
            MenuItem {
                text: "Stop"
                onTriggered: {
                    timer.running = false
                }
            }
            MenuItem {
                text: "Change Text"
                onTriggered: {
                    dataModel.change_text("fuck")
                }
            }
        }
    }
    Timer {
        id: timer
        interval: 500; running: false; repeat: true
        onTriggered: dataModel.update_serie(serie)
    }
    
    ChartView {
        anchors.fill: parent
        id: bscan0
        ValueAxis {
            id: axisx
            min: 0
            max: 10
        }
        ValueAxis {
            id: axisy
            min: -100
            max: 100
        }
        LineSeries{
            id: serie
            name: "Test"
            axisX: axisx
            axisY: axisy
        }
    }

    Text {
        id: text
        x: 260
        y: 22
        width: 80
        height: 20
        text: qsTr("Text Edit")
        font.pixelSize: 12
    }

    Connections {
        target: dataModel

        // Signal Handler
        onTextRes: {
            // textLabel - was given through arguments=['textLabel']
            text.text = textLabel
        }
        onSerRes: {
            text.text = qsTr("Transmitting")
        }
    }
}
