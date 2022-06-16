from os import sched_param
import random


list_one = ["bottle","pizza","phone","app", "plant", "hack", "kim kardashian"]
list_two = ["screams","cries","scratch","stops","guesses", "hacks"]

word_one = random.randint(0,len(list_one))
word_two = random.randint(0,len(list_two))

print ("the worst idea possible a {word_one} that {word_two}")
