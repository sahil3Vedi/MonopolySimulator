import random
from random import shuffle

PLACES="GO,Old Kent Road,COMMUNITY CHEST 1,Whitechapel Road,Income Tax,Kings Cross Station,The Angel Islington,CHANCE 1,Euston Road,Pentonville Road,JAIL,Pall Mall,Electric Company,Whitehall,Northumberland Avenue,Marylebon Station,Bow Street,COMMUNITY CHEST 2,Marlborough Station,Vine Street,Free Parking,The Strand,CHANCE 2,Fleet Street,Trafalgar Square,Fenchurch Street Station,Leicester Square,Coventry Street,Water Works,Piccadilly,GO TO JAIL,Regent Street,Oxford Street,COMMUNITY CHEST 3,Bond Street,Liverpool Street Station,CHANCE 3,Park Lane,Luxury Tax,Mayfair"

places=[]
for i in range(0,40):
    box=PLACES.split(",")[i]
    places.append(box)

places_count=[]
for i in range(0,40):
    places_count.append(0)

rolls=0

position=0

roll=[2,3,4,5,6,7,3,4,5,6,7,8,4,5,6,7,8,9,5,6,7,8,9,10,6,7,8,9,10,11,7,8,9,10,11,12]

toroll=10000000

default_chance=[]
default_community=[]
for i in range (0,15):
    default_chance.append(i)
    default_community.append(i)

chance=default_chance
community=default_community

doubles=0
three_doubles=0

k=0
j=0

while rolls<toroll:
    
    dice=int(36*random.random())
    move=roll[dice]

    position+=move
    position=position%40

    places_count[position]+=1

    if dice in [0,7,14,21,28,35]:
        doubles += 1
        toroll+=1
    else:
        doubles=0

    if doubles==3:
        position=10
        places_count[10]+=1
        three_doubles+=1

    if position==30:
        position=10
        places_count[10]+=1

    if position in (7,22,36):
        k+=1
        k=k%16
        if k==1:
            position=0
        elif k==2:
            position=24
        elif k==3:
            position=11
        elif k==4:
            if position in (36,22):
                position=28
            else:
                position=12
        elif k==5:
            if position==7:
                position=15
            elif position==22:
                position=25
            else:
                position=5
        elif k==8:
            position-=3
        elif k==9:
            position=10
        elif k==10:
            position=5
        elif k==11:
            position=39
        else:
            places_count[position]-=1
        places_count[position]+=1

    if position in (2,17,33):
        j+=1
        j=j%16
        if k==1:
            position=0
        elif k==6:
            position=10
        else:
            places_count[position]-=1
        places_count[position]+=1
        
    rolls+=1

for i in range(0,40):
    print(i," ",places[i],"--"," "*(40-len(places[i])-len(str(i))),"%.4f" %((places_count[i])*100/toroll),"%")

print("Number of rolls: ",toroll,"Number of triple double: ",three_doubles)

    







