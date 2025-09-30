import random

def generate_startup_names(n=5):
    adjectives = ["Quantum", "Neural", "Hyper", "Aero", "Cyber", "Fusion", "Eco", "Nano", "Meta", "Ultra"]
    nouns = ["Labs", "Systems", "Dynamics", "Tech", "Analytics", "Solutions", "Cloud", "Works", "Networks", "Forge"]

    names = []
    for _ in range(n):
        name = f"{random.choice(adjectives)} {random.choice(nouns)}"
        names.append(name)

    return names

# Example usage
if __name__ == "__main__":
    print(generate_startup_names(7))
