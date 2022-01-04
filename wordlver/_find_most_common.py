from collections import Counter
from collections import defaultdict


def get_most_common_word(positions: dict, rank: int = 1) -> str:
    most_common: defaultdict = defaultdict(dict)

    for position in positions.keys():
        counter: Counter = Counter(positions[position])
        counter_length: int = len(counter)
        c_rank = rank if (counter_length + 1) > rank else counter_length
        most_common[position] = counter.most_common(c_rank)[c_rank - 1][0]

    return "".join(c for c in most_common.values())
