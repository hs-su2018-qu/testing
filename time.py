from datetime import datetime


time = str(datetime.now())
time = "_".join(time.split())
print(time)
