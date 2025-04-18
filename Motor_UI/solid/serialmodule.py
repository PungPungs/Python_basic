from serial import Serial
import struct
from typing import List
import time


class SerialManager:
    def __init__(self):
        self._serial_connections = {}

    def connect(self ,model : str, port : str) -> bool:
        try:
            if model not in self._serial_connections:
                self._serial_connections[model] = Serial(port=port,timeout=1, baudrate=9600)
                time.sleep(2)
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
                'D' : 'D',
                'C' : '긴급 정지'

            }
    def __init__(self ,serial_manager : SerialManager):
        self.serial_manager = serial_manager

    def is_connected(self, model):
        '''
        모델의 이름을 가진 시리얼 연결 여부 확인
        '''
        return True if self.serial_manager.is_connected(model) else False

    def connect_to_port(self, model : str, port : str) -> bool:
        '''
        모델의 이름을 가진 시리얼 인스턴스 생성
        '''
        if self.serial_manager.is_connected(model):
            return False
        else:
            if self.serial_manager.connect(model,port):
                return True
            return False
        
    def disconnect_to_port(self,model):
        '''
        연결 해제
        '''
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
        """
        byte_msg : List = []
        if msg == ['S']:
            self.serial_manager.send_message(model,b'S')
            return True
        else:
            for i in range(len(msg)):
                if i == 3:
                    byte_msg.append(struct.pack('>H', msg[i]))  # 'H'는 unsigned short (2바이트)
                elif isinstance(msg[i], int):
                    byte_msg.append(struct.pack('B', msg[i]))  # 'B'는 unsigned char (1바이트)
                elif isinstance(msg[i], str):
                    byte_msg.append(struct.pack('c', msg[i].encode()))  # 'c'는 char (1바이트), encode() 필요
            middle_msg = b''.join(byte_msg)
            byte_msg = b'\x02'+ struct.pack('B', len(middle_msg)) + middle_msg + b'\x03'
            # byte_msg = b'\x02'+ struct.pack('<BBBBH',msg[0],msg[1],msg[2],msg[3],msg[4]) + b'\x03'
            self.serial_manager.send_message(model, byte_msg)
            return True
    
    def receive_msg(self,model):
        '''
        메세지 수신
        '''
        msg = self.serial_manager.receive_message(model)
        return msg if msg else None

    def readable(self,model):
        return True if self.serial_manager.readable(model) else False