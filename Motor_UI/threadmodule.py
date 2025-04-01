# 추후 사용 예정
from threading import Thread

class ThreadManager:

    def __init__(self):
        self._thread_connections = {}


    def connect(self,model : str, func):
        if model not in self._thread_connections:
            self._thread_connections[model] = Thread(daemon=True,target=func, args=[model])
            module = self._thread_connections.get(model, None)
            return module.start()
        else:
            print("생성된 쓰레드가 존재합니다.")
            return False
    
    def join_thread(self,model : str):
        self._thread_connections.get(model,None).join()
        del self._thread_connections[model]

class ThreadController:
    def __init__(self, thread_manager : ThreadManager):
        self._thread_manager = thread_manager

    def start_to_thread(self,model, func):
        return self._thread_manager.connect(model, func)
    
    def stop_to_thread(self,model):
        self._thread_manager.join_thread(model)