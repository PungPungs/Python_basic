# 추후 사용 예정
from threading import Thread

class ThreadManager:

    def __init__(self):
        self.thread_connections = {}


    def get_thread(self,model : str, func):
        self.thread_connections[model] = Thread(daemon=True,target=func(model))
        module = self.thread_connections.__getitem__(model)
        module.start()
    
    def join_thread(self,model : str):
        self.thread_connections[model].join()

    def __getItem__(self,model):
        return self.thread_connections.get(model)

class ThreadController:
    def __init__(self, thread_manager : ThreadManager):
        self.thread_manager = thread_manager

    def connection(self,model, func):
        self.thread_manager.get_thread(model, func)

