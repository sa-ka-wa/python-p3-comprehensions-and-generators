#!/usr/bin/env python3

def return_evens(num_list):
    # if num_list != 0:
    #     return []
    # if num_list % 2 == 0:
        return [num for num in num_list if num % 2 == 0]
    # pass

def make_exclamation(sentence_list):
    # if sentence_list != 0:
    #     return []
    # if sentence_list[-1] != '!':
        return [sentence + "!" for sentence in sentence_list]
    # pass