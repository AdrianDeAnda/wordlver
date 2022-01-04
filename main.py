from argparse import ArgumentParser
from collections import defaultdict
from typing import Sequence

from wordlver import get_common_characters
from wordlver import get_most_common_word
from wordlver import get_possible_words
from wordlver import words


def get_most_probable_characters(rank: int = 1, words_list: list = words) -> str:
    positions: dict = get_common_characters(words_list)
    return get_most_common_word(positions, rank)


def main(argv: Sequence[str] | None = None) -> int:
    args_rank: int = 1
    words_list_input: list = words

    parser = ArgumentParser()
    parser.add_argument("--rank", type=int, required=False)
    parser.add_argument("--word", type=str, required=False)
    arguments = parser.parse_args(argv)

    if arguments.rank:
        args_rank = arguments.rank

    if arguments.word:
        words_1: defaultdict = defaultdict()

        for idx, c in enumerate(arguments.word):
            if c != "_":
                words_1[idx] = c

        words_list_input = get_possible_words(words_1)
        print(f"Possible words list: {words_list_input}")

    print(
        f"Most common characters (in rank {args_rank}): {get_most_probable_characters(args_rank, words_list_input)}"
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
