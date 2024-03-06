import random
import time
from speech_rec import record_speech


def play_game( ):
    
    seviyeler = {

    "kolay": ["dairy", "mouse", "computer", "phone"],

    "orta": ["programming", "algorithm", "developer", "busy", "modelling"],

    "zor": ["neural network", "machine learning", "artificial intelligence"]

    }
    times = int(input("How many times would you like to play?(Please do it more than 1 time to actually have fun!)"))
    if times > 1:
        for i in range(times):
            a = input("In which level would you like to play?")
            print("You need to earn", times*3, "points at most and that would be awesome. But still try your best! :)")
            time.sleep(2)
            score = 0
            if a == 'kolay':
                seviye = seviyeler["kolay"]
                c = random.choice(seviye)
                print(c, 'read this word please?')
                word_user = record_speech()
                if word_user == c:
                    print(word_user)
                    time.sleep(1)
                    score += 1
                    print('Woohoo! You did it. Now try the harder levels maybe?')
                    print("Your score is now;", score)
                    time.sleep(1)

            if a == 'orta':
                seviye = seviyeler["orta"]
                c = random.choice(seviye)
                print(c, 'read this word please?')
                word_user = record_speech()
                if word_user == c:
                    print(word_user)
                    time.sleep(1)
                    score += 2
                    print('Waow! You did it! Now try the harder level maybe?')
                    print("Your score is now;", score)
                    time.sleep(1)

            if a == 'zor':
                seviye = seviyeler["zor"]
                c = random.choice(seviye)
                print(c, 'read this word please?')
                word_user = record_speech()
                print(word_user) 
                if  word_user == c:
                    time.sleep(1)
                    score +=3
                    print("Awesome! You did it! You're really good at English!")
                    print("Your score is now;", score)
                    time.sleep(1)
            else:
                print(word_user)
                print("I am sorry but you need to try again.:(")
                score += 0
                print("Your score is now;", score)
                time.sleep(1)

    else:
        times = int(input("Please write an appropriate value as an 'integer' or write numbers which are bigger than 1;"))

play_game()