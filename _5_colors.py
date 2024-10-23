def change_theme(self, theme):
    if theme == 'Tema Neutro Padrão':
        submenu_stylesheet = """
            QMenu::item:selected {
                background-color: #90c8f6;
            }
            QMenu::item:hover {
                background-color: #000000;
                font-size: 12px;
            }
        """
        menubar_stylesheet = """
            QMenuBar::item:selected {
                background-color: #90c8f6;
            }
            QMenuBar::item:hover {
                background-color: #000000;
                font-size: 12px;
            }
        """
    elif theme == 'Tema Claro':
        submenu_stylesheet = """
            QMenu::item:selected {
                background-color: #b3b3b3;
            }
            QMenu::item:hover {
                background-color: #333333;
                font-size: 12px;
            }
        """
        menubar_stylesheet = """
            QMenuBar::item:selected { 
                background-color: #b3b3b3; 
            }
            QMenuBar::item:hover { 
                background-color: #333333;
                font-size: 12px;
            }
        """
    elif theme == 'Tema Escuro':
        submenu_stylesheet = """
            QMenu::item:selected {
                background-color: #333333;
            }
            QMenu::item:hover {
                background-color: #b3b3b3;
                font-size: 12px;
            }
        """
        menubar_stylesheet = """
            QMenuBar::item:selected {
                background-color: #333333;
            }
            QMenuBar::item:hover {
                background-color: #b3b3b3;
                font-size: 12px;
            }
        """
    elif theme == 'Tema Azul':
        submenu_stylesheet = """
            QMenu::item:selected {
                background-color: #538cc6;
            }
            QMenu::item:hover {
                background-color: #1a3348;
                font-size: 12px;
            }
        """
        menubar_stylesheet = """
            QMenuBar::item:selected {
                background-color: #538cc6;
            }
            QMenuBar::item:hover {
                background-color: #1a3348;
                font-size: 12px;
            }
        """
    elif theme == 'Tema Vermelho':
        submenu_stylesheet = """
            QMenu::item:selected {
                background-color: #c65353;
            }
            QMenu::item:hover {
                background-color: #4d1a1a;
                font-size: 12px;
            }
        """
        menubar_stylesheet = """
            QMenuBar::item:selected {
                background-color: #c65353;
            }
            QMenuBar::item:hover {
                background-color: #4d1a1a;
                font-size: 12px;
            }
        """
    elif theme == 'Tema Verde':
        submenu_stylesheet = """
            QMenu::item:selected {
                background-color: #53c68c;
            }
            QMenu::item:hover {
                background-color: #1a4d33;
                font-size: 12px;
            }
        """
        menubar_stylesheet = """
            QMenuBar::item:selected {
                background-color: #53c68c;
            }
            QMenuBar::item:hover {
                background-color: #1a4d33;
                font-size: 12px;
            }
        """
    elif theme == 'Tema Roxo':
        submenu_stylesheet = """
            QMenu::item:selected {
                background-color: #8c53c6;
            }
            QMenu::item:hover {
                background-color: #331a4d;
                font-size: 12px;
            }
        """
        menubar_stylesheet = """
            QMenuBar::item:selected {
                background-color: #8c53c6;
            }
            QMenuBar::item:hover {
                background-color: #331a4d;
                font-size: 12px;
            }
        """
    elif theme == 'Tema Laranja':
        submenu_stylesheet = """
            QMenu::item:selected {
                background-color: #ff751a;
            }
            QMenu::item:hover {
                background-color: #993d00;
                font-size: 12px;
            }
        """
        menubar_stylesheet = """
            QMenuBar::item:selected {
                background-color: #ff751a;
            }
            QMenuBar::item:hover {
                background-color: #993d00;
                font-size: 12px;
            }
        """
    elif theme == 'Tema Amarelo':
        submenu_stylesheet = """
            QMenu::item:selected {
                background-color: #ffffb3;
            }
            QMenu::item:hover {
                background-color: #99993d;
                font-size: 12px;
            }
        """
        menubar_stylesheet = """
            QMenuBar::item:selected {
                background-color: #ffffb3;
            }
            QMenuBar::item:hover {
                background-color: #99993d;
                font-size: 12px;
            }
        """
    elif theme == 'Tema Rosa':
        submenu_stylesheet = """
            QMenu::item:selected {
                background-color: #ffb3e6;
            }
            QMenu::item:hover {
                background-color: #993d7a;
                font-size: 12px;
            }
        """
        menubar_stylesheet = """
            QMenuBar::item:selected {
                background-color: #ffb3e6;
            }
            QMenuBar::item:hover {
                background-color: #993d7a;
                font-size: 12px;
            }
        """

    self.theme_menu.setStyleSheet(submenu_stylesheet)
    self.config_menu.setStyleSheet(submenu_stylesheet)
    self.menu_bar.setStyleSheet(menubar_stylesheet)

def apply_neutral_standart_theme(self):
    self.setStyleSheet("""
    QWidget {
        background-color: #e6e6e6;
        color: #000000;
    }
    QMenu {
        background-color: #f0f0f0;
        border-style: solid;
        border-width: 1px;
        border-color: #d0d0d0;
        color: #000000;
    }
    QMenuBar {
        background-color: #ffffff;
        font-size: 13px;
        color: #000000;
    }
    QPushButton {
        background-color: #fafafa;
        border-style: solid;
        border-width: 1.2px;
        border-radius: 4px;
        border-color: #d0d0d0;
        font: normal 12px;
        min-width: 14em;
        max-width: 14em;
        padding: 2px;
        color: #000000;
    }
    QPushButton:hover {
        background-color: #bfdcf3;
        border-color: #0078d4;
        color: #000000;
    }
    QLabel {
        color: #000000;
    }
    QListWidget {
        background-color: #ffffff;
        border-style: solid;
        border-width: 1px;
        border-color: #828790;
        min-width: 150px;
        min-height: 140px;
        color: #000000;
    }
    """)
    self.change_theme('Tema Neutro Padrão')

def apply_light_theme(self):
    self.setStyleSheet("""
    QWidget {
        background-color: #f0f0f0;
        color: #333333;
    }
    QMenu {
        background-color: #f0f0f0;
        border-style: solid;
        border-width: 1px;
        border-color: #d0d0d0;
        color: #333333;
    }
    QMenuBar {
        background-color: #ffffff;
        font-size: 13px;
        color: #333333;
    }
    QPushButton {
        background-color: #e0e0e0;
        border-style: outset;
        border-width: 1.2px;
        border-radius: 4px;
        border-color: #b3b3b3;
        font: bold 12px;
        min-width: 14em;
        max-width: 14em;
        padding: 2px;
        color: #333333;
    }
    QPushButton:hover {
        background-color: #b3b3b3;
        border-color: #333333;
        color: #f0f0f0;
    }
    QLabel {
        color: #333333;
    }
    QListWidget {
        background-color: #e0e0e0;
        border-style: solid;
        border-width: 1px;
        border-color: #828790;
        min-width: 150px;
        min-height: 140px;
        color: #333333;
    }
    """)
    self.change_theme('Tema Claro')

def apply_dark_theme(self):
    self.setStyleSheet("""
    QWidget {
        background-color: #2b2b2b;
        color: #b3b3b3;
    }
    QMenu {
        background-color: #2b2b2b;
        border-style: solid;
        border-width: 1px;
        border-color: #1e1e1e;
        color: #b3b3b3;
    }
    QMenuBar {
        background-color: #2b2b2b;
        font-size: 13px;
        color: #b3b3b3;
    }
    QPushButton {
        background-color: #333333;
        border-style: outset;
        border-width: 1.2px;
        border-radius: 4px;
        border-color: #1e1e1e;
        font: bold 12px;
        min-width: 14em;
        max-width: 14em;
        padding: 2px;
        color: #b3b3b3;
    }
    QPushButton:hover {
        background-color: #1e1e1e;
        border-color: #b3b3b3;
        color: #f0f0f0;
    }
    QLabel {
        color: #f0f0f0;
    }
    QListWidget {
        background-color: #333333;
        border-style: solid;
        border-width: 1px;
        min-width: 150px;
        min-height: 140px;
        color: #f0f0f0;
    }
    """)
    self.change_theme('Tema Escuro')

def apply_blue_theme(self):
    self.setStyleSheet("""
    QWidget {
        background-color: #336699;
        color: #ffffff;
    }
    QMenu {
        background-color: #264d73;
        border-style: solid;
        border-width: 1px;
        border-color: #1a3348;
        color: #ffffff;
    }
    QMenuBar {
        background-color: #336699;
        font-size: 13px;
        color: #ffffff;
    }
    QPushButton {
        background-color: #264d73;
        border-style: outset;
        border-width: 1.2px;
        border-radius: 4px;
        border-color: #1a3348;
        font: bold 12px;
        min-width: 14em;
        max-width: 14em;
        padding: 2px;
        color: #ffffff;
    }
    QPushButton:hover {
        background-color: #1a3348;
        border-color: #ffffff;
        color: #b3d1ff;
    }
    QLabel {
        color: #ffffff;
    }
    QListWidget {
        background-color: #264d73;
        border-style: solid;
        border-width: 1px;
        min-width: 150px;
        min-height: 140px;
        color: #ffffff;
    }
    """)
    self.change_theme('Tema Azul')

def apply_red_theme(self):
    self.setStyleSheet("""
    QWidget {
        background-color: #993333;
        color: #ffffff;
    }
    QMenu {
        background-color: #732626;
        border-style: solid;
        border-width: 1px;
        border-color: #4d1a1a;
        color: #ffffff;
    }
    QMenuBar {
        background-color: #993333;
        font-size: 13px;
        color: #ffffff;
    }
    QPushButton {
        background-color: #732626;
        border-style: outset;
        border-width: 1.2px;
        border-radius: 4px;
        border-color: #4d1a1a;
        font: bold 12px;
        min-width: 14em;
        max-width: 14em;
        padding: 2px;
        color: #ffffff;
    }
    QPushButton:hover {
        background-color: #4d1a1a;
        border-color: #ffffff;
        color: #ff9999;
    }
    QLabel {
        color: #ffffff;
    }
    QListWidget {
        background-color: #732626;
        border-style: solid;
        border-width: 1px;
        min-width: 150px;
        min-height: 140px;
        color: #ffffff;
    }
    """)
    self.change_theme('Tema Vermelho')

def apply_green_theme(self):
    self.setStyleSheet("""
    QWidget {
        background-color: #339966;
        color: #ffffff;
    }
    QMenu {
        background-color: #26734d;
        border-style: solid;
        border-width: 1px;
        border-color: #1a4d33;
        color: #ffffff;
    }
    QMenuBar {
        background-color: #339966;
        font-size: 13px;
        color: #ffffff;
    }
    QPushButton {
        background-color: #26734d;
        border-style: outset;
        border-width: 1.2px;
        border-radius: 4px;
        border-color: #1a4d33;
        font: bold 12px;
        min-width: 14em;
        max-width: 14em;
        padding: 2px;
        color: #ffffff;
    }
    QPushButton:hover {
        background-color: #1a4d33;
        border-color: #ffffff;
        color: #99ffcc;
    }
    QLabel {
        color: #ffffff;
    }
    QListWidget {
        background-color: #26734d;
        border-style: solid;
        border-width: 1px;
        min-width: 150px;
        min-height: 140px;
        color: #ffffff;
    }
    """)
    self.change_theme('Tema Verde')

def apply_purple_theme(self):
    self.setStyleSheet("""
    QWidget {
        background-color: #663399;
        color: #ffffff;
    }
    QMenu {
        background-color: #4d2673;
        border-style: solid;
        border-width: 1px;
        border-color: #331a4d;
        color: #ffffff;
    }
    QMenuBar {
        background-color: #663399;
        font-size: 13px;
        color: #ffffff;
    }
    QPushButton {
        background-color: #4d2673;
        border-style: outset;
        border-width: 1.2px;
        border-radius: 4px;
        border-color: #331a4d;
        font: bold 12px;
        min-width: 14em;
        max-width: 14em;
        padding: 2px;
        color: #ffffff;
    }
    QPushButton:hover {
        background-color: #331a4d;
        border-color: #ffffff;
        color: #b399ff;
    }
    QLabel {
        color: #ffffff;
    }
    QListWidget {
        background-color: #4d2673;
        border-style: solid;
        border-width: 1px;
        min-width: 150px;
        min-height: 140px;
        color: #ffffff;
    }
    """)
    self.change_theme('Tema Roxo')

def apply_orange_theme(self):
    self.setStyleSheet("""
    QWidget {
        background-color: #ff6600;
        color: #ffffff;
    }
    QMenu {
        background-color: #cc5200;
        border-style: solid;
        border-width: 1px;
        border-color: #993d00;
        color: #ffffff;
    }
    QMenuBar {
        background-color: #ff6600;
        font-size: 13px;
        color: #ffffff;
    }
    QPushButton {
        background-color: #cc5200;
        border-style: outset;
        border-width: 1.2px;
        border-radius: 4px;
        border-color: #993d00;
        font: bold 12px;
        min-width: 14em;
        max-width: 14em;
        padding: 2px;
        color: #ffffff;
    }
    QPushButton:hover {
        background-color: #993d00;
        border-color: #ffffff;
        color: #ffcc99;
    }
    QLabel {
        color: #ffffff;
    }
    QListWidget {
        background-color: #cc5200;
        border-style: solid;
        border-width: 1px;
        min-width: 150px;
        min-height: 140px;
        color: #ffffff;
    }
    """)
    self.change_theme('Tema Laranja')

def apply_yellow_theme(self):
    self.setStyleSheet("""
    QWidget {
        background-color: #ffff66;
        color: #333333;
    }
    QMenu {
        background-color: #cccc52;
        border-style: solid;
        border-width: 1px;
        border-color: #99993d;
        color: #333333;
    }
    QMenuBar {
        background-color: #ffff66;
        font-size: 13px;
        color: #333333;
    }
    QPushButton {
        background-color: #cccc52;
        border-style: outset;
        border-width: 1.2px;
        border-radius: 4px;
        border-color: #99993d;
        font: bold 12px;
        min-width: 14em;
        max-width: 14em;
        padding: 2px;
        color: #333333;
    }
    QPushButton:hover {
        background-color: #99993d;
        border-color: #333333;
        color: #ffffcc;
    }
    QLabel {
        color: #333333;
    }
    QListWidget {
        background-color: #cccc52;
        border-style: solid;
        border-width: 1px;
        min-width: 150px;
        min-height: 140px;
        color: #333333;
    }
    """)
    self.change_theme('Tema Amarelo')

def apply_pink_theme(self):
    self.setStyleSheet("""
    QWidget {
        background-color: #ff66cc;
        color: #ffffff;
    }
    QMenu {
        background-color: #cc52a3;
        border-style: solid;
        border-width: 1px;
        border-color: #993d7a;
        color: #ffffff;
    }
    QMenuBar {
        background-color: #ff66cc;
        font-size: 13px;
        color: #ffffff;
    }
    QPushButton {
        background-color: #cc52a3;
        border-style: outset;
        border-width: 1.2px;
        border-radius: 4px;
        border-color: #993d7a;
        font: bold 12px;
        min-width: 14em;
        max-width: 14em;
        padding: 2px;
        color: #ffffff;
    }
    QPushButton:hover {
        background-color: #993d7a;
        border-color: #ffffff;
        color: #ffccf2;
    }
    QLabel {
        color: #ffffff;
    }
    QListWidget {
        background-color: #cc52a3;
        border-style: solid;
        border-width: 1px;
        min-width: 150px;
        min-height: 140px;
        color: #ffffff;
    }
    """)
    self.change_theme('Tema Rosa')

def apply_neutral_standart_theme_2(self):
    self.setStyleSheet("""
    QWidget {
        background-color: #e6e6e6;
        color: #000000;
    }
    QMenu {
        background-color: #f0f0f0;
        border-style: solid;
        border-width: 1px;
        border-color: #d0d0d0;
        color: #000000;
    }
    QMenu::item:selected {
        background-color: #90c8f6;
    }
    QMenu::item:hover {
        background-color: #000000;
        font-size: 12px;
    }
    QMenuBar {
        background-color: #ffffff;
        font-size: 13px;
        color: #000000;
    }
    QMenuBar::item:selected {
        background-color: #90c8f6;
    }
    QMenuBar::item:hover {
        background-color: #000000;
        font-size: 12px;
    }
    QPushButton {
        background-color: #fafafa;
        border-style: solid;
        border-width: 1.2px;
        border-radius: 4px;
        border-color: #d0d0d0;
        font: normal 12px;
        min-width: 14em;
        max-width: 14em;
        padding: 2px;
        color: #000000;
    }
    QPushButton:hover {
        background-color: #bfdcf3;
        border-color: #0078d4;
        color: #000000;
    }
    QLabel {
        color: #000000;
    }
    QListWidget {
        background-color: #ffffff;
        border-style: solid;
        border-width: 1px;
        border-color: #828790;
        min-width: 150px;
        min-height: 140px;
        color: #000000;
    }
    """)

def apply_dialog_box_theme(self):
    self.setStyleSheet("""
    QFileDialog {
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
    }
    QTreeView {
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
    }
    QTreeView::item:hover {
        background-color: rgb(191, 220, 243);
        border-color: rgb(0, 120, 212);
        border-style: solid;
        border-width: 1.2px;
        border-radius: 0px;
        color: rgb(0, 0, 0);
    }
    QTreeView::item:selected {
        background-color: rgb(128, 200, 255);
        color: rgb(0, 0, 0);
    }
    QListView {
        background-color: rgb(255, 255, 255);
        border-color: rgb(197, 197, 197);
        border-style: solid;
        border-width: 1.4px;
        border-radius: 0px;
        color: rgb(0, 0, 0);
    }
    QListView::item:hover {
        background-color: rgb(191, 220, 243);
        border-color: rgb(0, 120, 212);
        border-style: solid;
        border-width: 1.2px;
        border-radius: 0px;
        color: rgb(0, 0, 0);
    }
    QListView::item:selected {
        background-color: rgb(128, 200, 255);
        color: rgb(0, 0, 0);
    }
    QLineEdit {
        background-color: rgb(255, 255, 255);
        border-color: rgb(197, 197, 197);
        border-style: solid;
        border-width: 1.4px;
        border-radius: 0px;
        color: rgb(0, 0, 0);
    }
    QComboBox {
        background-color: rgb(255, 255, 255);
        border-color: rgb(197, 197, 197);
        border-style: solid;
        border-width: 1.4px;
        border-radius: 0px;
        color: rgb(0, 0, 0);
    }
    QComboBox::item:hover {
        background-color: rgb(191, 220, 243);
        border-color: rgb(0, 120, 212);
        border-style: solid;
        border-width: 1.2px;
        border-radius: 0px;
        color: rgb(0, 0, 0);                   
    }
    QComboBox::item:selected {
        background-color: rgb(128, 200, 255);
        color: rgb(0, 0, 0);
    }
    QLabel {
        background-color: rgb(255, 255, 255);
    color: rgb(0, 0, 0);
    }
    QToolButton {
        background-color: rgb(255, 255, 255);
    }
    QPushButton {
        background-color: rgb(255, 255, 255);
        border-color: rgb(197, 197, 197);
        border-style: solid;
        border-width: 1.4px;
        border-radius: 4px;
        font: normal 12px;
        min-width: 7em;
        max-width: 7em;
        padding: 2px;
        color: rgb(0, 0, 0);
    }
    QPushButton:hover {
        background-color: rgb(191, 220, 243);
        border-color: rgb(0, 120, 212);
        border-style: solid;
        border-width: 1.4px;
        border-radius: 4px;
        font: normal 12px;
        min-width: 7em;
        max-width: 7em;
        padding: 2px;
        color: rgb(0, 0, 0);
    }
    """)

def apply_message_box_theme(self):
    self.setStyleSheet("""
    QMessageBox {
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
    }
    QLabel {
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
    }
    QPushButton {
        background-color: rgb(255, 255, 255);
        border-color: rgb(197, 197, 197);
        border-style: solid;
        border-width: 1.4px;
        border-radius: 4px;
        font: normal 12px;
        min-width: 10em;
        max-width: 10em;
        padding: 2px;
        color: rgb(0, 0, 0);
    }
    QPushButton:hover {
        background-color: rgb(191, 220, 243);
        border-color: rgb(0, 120, 212);
        border-style: solid;
        border-width: 1.4px;
        border-radius: 4px;
        font: normal 12px;
        min-width: 10em;
        max-width: 10em;
        padding: 2px;
        color: rgb(0, 0, 0);
    }
    """)
