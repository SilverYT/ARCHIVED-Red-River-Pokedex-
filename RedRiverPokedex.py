# start 
# Imports #
import os
import time
# Welcome Page #
def welcome_screen():
    print('''-------------------------------------------------------------------------''')
    print('''!!! Welcome To RedRiverPokedex's un-official rework !!! (RRP)''')
    print('''-------------------------------------------------------------------------''')
    print(''' QUICK TIP!: If you do not know what fish to look up, consider typing "!help" for a list of fish! :D ''')
    print(''' Tip Number Two: When you want to clear the screen just type "!clear" ''')
    print(''' Tip Number Three...: If you would like to restart the program just type "!restart" ''')
    print('''-------------------------------------------------------------------------''')
    print('...Please enter your favorite fish from the red river :)')
    print('''-------------------------------------------------------------------------''')
welcome_screen()
# Fishy Dictionary #
while True:
    fish_chosen = input("RRP:~> ")
    fishy_refrence = ('catfish', 'carp', 'walleye', 'pike')
    catfish = ('''Catfish are apart of the ictalurid family. Catfish have barbels on their mouths that feel around. Catfish are bottom feeders.''')
    carp = ('''Common carp are apart of the cyprindae family. Common carp are bottom feeders.''')
    walleye = ('''Walleye are apart of the Percidae family. walleye are predators, they eat smaller fish like minnows and leeches.''')
    northern_pike = ('''Northern Pike are apart of the Esox family. Northern Pike are predators and eat minnows and smaller fish.''')
    pike = ('''Pike are apart of the Esox family. Pike are predators and eat minnows and smaller fish.''')
    help = ("So far, here are the following fish stored in the RedRiverPokedex: ") + str(fishy_refrence)
# Fish Input Detection #
    if fish_chosen.lower().strip() == "catfish":
        time.sleep(1)
        print(catfish)
        time.sleep(0.5)
        print("And also, that is Silver's Favorite Fish Too")
    if fish_chosen.lower().strip() == "carp":
        time.sleep(1)
        print(carp)
    if fish_chosen.lower().strip() == "walleye":
        time.sleep(1)
        print(walleye)
    if fish_chosen.lower().strip() == "pike":
        time.sleep(1)
        print(pike)
    # Custom Console Commands #
    if fish_chosen.lower().strip() == "!help":
        time.sleep(2)
        print(help)
    if fish_chosen.lower().strip() == "!clear":
        time.sleep(2)
        os.system("cls")
    if fish_chosen.lower().strip() == "!restart":
        time.sleep(2)
        os.system("cls")
        welcome_screen()
    if fish_chosen.lower().strip() == "!exit":
        time.sleep(3)
        break
# end



    




