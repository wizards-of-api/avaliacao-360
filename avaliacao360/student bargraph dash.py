from PyQt5 import QtWidgets, QtCore,QtGui
import pyqtgraph as pg
import numpy as np
import sys

app = QtWidgets.QApplication(sys.argv)

main_window = QtWidgets.QWidget()
#main_window.resize(800, 600)  # Define o tamanho da janela
main_window.setWindowTitle("WIZARDS OF API")


plot_widget = pg.PlotWidget()

layout = QtWidgets.QVBoxLayout()
layout.addWidget(plot_widget)
main_window.setLayout(layout)
plot_widget.setBackground('lightGray')




# Dados dos aspectos avaliados e suas notas
aspectos_nomes = ['Comunicação', 'Contribuição', 'Autoconhecimento', 'Conhecimento\n Técnico', 'Pontualidade', 'Autogestão']
aspectos = {'Comunicação': 0, 'Contribuição': 1, 'Autoconhecimento': 2, 'Conhecimento\n Técnico': 3, 'Pontualidade': 4, 'Autogestão': 5}
notas = [3, 4, 2, 4, 5, 4]

# Converter nomes dos aspectos em valores numéricos
x = np.array(list(map(lambda aspecto: aspectos[aspecto], aspectos_nomes)))
y = np.array(notas)

# Calcular a média de cada aspecto
medias = [4, 3, 3, 4, 3, 4]

# Definir as cores para cada barra
cores = ['r', 'g', 'b', 'y', 'm', 'c'][:len(x)]
cor_media = 'w'

# Criar o gráfico de barras com as cores definidas
bar_item = pg.BarGraphItem(x=x, height=y, width=0.6, brushes=cores)
plot_widget.addItem(bar_item)

# Criar o gráfico de barras cinzas para as médias
media_item = pg.BarGraphItem(x=x + 2, height=medias, width=0.6, brushes=cor_media)
plot_widget.addItem(media_item)

plot_widget.setTitle("Notas Ana",color='black',  size='20pt')
plot_widget.setLabel('left', '<font color="black" size="5">Nota</font>')
plot_widget.setLabel('bottom', '<font color="black" size="5">Aspectos Avaliados</font>')
plot_widget.setMouseEnabled(x=False, y=False)

# Definir o fundo branco
plot_widget.setBackground('lightgray')

main_window.show()

sys.exit(app.exec_())
