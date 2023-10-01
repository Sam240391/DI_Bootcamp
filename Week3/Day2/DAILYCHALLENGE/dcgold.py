import random

class Gene:
    def __init__(self):
        self.value = random.randint(0, 1)

    def mutate(self):
        self.value = 1 - self.value

class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]

    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.5:  # 50% chance to flip each gene
                gene.mutate()

    def __str__(self):
        return "".join(str(gene.value) for gene in self.genes)

class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]

    def mutate(self):
        for chromosome in self.chromosomes:
            if random.random() < 0.5:  # 50% chance to flip each chromosome
                chromosome.mutate()

    def __str__(self):
        return " ".join(str(chromosome) for chromosome in self.chromosomes)

class Organism:
    def __init__(self, dna, environment_prob):
        self.dna = dna
        self.environment_prob = environment_prob
        self.generations = 0

    def mutate(self):
        if random.random() < self.environment_prob:
            self.dna.mutate()
        self.generations += 1

    def has_only_ones(self):
        return all(gene.value == 1 for chromosome in self.dna.chromosomes for gene in chromosome.genes)

# Simulation
environment_prob = 0.02  # Probability for DNA to mutate in the environment
population_size = 50    # Number of organisms in the population

organisms = [Organism(DNA(), environment_prob) for _ in range(population_size)]

# Main loop
while True:
    for organism in organisms:
        organism.mutate()
        if organism.has_only_ones():
            print(f"Generations needed to reach all ones DNA: {organism.generations}")
            break
    else:
        continue  # No organism reached the goal, continue looping
    break