from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, student_name, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.student_name = student_name
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        sprint = [1, 2, 3, 4]
        ana = [22, 19, 23, 28]
        media_sprint = [20, 25, 21, 23]

        self.graphWidget.setBackground('lightGray')
        self.graphWidget.setTitle("Media das Sprints x \n{}".format(self.student_name), color="k", size="20pt")
        styles = {"color": "b", "font-size": "20px"}
        self.graphWidget.setLabel("left", "Nota do Aluno\n por Sprint", **styles)
        self.graphWidget.setLabel("bottom", "Sprints", **styles)
        self.graphWidget.addLegend()
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.setXRange(0, 6)
        self.graphWidget.setYRange(0, 30)
        ticks = [ (i, str(i)) for i in range(0, 31, 2) ]
        self.graphWidget.getAxis('left').setTicks([ticks])
        self.graphWidget.setMouseEnabled(x=False, y=False)
        self.setWindowTitle('WIZARDS OF API')

        self.plot(sprint, ana, "{} ".format(self.student_name), 'r')
        self.plot(sprint, media_sprint, "Media da Sprint", 'b')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.graphWidget)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color, width=8)
        self.graphWidget.plot(x, y, name=plotname, pen=pen,)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow("Ana")
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
