from serial import Serial
import struct
from typing import Optional, List
class SerialManager:
    def __init__(self):
        self._serial_connections = {}    

    def connect(self ,model : str, port : str) -> bool:
        try:
            if model not in self._serial_connections:
                self._serial_connections[model] = Serial(port=port)
                return True
        except Exception as e:
            print(e)
            return False
       
    def close_serial(self, model : str) -> bool:
        try:
            if model in self._serial_connections:
                self._serial_connections[model].close()
                del self._serial_connections[model]
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def is_connected(self, model) -> bool:
        return model in self._serial_connections and self._serial_connections[model].is_open
    
    def send_message(self,model, msg):
        serial = self._serial_connections.get(model, None)
        if serial:
            serial.write(msg)
            return True
        else:
            return False
        
    def receive_message(self,model):
        serial = self._serial_connections.get(model, None)
        if serial:
            msg = serial.read()
            return msg
        else:
            return False
    
class SerialController():
    SER_MSG = {
                'B' : '모터 시작',
                'S' : '모터 정지',
                'E' : '모터 이동 완료',
                'U' : 'U',
                'D' : 'D'
            }
    def __init__(self ,serial_manager : SerialManager):
        self.serial_manager = serial_manager

    def is_connected(self, model):
        return True if self.serial_manager.is_connected(model) else False

    def connect_to_port(self, model : str, port : str) -> bool:
        if self.serial_manager.is_connected(model):
            return False
        else:
            if self.serial_manager.connect(model,port):
                return True
            return False
        
    def disconnect_to_port(self,model):
        return True if self.serial_manager.close_serial(model) else False
    



    def send_protocol(self, model : str, msg : List) -> bool:
        # [길이, ,속도, 이동거리]
        if msg == ['S']:
            self.serial_manager.send_message(model,b'S')
            return True
        elif len(msg) < 4:
            return False
        else:
            byte_msg = b'0x2'+ struct.pack(">BBBI",msg[0],msg[1],msg[2],msg[3]) + b'0x3'
        self.serial_manager.send_message(model, byte_msg)
        return True
    
    def receive_msg(self,model):
        msg = self.serial_manager.receive_message(model)
        True if msg else False