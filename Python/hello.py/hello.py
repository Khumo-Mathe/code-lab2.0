from collections import defaultdict


def map_function(data):
    results = []

    for line in data:
        words = line.split()

        for word in words:
            results.append((word, 1))

    return results


def reduce_function(mapped_data):
    result = defaultdict(int)

    for word, count in mapped_data:
        result[word] += count

    return dict(result)


def map_reduce(data_chunks):
    mapped = []

    for chunk in data_chunks:
        mapped.extend(map_function(chunk))

    return reduce_function(mapped)