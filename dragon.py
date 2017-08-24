import random
import time

def displayIntro():
    print('''You wake up one morning and find yourself in a land full of dragons. In front of you, you see two caves. In one cave, you think the dragon is friendly and will share her treasure with you. But if you choose wrong, the other dragon is grumpy, and he will probably eat you on sight.''')
    print()
    
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave do you choose? (1 or 2)')
        cave = input()
    return cave
    
def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('You hope this wasn\'t a mistake....')
    time.sleep(2)
    print('A large dragon jumps out in front of you! You stumble backwards! Is this the end?')
    print()
    time.sleep(2)
    
    friendlyCave = random.randint(1, 2)
    
    if chosenCave == str(friendlyCave):
        print('The dragon smiles and welcomes you inside! She tells you her name is Gwendolyn, offers you some tea, and gives you some of her treasure! She also complains about her neighbor in the cave next door who sometimes eats her guests. You suggest that perhaps she put a sign outside her cave so that her future visitors don\'t get eaten. She thanks you for the brilliant idea, and gives you some extra treasure in appreciation before you leave. She invites you to visit any time.')
    else:
        print('Oh no!\n\nThe dragon looms over you...\n\nopens his enormous jaw with pointy sharp teeth and fiery breath...\n\nand gobbles you up in one delicious bite!\n\n')
        time.sleep(2)
        print('The end.')
        
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    
    print('Do you want to play again? (yes or no)')
    playAgain = input()
    