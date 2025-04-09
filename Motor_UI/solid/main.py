from motorui import Ui_MainWindow
from serialmodule import SerialController, SerialManager
from threadmodule import ThreadManager, ThreadController
from serial.tools import list_ports
from PySide6.QtWidgets import QMainWindow, QApplication
import sys
from PySide6.QtCore import QMetaObject, Q_ARG, Qt
from model import Model
from filemanager import TxtManager
from typing import List
from config import UiConfig

class Main(Ui_MainWindow, QMainWindow):
    def __init__(self, serial_controller : SerialController, thread_controller : ThreadController, txt_manager : TxtManager):
        super().__init__()
        self.setupUi(self)
        self.serial_controller = serial_controller
        self.thread_controller = thread_controller
        self.txt_manager = txt_manager

        # 가변 변수들..
        self.config = UiConfig(port=self.get_ports())

        self.models = {
            "sss" : Model("sss",["0","10cm","20cm","30cm","40cm"], ["0","1","2","3","4"], 0.392),
            "mag" : Model("mag",["0m","10m","15m","20m","25m"], ["0","1","2","3","4"], 2.872),
            "ss" : Model("ss",["0m","10m","15m","20m","25m"], ["0","1","2","3","4"], 2.872)
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
    def run_winch(self,model : str):
        try:
            if self.serial_controller.is_connected(model):
                types = 'L' if model == 'sss' else 'W'
                rpm = int(getattr(self,f"cb_rpm_{model}").currentText()) // 100
                distance = int(self.check_radio(model)) * 100
                cw, distance = self.models[model].calculate_distance(distance)
                msg = [types, rpm, cw, distance]
                self.serial_controller.send_protocol(model,msg)
        except Exception as e:
            self._write_state(model, e)

    def stop_winch(self,model) -> None:
        self.serial_controller.send_protocol(model,['S'])


    def thread_func(self, model):
        try:
            while(True):
                if self.serial_controller.readable(model):
                    key = self.serial_controller.receive_msg(model)
                    if key:
                        msg = self.serial_controller.SER_MSG.get(key.decode(),key)
                        if self.models[model].update_distance(msg) == False:
                            QMetaObject.invokeMethod(getattr(self,f"te_{model}_state"), "setText", Qt.QueuedConnection,Q_ARG(str,str(msg)))
                    _distance =str(self.models[model].distance//1) + "mm"
                    QMetaObject.invokeMethod(getattr(self,f"te_{model}_distance"), "setText", Qt.QueuedConnection,Q_ARG(str,_distance))
                    self.txt_manager.save(model,_distance)
                if not self.serial_controller.is_connected(model):
                    return
        except:
            pass
        
    def open_and_close(self, model):
        port = getattr(self, f"cb_{model}").currentText()
        if self.serial_controller.connect_to_port(model, port):
            self._open(model)
        elif self.serial_controller.disconnect_to_port(model):
            self._close(model)

    def _open(self, model : str) -> bool | str:
        try:
            button = getattr(self, f"pb_{model}")
            button.setText("닫기")
            self.thread_controller.start_to_thread(model,self.thread_func)
            self._write_state(model,"연결 완료")
        except Exception as e:
            self._write_state(model,e)

    def _close(self, model : str) -> bool | str:
        try:
            button = getattr(self, f"pb_{model}")
            self.thread_controller.stop_to_thread(model)
            button.setText("열기")
            self._write_state(model,"닫기 완료")
        except Exception as e:
            self._write_state(model,e)

    def check_radio(self, model):
        for idx, value in enumerate(self.models[model].value_list):
            if getattr(self,f"rb_{model}_{idx}").isChecked():
                return value
        self._write_state(model, "거리를 선택해주세요")
        return -1
    
    def get_ports(self) -> List[str]:
            return [port.device for port in list_ports.comports()]

    def _set_config(self):
        for model in self.models:
            self._set_to_radio(f"rb_{model}", self.models[model].label_list)
            self._add_to_combo(f"cb_rpm_{model}", self.config.rpm)
            self._add_to_combo(f"cb_{model}", self.config.port)
            _distance = self.txt_manager.load(model)
            if _distance is not False:
                self.models[model].distance = _distance
            else:
                self._write_state(model,"거리 불러오기 실패")
    


    def _add_to_combo(self,combo_name : str, items: list[str]) -> None:
        combobox = getattr(self,combo_name)
        combobox.clear()
        for item in items:
            combobox.addItem(item)

    def _set_to_radio(self,radio_name, items : list[str]) -> None:
        for idx,item in enumerate(items):
            getattr(self,f"{radio_name}_{idx}").setText(item)


    def _write_state(self, model : str, msg : str) -> None:
        state = getattr(self,f"te_{model}_state")
        state.setText(msg)

if __name__== "__main__":
    app = QApplication(sys.argv)
    main = Main(SerialController(SerialManager()), ThreadController(ThreadManager()), TxtManager())
    sys.exit(app.exec())