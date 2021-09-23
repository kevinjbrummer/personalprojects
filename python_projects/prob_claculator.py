import random
import copy

#The goal of this project is to have a class called Hat that will initialize with
#any number of colored balls, which are defined by user. Then, it will create a list
#called contents that will write out the color of the ball, equal to the value, and put
#it in a list. 
class Hat:
    
    def __init__(self, **kwargs):
        self.contents = []
        for k,v in kwargs.items():
            for i in range(v):
                self.contents.append(k)
                
#The draw function will take out a number of balls, n, and take them out 
#without replacing them. It will return a list containing the balls taken
#out of hat.contents.

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

#Finally, we have the experiment function. This will run a number of experiemnts,
#num_experiments, and find out how many times the expected balls are drawn from 
#the hat. Then it will compare the number of successes to the number of 
#experiments and return the probability of pulling the expected balls.
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
