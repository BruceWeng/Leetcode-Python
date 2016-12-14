import time

class Data:
    def __init__(self, value, duration):
        self.value = value
        self.duration = duration
        self.startTime = int(round(time.time()))

class ExpireMap:
    def __init__(self):
        self.map = {}

    def get(self, key):
        data = self.map[key]
        if data == None:
            return None

        currTime = int(round(time.time()))
        if currTime - data.startTime <= data.duration:
            return data.value
        else:
            del data

    def set(self, key, value, duration):
        data = Data(value, duration)
        self.map[key] = data



test1 = ExpireMap()
test1.set(1, 5, 3)
time.sleep(2)
print test1.get(1)
time.sleep(2)
print test1.get(1)
