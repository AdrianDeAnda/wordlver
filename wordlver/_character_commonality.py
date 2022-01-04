from collections import defaultdict


def get_common_characters(words_list: list) -> dict:
    positions: defaultdict = defaultdict(list)

    for word in words_list:
        for idx, c in enumerate(word):
            positions[idx] += c

    return positions
