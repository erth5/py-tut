import time

while True:
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print(result)
    time.sleep(1)

# Outputs:
#02: 10:50
#PM
#02: 10:51
#PM