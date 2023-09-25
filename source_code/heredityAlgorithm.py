#heredityAlgorithm

import random as r

def createNewRandomChromosome():    #랜덤 염색체 생성
    newRandomChromosome = []
    for i in range(112):
        newRandomChromosome.append(r.randrange(2))
    return newRandomChromosome

def createNewRandomPopulation():    #랜덤 개체군 생성
    newRandomPopulation = []
    for i in range(16):
        newIndividual = []
        for j in range(2):
            newIndividual += [createNewRandomChromosome()]
        newRandomPopulation += [newIndividual]
    return newRandomPopulation

def createNextPopulation(oldPopulation):    #다음세대 개체군 생성
    nextPopulation = []
    surviveIdxList=[]
    mainIndividual = breeding(oldPopulation[0], oldPopulation[1])
    nextPopulation+=[mainIndividual]
    
    oldIdxList = [i for i in range(16)]
    for i in range(15):
        newone = []
        parent = r.sample(oldIdxList, 2)
        father = oldPopulation[parent[0]]
        mother = oldPopulation[parent[1]]
        newone = breeding(father, mother)
        nextPopulation.append(newone)
    return nextPopulation

def breeding(individual1, individual2): #두 개체를 인자로 받은 후 교배시킨 새로운 개체 반환
    newIndividual = []
    newIndividual.append(individual1[r.randrange(2)])
    newIndividual.append(individual2[r.randrange(2)])
    return newIndividual

def selectIndividual(population):   #미로 개체군 속 처음을 제외한 15개의 미로 중 하나의 미로 선택
    selectedIndividual=[]
    randomSelectIdx = r.randrange(1, 16)
    selectedIndividual = population[randomSelectIdx]
    return selectedIndividual

def phenotype(individual):  #개체의 표현형 리스트 반환
    pheno=[]
    for i in range(112):
        decide = 0
        for chromosome in individual:
            if chromosome[i] == 1:
                decide += 1
        if decide == 1:
            pheno.append(1)
        else:
            pheno.append(0)
    return pheno
