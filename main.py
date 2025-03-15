from motorui import Ui_MainWindow
from serial.tools import list_ports
from serial import Serial
# from customserial import SerialFactory
from PySide6.QtWidgets import QMainWindow, QApplication
import sys

class SerialManager:
    def __init__(self):
        self.serial_connections = {}
    
    def get_serial(self ,model : str, port : str) -> None:
        if model not in self.serial_connections:
            try:
                self.serial_connections[model] = Serial(port=port)
                return True
            except Exception as e:
                print(e)
                return None

        
    def close_serial(self, model : str) -> None:
        if model in self.serial_connections:
            self.serial_connections[model].close()
            del self.serial_connections[model]

    def is_connected(self, model) -> bool:
        return model in self.serial_connections



class Main(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.serial_manager = SerialManager()
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
        button = getattr(self, f"pb_{model}")
        connected = self.serial_manager.is_connected(model)
        if button.text() == "열기" and not connected:
            if self._generator(model) is not None:  # 연결 성공 여부 확인
                button.setText("닫기")
        elif button.text() == "닫기" and connected:
            self.serial_manager.close_serial(model)
            button.setText("열기")

            

    def _generator(self, model : str):
            port = getattr(self,f"cb_{model}").currentText()
            return self.serial_manager.get_serial(model=model, port=port)


    def get_movement(self, model):
        for idx in range(5):
            if getattr(self,f"rb_{model}_{idx}").isChecked():
                return idx
        return -1
    
    def get_ports(self):
            return [port.device for port in list_ports.comports()]

    def set_config(self):
        models = self.config["models"]
        for model in models:
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
    main = Main()
    sys.exit(app.exec())