

from gui.windows.main_window.page_maquinas.maquinas import new_maquinas
from gui.windows.main_window.page_planilha.planilha import colunas
from gui.widgets.py_button import PyPushButton
from typing import AsyncIterable, Text

from PySide6 import QtWidgets
from qt_core import *

from gui.pages.ui_pages import Ui_StackedWidget

from gui.widgets.py_button import PyPushButton

from gui.windows.main_window.new_client_page.client_page import page_new_client


class UI_MainWindow(object):

    def setup_ui(self,parent):
        parent.setObjectName("MainWindow")
        parent.resize(1000,600)
        parent.setMinimumSize(1000,500)

        


        #VARIABLES
        self.content_max = 10
        self.content = [0]*self.content_max
        
        #CENTRAL WIDGET
        self.central_frame = QFrame()

        #MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)


        #BARRA-LATERAL
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color:rgb(45,45,45)")
        self.left_menu.setMaximumWidth(40)
        self.left_menu.setMinimumWidth(40)


        #BARRA LATERAL 2 --NEW-CLIENT--

        self.left_menu2 = QFrame()
        self.left_menu2.setStyleSheet("background-color:rgb(60,60,60)")
        self.left_menu2.setMaximumWidth(1)
        self.left_menu2.setMinimumWidth(1)

        self.new_client = page_new_client()
        self.new_client.create(self.left_menu2)

        #BARRA LATERAL 3 --REMOVE-PLAYER--

        self.left_menu3 = QFrame()
        self.left_menu3.setStyleSheet("background-color:rgb(60,60,60)")
        self.left_menu3.setMaximumWidth(1)
        self.left_menu3.setMinimumWidth(1)

        self.remove_client = page_new_client()
        self.remove_client.create(self.left_menu3,"REMOVE CLIENT","A")
        self.remove_client.preco_new_client.hide()
        #self.remove_client.frame.hide()


        #BUTTOES-LATERAL
        self.butt_menu = PyPushButton(text="Ocultar menu",icon_path="menu.svg",icon_color="rgb(110,110,100)",btn_color="rgb(50,50,50)",btn_hover="rgb(100,100,100)",text_color="rgb(20,20,20)")


        #-------BUTT-PAGINA-1-------##
        self.butt_pag1 = PyPushButton(text="Controle",icon_path="pag1.svg",btn_color="rgb(50, 50, 50)",is_active=True)
        self.butt_pag1.setMinimumSize(140,40)


        #-------BUTT-PAGINA-2-------##
        self.butt_pag2 = PyPushButton(text="Usuário",icon_path="user.svg",btn_color="rgb(50, 50, 50)")
        self.butt_pag2.setMinimumSize(140,40)


        #-------BUTT-PAGINA-3-------##
        self.butt_pag3 = PyPushButton(text="Estatísticas",icon_path="file-text.svg",btn_color="rgb(50, 50, 50)")
        self.butt_pag3.setMinimumSize(140,40)


        #-------BUTT-PAGINA-4-------##
        self.butt_pag4 = PyPushButton(text="Máquinas",icon_path="hard-drive.svg",btn_color="rgb(50, 50, 50)")
        self.butt_pag4.setMinimumSize(140,40)



        #-------BUTT-SETTS-------##
        self.butt_setts = PyPushButton(text="Configuração",icon_path="settings.svg",icon_color="rgb(110,110,100)",btn_color="rgb(50,50,50)",btn_hover="rgb(100,100,100)")
        self.butt_setts.setMinimumSize(140,40)


        self.verticalSpacer = QSpacerItem(20, 476, QSizePolicy.Minimum, QSizePolicy.Expanding)
   


        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)
        self.left_menu_layout.setSpacing(0)



        #BARRA SUPERIOR
        self.top_bar = QFrame()
        self.top_bar.setStyleSheet("background-color:rgb(100,100,130)")
        self.top_bar.setMinimumHeight(40)
        self.top_bar.setMaximumHeight(40)


            #==== BUTT 2 BARRA SUPERIOR ====#
        self.butt_1_topbar = PyPushButton(border_is_active=False,icon_path="user-minus.svg",btn_color="#646482")
        self.butt_1_topbar.setMaximumWidth(40)

            #==== BUTT 2 BARRA SUPERIOR ====#
        self.butt_2_topbar = PyPushButton(border_is_active=False,icon_path="user-plus.svg",btn_color="#646482")
        self.butt_2_topbar.setMaximumWidth(40)

        self.butt_3_topbar = PyPushButton(border_is_active=False,icon_path="edit.svg",btn_color="#646482")
        self.butt_3_topbar.setMaximumWidth(40)
        self.butt_3_topbar.hide()



        self.label_top_bar = QLabel(self.top_bar)
        self.label_top_bar.setText("Developed by Ismael Brasil")

        self.top_bar_layout =QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(2,0,0,0)
        self.top_bar_layout.setSpacing(8)


        self.top_bar_layout.addWidget(self.label_top_bar)
        self.top_bar_layout.addWidget(self.butt_1_topbar)
        self.top_bar_layout.addWidget(self.butt_2_topbar)
        self.top_bar_layout.addWidget(self.butt_3_topbar)
        


        #AREA-PRINCIPAL
        self.area = QFrame()
        self.area.setStyleSheet("background-color:rgb(100,100,100)")

        self.area_layout = QVBoxLayout(self.area)
        self.area_layout.setContentsMargins(0,0,0,0)
        self.area_layout.setSpacing(0)


        #PAGINAS
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("background-color: rgb(60,60,60)")
        self.ui_pages = Ui_StackedWidget()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentIndex(0)
        self.pages.setStyleSheet("border:none")

        #PAGINA-1 ====SLOTS=====

        self.page_creator = colunas(self.ui_pages.verticalLayout_8)
        self.page_creator.new_frame()


        self.spacer_content = QSpacerItem(20, 476, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.ui_pages.verticalLayout_8.addItem(self.spacer_content)       

        #PAGINA-2 =====BUTTS=====

        self.ok_maquinas = PyPushButton("Salvar",icon_path="check.svg")
        self.quit_maquinas = PyPushButton("Sair",icon_path="x.svg")

        self.layou_maquinas = QHBoxLayout(self.ui_pages.frame_14)
        self.layou_maquinas.addWidget(self.quit_maquinas)
        self.layou_maquinas.addWidget(self.ok_maquinas)

        self.ui_pages.frame_9.setMaximumWidth(1)
     





        self.new_maq = new_maquinas(self.ui_pages.frame_15,10)



        #BARRA INFERIOR
        self.botton_bar = QFrame()
        self.botton_bar.setStyleSheet("background-color:rgb(100,100,130)")
        self.botton_bar.setMinimumHeight(20)
        self.botton_bar.setMaximumHeight(20)



        #ADD WIDGETS  MAIN LAYOUT
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.left_menu2)
        self.main_layout.addWidget(self.area)
        self.main_layout.addWidget(self.left_menu3)
       

        #ADD WIDGETS  LAYOUT DO CONTENT
        self.area_layout.addWidget(self.top_bar)
        self.area_layout.addWidget(self.pages)
        self.area_layout.addWidget(self.botton_bar)


        #ADD WIDGETS   LAYOUT DO MENU LATERAL
        self.left_menu_layout.addWidget(self.butt_menu)
        self.left_menu_layout.addWidget(self.butt_pag1)
        self.left_menu_layout.addWidget(self.butt_pag2)
        self.left_menu_layout.addWidget(self.butt_pag3)
        self.left_menu_layout.addWidget(self.butt_pag4)
        self.left_menu_layout.addItem(self.verticalSpacer)
        self.left_menu_layout.addWidget(self.butt_setts)




        parent.setCentralWidget(self.central_frame)



