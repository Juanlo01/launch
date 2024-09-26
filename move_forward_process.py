from multiprocessing import Process, Value
from motor.MotorWrapper import Can_Wrapper
from subprocess import call
import time

class MoveForward:
    def __init__(self, shared_memory_object):
        self.shared_memory_object = shared_memory_object
        self.move_matrix = [6, 0, 0, 0, 0, 0]
        # self.max iterations = 10000000
        self.can = Can_Wrapper()


    def run_loop(self):
        while self.shared_memory_object.running.value:
            start = time.time()

            #if times ran is divisible by 10, go forward, else do nothing
            if self.shared_memory_object.iterations.value % 10 == 0:
                #update shared memory
                for i in range(6):
                    #setting each value individually
                    self.shared_memory_object.motor_values[i] += self.move_matrix[i]
                
                #update motor wrapper from shared memory
                self.can.move_from_matrix(self.shared_memory_object.motor_values)
        
            end = time.time()
            if (.05 - (end - start)) > .0:
                time.sleep(.05 - (end - start))
                self.shared_memory_object.iterations.value += 1

            self.can.send_command()

            #end
            pass
