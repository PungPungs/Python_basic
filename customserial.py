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
    def send(self):
        pass

class SerialFactory(SerialContructure):
    @staticmethod
    def create_serial(port : str, baudrate : int = 9600) -> SerialInterface:
        return SerialModule(port, baudrate)

class SerialModule(SerialInterface):
    def __init__(self, port : str, baudrate : int):
        self.model = Serial(port = port, baudrate = baudrate)

    def send(self,msg = b"A") -> bytearray:
        self.model.write(msg)

    def close(self,msg) -> None:
        self.model.close()