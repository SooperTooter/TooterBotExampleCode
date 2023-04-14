import random


def two_point_crossover(parent1, parent2):
    crossover_points = sorted(random.sample(range(1, len(parent1)), 2))  # Randomly select two crossover points and sort them
    child = parent1[:crossover_points[0]] + parent2[crossover_points[0]:crossover_points[1]] + parent1[crossover_points[1]:]  # Join parts of two parent chromosomes at two points
    return child


parent1 = "123456789"
parent2 = "ABCDEFGHI"
print(two_point_crossover(parent1, parent2))