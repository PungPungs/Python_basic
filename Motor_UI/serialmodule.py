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
        serial : Serial = self._serial_connections.get(model, None)
        if serial:
            serial.write(msg)
            return True
        else:
            return False
        
    def receive_message(self,model):
        serial : Serial= self._serial_connections.get(model, None)
        if serial:
            msg = serial.read(1)
            return msg
        else:
            return False
        
    def readable(self,model):
        serial : Serial= self._serial_connections.get(model, None)
        try:
            return True if serial.readable() else False
        except:
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
        list_size : 5
        types : lift or winch ['L' or 'W'], 1byte, unsigned char
        cw : up or down ['U' or 'D'], 1byte, unsigned char
        rpm : 0 ~ 500 [1 ~ 5], 1byte, unsigned char
        distance : 
            'W' -> 0 ~ 25m, 2byte, unsigned sort -> 0 ~ 25000 
            'L' -> 0 ~ 40cm, 2byte, unsigned sort -> 0 ~ 400
        0x2LD3
        """
        print(msg)
        byte_msg : List = []
        for i in range(len(msg)):
            if i == 4:
                byte_msg.append(struct.pack('H', msg[i]))  # 'H'는 unsigned short (2바이트)
            elif isinstance(msg[i], int):
                byte_msg.append(struct.pack('B', msg[i]))  # 'B'는 unsigned char (1바이트)
            elif isinstance(msg[i], str):
                byte_msg.append(struct.pack('c', msg[i].encode()))  # 'c'는 char (1바이트), encode() 필요
        if msg == ['S']:
            self.serial_manager.send_message(model,b'S')
            return True
        elif len(msg) < 4:
            return False
        else:
            byte_msg = b'\x02'+ byte_msg[0] + byte_msg[1] + byte_msg[2] + byte_msg[3] + byte_msg[4] + b'\x03'
            # byte_msg = b'\x02'+ struct.pack('<BBBBH',msg[0],msg[1],msg[2],msg[3],msg[4]) + b'\x03'
        self.serial_manager.send_message(model, byte_msg)
        return True
    
    def receive_msg(self,model):
        msg = self.serial_manager.receive_message(model)
        print(msg)
        True if msg else False

    def readable(self,model):
        return True if self.serial_manager.readable(model) else False