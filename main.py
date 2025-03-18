from motorui import Ui_MainWindow
from serialmodule import SerialController, SerialManager
from threadmodule import ThreadManager, ThreadController
from serial.tools import list_ports
from threading import Thread
# from customserial import SerialFactory
from PySide6.QtWidgets import QMainWindow, QApplication
import sys

class Main(Ui_MainWindow, QMainWindow):
    def __init__(self, serial_controller : SerialController, thread_controller : ThreadController):
        super().__init__()
        self.setupUi(self)
        self.serial_controller = serial_controller
        self.thread_controller = thread_controller

        # 가변 변수들..
        self.config = {
            "models" : ["sss", "mag", "ss"],
            "rpms" : ["100","300","500"],
            "movements" : ["0","10","15","20","25"],
            "ports" : self.get_ports()
        }

        self._set_config()


        self.pb_sss.clicked.connect(lambda _ : self.open_and_close(model="sss"))
        self.pb_mag.clicked.connect(lambda _ : self.open_and_close(model="mag"))
        self.pb_ss.clicked.connect(lambda _ : self.open_and_close(model="ss"))
        self.pb_sss_start.clicked.connect(lambda _ : self.run_winch(model="sss"))
        self.pb_mag_start.clicked.connect(lambda _ : self.run_winch(model="mag"))
        self.pb_ss_start.clicked.connect(lambda _ : self.run_winch(model="ss"))
        self.pb_sss_stop.clicked.connect(lambda _ : self.stop_winch(model="sss"))
        self.pb_mag_stop.clicked.connect(lambda _ : self.stop_winch(model="mag"))
        self.pb_ss_stop.clicked.connect(lambda _ : self.stop_winch(model="ss"))
        
        self.show()
    # msg_length,rpm, cw, mode, distance
    def run_winch(self,model : str,mode : str = 'C'):
        if self.serial_controller.is_connected(model):
            distance = self.check_radio(model)
            rpm = getattr(self,f"cb_rpm_{model}").currentText()
            mode = ord(mode)
            msg = [int(rpm)//100, mode, int(distance)]
            msg.insert(0,len(msg))
            if self.serial_controller.send_protocol(model,msg):
                self.thread_controller.start_to_thread(model,self.thread_func)
        else:
            False

    def stop_winch(self,model) -> None:
        if self.serial_controller.send_protocol(model,['S']):
            print("성공")
        else:
            print("실패")

    def thread_func(self, model):
        while(True):
            key = self.serial_controller.receive_msg(model)
            if key != None:
                msg = self.serial_controller.SER_MSG.get(msg,None)
                if msg:
                    print(msg)
            else:
                break

    def open_and_close(self, model):
        port = getattr(self, f"cb_{model}").currentText()
        button = getattr(self, f"pb_{model}")
        if self.serial_controller.connect_to_port(model, port):
            button.setText("닫기")
            print("연결 완료")
        elif self.serial_controller.disconnect_to_port(model):
            try:
                self.thread_controller.stop_to_thread(model)
            except:
                pass
            button.setText("열기")
            print("닫기 완료")


    def check_radio(self, model):
        for idx, _ in enumerate(self.config["movements"]):
            if getattr(self,f"rb_{model}_{idx}").isChecked():
                return idx
        return -1
    
    def get_ports(self):
            return [port.device for port in list_ports.comports()]

    def _set_config(self):
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
    thread_manager = ThreadManager()
    serial_controller = SerialController(serial_manager)
    thread_controller = ThreadController(thread_manager)
    main = Main(serial_controller, thread_controller)
    sys.exit(app.exec())