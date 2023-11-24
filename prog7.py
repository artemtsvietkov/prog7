import os
import time
import msvcrt
from colors import bcolors
import random
os.system('cls')

# 1. Gör ett valfritt program som suddar skärmen med os.system(‘cls’) vid flera tillfällen. Du kan även uppdatera ett gammalt program
# while True:
#     inputus = input("Write cls ")
#     if inputus == 'cls':
#         os.system('cls')

# 2. Använd sleep()-kommandot i valfritt projekt och spara som nytt. Filnamn sleep() används när du vill att programmet väntar innan det fortsätter
# while True:
#     inputs = input("Hi ")
#     if inputs == 'Hi':
#         time.sleep(5)
#         os.system('cls')
# 3. Gör ett välkomstprogram som väntar på en knapptryckning (utan ENTER) innan det avslutas - getwch()
# while True:
#     name = input(bcolors.BLUE + "Hello, write your name " + bcolors.DEFAULT)
#     print(f"{name} if you wish to exit press any key except ENTER")
#     if msvcrt.getwch() != "\r":
#         break
#     else:
#         continue
# 4. Gör en modul som ändrar färg (kolla flödet här på CR)
# print(bcolors.YELLOW + "Heya" +bcolors.DEFAULT)
# 5. Skapa ett färgstarkt program som använder färg samt något mer du lärt dig
# os.system("cls")
# colors = {
#      1: bcolors.PURPLE,
#      2: bcolors.BLUE,
#      3: bcolors.CYAN,
#      4: bcolors.GREEN,
#      5: bcolors.YELLOW,
#      6: bcolors.RED
# }

# while True:
#     for index in colors.keys:
#         textcolor = colors[index] 
#         print(textcolor + "AM I INTERRUPTING?" + bcolors.DEFAULT)    
#         time.sleep(1)
#         os.system("cls")
# 6. Uppdatera gärna något annat gammalt program med getwch() och färger!
def math(x):
    return 2*10
    for x in range (1,11):
        print(math(2))
# 7. ÖVERKURS: Skapa en egen modul och importera till ett program!