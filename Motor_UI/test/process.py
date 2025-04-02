from serial import Serial
from threading import Thread
from multiprocessing import process, Queue
import multiprocessing

class Process:
    def __init__(self, q):
        self.q = q
        
    def receiver(q):
        proq = multiprocessing.current_process()
        model = Serial('COM7')
        while(1):
            if model.readable():
                data = model.read()
                q.put()

class Process_object:       
    def __init__(self):
        pass
    
    def get_data(self,q):
        proq = multiprocessing.current_process()
        model = Serial('COM7')
        while(1):
            if model.readable():
                data = model.read()
                q.put(data)


class Sender(Thread):
    def __init__(self,q):
        super().__init__()
        self.q = q

    def get_msg(self):
        data = self.q.get()
        print(data)
