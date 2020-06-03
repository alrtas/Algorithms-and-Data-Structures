import fastPowering as f
import time

start_time = time.time()

print(f.naiveAlgorithm(2, -2))

print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()

print(f.fastPowering(3, 100))

print("--- %s seconds ---" % (time.time() - start_time))

