'''
Created on Nov 4, 2013

@author: Songfan
'''
from __future__ import division
from queue import Queue
from random import randrange
import numpy as np


##### printer class #####
class Printer():
 
    def __init__(self, speed):
        self.speed = speed
        self.queue = Queue()
    
    def isIdle(self):
        return self.queue.isEmpty()
    
    def addTask(self, t):
        self.queue.enqueue(t)
        
    def removeTask(self):
        if not self.queue.isEmpty():
            return self.queue.dequeue()
    
    def getQueueSize(self):
        return self.queue.size()
    
    def getTimeToFinishCurrentTask(self):
        if self.queue.isEmpty():
            return 0
        else:
            return self.queue.peek().getPage() / float(self.speed)
        
##### Task class #####
class Task():
    def __init__(self,current_time):
        self.pages = self.__setPage()
        self.create_time = current_time
    
    def __setPage(self):
        return randrange(1,21)
    
    def getPage(self):
        return self.pages
    
    def getProcessTime(self,current_time):
        return current_time - self.create_time
    
    
    
    
def newPrintTask():
    return randrange(1,181)==180
    

##### Simulation class #####
class PrintingSimulation():
    def __init__(self, total_time, printer_speed):
        self.total_time = total_time
        self.printer_speed = printer_speed
        
    def getAverageWaitTime(self):
        p = Printer(self.printer_speed)
        waitTime = []
        for current_time in range(self.total_time):
            if(newPrintTask()):
                t = Task(current_time)
                p.addTask(t)
                if 'time_to_finished_current_task' not in locals():
                    time_to_finished_current_task = p.getTimeToFinishCurrentTask()
                elif time_to_finished_current_task > 0:
                    time_to_finished_current_task -= 1
                else:
                    t_out = p.removeTask()
                    waitTime.append(t_out.getProcessTime(current_time))
                    time_to_finished_current_task = None
            elif 'time_to_finished_current_task' in locals():
                if time_to_finished_current_task > 0:
                    time_to_finished_current_task -= 1
                else:
                    t_out = p.removeTask()
                    waitTime.append(t_out.getProcessTime(current_time))
                    time_to_finished_current_task = None ;.
            current_time += 1
        return np.mean(waitTime)
                

p = PrintingSimulation(3600, 100)
print p.getAverageWaitTime()
    
    