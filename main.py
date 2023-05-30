import sys
import json
from PyQt5.QtWidgets import QApplication
from onder_ui import Ui_MainWindow

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, Qt, pyqtSlot
from ui_functions import *

class ui_windows(QMainWindow):
    def __init__(self):
        super(ui_windows, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: UIFunctions.print_mouse_position(self))

        self.button_clicks()
        self.initial_variables()
    
    def initial_variables(self):
        self.ui.settings_pages.setCurrentWidget(self.ui.admin_page)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        self.stations = []
        self.mapping = False
        self.lin_vel = 0
        self.ang_vel = 0
        self.linear_vel = 0.2
        self.angular_vel = 0.5
        UIFunctions.set_velocity(self, 0.0)
        self.X1, self.Y1 = self.ui.joy_inside.geometry().x(), self.ui.joy_inside.geometry().y()
    
    def button_clicks(self):
        for i in range(0, self.ui.home_gridlayout.count()):
            self.ui.home_gridlayout.itemAt(i).widget().clicked.connect(self.station_click)
        self.ui.backspace_btn.clicked.connect(self.delete_path)
        self.ui.settings_btn.clicked.connect(lambda: self.main_page_navigation(self.ui.rviz_page))
        self.ui.close_setting.clicked.connect(lambda: self.main_page_navigation(self.ui.home_page))
        self.ui.close_map.clicked.connect(lambda: self.admin_page_navigation(self.ui.admin_page))
        self.ui.new_map_3.clicked.connect(lambda: self.admin_page_navigation(self.ui.map_page))
        self.ui.start_map_2.clicked.connect(self.start_mapping)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.timer.start(5)
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.ui.joy_inside.move(self.X1, self.Y1)
            self.ang_vel, self.lin_vel = 0.00, 0.00
            UIFunctions.set_velocity(self, abs(round(self.lin_vel, 2)))
            # print(-round(self.lin_vel, 2), round(self.ang_vel, 2))
            # self.client.send_vel({'lin_vel': -self.lin_vel, 'ang_vel': -self.ang_vel})
            self.timer.stop()
    
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
    
    def main_page_navigation(self, page):
        self.ui.stackedWidget.setCurrentWidget(page)
        self.ui.save_frame_2.setMaximumHeight(0)
    
    def admin_page_navigation(self, page):
        self.ui.save_frame_2.setMaximumHeight(0)
        self.ui.mapping_info_2.setText('Click on record button to start mapping')
        self.ui.settings_pages.setCurrentWidget(page)
    
    def start_mapping(self):
        if not self.mapping:
            self.ui.mapping_info_2.setText('Mapping ...')
            self.sender().setStyleSheet(self.get_style()['stop_style'])
            UIFunctions.animations(self, 0, self.ui.save_frame_2)
            self.mapping = True
        else:
            self.ui.mapping_info_2.setText('Type map name then click save')
            self.sender().setStyleSheet(self.get_style()['record_style'])
            UIFunctions.animations(self, 150, self.ui.save_frame_2)
            self.mapping = False



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ui_windows()

    win.show()
    sys.exit(app.exec_())