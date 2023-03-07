import copy
import random
# Consider using the modules imported above.

def bals_dict_to_list(balls):
    res = []
    for ball, amount in balls.items():
        res.extend([ball] * amount)
    return res

class Hat:
    def __init__(self, **kwargs):
        self.contents = bals_dict_to_list(kwargs)

    def draw(self, balls_to_draw_number):
        self.balls_removed = []
        for i in range(balls_to_draw_number):
            if len(self.contents) != 0:
                idx = random.randrange(len(self.contents))
                self.balls_removed.append(self.contents.pop(idx))
            else:
                break
        return self.balls_removed
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    matches = 0
    expected_balls_list = bals_dict_to_list(expected_balls)
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        temp = hat_copy.draw(num_balls_drawn)
        temp_len = len(temp)
        for ball in expected_balls_list:
            if ball in temp:
                temp.remove(ball)
                
        if temp_len - len(temp) == len(expected_balls_list):
            matches += 1
    return matches/num_experiments
    



# hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
# probability = experiment(hat=hat,
#                   expected_balls={"yellow":2,"blue":3,"test":1},
#                   num_balls_drawn=20,
#                   num_experiments=100)
# print(probability)
