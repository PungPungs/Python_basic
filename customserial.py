from serial import Serial
from abc import ABC, abstractmethod
from threading import Thread
# 각 윈치의 인스턴스 생성, 엔코더값 계산을 위한 쓰레드 생성
class SerialContructure(ABC):
    @abstractmethod
    def create_serial(self) -> Serial:
        pass

class SerialInterface(ABC):

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def _make_msg(self):
        pass

class SerialFactory(SerialContructure):
    @staticmethod
    def create_serial(port : str, baudrate : int = 9600) -> SerialInterface:
        return SerialModule(port, baudrate)

class SerialModule(SerialInterface):
    def __init__(self, port, baudrate):
        self.model = Serial(port, baudrate)

    def close(self):
        self.model.close()

    def start(self,msg : bytearray):
        self.model.write(msg)

    def stop(self, msg):
        self.model.write(msg)

    def _make_msg(self):
        pass

    