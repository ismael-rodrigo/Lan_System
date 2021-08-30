from gui.windows.main_window.main_window import UI_MainWindow
import sys
import os

from qt_core import *

from gui.windows.main_window import *



#TELA PRINCIPAL 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        self.show()
        self.id = 0


        #MENU LATERAL
        self.ui.butt_menu.clicked.connect(self.menu_toggled)
        self.ui.butt_pag1.clicked.connect(self.open_page1)
        self.ui.butt_pag2.clicked.connect(self.open_page2)
        self.ui.butt_pag3.clicked.connect(self.open_page3)
        self.ui.butt_pag4.clicked.connect(self.open_page4)

        #MENU-ADD-CLIENT
        self.ui.butt_2_topbar.clicked.connect(self.new_client_toggled)

        self.ui.new_client.butt_ok.clicked.connect(self.ok_new_client)
        self.ui.butt_1_topbar.clicked.connect(self.remove_client)  


        #PAGINA 4
        self.ui.butt_3_topbar.clicked.connect(self.butt_3_topbar_clicked)



    def client_add(self,username,tempo,maquina,game,valor):

        self.ui.page_creator.user_content[self.id].setText(username)
        self.ui.page_creator.tempo_content[self.id].setText(tempo)
        self.ui.page_creator.maquina_content[self.id].setText(maquina)
        self.ui.page_creator.game_content[self.id].setText(game)
        self.ui.page_creator.preco_content[self.id].setText(valor)
        self.ui.page_creator.new_content[self.id].show() 
        self.anim = QPropertyAnimation(self.ui.page_creator.new_content[self.id],b"maximumWidth")
        self.anim.setStartValue(0)
        self.anim.setEndValue(4000)
        self.anim.setDuration(800)
        self.anim.setEasingCurve(QEasingCurve.InCurve)
        self.anim.start()
        self.id += 1


    def ok_new_client(self):
        nome = str(self.ui.new_client.nome_new_client.text())
        tempo = str(self.ui.new_client.tempo_new_client.text())
        preco = str(self.ui.new_client.preco_new_client.text())

        if self.ui.new_client.check_1.isChecked():
            self.opcao = "PS4"
        elif self.ui.new_client.check_2.isChecked():
            self.opcao = "XBOX"
        elif self.ui.new_client.check_3.isChecked():
            self.opcao = "PC"
        else:
            self.opcao = "NONE"

        if nome.isalpha() and preco.isnumeric() and tempo.isnumeric():
            self.nome = nome
            self.tempo = tempo
            self.preco = preco
            self.client_add(nome,tempo,self.opcao,"DEFAULT",preco)
            self.reset_menus(self.ui.left_menu2)

            self.ui.new_client.nome_new_client.setText("")    
            self.ui.new_client.preco_new_client.setText("")    
            self.ui.new_client.tempo_new_client.setText("")
            self.ui.new_client.label_error.hide()


        else:
            self.ui.new_client.label_error.show()

    def menu_toggled(self):
        self.anim_menus(self.ui.left_menu,140,40)


    def new_client_toggled(self):        
        self.anim_menus(self.ui.left_menu2,time=400)
        if self.ui.left_menu3.width() > 1:
            self.reset_menus(self.ui.left_menu3)



    def remove_client(self):      
        self.anim_menus(self.ui.left_menu3,time=400)

        if self.ui.left_menu2.width() > 1:
            self.reset_menus(self.ui.left_menu2)



    def anim_menus(self, parent , miximumX = 260,minimumX =1,time = 300):  

  
        bar_width = parent.width()

        width = minimumX

        if bar_width == minimumX:
            width = miximumX
        
        self.anim = QPropertyAnimation(parent,b"minimumWidth")
        anim = self.anim
        anim.setStartValue(bar_width)
        anim.setEndValue(width)
        anim.setDuration(time)
        anim.setEasingCurve(QEasingCurve.InOutCirc)
        anim.start()



    def reset_menus(self, parent):  
        
        if parent.width() > 1:
            self.reset = QPropertyAnimation(parent,b"minimumWidth")
            anim = self.reset
            anim.setStartValue(260)
            anim.setEndValue(1)
            anim.setDuration(300)
            anim.setEasingCurve(QEasingCurve.InOutCirc)
            anim.start()




    def reset_pages(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass
  
    def reset_leftBar(self):

        if self.ui.left_menu2.width() > 1:
            self.reset_menus(self.ui.left_menu2)
        if self.ui.left_menu3.width () > 1:
            self.reset_menus(self.ui.left_menu3)



    def open_page1(self):
        self.ui.butt_2_topbar.show()
        self.ui.butt_1_topbar.show()
        self.ui.butt_3_topbar.hide()
        self.reset_leftBar()
        self.reset_pages()
        self.ui.butt_pag1.set_active(True)
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page)

    def open_page2(self):
        self.ui.butt_2_topbar.hide()
        self.ui.butt_1_topbar.hide()
        self.ui.butt_3_topbar.hide()
        self.reset_leftBar()
        self.reset_pages()
        self.ui.butt_pag2.set_active(True)
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)


    def open_page3(self):
        self.reset_leftBar()
        self.ui.butt_2_topbar.hide()
        self.ui.butt_1_topbar.hide()
        self.ui.butt_3_topbar.hide()
        self.reset_pages()
        self.ui.butt_pag3.set_active(True)
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)


    def open_page4(self):
        self.reset_leftBar()
        self.ui.butt_2_topbar.hide()
        self.ui.butt_1_topbar.hide()
        self.ui.butt_3_topbar.show()
        self.reset_pages()
        self.ui.butt_pag4.set_active(True)
        if self.ui.pages.currentIndex() != 3:
            self.ui.ui_pages.frame_9.setFixedWidth(1)
            
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_4)




    def butt_3_topbar_clicked(self):
        self.anim_menus(self.ui.ui_pages.frame_9,400)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()   
    sys.exit(app.exec())
