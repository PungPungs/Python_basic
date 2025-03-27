from serial import Serial
import struct
from typing import Optional, List
class SerialManager:
    def __init__(self):
        self._serial_connections = {}    

    def connect(self ,model : str, port : str) -> bool:
        try:
            if model not in self._serial_connections:
                self._serial_connections[model] = Serial(port=port,timeout=1)
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
        serial : Serial= self._serial_connections.get(model, None)
        if serial:
            msg = serial.read()
            print(msg)
            print("msg")
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
        """
        types : lift or winch ['L' or 'W'], 1byte, unsigned char
        cw : up or down ['U' or 'D'], 1byte, unsigned char
        rpm : 0 ~ 500 [1 ~ 5], 1byte, unsigned char
        distance : 
            'W' -> 0 ~ 25m, 2byte, unsigned sort -> 0 ~ 25000 
            'L' -> 0 ~ 40cm, 2byte, unsigned sort -> 0 ~ 400
        0x2LD3
        """
        if msg == ['S']:
            self.serial_manager.send_message(model,b'S')
            return True
        elif len(msg) < 5:
            return False
        else:
            byte_msg = b'0x2'+ struct.pack("BBBBH",msg[0],msg[1],msg[2],msg[3],msg[4]) + b'0x3'
            # byte_msg = b'0x2'+ struct.pack("B",msg[0]) + struct.pack("B",msg[1]) + struct.pack("B",msg[2]) + struct.pack("B",msg[3]) + struct.pack("H",msg[4]) + b'0x3'
        self.serial_manager.send_message(model, byte_msg)
        return True
    
    def receive_msg(self,model):
        msg = self.serial_manager.receive_message(model)
        print(msg)
        True if msg else False