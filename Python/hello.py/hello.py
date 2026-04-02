import hashlib


def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()


def build_merkle_tree(data_list):
    nodes = [hash_data(item) for item in data_list]

    while len(nodes) > 1:
        new_level = []

        for i in range(0, len(nodes), 2):
            left = nodes[i]
            right = nodes[i + 1] if i + 1 < len(nodes) else left

            combined = hash_data(left + right)
            new_level.append(combined)

        nodes = new_level

    return nodes[0]