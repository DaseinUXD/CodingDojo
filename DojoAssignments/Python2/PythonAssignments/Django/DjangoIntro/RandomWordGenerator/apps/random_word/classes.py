class attemptCounter(object):
    def __init__(self, count):
        self.count = count


    def increment(self):
        self.count = self.count + 1
        return self

    def reset(self):
        self.reset = 0
        return self
