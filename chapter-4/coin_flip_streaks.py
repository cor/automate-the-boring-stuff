import random
from statistics import mean

# Generate a sequence of 100 'H' (Heads) and 'T' (Tails) throws
# and return the amount of 6-long chains of the same value
def experiment():
    flip_results = random.choices(('H', 'T'), k=100)
    streak_count = 0
    for i in range(len(flip_results)-6):
        if (flip_results[i] == 'H' and 'T' not in flip_results[i:i+6]) or \
           (flip_results[i] == 'T' and 'H' not in flip_results[i:i+6]):
            streak_count += 1
    return streak_count

results = []
for i in range(10_000):
    results.append(experiment())

print(mean(results))