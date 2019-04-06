import itertools, random
# from math import ceil
#
# # list of competitors (does not need to be even, in this case, 7)
# # maybe this should be a dict with their wins and loses like:
# # {'Andy': [2,['Bob','Charlie'],0,[]], ... }
# # which means andy won 2 times, against bob and charlie, and lost 0 times
#
#
#
# # round handler
# def sort_matches(teams):
#     result = []
#     matches = itertools.combinations(teams, 2)
#     for match in matches:
#         result.append(match)
#     return result
#
# def sort_groups(team_list, limit_match_day = 3):
#     groups = {}
#     matches_played = []
#     #shuffle the teams
#     random.shuffle(team_list)
#     #retrive all matches
#     matches_list = sort_matches(team_list)
#     for i in range(1, len(matches_list)+1):
#         if len(matches_played) < len(matches_list):
#             groups['DATE-'+str(i)] = groups.get('Group-'+str(i), [])
#             random.shuffle(matches_list)
#             for match in matches_list:
#                 if len(groups['DATE-' + str(i)]) == limit_match_day:
#                     break
#                 if not team_in_matches(match, groups['DATE-'+str(i)]) and match not in matches_played:
#                     groups['DATE-' + str(i)] += [match]
#                     matches_played.append(match)
#     return groups
#
# def team_in_matches(match, list):
#     for l in list:
#         if match[0] in l or match[1] in l:
#             return True
#     return False
#
# competitors = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
#
# total = 0
# for date, match in sort_groups(competitors, ceil(len(competitors)/2)).items():
#     print(date, match, len(match), sep=": ")
#     total += len(match)
#
# print(total)

#!/usr/bin/python

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




