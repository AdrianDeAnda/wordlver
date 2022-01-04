# Worldver

## Python script to help solve [Wordle puzzles](https://www.powerlanguage.co.uk/wordle/)


[![Continuous Integration](https://github.com/AdrianDeAnda/wordlver/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/AdrianDeAnda/wordlver/actions/workflows/ci.yml) [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit) <a href="https://github.com/psf/black"> <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

---

## *_This is just for fun, not guaranteed to work. WIP_*


### Usage:

To get the most common characters for each position:

```python
python main.py
```

To get the second, third, etc common characters for each position:

```python
python main.py --rank 2
python main.py --rank 3
```

To get most common characters after the word has been solved partially:


```python
python main.py --word "__o_s"
```

This flag will also print all the possible words with those characters in that positions.

It can algo be combined with the rank flag:

```python
python main.py --word "__o_s" --rank 2
```
