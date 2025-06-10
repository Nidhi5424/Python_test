class Counter:


    def __init__(self):
        self.count = 0


    def getData(self):
       for i in range(10):
        self.count += 1
        print("Count is:", self.count)

s1 = Counter()

s1.getData()


