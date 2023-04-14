import random


def crossover(parent1, parent2, parent3):
    crossover_point = random.randint(1, len(parent1)-1)  # Randomly select a crossover point
    child_intermediate = parent1[:crossover_point] + parent2[crossover_point:]  # Join parts of two parent chromosomes
    crossover_point = random.randint(1, len(parent1) - 1)  # Randomly select a crossover point again
    child = child_intermediate[:crossover_point] + parent3[crossover_point:]  # Join the third parent
    return child


parent1 = "123456789"
parent2 = "ABCDEFGHI"
parent3 = "!@#$%^&*("
print(crossover(parent1, parent2, parent3))