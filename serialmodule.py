from serial import Serial

class SerialManager:
    def __init__(self):
        self._serial_connections = {}
    
    def get_serial(self ,model : str, port : str) -> bool:
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
        except Exception as e:
            print(e)
            return False

    def is_connected(self, model) -> bool:
        return model in self._serial_connections
    
    def get_serial_instance(self,model):
        return self._serial_connections.get(model, None)

class SerialController():
    def __init__(self ,serial_manager : SerialManager):
        self.serial_manager = serial_manager

        self.ser_msg = {
            'B' : '모터 시작',
            'S' : '모터 정지',
            'E' : '모터 이동 완료',
            'U' : 'U',
            'D' : 'D'
        }
    def connection(self, model : str, port : str) -> bool:
        return False if self.serial_manager.is_connected(model) else self.serial_manager.get_serial(model,port)
    
    # thread target func
    def only_read(self, model):
        count = 0
        while(self.serial_manager.is_connected(model)):
            serial = self.serial_manager.get_serial_instance(model)
            if serial.in_waiting > 0:
                key = serial.read().decode('utf-8')
                msg = self.ser_msg.get(key)
                if msg:
                    print(msg)
                else:
                    print(key)