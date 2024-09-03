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
    counts = {i: 0 for i in range(1, 7)}

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
                Simulation.counts[dice.outcome] +=1

game1 = Simulation(50000, 2)
Simulation.get_game_results(game1)

print(f"     Num of dices: {game1.number_of_dices}. \n \
    Num of rolls: {game1.number_of_rolls} \n \
    Final Sum: {Simulation.final_sum} \n \
    Count of 1s: {Simulation.counts[1]} \n \
    Count of 2s: {Simulation.counts[2]} \n \
    Count of 3s: {Simulation.counts[3]} \n \
    Count of 4s: {Simulation.counts[4]} \n \
    Count of 5s: {Simulation.counts[5]} \n \
    Count of 6s: {Simulation.counts[6]} \n \
    sums_per_iteration: {list(Simulation.sums_per_iteration)}")

sorted_elements = list(sorted(set(Simulation.sums_per_iteration)))
count_of_each_outcome = [Simulation.sums_per_iteration.count(x) for x in sorted_elements]

title = plt.title("Bar Chart Dice Rolls")
plt.xlabel('Sums per Iteration')
plt.ylabel('Number of Rolls Per Outcome')

x = sorted_elements
y = count_of_each_outcome
print(list(Simulation.counts.items()))

plt.bar(x, y)
plt.show()
