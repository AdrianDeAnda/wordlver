from wordlver._constants import words


def get_possible_words(words_list: dict) -> list:
    possible_words: list = []

    for w in words:
        if all(c in w[position] for position, c in words_list.items()):
            possible_words.append(w)

    return possible_words
