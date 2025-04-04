from motorui import Ui_MainWindow
from serialmodule import SerialController, SerialManager
from threadmodule import ThreadManager, ThreadController
from serial.tools import list_ports
from threading import Thread
# from customserial import SerialFactory
from PySide6.QtWidgets import QMainWindow, QApplication
import sys
from PySide6.QtCore import QMetaObject, Q_ARG, Qt


class Main(Ui_MainWindow, QMainWindow):
    def __init__(self, serial_controller : SerialController, thread_controller : ThreadController):
        super().__init__()
        self.setupUi(self)
        self.serial_controller = serial_controller
        self.thread_controller = thread_controller
        self.distance = 0
        self.movement = {
            "sss" : 0.392,
            "mag" : 2.872,
            "ss" : 2.872,
        }

        # 가변 변수들..
        self.config = {
            "models" : ["sss", "mag", "ss"],
            "types" : ["lift","winch"],
            "rpms" : ["100","300","500"],
            "sss" : ["0","1","2","3","4"],
            "mag" : ["0","100","150","200","250"],
            "ss" : ["0","100","150","200","250"],
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
    # msg_length,rpm, cw, distance
    def run_winch(self,model : str, cw : str = 'D'):
        if self.serial_controller.is_connected(model):
            types = 'L' if model == 'sss' else 'W'
            cw = cw
            rpm = int(getattr(self,f"cb_rpm_{model}").currentText()) // 100
            distance = int(self.check_radio(model)) * 100
            msg = [types, rpm, cw, distance]
            self.serial_controller.send_protocol(model,msg)
        else:
            False

    def stop_winch(self,model) -> None:
        if self.serial_controller.send_protocol(model,['S']):
            print("성공")
        else:
            print("실패")

    def thread_func(self, model):
        try:
            while(True):
                if self.serial_controller.readable(model):
                    key = self.serial_controller.receive_msg(model)
                    if key:
                        msg = self.serial_controller.SER_MSG.get(key.decode(),key)
                        if msg == 'U':
                            self.distance += self.movement.get(model,0)
                        elif msg == 'D':
                            self.distance -= self.movement.get(model,0)
                    te = getattr(self,f"te_{model}_distance")
                    _distance =str(self.distance) + "mm"
                    QMetaObject.invokeMethod(te, "setText", Qt.QueuedConnection,Q_ARG(str,_distance))
                if not self.serial_controller.is_connected(model):
                    return
        except:
            pass
        
    def open_and_close(self, model):
        port = getattr(self, f"cb_{model}").currentText()
        button = getattr(self, f"pb_{model}")
        if self.serial_controller.connect_to_port(model, port):
            button.setText("닫기")
            self.thread_controller.start_to_thread(model,self.thread_func)
            print("연결 완료")
        elif self.serial_controller.disconnect_to_port(model):
            try:
                self.thread_controller.stop_to_thread(model)
            except:
                print("쓰레드 해제 실패")
            button.setText("열기")
            print("닫기 완료")


    def check_radio(self, model):
        for idx, value in enumerate(self.config[model]):
            if getattr(self,f"rb_{model}_{idx}").isChecked():
                return value
        return -1
    
    def get_ports(self):
            return [port.device for port in list_ports.comports()]

    def _set_config(self):
        for model in self.config["models"]:
            self._set_to_radio(f"rb_{model}", self.config[model])
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