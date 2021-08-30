from qt_core import *

class new_maquinas():
    def __init__(self,parent,qtd):
        self.parent_layout = QVBoxLayout(parent)
        self.parent_layout.setSpacing(10)

        self.content = [0]*qtd


        for x in range(qtd):
            self.content[x] = QFrame()
            self.content[x].setStyleSheet("background-color:rgb(200,80,80)")
            self.content[x].setMinimumHeight(80)
            self.content[x].setMaximumHeight(80)
            self.parent_layout.addWidget(self.content[x])


        