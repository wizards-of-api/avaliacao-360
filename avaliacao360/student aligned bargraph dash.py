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


# Criando um plot de barras
plot = win.addPlot(title="Avaliação Individual por Quesito",)
plot.setTitle("Avaliação Individual por Quesito", color='black', size='20pt')



# Definindo a posição e largura das barras
pos = np.arange(len(data))
width = 0.4

# Criando as barras principais
main_bars = pg.BarGraphItem(x=pos, height=data, width=width, brush='b')

# Criando as barras deslocadas
offset = width/2
offset_bars = pg.BarGraphItem(x=pos+offset, height=data/2, width=width, brush='r')

# Adicionando as barras ao plot
plot.addItem(main_bars)
plot.addItem(offset_bars)

# Configurando os eixos
plot.setXRange(-0.5, len(data)-0.5)
plot.setYRange(0, max(data)*1.1)
plot.setLabel('left', 'Notas', color='black')
plot.setLabel('bottom', 'Quesitos', color='black')
plot.setMouseEnabled(x=False, y=False)

 # Adicionando as legendas
for i in range(len(data)):
    x = pos[i]  # posição x da barra
    y = data[i]  # altura da barra
    text = pg.TextItem(text=f'Barra {i+1}', anchor=(0.5, 1))
    text.setPos(x, y)
    plot.addItem(text)

# Exibindo a janela
sys.exit(app.exec_())
