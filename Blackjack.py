#Random lib for selecting random cards
import random

def check(a):
    """To check if user has ace card i.e '11' and sum is greater than 21
then consider value of ace as '1' """
    for i in a:
        if i==11 and sum(a)>21:
            a[a.index(11)]=1
    return a

def checkcom(a,deck):
    """TO check is computer has cards that has sum less tha '16'
    the he will pick up cards from deck """
    while sum(a)<16:
        a.append(random.choice(deck))
    return a
        
def blackjack(): 
    """deck contains cards such as 11 for ace 
    and last three 10 for king, queen and jack"""     
    deck=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    user,comp=[],[]
    for i in range(2):
        user.append(random.choice(deck))
        comp.append(random.choice(deck))
    print(f"Your cards {user}   Opponent cards [{comp[0]}]")
    while True:
        if sum(check(user))>21:
            print("you lose")
            print(f"Your cards {user}   Opponent cards {comp}")
            break
        elif sum(check(user))==21 and sum(check(checkcom(comp,deck)))==21:
            print("draw")
            print(f"Your cards {user}   Opponent cards {comp}")
            break
        elif sum(check(user))==21 and sum(check(checkcom(comp,deck)))<21:
            print("you won")
            print(f"Your cards {user}   Opponent cards {comp}")
            break
        elif sum(check(comp))==21 and sum(check(user))<21:
            print("you lose")
            print(f"Your cards {user}   Opponent cards {comp}")
            break
        inp=input("press hit or stand: ")
        if inp=="hit":
            user.append(random.choice(deck))
            print(f"Your cards {user}   Opponent cards [{comp[0]}]")
        elif inp=="stand":
            if sum(check(checkcom(comp,deck)))>21:
                print("you won")
                print(f"Your cards {user}   Opponent cards {comp}")
                break
            elif sum(check(user))>sum(check(checkcom(comp,deck))):
                print("you won")
                print(f"Your cards {user}   Opponent cards {comp}")
                break
            elif sum(check(user))<sum(check(checkcom(comp,deck))):
                print("you lose")
                print(f"Your cards {user}   Opponent cards {comp}")
                break
            elif sum(check(user))==sum(check(checkcom(comp,deck))):
                print("Draw")
                print(f"Your cards {user}   Opponent cards {comp}")
                break
        else:
            print("Please choose the correct option")

inpu="yes"
while inpu=="yes":
   print()
   blackjack()
   print()
   inpu=input("Do you want to play more press yes or no: ")


