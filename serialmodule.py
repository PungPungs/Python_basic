from serial import Serial


class SerialManager:
    def __init__(self):
        self.serial_connections = {}
    
    def get_serial(self ,model : str, port : str) -> bool:
        try:
            if model not in self.serial_connections:
                self.serial_connections[model] = Serial(port=port)
                return True
        except Exception as e:
            print(e)
            return False
       
    def close_serial(self, model : str) -> bool:
        try:
            if model in self.serial_connections:
                self.serial_connections[model].close()
                del self.serial_connections[model]
        except Exception as e:
            print(e)
            return False

    def is_connected(self, model) -> bool:
        return model in self.serial_connections

class SerialController():
    def __init__(self ,serial_manager : SerialManager):
        self.serial_manager = serial_manager

    def connection(self, model : str, port : str):
        return False if self.serial_manager.is_connected(model) else self.serial_manager.get_serial(model,port)