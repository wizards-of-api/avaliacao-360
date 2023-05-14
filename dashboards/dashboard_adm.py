from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget
from PyQt5.QtChart import (QChart, QChartView, QBarSet, QBarSeries, QLineSeries, QPieSeries, QBarCategoryAxis)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Cria os dados para o gráfico de barras e linhas
        bar_set1 = QBarSet("Fatores")
        bar_set1.append([5, 5, 4, 3, 4])
        bar_series1 = QBarSeries()
        bar_series1.append(bar_set1)

        line_series1 = QLineSeries()
        x_data = [1, 2, 3, 4, 5]
        y_data = [3.8, 3.8, 3.8, 3.8, 3.8]
        for x, y in zip(x_data, y_data):
            line_series1.append(x, y)

        # Cria o gráfico de barras e linhas
        bar_line_chart1 = QChart()
        bar_line_chart1.addSeries(bar_series1)
        bar_line_chart1.addSeries(line_series1)
        bar_line_chart1.createDefaultAxes()
        bar_line_chart1.setTitle("<b>Desempenho Médio por Fator</b>")
        bar_line_chart1.setTitleFont(QFont("Arial", weight=QFont.Bold))

        # Define as categorias do eixo X do gráfico bar_series1
        categories_bar1 = ["Comunicação", "Colaboração", "Autogestão", "Entregas", "Competência"]
        axisX_bar1 = QBarCategoryAxis()
        axisX_bar1.append(categories_bar1)
        bar_line_chart1.setAxisX(axisX_bar1, bar_series1)

        # Oculta os valores de x_data no gráfico line_series1
        axisX_line1 = QBarCategoryAxis()
        axisX_line1.setVisible(False)
        bar_line_chart1.setAxisX(axisX_line1, line_series1)

        # Adiciona a legenda para a linha
        bar_line_chart1.legend().setVisible(True)
        bar_line_chart1.legend().setAlignment(Qt.AlignBottom)
        bar_line_chart1.legend().markers(line_series1)[0].setLabel("Média")

        # Cria a visualização do gráfico de barras e linhas
        bar_line_chart_view1 = QChartView(bar_line_chart1)

        # Cria os dados para o gráfico de barras e linhas
        bar_set2 = QBarSet("Grupos")
        bar_set2.append([5, 4, 5, 3, 2])
        bar_series2 = QBarSeries()
        bar_series2.append(bar_set2)

        line_series2 = QLineSeries()
        x_data = [1, 2, 3, 4, 5]
        y_data = [3.8, 3.8, 3.8, 3.8, 3.8]
        for x, y in zip(x_data, y_data):
            line_series2.append(x, y)

        # Cria o gráfico de barras e linhas
        # Cria o gráfico de barras e linhas
        bar_line_chart2 = QChart()
        bar_line_chart2.addSeries(bar_series2)
        bar_line_chart2.addSeries(line_series2)
        bar_line_chart2.createDefaultAxes()
        bar_line_chart2.setTitle("<b>Desempenho por Grupo</b>")
        bar_line_chart2.setTitleFont(QFont("Arial", weight=QFont.Bold))

        # Define as categorias do eixo X do gráfico bar_series2
        categories_bar2 = [
            "Wizards API",
            "BDmasters",
            "Sabha3+",
            "MoisesGroup",
            "DataFuture",
        ]
        axisX_bar2 = QBarCategoryAxis()
        axisX_bar2.append(categories_bar2)
        bar_line_chart2.setAxisX(axisX_bar2, bar_series2)

        # Adiciona a legenda para a linha
        bar_line_chart2.legend().setVisible(True)
        bar_line_chart2.legend().setAlignment(Qt.AlignBottom)
        bar_line_chart2.legend().markers(line_series2)[0].setLabel("Média")

        # Oculta os valores de x_data no gráfico line_series2
        axisX_line2 = QBarCategoryAxis()
        axisX_line2.setVisible(False)
        bar_line_chart2.setAxisX(axisX_line2, line_series2)

        # Cria a visualização do gráfico de barras e linhas
        bar_line_chart_view2 = QChartView(bar_line_chart2)

        # Cria os dados para o gráfico de pizza
        pie_series = QPieSeries()
        pie_series.append("Avaliações pendentes", 150)
        pie_series.append("Avaliações concluídas", 110)

        # Cria o gráfico de pizza
        pie_chart = QChart()
        pie_chart.addSeries(pie_series)
        pie_chart.setTitle("<b>Quantidades de Respostas</b>")
        pie_chart.setTitleFont(QFont("Arial", weight=QFont.Bold))

        # Cria a visualização do gráfico de pizza
        pie_chart_view = QChartView(pie_chart)

        # Cria o layout e o widget central
        layout = QGridLayout()
        layout.addWidget(bar_line_chart_view1, 0, 1)
        layout.addWidget(pie_chart_view, 0, 0)
        layout.addWidget(bar_line_chart_view2, 1, 0, 1, 2)  # Adicionei a visualização do gráfico de barras e linhas ocupando duas colunas

        central_widget = QWidget()
        central_widget.setLayout(layout)

        # Define o widget central da janela principal
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

