moin
import random
import time

playGame = 'start'
HowToPlay = 'rules'
Play = '0'
Solve = random.randint(7,7)
Number = random.randint(1,50)
NumberTry = 0
city = 0
location = 0
LocationCity = 0



def displayIntro():

      print('You are a worldwide known detective, who can solve any complicated case.\n'
            'One beautiful day you get a mysterious letter from an anonymous person.\n'
            '\n'
            'Hello Mr. Smith,\n'
            'I have a very interesting but even for you unsolveable case.\n'
            'I kidnapped my neighbour and hided her at a safe and unfoundable place. A bomb is hided near at her. In 2 hours it will detonate.\n'
            'If you will find her (what you wont), I will accept my loss. If not, than she will die and you will loos your reputation.\n'
            'I wish you good luck.\n'
            'Yours sincerly.\n'
            'Mr.X\n')

def Olympia(location):
    if location == Solve:
        print('You enter the Olympiastadion and hear a terrible scream...')
        time.sleep(2)
        print('You enter the football pitch...')
        time.sleep(2)
        print(
            'And see a woman with her arms and legs bound together. Next to her you see a little teddybear, which is probably the bomb.\n'
            'You enter the football pitch and liberate the woman. "Thank you very much, Mr. Smith. You saved my life", she screams.\n'
            'No problem, but we have to defuse the bomb. Lets see...\n'
            'You extract the bomb carefully out of the teddy bear. It is a "Guess-a-number"-bomb.\n'
            'You have to guess a number between 1 and 50 in 5 tries to extract the bomb, otherwise it will detonate.\n'
            'Try and pick a number between 1 and 50.')
        NumberTry = int(input())
        if NumberTry == Number:
            print(
                'Hurray!!! You found the number. You saved a beautiful woman and (more importantly) the Elbe Philharmonic Hall.\n'
                'Congratulations!\n')
    else:
        print('You enter the Olympiastadion and hear a terrible scream...')
        time.sleep(2)
        print('You enter the football pitch...')
        time.sleep(2)
        print(
            'And see a stadium full of people celebrating a goal for their team.\n'
            'Bloody hell...Lets look for another location.\n'
            'Type 5 to look at the Television Tower, 2 to fly to Hamburg or 3 to fly to Munich')
        LocationCity = int(input())
        if LocationCity == 5:
            TV()
        if LocationCity == 2:
            Hamburg()
        if LocationCity == 3:
            Munich()

def TV(location):
    if location == Solve:
        print('You enter the Television Tower and hear a terrible scream...')
        time.sleep(2)
        print('You enter the highest floor of the Tower...')
        time.sleep(2)
        print(
            'And see a woman with her arms and legs bound together. Next to her you see a little teddybear, which is probably the bomb.\n'
            'You enter the floor and liberate the woman. "Thank you very much, Mr. Smith. You saved my life", she screams.\n'
            'No problem, but we have to defuse the bomb. Lets see...\n'
            'You extract the bomb carefully out of the teddy bear. It is a "Guess-a-number"-bomb.\n'
            'You have to guess a number between 1 and 50 in 5 tries to extract the bomb, otherwise it will detonate.\n'
            'Try and pick a number between 1 and 50.')
        NumberTry = int(input())
        if NumberTry == Number:
            print(
                'Hurray!!! You found the number. You saved a beautiful woman and (more importantly) the Elbe Philharmonic Hall.\n'
                'Congratulations!\n')
    else:
        print('You enter the Television Tower and hear a terrible scream...')
        time.sleep(2)
        print('You enter the highest floor of the tower...')
        time.sleep(2)
        print(
            'And see a woman screaming because of her height anxiety.\n'
            'Man oh man...Lets look for another location.\n'
            'Type 4 to look at the Olympiastadion, 2 to fly to Hamburg or 3 to fly to Munich')
        LocationCity = int(input())
        if LocationCity == 4:
            Olympia()
        if LocationCity == 2:
            Hamburg()
        if LocationCity == 3:
            Munich()

def Elphi(location):
    if location == Solve:
        print('You enter the Elbe Philharmonic Hall and hear a terrible scream...')
        time.sleep(2)
        print('You open the door to the concert hall...')
        time.sleep(2)
        print(
        'And see a woman with her arms and legs bound together. Next to her you see a little teddybear, which is probably the bomb.\n'
        'You enter the concert hall and liberate the woman. "Thank you very much, Mr. Smith. You saved my life", she screams.\n'
        'No problem, but we have to defuse the bomb. Lets see...\n'
        'You extract the bomb carefully out of the teddy bear. It is a "Guess-a-number"-bomb.\n'
        'You have to guess a number between 1 and 50 in 5 tries to extract the bomb, otherwise it will detonate.\n'
        'Try and pick a number between 1 and 50.')
        NumberTry = int(input())
        if NumberTry == Number:
            print(
            'Hurray!!! You found the number. You saved a beautiful woman and (more importantly) the Elbe Philharmonic Hall.\n'
            'Congratulations!\n')
    else:
        print('You enter the Elbe Philharmonic Hall and hear a terrible scream...')
        time.sleep(2)
        print('You open the door to the concert hall...')
        time.sleep(2)
        print(
        'And see a concert hall full of people and a stout woman in a beautiful dress on the stage screaming for her life.\n'
        'Well...that was nothing. Lets look for another location.\n'
        'Type 7 to look at the Dungeon, 1 to fly to Berlin or 3 to fly to Munich')
        LocationCity = int(input())
        if LocationCity == 7:
            Dungeon()
        if LocationCity == 1:
            Berlin()
        if LocationCity == 3:
            Munich()

def Dungeon(location):
    if location == Solve:
        print('You enter the Dungeon and hear a terrible scream...')
        time.sleep(2)
        print('You open the door to the prison room...')
        time.sleep(2)
        print(
        'And see a woman with her arms and legs bound together. Next to her you see a little teddybear, which is probably the bomb.\n'
        'You enter the prison room and liberate the woman. "Thank you very much, Mr. Smith. You saved my life", she screams.\n'
        'No problem, but we have to defuse the bomb. Lets see...\n'
        'You extract the bomb carefully out of the teddy bear. It is a "Guess-a-number"-bomb.\n'
        'You have to guess a number between 1 and 50 in 5 tries to extract the bomb, otherwise it will detonate.\n'
        'Try and pick a number between 1 and 50.')
        NumberTry = int(input())
        if NumberTry == Number:
            print(
            'Hurray!!! You found the number. You saved a beautiful woman and (more importantly) the Elbe Philharmonic Hall.\n'
            'Congratulations!\n')
    else:
        print('You enter the Dungeon and hear a terrible scream...')
        time.sleep(2)
        print('You open the door to the prison room...')
        time.sleep(2)
        print(
        'And see a woman with her arms and legs bound together. "I will save you!!!".\n'
        'You unbound her and try to help her to stand up. Suddenly she pushes you away and rips the tape of her mouth\n'
        'WHAT THE F*** ARE YOU DOING??? You think thats a location to harass some women. SECURITY!!!\n'
        'In a few seconds a large security guard comes around, takes you by the collar and throws you out of the entry.'
        'Damn it...Lets look for another location.\n'
        'Type 6 to look at the Elbe Philharmonic Hall, 1 to fly to Berlin or 3 to fly to Munich')
        LocationCity = int(input())
        if LocationCity == 6:
            Elphi()
        if LocationCity == 1:
            Berlin()
        if LocationCity == 3:
            Munich()

def Beer(location):
    if location == Solve:
        print('You enter the Hofbraeuhaus and hear a terrible scream...')
        time.sleep(2)
        print('You open the door...')
        time.sleep(2)
        print(
        'And see a woman with her arms and legs bound together. Next to her you see a little teddybear, which is probably the bomb.\n'
        'You enter the Hofbraeuhaus and liberate the woman. "Thank you very much, Mr. Smith. You saved my life", she screams.\n'
        'No problem, but we have to defuse the bomb. Lets see...\n'
        'You extract the bomb carefully out of the teddy bear. It is a "Guess-a-number"-bomb.\n'
        'You have to guess a number between 1 and 50 in 5 tries to extract the bomb, otherwise it will detonate.\n'
        'Try and pick a number between 1 and 50.')
        NumberTry = int(input())
        if NumberTry == Number:
            print(
            'Hurray!!! You found the number. You saved a beautiful woman and (more importantly) the Elbe Philharmonic Hall.\n'
            'Congratulations!\n')
    else:
        print('You enter the Hofbraeuhaus and hear a terrible scream...')
        time.sleep(2)
        print('You open the door...')
        time.sleep(2)
        print(
        'And see a woman screaming because her husband drank too much beer and puked on her shoes.\n'
        'Disgusting...Lets look for another location.\n'
        'Type 9 to look at the Cathedralof Our Dear Lady, 1 to fly to Berlin or 3 to fly to Munich')
        LocationCity = int(input())
        if LocationCity == 9:
            Lady()
        if LocationCity == 1:
            Berlin()
        if LocationCity == 2:
            Hamburg()

def Lady(location):
    if location == Solve:
        print('You enter the Cathedral of Our Dear Lady and hear a terrible scream...')
        time.sleep(2)
        print('You enter the Cathedral...')
        time.sleep(2)
        print(
            'And see a woman with her arms and legs bound together. Next to her you see a little teddybear, which is probably the bomb.\n'
            'You enter the Cathedral and liberate the woman. "Thank you very much, Mr. Smith. You saved my life", she screams.\n'
            'No problem, but we have to defuse the bomb. Lets see...\n'
            'You extract the bomb carefully out of the teddy bear. It is a "Guess-a-number"-bomb.\n'
            'You have to guess a number between 1 and 50 in 5 tries to extract the bomb, otherwise it will detonate.\n'
            'Try and pick a number between 1 and 50.')
        NumberTry = int(input())
        if NumberTry == Number:
            print(
                'Hurray!!! You found the number. You saved a beautiful woman and (more importantly) the Elbe Philharmonic Hall.\n'
                'Congratulations!\n')
    else:
        print('You enter the Cathedral of Our Dear Lady and hear a terrible scream...')
        time.sleep(2)
        print('You enter the Cathedral...')
        time.sleep(2)
        print(
            'And see a Cathedral full of people singing at a church service.\n'
            'God,forgive me...Lets look for another location.\n'
            'Type 8 to look at the Hofbraeuhaus, 2 to fly to Hamburg or 3 to fly to Munich')
        LocationCity = int(input())
        if LocationCity == 8:
            Beer()
        if LocationCity == 1:
            Berlin()
        if LocationCity == 2:
            Hamburg()

def Berlin():
    print('You fly to the capital city of Germany: Berlin. You have two locations to choose from:\n'
          'The Olympiastadion or the Television Tower.\n'
          'Which one you will choose? (4 (Olympiastadion) or 5 (Television Tower))')
    location = int(input())
    if location == 4:
        Olympia(location)
    if location == 5:
        TV(location)

def Hamburg():
    print('You fly to the pearl of the North: Hamburg. You have two locations to choose from:\n'
          'The Elbe Philharmonic Hall or The Dungeon.\n' 
          'Which one you will choose? (6 (Elbe Philharmonic Hall) or 7 (Dungeon))')
    location = int(input())
    if location == 6:
        Elphi(location)
    if location == 7:
        Dungeon(location)

def Munich():
    print('You fly to the home of the Bavarians: Munich. You have two locations to choose from:\n'
          'The Hofbraeuhaus am Platzl or the Cathedral of Our Dear Lady.\n'
          'Which one you will choose? (8 (Hofbraeuhaus) or 9 (Cathedral))')
    location = int(input())
    if location == 8:
        Beer(location)
    if location == 9:
        Lady(location)

def chooseCity():
     print('Which city will you fly to? (1 (Berlin), 2 (Hamburg), 3 (Munich))')
     city = int(input())
     if city == 1:
         Berlin()
     if city == 2:
        Hamburg()
     if city == 3:
         Munich()

displayIntro()
print('Do you want to start or to find out how to play? (Type "start" or "rules")')
Play = input()
if Play == playGame:
    print('OK. Lets start.')
    chooseCity()
if Play == HowToPlay:
    print ('There are three cities (Berlin, Hamburg and Munich) that are possibly the searched place. In each one are two locations, in which the woman could be hided.\n'
           'You have a total of three tries to find the right location. To begin tap 1, 2 or 3 for the city you want to search in. Than one of numbers 4-9 to look at the locations.\n'
           'If you find the right location in three tries, you win, if not, you lose. Now have fun and enjoy to be a professional detective :D')
if Play != playGame and Play != HowToPlay:
    print('You entered a wrong word. Please restart the game ;)')





def checkCave(chosenCave):

     print('You approach the cave...')

     time.sleep(2)

     print('It is dark and spooky...')

     time.sleep(2)

     print('A large dragon jumps out in front of you! He opens his jaws and...')

     print()

     time.sleep(2)

     friendlyCave = random.randint(1, 2)

     if chosenCave == str(friendlyCave):
          print('Gives you his treasure!')

     else:
          print('Gobbles you down in one bite!')

playAgain = 'yes'


