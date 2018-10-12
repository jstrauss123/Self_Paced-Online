# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 12:35:18 2018

@author: Laura.Fiorentino
"""
import random
file = open('hound_small.txt', 'r', encoding='utf8')
# file = open('testbook.txt', 'r')
lines = file.readlines()
del lines[:38]
word_list = []
for line in lines:
    for word in line.split():
        word_list.append(word)
word_dict = {}
for it in range(len(word_list)-2):
    if word_list[it] + ' ' + word_list[it+1] in word_dict:
        word_dict[word_list[it] + ' ' +
                  word_list[it+1]].append(word_list[it+2])
    else:
        word_dict[word_list[it] + ' ' + word_list[it+1]] = [word_list[it+2]]
word_list_new = ['Holmes', 'leaned']
word_key = word_list_new[0] + ' ' + word_list_new[1]
n=1
while True:
    if word_key not in word_dict:
        break
    word_list_new.append(random.choice(word_dict[word_key]))
    word_key =  word_list_new[n] + ' ' + word_list_new[n+1]
    n=n + 1
file.close()

new_book = ' '.join(word_list_new)