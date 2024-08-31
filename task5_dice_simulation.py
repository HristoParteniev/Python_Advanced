"""imports"""
import random
from matplotlib import pyplot as plt


class Dice:
    """ class Dice is used to create object dice"""

    def __init__(self) -> None:
        self.side = None
        self.values = [1, 2, 3, 4, 5, 6]
        self.outcome = None

    def roll_the_dice(self):
        """function setting outcome after rolling the dice"""
        self.outcome = random.choice(self.values)

class Simulation:
    """class Simulation is used to create a game"""

    final_sum = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0

    sums_per_iteration = []

    def __init__(self, number_of_rolls: int, number_of_dices: int) -> None:
        self.number_of_rolls = number_of_rolls
        self.number_of_dices = number_of_dices
        self.dices = [Dice() for _ in range (self.number_of_dices)]

    def get_game_results(self):
        """function to roll the dices n times"""
        for _ in range(self.number_of_rolls):
            current_sum = 0
            for dice in self.dices:
                dice.roll_the_dice()
                current_sum += dice.outcome

            Simulation.sums_per_iteration.append(current_sum)

            for dice in self.dices:
                Simulation.final_sum += dice.outcome
                if dice.outcome == 1:
                    Simulation.count_1 += 1
                elif dice.outcome == 2:
                    Simulation.count_2 += 1
                elif dice.outcome == 3:
                    Simulation.count_3 += 1
                elif dice.outcome == 4:
                    Simulation.count_4 += 1
                elif dice.outcome == 5:
                    Simulation.count_5 += 1
                elif dice.outcome == 6:
                    Simulation.count_6 += 1

game1 = Simulation(50000, 2)
Simulation.get_game_results(game1)

print(f"     Num of dices: {game1.number_of_dices}. \n \
    Num of rolls: {game1.number_of_rolls} \n \
    Final Sum: {Simulation.final_sum} \n \
    Count of 1s: {Simulation.count_1} \n \
    Count of 2s: {Simulation.count_2} \n \
    Count of 3s: {Simulation.count_3} \n \
    Count of 4s: {Simulation.count_4} \n \
    Count of 5s: {Simulation.count_5} \n \
    Count of 6s: {Simulation.count_6} \n \
    sums_per_iteration: {list(Simulation.sums_per_iteration)}")

sorted_elements = list(sorted(set(Simulation.sums_per_iteration)))
count_of_each_outcome = [Simulation.sums_per_iteration.count(x) for x in sorted_elements]

title = plt.title("Bar Chart Dice Rolls")
plt.xlabel('Sums per Iteration')
plt.ylabel('Number of Rolls Per Outcome')

x = sorted_elements
y = count_of_each_outcome

plt.bar(x, y)
plt.show()
