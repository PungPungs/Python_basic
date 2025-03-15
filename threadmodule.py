# 추후 사용 예정
from threading import Thread

class ThreadManager:
    def __init__(self):
        self.thread_connections = {}

    def get_thread(self,model : str):
        self.thread_connections[model] = Thread(daemon=True)
        self.thread_connections[model].start()

    def join_thread(self,model : str):
        self.thread_connections[model].join()