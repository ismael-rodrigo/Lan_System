


from gui.pages.scrol_page.scroll import Ui_Frame
from qt_core import *

from gui.widgets.py_button import PyPushButton

class page_new_client():
    def __init__(self):
        self.font = QFont()
        self.font.setFamilies([u"Bahnschrift Light"])
        self.font.setPointSize(12)


    def create(self,parent,name = "NEW CLIENT",tipo = "B"):
        self.left_menu2_layout = QVBoxLayout(parent)
        self.left_menu2_layout.setContentsMargins(10,2,10,10)
        self.left_menu2_layout.setSpacing(10)

        self.title_new_client = QLabel()
        self.title_new_client.setText(name)
        self.title_new_client.setMinimumHeight(40)
        self.title_new_client.setAlignment(Qt.AlignCenter)
        self.title_new_client.setFont(self.font)

        self.title_new_client.setStyleSheet("""
        color:rgb(200,80,80);
        border-bottom:2px solid rgb(200,80,80)
        """)

        self.style_line = """
        QLineEdit{
            border:2px solid rgb(80,80,80);
            border-radius:10px;
            background-color:rgb(60,60,60);
            padding:7px;
        }
        QLineEdit:hover{
            border:2px solid rgb(110,110,110);
            }
        QLineEdit:focus{
        border:2px solid rgb(200,80,80);
        } 
        """




        self.style = """
    
        QRadioButton{
        color:rgb(30,30,30)
        }
        QRadioButton:hover{
            color:rgb(110,110,110)
        }

        QRadioButton::indicator{
             background-color:rgb(110,110,110);
             border:2px solid rgb(100,100,100);
             
             width:13px;
             height:13px;

             border-radius:7px;
             }

        QRadioButton::indicator:checked{
             background-color:rgb(200,80,80);
             border:2px solid rgb(100,100,100);
             }

        QRadioButton::indicator:hover{
             border:2px solid rgb(140,140,140);
             
             }
        """



        self.nome_new_client = QLineEdit()
        self.nome_new_client.setMinimumHeight(50)
        self.nome_new_client.setPlaceholderText("UserName")
        self.nome_new_client.setStyleSheet(self.style_line)
        self.nome_new_client.setFont(self.font)




        self.tempo_new_client = QLineEdit()
        self.tempo_new_client.setMinimumHeight(50)
        self.tempo_new_client.setPlaceholderText("Tempo (min)")
        self.tempo_new_client.setStyleSheet(self.style_line)
        self.tempo_new_client.setFont(self.font)
        self.tempo_new_client.setMaxLength(4)




        self.preco_new_client = QLineEdit()
        self.preco_new_client.setMinimumHeight(50)
        self.preco_new_client.setPlaceholderText("Preço (R$/hora)")
        self.preco_new_client.setMaxLength(3)

        self.preco_new_client.setStyleSheet(self.style_line)
        self.preco_new_client.setFont(self.font)

        self.frame = QFrame()
        self.frame_layout = QHBoxLayout(self.frame)
        self.frame_layout.setContentsMargins(20,10,0,0)
        self.frame_layout.setSpacing(0)


        self.frame2 = QFrame()
        self.frame2_layout = QVBoxLayout(self.frame2)
        self.frame2_layout.setContentsMargins(50,0,0,0)
        self.frame2_layout.setSpacing(0)





        self.scrollframe = QFrame()
        self.scrollframe.setMinimumHeight(200)


        self.scroll = Ui_Frame()
        self.scroll.setupUi(self.scrollframe)
        self.scroll.scrollArea.setStyleSheet("border:2px solid rgb(90,90,90);border-radius:7px ; ")
        


        self.frame_butt_bottom = QFrame()
        self.frame_butt_layout = QHBoxLayout(self.frame_butt_bottom)


        self.butt_sair = PyPushButton("Sair",icon_path="x.svg")
        self.butt_ok = PyPushButton("Ok",icon_path="check.svg")

        self.frame_butt_layout.addWidget(self.butt_sair)
        self.frame_butt_layout.addWidget(self.butt_ok)








        self.check_1 = QRadioButton()
        self.check_1.setText("Sony")
        self.check_1.setStyleSheet(self.style)
        self.check_1.setFont(self.font)



        self.check_2 = QRadioButton()
        self.check_2.setText("Xbox")
        self.check_2.setStyleSheet(self.style)
        self.check_2.setFont(self.font)


        self.check_3 = QRadioButton()
        self.check_3.setText("Pc")
        self.check_3.setStyleSheet(self.style)
        self.check_3.setFont(self.font)

        self.check_box = QRadioButton()
        
        self.check_box.setCheckable(True)
        self.check_box.setAutoExclusive(False)
        self.check_box.setText("Armazenar horas")
        self.check_box.setStyleSheet(self.style)
        self.check_box.setFont(self.font)


        self.frame_layout.addWidget(self.check_1)
        self.frame_layout.addWidget(self.check_2)
        self.frame_layout.addWidget(self.check_3)


        self.frame2_layout.addWidget(self.check_box)



        self.label_error = QLabel()
        self.label_error.setAlignment(Qt.AlignCenter)
        self.label_error.setFont(self.font)
        self.label_error.setText("*Insira os campos corretamente")
        self.label_error.setStyleSheet("color:rgb(200,80,80);")
        self.label_error.hide()







        self.new_client_spacer = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)
        



        self.left_menu2_layout.addWidget(self.title_new_client)
        self.left_menu2_layout.addWidget(self.nome_new_client)
        self.left_menu2_layout.addWidget(self.tempo_new_client)
        self.left_menu2_layout.addWidget(self.preco_new_client)
        self.left_menu2_layout.addWidget(self.frame)
        self.left_menu2_layout.addWidget(self.frame2)
        self.left_menu2_layout.addWidget(self.scrollframe)
        self.left_menu2_layout.addWidget(self.label_error)
        self.left_menu2_layout.addItem(self.new_client_spacer)

        self.left_menu2_layout.addWidget(self.frame_butt_bottom)




        if tipo == "A":
            self.check_1.hide()
            self.check_2.hide()
            self.check_3.hide()
            self.scrollframe.hide()
        else:
            self.check_box.hide()
