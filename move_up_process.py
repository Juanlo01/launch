from multiprocessing import Process, Value
from subprocess import call

class move_up:
    def __init__(self, shared_memory_object):
        self.shared_memory_object = shared_memory_object


    def run_loop(self):
        while self.shared_memory_object.running.value:
            #write code here
            self.can.move_up(6)
            self.can.send_command()
            
            #end
            pass
