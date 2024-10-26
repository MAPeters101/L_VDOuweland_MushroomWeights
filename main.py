import random

mushroom_weights = [34, 101, 120, 86, 112, 76, 21, 212, 653, 234, 122, 84, 312, 77, 54, 21]

# Initialize
population_count = 20 # Combinations to choose the best solution from.
rounds = 1  # Evolutions count
chromosomes = [[random.choice([True, False]) for _ in mushroom_weights] for _ in range(population_count)]

for r in range(rounds):
    print(f"=== ROUND {r}, population {len(chromosomes)} ===")

