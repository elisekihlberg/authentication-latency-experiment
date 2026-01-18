import hashlib
import time
import statistics

ITERATIONS = 1000

def simple_auth():
    username = "user"
    password = "password123"
    return username == "user" and password == "password123"

def lightweight_auth():
    password = "password123"
    hashed = hashlib.sha256(password.encode()).hexdigest()
    verify = hashlib.sha256(hashed.encode()).hexdigest()
    return verify is not None

def heavy_auth():
    value = b"password123"
    for _ in range(1000):
        value = hashlib.sha256(value).digest()
    return value is not None

def measure_latency(func):
    times = []
    for _ in range(ITERATIONS):
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        times.append((end - start) * 1000)
    return times

simple_times = measure_latency(simple_auth)
light_times = measure_latency(lightweight_auth)
heavy_times = measure_latency(heavy_auth)

print("Simple auth mean latency (ms):", statistics.mean(simple_times))
print("Lightweight auth mean latency (ms):", statistics.mean(light_times))
print("Heavy auth mean latency (ms):", statistics.mean(heavy_times))

