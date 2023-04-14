import random


def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1)-1)  # Randomly select a crossover point
    child = parent1[:crossover_point] + parent2[crossover_point:]  # Join parts of two parent chromosomes
    return child


parent1 = "123456789"
parent2 = "ABCDEFGHI"
print(crossover(parent1, parent2))