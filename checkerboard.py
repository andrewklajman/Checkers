import pygame

RES = (800,400)
SIZE = 4

cDim = int(RES[0]/SIZE)
rDim = int(RES[1]/SIZE)


[print((c,r),end=',') for r in range(0,RES[1], rDim * 2) for c in range(0,RES[0], cDim * 2)]
print()

##[print((c + ,r),end=',') for r in range(0,RES[1], rDim * 2) for c in range(0,RES[0], cDim * 2)]
##print()

##[print(r,end=',') for r in range(0,RES[1], rDim * 2)]
##print()

##[print((c,0),end=',') for c in range(0,RES[0], cDim * 2)]
##print()





