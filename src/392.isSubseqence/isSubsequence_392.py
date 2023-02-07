# https://leetcode.com/problems/is-subsequence/?envType=study-plan&id=level-1
# description amd other conditions - ./392.isSubsequence.ipynb

def isSubsequence(firstString: str, secondString: str) -> bool:
    indexFirstString, indexSecondString = 0, 0
    lengthFisrtString, lengthSecondString = len(firstString), len(secondString)
    while (indexFirstString < lengthFisrtString) and (indexSecondString < lengthSecondString):
        if firstString[indexFirstString] == secondString[indexSecondString]:
            indexFirstString += 1
        indexSecondString += 1
    
    return indexFirstString == lengthFisrtString


isSubsequence("abd","asdbfdgc")