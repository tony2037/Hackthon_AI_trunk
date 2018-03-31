from multiprocessing import Process
from multiprocessing import Pool
import os ,time

def aaa():
    #time.sleep(1)
    for i in range(10):
        print("aaa")
def bbb():
    for i in range(10):
        print("bbb")
if __name__=='__main__':
    p = Pool()
    p.apply_async(aaa)
    p.apply_async(bbb)
    p.close()
    p.join()
