import Classes
import Data
import Debug

maxHitPoints = 10;
hitPoints = 10;
attak = 1;
defence = 0;
exp = 0;
level = 1;

chatacterName = "empty";
gold = 0;

itemsId: int = [];

currentLocationId = 0; 

def LoadStats(new_maxHitPoints, new_hitPoints, new_defence, new_attack, new_exp, new_level, new_chatacterName, new_gold, new_itemsId, new_currentLocationId):
    global  maxHitPoints, hitPoints, defence, attak, exp, level, chatacterName, gold, itemsId, currentLocationId;

    maxHitPoints = new_maxHitPoints;
    hitPoints = new_hitPoints;
    defence = new_defence;
    attak = new_attack;
    exp = new_exp;
    level = new_level;
    chatacterName =new_chatacterName;
    gold = new_gold;
    level = new_level;
    itemsId = new_itemsId;
    currentLocationId = new_currentLocationId;

def PlayerChoice():
    if currentLocationId == 0:
            PlayerChoiceInTown();
    else:
            PlayerChoiceInAdventure();

def PlayerChoiceInAdventure():
    print("Wybierz akcję:")
    print("0. Miasto")
    print("1. Powrót do miasta")
    print("2. Pójście dalej")
    print("3. Otworzenie ekwipunku")

    choice = input("Twój wybór: ")

    if choice == '0':
        city()
    elif choice == "1":
        ReturnToCity()
    elif choice == "2":
        ContinueJourney()
    elif choice == "3":
        OpenInventory()
    else:
        print("Niepoprawny wybór. Spróbuj ponownie.")
        PlayerChoiceInAdventure()

def PlayerChoiceInTown():
    print("Wybierz akcję:")
    print("0. Miasto")
    print("1. Powrót do miasta")
    print("2. Pójście dalej")
    print("3. Otworzenie ekwipunku")

    choice = input("Twój wybór: ")

    if choice == '0':
        city()
    elif choice == "1":
        ReturnToCity()
    elif choice == "2":
        ContinueJourney()
    elif choice == "3":
        OpenInventory()
    else:
        print("Niepoprawny wybór. Spróbuj ponownie.")
        PlayerChoice()

def ReturnToCity():
    print("Powrót do miasta.")

def ContinueJourney():
    print("Idziesz dalej w podróż.")

def OpenInventory():
    print("Otwarcie ekwipunku.")

def city():
    print("miasto")

def StartGame():
    print(f"grasz jako {chatacterName} na poziomie {level}")
    ImportData();
    DebugFiles();

def ImportData():
    Data.ImportEnemy();
    Data.ImportItems();
    Data.ImportLocation();
    Data.ImportEvent();
    Data.ImportRedward();
    Data.ImportShop();
    Data.ImportTrap();

def DebugFiles():
    Debug.print_enemy_list(Data.enemyList);
    Debug.print_items_list(Data.itemsList);
    Debug.print_location_list(Data.locationList);
    Debug.print_events_list(Data.eventsList);
    Debug.print_shops_list(Data.shopList);
    Debug.print_traps_list(Data.trapsList);
    Debug.print_rewards_list(Data.rewardList);
