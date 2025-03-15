from motorui import Ui_MainWindow
from serialmodule import SerialController, SerialManager
from threadmodule import ThreadManager
from serial.tools import list_ports
from threading import Thread
# from customserial import SerialFactory
from PySide6.QtWidgets import QMainWindow, QApplication
import sys

class Main(Ui_MainWindow, QMainWindow):
    def __init__(self, serial_controller : SerialController):
        super().__init__()
        self.setupUi(self)
        self.serial_controller = serial_controller
        self.thread_manager = ThreadManager()
        # 가변 변수들..
        self.config = {
            "models" : ["sss", "mag", "ss"],
            "rpms" : ["100","300","500"],
            "movements" : ["0","10","15","20","25"],
            "ports" : self.get_ports()
        }
        self.set_config()


        self.pb_sss.clicked.connect(lambda _ : self.open_and_close(model="sss"))
        self.pb_mag.clicked.connect(lambda _ : self.open_and_close(model="mag"))
        self.pb_ss.clicked.connect(lambda _ : self.open_and_close(model="ss"))
        
        self.show()


    def open_and_close(self, model):
        port = getattr(self, f"cb_{model}").currentText()
        button = getattr(self, f"pb_{model}")
        return button.setText("닫기") if self.serial_controller.connection(model, port) else button.setText("열기")

    def check_radio(self, model):
        for idx, _ in enumerate(self.config["movements"]):
            if getattr(self,f"rb_{model}_{idx}").isChecked():
                return idx
        return -1
    
    def get_ports(self):
            return [port.device for port in list_ports.comports()]

    def set_config(self):
        for model in self.config["models"]:
            self._set_to_radio(f"rb_{model}", self.config["movements"])
            self._add_to_combo(f"cb_rpm_{model}", self.config["rpms"])
            self._add_to_combo(f"cb_{model}", self.config["ports"])

    def _add_to_combo(self,combo_name : str, items: list[str]) -> None:
        combobox = getattr(self,combo_name)
        combobox.clear()
        for item in items:
            combobox.addItem(item)

    def _set_to_radio(self,radio_name, items : list[str]) -> None:
        for idx,item in enumerate(items):
            getattr(self,f"{radio_name}_{idx}").setText(item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    serial_manager = SerialManager()
    serial_controller = SerialController(serial_manager)
    main = Main(serial_controller)
    sys.exit(app.exec())