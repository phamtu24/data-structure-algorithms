from multiprocessing import Process, Value, Array
import time

def f():
    for _ in range(10):
        time.sleep(1)
        print('1s')

def run():
    processes = []
    for _ in range(10):
        f()

        
run()