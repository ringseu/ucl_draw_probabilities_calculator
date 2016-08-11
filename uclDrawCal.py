# coding:utf-8

'''
Module: uclDrawCal

Created on 2015-12-10

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
    for i in range(0,7):
        if (list2[i].group == list1[i].group) or (list2[i].country == list1[i].country):
            return False
    return True


def getProbabilityByTeam(list1, list2, allResult2, index):
    print (list1[index].name)
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
    for i in range(0, 7):
        print ("draw: ", list2[i].name, "  probability: ", proList[list2[i].name]*1.0/totalCount)


realmadrid = team("Real Madrid", "A", "Spain", "1")
wolfsburg = team("Wolfsburg", "B", "Germany", "1")
atmadrid = team("A.T.Madrid", "C", "Spain", "1")
mancity = team("Man City", "D", "England", "1")
barcelona = team("Barcelona", "E", "Spain", "1")
bayernmunich = team("Bayern Munich", "F", "Germany", "1")
chelsea = team("Chelsea", "G", "England", "1")
zenit = team("Zenit", "H", "Russia/Ukraine", "1")
paris = team("Paris Saint Germain", "A", "France", "2")
psv = team("PSV", "B", "Holland", "2")
benfica = team("Benfica", "C", "Portugal", "2")
juventus = team("Juventus", "D", "Italy", "2")
roma = team("Roma", "E", "Italy", "2")
arsenal = team("Arsenal", "F", "England", "2")
kyiv = team("Dinamo Kyiv", "G", "Russia/Ukraine", "2")
gent = team("Gent", "H", "Danmark", "2")

listFirst = [realmadrid, wolfsburg, atmadrid, mancity, barcelona, bayernmunich, chelsea, zenit]
listSecond = [paris, psv, benfica, juventus, roma, arsenal, kyiv, gent]
firstAllResult = list(itertools.permutations(listFirst, len(listFirst)))
secondAllResult = list(itertools.permutations(listSecond, len(listSecond)))


def main():
    for i in range(0, 7):
        getProbabilityByTeam(listFirst, listSecond, secondAllResult, i)
    for j in range(0, 7):
        getProbabilityByTeam(listSecond, listFirst, firstAllResult, j)


main()
