import random

def roll_dice(num_rolls=5):
    """
    Simulates rolling a six-sided die multiple times.
    Returns a dictionary with each face value and how many times it appeared.
    """
    results = {i: 0 for i in range(1, 7)}  # Initialize counts for each face (1–6)

    for _ in range(num_rolls):
        roll = random.randint(1, 6)  # Roll a number between 1 and 6
        results[roll] += 1  # Increment count for that face

    return results


def analyze_results(results):
    """
    Analyzes the results to find:
    - The most rolled number
    - The least rolled number
    """
    most_common = max(results, key=results.get)
    least_common = min(results, key=results.get)

    return {
        "most_common": most_common,
        "least_common": least_common,
        "results": results
    }


# Example usage
if __name__ == "__main__":
    rolls = roll_dice(20)  # Roll the dice 20 times
    stats = analyze_results(rolls)

    # Display results neatly
    print("🎲 Dice Roll Results:")
    for face, count in stats["results"].items():
        print(f"Face {face}: {count} times")

    print(f"\nMost Rolled: {stats['most_common']}")
    print(f"Least Rolled: {stats['least_common']}")

