import time,datetime
wait_seconds=60
timeout=time.time()+wait_seconds

print(timeout)
print(time.time())

if time.time()>timeout:
    print("ok")
    timeout=time.time()+wait_seconds
    print(timeout)
print(timeout)
print(time.time())    