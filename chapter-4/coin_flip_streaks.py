import random
from statistics import mean


# For more implementations of this problem, including a test runner that check which one is the fastest, see:
# https://github.com/cor/drudgery
# for an implementation of this problem in Rust, see:
# https://github.com/cor/coin-flip-streaks-rs


# Generate a sequence of 100 'H' (Heads) and 'T' (Tails) throws
# and return the amount of 6-long chains of the same value
def experiment():
    flip_results = "".join(random.choices(('H', 'T'), k=100))
    streak_count = 0
    for i in range(len(flip_results) - 6):
        streak_count += (flip_results[i:i + 6] == flip_results[i] * 6)
    return streak_count


results = []
for _ in range(10_000):
    results.append(experiment())

print(mean(results))
