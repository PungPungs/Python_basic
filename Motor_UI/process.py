from multiprocessing import Process, Queue
import multiprocessing


class ProcessHandler:
    def __init__(self, name, target):
        self.name = name
        self.target = target
        que = Queue()
        self.que = que
        p = Process(name=self.name, target=self.target, args=(self.que,), daemon=True)
    
