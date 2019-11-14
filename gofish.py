# Your code for Go Fish goes here
# 
import random 
deck=['goldfish','goldfish','goldfish','goldfish','catfish','catfish','catfish','catfish','trout','trout','trout','trout','grouper','grouper','grouper','grouper','tuna','tuna','tuna','tuna','salmon','salmon','salmon','salmon','sturgeon','sturgeon','sturgeon','sturgeon','piranha','piranha','piranha','piranha','swordfish','swordfish','swordfish','swordfish','clownfish','clownfish','clownfish','clownfish']
dict={'goldfish':1,'catfish':2,'trout': 1,'grouper': 1,'tuna': 2,'salmon': 2, 'sturgeon': 2,'piranha': 3,'swordfish': 4,'clownfish': -1}
random.shuffle(deck)
player=[]
ai=[]
player_score=0
ai_score=0
i=0
for i in deck[:7]:
    player.append(i)
    deck.remove(i)

for i in deck[:7]:
    ai.append(i)
    deck.remove(i)
    
player_collection=[]
ai_collection=[]

for i in player:
    player.remove(i)
    if i in player:
        player_collection.append(i)
        player.remove(i)
    else:
        player.append(i)
            
for i in ai:
    ai.remove(i)
    if i in ai:
        ai_collection.append(i)
        ai.remove(i)
    else:
        ai.append(i)           
            
            
print('You have a pair of: ') 
print(player_collection)
print('The computer has a pair of: ')
print(ai_collection)

while player.count(i) > 0 or ai.count(i) > 0 or deck.count(i) > 0 :
    print('Your hand is: ')
    print(player)
    print('Your collection is: ')
    print(player_collection)

    ask = input('Pick a card to ask for: ')
    print('You ask the computer for a ') 
    print(ask)

    if ask in ai:
        player_collection.append(ask)
        player_collection.append(ask)
        ai.remove(ask)
        player.remove(ask)
        print('The computer has a: ')
        print(ask)
        print('You now have a pair of: ')
        print(ask)
    else:
        print('Go Fish!')
        i=deck.pop(0)
        player.append(i)
        print('You draw a: ')
        print(i)
#       deck.pop(0)
#        for i in player:
#           player.remove(i)
        if player.count(i)>1:
            print('You have a pair of: ')
            print(i)
            player_collection.append(i)
            player_collection.append(i)
            player.remove(i)
            player.remove(i)
        else:
            player.append(i)

    ask = ai[0]

    print('The computer asks you for a: ') 
    print(ask)      
    if ask in player:
        ai_collection.append(ask)
        ai.remove(ask)
        player.remove(ask)
        print('You give the computer your: ')
        print(ask)
        print('The computer now has a pair of: ')
        print(ask)
    else:
        print('Go Fish!')
        i=deck.pop(0)
        ai.append(i)
        deck.pop(0)
        print('The computer draws a card.')
        if ai.count(i)>1:
            ai_collection.append(i)
            ai_collection.append(i)
            ai.remove(i)
            ai.remove(i)
            print('The computer has a pair of: ')
            print(i)
        else:
            ai.append(i)
print('You are out of cards')
print('Your collection is: ', player_collection)


def weightedsum(l,d):
    sum=0
    for e in l:
        sum=sum+d[e]
    return sum

player_score=weightedsum(player_collection,dict)
print('Your score is: ',player_score)

print('The computer collection is: ', player_collection)
ai_score=weightedsum(ai_collection,dict)
print('The computer score is: ',player_score)

if player_score > ai_score:
    print('You win!')
else:    
    print('You lose!')



      


        
                        


  
    
