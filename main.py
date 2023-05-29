import sys
import json
from PyQt5.QtWidgets import QApplication
from onder_ui import Ui_MainWindow

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from ui_functions import *

class ui_windows(QMainWindow):
    def __init__(self):
        super(ui_windows, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.button_clicks()
        self.initial_variables()
    
    def initial_variables(self):
        self.stations = []
        self.mapping = False
    
    def button_clicks(self):
        for i in range(0, self.ui.home_gridlayout.count()):
            self.ui.home_gridlayout.itemAt(i).widget().clicked.connect(self.station_click)
        self.ui.backspace_btn.clicked.connect(self.delete_path)
        self.ui.settings_btn.clicked.connect(lambda: self.page_navigation(self.ui.setting_page))
        self.ui.close_settings.clicked.connect(lambda: self.page_navigation(self.ui.home_page))
        self.ui.close_mapping.clicked.connect(lambda: self.page_navigation(self.ui.setting_page))
        self.ui.new_map.clicked.connect(lambda: self.page_navigation(self.ui.mapping_page))
        self.ui.start_map.clicked.connect(self.start_mapping)
    
    def get_style(self):
        with open('styles/stylesheets.json', 'r') as readfile:
            obj = json.loads(readfile.read())
        return obj

    def station_click(self):
        self.stations.append(self.sender().objectName().split('_')[1])
        self.ui.planner_label.setText('→'.join(self.stations))
    
    def delete_path(self):
        if self.stations:
            self.stations.pop()
        self.ui.planner_label.setText('→'.join(self.stations))
    
    def page_navigation(self, page):
        self.ui.stackedWidget.setCurrentWidget(page)
        self.ui.save_frame.setMaximumHeight(0)
    
    def start_mapping(self):
        if not self.mapping:
            self.ui.start_map.setStyleSheet(self.get_style()['stop_style'])
            UIFunctions.animations(self, 0, self.ui.save_frame)
            self.mapping = True
        else:
            self.ui.start_map.setStyleSheet(self.get_style()['record_style'])
            UIFunctions.animations(self, 150, self.ui.save_frame)
            self.mapping = False



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ui_windows()

    win.show()
    sys.exit(app.exec_())