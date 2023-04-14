import random


def mutation(chromosome):
    mutated_chromosome = chromosome[:]  # Make a copy of the chromosome
    i = random.randint(0, len(mutated_chromosome)-1)  # Randomly select a digit to mutate
    mutated_digit = random.randint(0, 9)  # Generate a random digit
    mutated_chromosome = mutated_chromosome[:i] + str(mutated_digit) + mutated_chromosome[i+1:]  # Replace the mutated digit in the chromosome
    return mutated_chromosome


old_chromosome = "123456789"
new_chromosome = mutation(old_chromosome)
print(new_chromosome)
