from itertools import permutations


def possible_permutations(elements):
    for perm in permutations(elements):
        yield list(perm)