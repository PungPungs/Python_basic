from motorui import Ui_MainWindow
from serialmodule import SerialController, SerialManager
from threadmodule import ThreadManager, ThreadController
from serial.tools import list_ports
from threading import Thread
# from customserial import SerialFactory
from PySide6.QtWidgets import QMainWindow, QApplication
import sys
from PySide6.QtCore import QMetaObject, Q_ARG, Qt, Signal
import os

class Main(Ui_MainWindow, QMainWindow):
    def __init__(self, serial_controller : SerialController, thread_controller : ThreadController):
        super().__init__()
        self.setupUi(self)
        self.serial_controller = serial_controller
        self.thread_controller = thread_controller
    
        self.distance = {
            "sss" : 0,
            "mag" : 0,
            "ss" : 0
        }

        self.movement = {
            "sss" : 0.392,
            "mag" : 2.872,
            "ss" : 2.872,
        }

        # 가변 변수들..
        self.config = {
            "models" : ["sss", "mag", "ss"],
            "types" : ["lift","winch"],
            "rpms" : ["100","200","300","400","500"],
            "lb_sss" : ["0","10cm","20cm","30cm","40cm"],
            "sss" : ["0","1","2","3","4"],
            "lb_mag" : ["0m","10m","15m","20m","25m"],
            "mag" : ["0","100","150","200","250"],
            "lb_ss" : ["0m","10m","15m","20m","25m"],
            "ss" : ["0","100","150","200","250"],
            "ports" : self.get_ports()
        }

        # 단위를 표기해야하는데 깔끔한 방법이 없을까?
        # self.config = {
        #     "models" : ["sss", "mag", "ss"],
        #     "types" : ["lift","winch"],
        #     "rpms" : ["100","200","300","400","500"],
        #     "sss" : ["0","1","2","3","4"],
        #     "mag" : ["0","100","150","200","250"],
        #     "ss" : ["0","100","150","200","250"],
        #     "ports" : self.get_ports()
        # }

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
    def run_winch(self,model : str):
        if self.serial_controller.is_connected(model):
            types = 'L' if model == 'sss' else 'W'
            rpm = int(getattr(self,f"cb_rpm_{model}").currentText()) // 100
            distance = int(self.check_radio(model)) * 100
            cw,distance = self.calculate_distance(model,distance)
            msg = [types, rpm, cw, distance]
            self.serial_controller.send_protocol(model,msg)
        else:
            False

    def stop_winch(self,model) -> None:
        self.serial_controller.send_protocol(model,['S'])


    def thread_func(self, model):
        try:
            while(True):
                if self.serial_controller.readable(model):
                    key = self.serial_controller.receive_msg(model)
                    if key:
                        msg = self.serial_controller.SER_MSG.get(key.decode(),key)
                        if msg == 'U':
                            self.distance[model] -= self.movement.get(model,0)
                        elif msg == 'D':
                            self.distance[model] += self.movement.get(model,0)
                        else:
                            QMetaObject.invokeMethod(getattr(self,f"te_{model}_state"), "setText", Qt.QueuedConnection,Q_ARG(str,str(msg)))
                    _distance =str(self.distance.get(model,'0')//1) + "mm"
                    QMetaObject.invokeMethod(getattr(self,f"te_{model}_distance"), "setText", Qt.QueuedConnection,Q_ARG(str,_distance))
                    self._write_distance(model)
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
            self._write_state(model,"연결 완료")
        elif self.serial_controller.disconnect_to_port(model):
            try:
                self.thread_controller.stop_to_thread(model)
            except:
                self._write_state(model,"쓰레드 해제 실패")
            button.setText("열기")
            self._write_state(model,"닫기 완료")


    def check_radio(self, model):
        for idx, value in enumerate(self.config[model]):
            if getattr(self,f"rb_{model}_{idx}").isChecked():
                return value
        return -1
    
    def get_ports(self):
            return [port.device for port in list_ports.comports()]

    def _set_config(self):
        for model in self.config["models"]:
            self._set_to_radio(f"rb_{model}", self.config['lb_'+model])
            self._add_to_combo(f"cb_rpm_{model}", self.config["rpms"])
            self._add_to_combo(f"cb_{model}", self.config["ports"])
            self._read_distance(model)

    def _add_to_combo(self,combo_name : str, items: list[str]) -> None:
        combobox = getattr(self,combo_name)
        combobox.clear()
        for item in items:
            combobox.addItem(item)

    def _set_to_radio(self,radio_name, items : list[str]) -> None:
        for idx,item in enumerate(items):
            getattr(self,f"{radio_name}_{idx}").setText(item)

    def _read_distance(self,model):
        items = os.listdir()
        if 'record' not in items:
            os.mkdir('record')
        path = f'./record/{model}.txt'
        with open(path,'r') as txt:
            if txt.readable():
                self.distance[model] = float(txt.read())
            else:
                self.distance[model] = 0

    def _write_distance(self,model):
        items = os.listdir()
        if 'record' not in items:
            os.mkdir('record')
        path = f'./record/{model}.txt'
        with open(path,'w') as txt:
                txt.write(str(self.distance.get(model,0)))


    def calculate_distance(self,model,distance) -> int:
        now = self.distance.get(model, 0)
        _cw = ""
        r_distance = 0
        # 현재보다 목표보다 작으면
        # 30mm > 20mm = 10mm U
        if now > distance:
            r_distance = now - distance
            _cw = 'U'
        # 20mm < 30mm
        elif now < distance:
            r_distance = distance - now
            _cw = 'D'
        elif now == distance or now == 0:
            return
        return _cw, int(r_distance)
    
    def _write_state(self, model : str, msg : str) -> None:
        state = getattr(self,f"te_{model}_state")
        state.setText(msg)


    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    serial_manager = SerialManager()
    thread_manager = ThreadManager()
    serial_controller = SerialController(serial_manager)
    thread_controller = ThreadController(thread_manager)
    main = Main(serial_controller, thread_controller)
    sys.exit(app.exec())