# coding:utf-8

'''
Module: uclDrawCal
Created on 2016-12-8
@author: Ring
'''


import itertools


class team:
    
    def __init__(self, teamName="", teamGroup="", teamCountry="", teamRanking="1"):
        self.name = teamName
        self.group = teamGroup
        self.country = teamCountry
        self.ranking = teamRanking
    
    def printTeam(self):
        print (self.name, "-",  self.country, "-", self.group+self.ranking)
    

def isDrawCorrect(list1, list2):
    for i in range(0,8):
        if (list2[i].group == list1[i].group) or (list2[i].country == list1[i].country):
            return False
    return True


def getProbabilityByTeam(list1, list2, allResult2, index):
    print ('\n',list1[index].name)
    totalCount = 0
    proList = {
               list2[0].name:0, list2[1].name:0, list2[2].name:0, list2[3].name:0, \
               list2[4].name:0, list2[5].name:0, list2[6].name:0, list2[7].name:0
               }
    for someResult in allResult2:
        if isDrawCorrect(list1, someResult):
            totalCount += 1
            proList[someResult[index].name] += 1
        else:
            pass
    for i in range(0, 8):
        print ("draw: ", list2[i].name+": ", proList[list2[i].name]*1.0/totalCount)


A1 = team("Arsenal", "A", "England", "1")
B1 = team("Napoli", "B", "Italy", "1")
C1 = team("Barcelona", "C", "Spain", "1")
D1 = team("ATM", "D", "Spain", "1")
E1 = team("Monaco", "E", "France", "1")
F1 = team("Dortmund", "F", "Germany", "1")
G1 = team("Leicester City", "G", "England", "1")
H1 = team("Juventus", "H", "Italy", "1")
A2 = team("Paris Saint Germain", "A", "France", "2")
B2 = team("Benfica", "B", "Portugal", "2")
C2 = team("Man City", "C", "England", "2")
D2 = team("Bayern Munich", "D", "Germany", "2")
E2 = team("Lerverkusen", "E", "Germany", "2")
F2 = team("Real Madrid", "F", "Spain", "2")
G2 = team("Porto", "G", "Portugal", "2")
H2 = team("Sevilla", "H", "Spain", "2")

listFirst = [A1, B1, C1, D1, E1, F1, G1, H1]
listSecond = [A2, B2, C2, D2, E2, F2, G2, H2]
firstAllResult = list(itertools.permutations(listFirst, len(listFirst)))
secondAllResult = list(itertools.permutations(listSecond, len(listSecond)))


def main():
    for i in range(0, 8):
        getProbabilityByTeam(listFirst, listSecond, secondAllResult, i)
    for j in range(0, 8):
        getProbabilityByTeam(listSecond, listFirst, firstAllResult, j)


main()
