from random import choice
DIRECTIONS = [1, -1]
DISTANCE = [0, 1, 2, 3, 4]
class RandomWalk:
    """A class to generate random walks"""
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
    
    #Refactoring, haciendolo mas simple

    def get_step(self):
        direction = choice(DIRECTIONS)
        distance = choice (DISTANCE)
        step = direction * distance
        return step

    def next_steps(self):
        while True:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step != 0 and y_step !=0:
                return (x_step, y_step)

    def fill_walk(self):
        """Calculate all the points in the walk"""
        for _  in range(self.num_points -1):
            x_step, y_step = self.next_steps()
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

        # while len(self.x_values) < self.num_points:
        #     x_direction = choice([1, -1])
        #     x_distance = choice([0, 1, 2, 3, 4])
        #     x_step = x_direction * x_distance

        #     y_direction = choice([1, -1])
        #     y_distance = choice([0, 1, 2, 3, 4])
        #     y_step = y_direction * y_distance

        #     if x_step == 0 and y_step == 0:
        #         continue 
        
        #     x = self.x_values[-1] + x_step
        #     y = self.y_values[-1] + y_step

        #     self.x_values.append(x)
        #     self.y_values.append(y)