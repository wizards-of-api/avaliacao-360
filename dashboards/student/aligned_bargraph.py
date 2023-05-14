from PyQt5 import QtWidgets, QtCore, QtGui
import pyqtgraph as pg
import numpy as np
import random
import sys 

# Definindo dados para as barras
#Dados dos aspectos avaliados e suas notas

data = np.array([4,3,2,4,2,3])

# Criando o aplicativo e a janela
app = QtWidgets.QApplication(sys.argv)
win = pg.GraphicsLayoutWidget(show=True)
win.setWindowTitle('WIZARDS OF API')
win.resize(800, 600)
win.setBackground('lightgray') # define o fundo do grafico

# Criando um individual de barras
individual = win.addPlot(title="Avaliação Individual por Quesito",)
individual.setTitle("Avaliação Individual por Quesito", color='black', size='20pt')


# Definindo a posição e largura das barras
pos = np.arange(len(data))
width = 0.4

# Criando as barras principais
main_bars = pg.BarGraphItem(x=pos, height=data, width=width, brush='b')

# Criando as barras deslocadas
offset = width/2
offset_bars = pg.BarGraphItem(x=pos+offset, height=data/2, width=width, brush='r')

# Adicionando as barras ao individual
individual.addItem(main_bars)
individual.addItem(offset_bars)

# Configurando os eixos
individual.setXRange(-0.5, len(data)-0.5)
individual.setYRange(0, max(data)*1.1)
individual.setLabel('left', 'Notas', color='black')
individual.setLabel('bottom', 'Quesitos', color='black')
individual.setMouseEnabled(x=False, y=False)

 # Adicionando as legendas
for i in range(len(data)):
    x = pos[i]  # posição x da barra
    y = data[i]  # altura da barra
    text = pg.TextItem(text=f'Barra {i+1}', anchor=(0.5, 1))
    text.setPos(x, y)
    individual.addItem(text)

plot_widget = pg.PlotWidget()

layout = QtWidgets.QVBoxLayout()
layout.addWidget(plot_widget)
win.setLayout(layout)
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

# Exibindo a janela
sys.exit(app.exec_())
