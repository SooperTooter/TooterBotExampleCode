import random


def swap_mutation(chromosome):
    chromosome_list = list(chromosome)  # Convert the string to a list of characters
    pos1, pos2 = random.sample(range(len(chromosome)), 2)  # Choose two random positions in the chromosome
    chromosome_list[pos1], chromosome_list[pos2] = chromosome_list[pos2], chromosome_list[pos1]  # Swap the characters at the chosen positions
    return ''.join(chromosome_list)  # Convert the list back to a string and return it


old_chromosome = "123456789"
new_chromosome = swap_mutation(old_chromosome)
print(new_chromosome)