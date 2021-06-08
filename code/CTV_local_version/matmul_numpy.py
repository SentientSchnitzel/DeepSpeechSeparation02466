import os
import time
import numpy as np

n = 1
if os.environ.get('OPENBLAS_NUM_THREADS'):
    n = os.environ.get('OPENBLAS_NUM_THREADS')
compute_hardware = f'(CPU, num_threads: {n})'


start_total = time.time()

N = int(2000)
A = np.ones([N, N])
B = np.zeros([N, N])


start_matmul = time.time()
reps = 50
for _ in range(reps):
	C = np.matmul(A, B)
	
end = time.time()
t_matmul = (end-start_matmul)*1e3
t_total = (end-start_total)

print(f'Time to process: \t {t_matmul/reps:.2f} ms/matmul \t ({t_total:.2f} s total) \t {compute_hardware}')



