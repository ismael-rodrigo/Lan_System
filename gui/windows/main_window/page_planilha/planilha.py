




from PySide6.QtWidgets import QFrame
from qt_core import *

class colunas():
    def __init__(self,parent ,qtd = 10):
        self.font = QFont()
        self.font.setFamilies([u"Bahnschrift Light"])
        self.font.setPointSize(12)

        self.parent = parent

        self.qtd = qtd
        self.new_content =        [0]*qtd
        self.user_content =       [0]*qtd
        self.tempo_content =      [0]*qtd
        self.maquina_content =    [0]*qtd
        self.game_content =       [0]*qtd
        self.preco_content =      [0]*qtd
        self.new_content_layout = [0]*qtd 
    

    def new_frame(self):


        for x in range(self.qtd):

            self.new_content[x] = QFrame()
            self.new_content[x].setMinimumHeight(50)
            self.new_content[x].setMaximumHeight(50)
            self.new_content[x].setStyleSheet("border-bottom:2px solid rgb(100,100,100)")
        
            
            self.user_content[x] = QLabel()
            self.user_content[x].setMinimumHeight(50)
            self.user_content[x].setFont(self.font)
            self.user_content[x].setStyleSheet("border-right:1px solid rgb(100,100,100)")


            self.tempo_content[x] = QLabel()
            self.tempo_content[x].setMinimumHeight(50)
            self.tempo_content[x].setText("TEMPO :") 
            self.tempo_content[x].setAlignment(Qt.AlignCenter)
            self.tempo_content[x].setFont(self.font)
            self.tempo_content[x].setStyleSheet("border-right:1px solid rgb(100,100,100)")       


            self.maquina_content[x] = QLabel()
            self.maquina_content[x].setMinimumHeight(50)
            self.maquina_content[x].setText("Maquina in game")
            self.maquina_content[x].setAlignment(Qt.AlignCenter)
            self.maquina_content[x].setFont(self.font)
            self.maquina_content[x].setStyleSheet("border-right:1px solid rgb(100,100,100)")


            self.game_content[x] = QLabel()
            self.game_content[x].setMinimumHeight(50)
            self.game_content[x].setMaximumWidth(250)
            self.game_content[x].setText("game ")
            self.game_content[x].setAlignment(Qt.AlignCenter)
            self.game_content[x].setFont(self.font)
            self.game_content[x].setStyleSheet("border-right:1px solid rgb(100,100,100)")


            self.preco_content[x] = QLabel()
            self.preco_content[x].setMinimumHeight(50)
            self.preco_content[x].setMaximumWidth(100)
            self.preco_content[x].setText("Price")
            self.preco_content[x].setAlignment(Qt.AlignCenter)
            self.preco_content[x].setFont(self.font)
            self.preco_content[x].setStyleSheet("border-right:1px solid rgb(100,100,100)")


            self.new_content_layout[x] = QHBoxLayout(self.new_content[x])
            self.new_content_layout[x].setSpacing(0)
            self.new_content_layout[x].setContentsMargins(0,0,0,0)

            self.new_content_layout[x].addWidget(self.user_content[x])
            self.new_content_layout[x].addWidget(self.tempo_content[x])
            self.new_content_layout[x].addWidget(self.maquina_content[x])
            self.new_content_layout[x].addWidget(self.game_content[x])
            self.new_content_layout[x].addWidget(self.preco_content[x])
            self.parent.addWidget(self.new_content[x])


            self.new_content[x].hide()
