import random

mushroom_weights = [34, 101, 120, 86, 112, 76, 21, 212, 653, 234, 122, 84, 312, 77, 54, 21]

# Initialize
population_count = 20 # Combinations to choose the best solution from.
rounds = 1  # Evolutions count
chromosomes = [[random.choice([True, False]) for _ in mushroom_weights] for _ in range(population_count)]

class Weighted:
    max_weight = 1300  # grams
    def __init__(self, mushroom_weights, chromosome):
        self.mushrooms_in_bag = [w for w, c in zip(mushroom_weights, chromosome) if c is True]
        self.total_weight = sum(self.mushrooms_in_bag)
        if self.total_weight > self.max_weight:
            self.total_weight = 0

    def __lt__(self, other):
        # Rule: less difference between max_weight and total_weight, results in higher ranking.
        return self.max_weight - self.total_weight < self.max_weight - other.total_weight

for r in range(rounds):
    print(f"=== ROUND {r}, population {len(chromosomes)} ===")
    weighted = [Weighted(mushroom_weights, chromosome) for chromosome in chromosomes]
    for w in sorted(weighted):
        print(w.total_weight)




