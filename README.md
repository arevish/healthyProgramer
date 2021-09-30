# Health Management System  ![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)
created a program for real life problem to keep remind you to do specific tasks to keep you healthy and help you to stay fit. Program will play mp3 files assigned to specific tasks using pygame on loop untill you do that task and update your status to stop the alarm. Program also keep log of your task for you to checks what you do at what time.
You may notice this file contains a scenario. The reason for that is just to develop your interest in the problems So, let me give a brief introduction of the scenario here. ;)

## scenario
Assume that a programmer works at the office from 9am-5 pm. We have to take care of his health and remind him three things,

1. To drink a total of 3.5-liter water after some time interval between 9-5 pm.(ever 40 min)
2. To do eye exercise after every 30 minutes.
3. To perform physical activity after every 45 minutes.

## Instructions to follow:
The task is to create a program that plays mp3 audio until the programmer enters the input which implies that he has done the task.

* For Water, the user should enter “Drank”
* For Eye Exercise, the user should enter “EyDone”
* For Physical Exercise, the user should enter “ExDone”
After the user enters the input, a file should be created for every task separately, which contains the details about the time when the user performed a certain task.
**for example:**
```
Drank water at  2021-08-28 10:20:03.935958
Drank water at  2021-08-28 11:00:27.470998
Drank water at  2021-08-28 11:40:21.795566

```

### Module used
python modules
```
from pygame import mixer
from datetime import datetime
from time import time
```

## PRE-REQUISITES
Your laptop with 3.6.x (onwards) installed.

**NOTE:** Those with Linux and MacOSX would have Python installed by default, no action required.

Windows: Download the version for your laptop via https://www.python.org/downloads/

**NOTES**
In your preferred editor, make sure indentation is set to "4 spaces".

Make sure you have **pygame** installed in python otherwise code may fail, to install pygame in your machine > open python in your terminal then type `pip install pygame` to install. :warning:


## Run using Python3.8+
1. Clone or download repositiory: https://github.com/arevish/healthyProgramer.git
2. In source folder, run `python3 'healthy programer.py'` to start program, optionally, run with `--help` argument to see other runtime options.
