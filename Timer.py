import time

class Timer:
    def __init__(self, time):
        self.time = time
        
    # def countdown(self):
    #     while self.time > 0:
    #         print(self.time)
    #         self.time -= 1
    #         time.sleep(1)
    #     print("Time's up!")
    
    def update(self):
        self.time -= 1

    def reset(self, time):
        self.time = time

#timer = Timer(15)
#timer.countdown()
