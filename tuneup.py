#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Jordan Davidson"

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    def decorator(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        stats = pstats.Stats(pr)
        stats.sort_stats('cumulative')
        stats.print_stats()
        return result
    return decorator


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False

@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    movieDict = {}
    for movie in movies:
        if movie not in movieDict:
            movieDict[movie] = 1
        else:
            movieDict[movie] += 1
    for movie in movieDict:
        if movieDict[movie] > 1:
            duplicates.append(movie)
    return duplicates

def timeit_helper():
    t = timeit.Timer(stmt='main()', setup='import tuneup')
    res = t.repeat(repeat=7, number=3)
    return 'best timing of 7 repeats of 3 runs per repeat: {} sec'.format(min(res) / 3)


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))
    print(timeit_helper())


if __name__ == '__main__':
    main()