import itertools, random

div1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, 21,22,23,24,25]
random.shuffle(div1)
times = ['08:00', '09:00', '10:00', '11:00']
days = ['SAT', 'SUN']

available_dates = list(itertools.product(days, times))
print(available_dates)

def create_schedule(list):
    """ Create a schedule for the teams in the list and return it"""
    s = []
    rounds = {}

    if len(list) % 2 == 1: list = list + [len(list)]

    for i in range(len(list)-1):

        mid = int(len(list) / 2)
        l1 = list[:mid]
        l2 = list[mid:]
        l2.reverse()

        # Switch sides after each round
        if(i % 2 == 1):
            s = s + [ zip(l1, l2) ]
        else:
            s = s + [ zip(l2, l1) ]
        list.insert(1, list.pop())
    for n, round in enumerate(s):
        rounds["ROUND - " + str(n + 1)] = []
        for match in round:
            rounds["ROUND - " + str(n + 1)] += [match]
    return rounds




