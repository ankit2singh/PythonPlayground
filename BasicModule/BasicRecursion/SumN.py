# functional recusrsion, most Imprtant

def sumn(N):
    if N == 1:
        return 1
    
    return N + sumn(N-1)

print(sumn(5))