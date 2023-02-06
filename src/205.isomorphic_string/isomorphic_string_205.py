# https://leetcode.com/problems/isomorphic-strings/?envType=study-plan&id=level-1
# description amd other conditions - ./205.isomorphic_string.ipynb

def isIsomorphic(s: str, t: str) -> bool:
    mapS2T, mapT2S = {}, {}
    for indexS, indexT in zip(s,t):
        if ((indexS in mapS2T and mapS2T[indexS] != indexT) or
            (indexT in mapT2S and mapT2S[indexT] != indexS)):
            return False 
        mapS2T[indexS] = indexT
        mapT2S[indexT] = indexS
    return True

isIsomorphic("egg","add")