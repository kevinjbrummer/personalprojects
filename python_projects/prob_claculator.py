import random
import copy

class Hat:
    
    def __init__(self, **kwargs):
        self.contents = []
        for k,v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, n):
        balls = []
        if n >= len(self.contents):
            balls = self.contents
            self.contents = []
            return balls
        else:
            while n > 0:
                rand = random.randint(0, len(self.contents)-1)
                balls.append(self.contents[rand])
                del self.contents[rand]
                n = n -1
            return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    runs = 0
    while runs != num_experiments:
        clone_hat = copy.deepcopy(hat)
        balls = clone_hat.draw(num_balls_drawn)
        result = False
        for k,v in expected_balls.items():
            counter = 0
            for i in balls:
                if i == k:
                    counter = counter + 1
            if counter >= v:
                result = True
            else:
                result = False
                break
        if result:
            successes = successes + 1
        runs = runs + 1
    return successes/num_experiments

hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1},
                         num_balls_drawn=4, num_experiments=10)
print(probability)
