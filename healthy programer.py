from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        user_input = input()
        if user_input == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40*60
    eyesecs = 30*60    
    exercisesecs = 45*60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking Time. Enter 'drank' to stop the alarm.")
            musiconloop("water.mp3" , "drank")
            init_water = time()
            log_now("Drank water at ")

        if time() - init_eyes > eyesecs:
            print("Eye exercise time. Enter 'eyedone' to stop the alarm.")
            musiconloop("eye.mp3" , "eyedone")
            init_eyes = time()
            log_now("Eyes exercise done at ")

        if time() - init_exercise > exercisesecs:
            print("Physical activity Time. Enter 'exdone' to stop the alarm.")
            musiconloop("exercise.mp3" , "exdone")
            init_exercise = time()
            log_now("Physical Activity done at ")
