import multiprocessing as mp
import time
import itertools

def f(x, y, result_dict):
    for i in x:
        time.sleep(1)
        result_dict[i+y] = i+y

if __name__ == '__main__':
    start = time.perf_counter()
    result = mp.Manager()
    result_dict = result.dict()
    p1 = mp.Process(target=f, args=([1, 2], 1000, result_dict))
    p2 = mp.Process(target=f, args=([3, 4], 1000, result_dict))
    p1.start()
    p2.start()
    a = p1.join()
    b = p2.join()
    print(result_dict.values())
    finish = time.perf_counter()
    print(f'finish in {finish - start} seconds')

