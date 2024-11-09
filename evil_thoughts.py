import random

'''
this is a program that randomly match actors and 
actresses for having sex with each other in various postures.
Let's go!
'''

# select some lucky ones(I kind of hate actors but not actresses in my opinion for love ot mine to the beauty ：） except Yang Li)
actors = ["Hua Chenyu", "Xiao zhan", "Fan Chenchen", "Wang Yibo", "Wang Heli", "YiYang Qianxi", "Chen Linong", "Wang Junkai"]
actresses = ["Yang Li - Assole", "Liu Yifei", "Yang Mi", "Zhou Ye", "Song Yi", "Fan Bingbing", "Zhang Tianai", "Jin Chen"]
sexPositions = ["Doggy", "Missionary", "Cowgirl", "Reverse cowgirl", "Spooning", "69", "Scissoring", "Prone boning", "Oral", "mutual maz", ]

numberOfActors = len(actors)
numberOfActresses = len(actresses)
pairingResults = set()
def pairThem():
    print("-------------------------------------------------------------------------------------------------------------------\n\n\n\n")

    for actor in actors:
        actressSeleted = random.choice(actresses)
        pairingResults.add(f"{actressSeleted} is being fucked by {actor} in the {random.choice(sexPositions)} position! What an exciting scene!")
        actresses.remove(actressSeleted)
    for pair in pairingResults:
        print(pair + "\n")

    numberOfPairingResults = len(pairingResults)
    print("\n\n")
    print(f"The Number of Actors: {numberOfActors}")
    print(f"The Number of Actresses: {numberOfActresses}")
    print(f"The Number of pairing esults: {numberOfPairingResults}")
    print("-------------------------------------------------------------------------------------------------------------------\n\n\n\n")
pairThem()
