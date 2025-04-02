import multiprocessing
import multiprocessing.process


class ProcessManager:
    def __init__(self):
        self._processing_connections = {}


    def connect(self,model : str, func):
        if model not in self._processing_connections:
            self._processing_connections[model] = multiprocessing.Process(daemon=True)
            module = self._processing_connections.get(model, None)
            return module.start()
        else:
            print("생성된 프로세스가 존재합니다.")
            return False
    
    def join_process(self,model : str):
        self._processing_connections.get(model,None).join()
        del self._processing_connections[model]

class ProcessController:
    def __init__(self, process_manager : ProcessManager):
        self._process_manager = process_manager

    def start_to_process(self,model, func):
        return self._process_manager.connect(model, func)
    
    def stop_to_process(self,model):
        self._process_manager.join_process(model)

