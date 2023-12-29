import Classes
import os
import glob

def ImportEnemy():
    enemyList = [] ;
    try:
        with open("enemy.txt", "r") as file:
            for line in file:
                name, hitPoints, attack, defence, expDrop = line.strip().split(',');
                enemyList.append(Classes.Enemy(name, int(hitPoints), int(attack), int(defence), int(expDrop)));
    except FileNotFoundError:
        print("Plik 'enemy.txt' nie istnieje.");

    return enemyList

def AddEnemyToFile():
    while True:
        name = input("Podaj nazwę wroga: ");
        if name.strip():
            break;
        print("Nie podano wartosci");

    while True:
        hitPoints = input("Podaj ilość punktów życia: ");
        if hitPoints.strip().isdigit():
            break;

    while True:
        attack = input("Podaj wartość ataku: ");
        if attack.strip().isdigit():
            break;
        print("Nie podano wartosci");

    while True:
        defence = input("Podaj wartość obrony: ");
        if defence.strip().isdigit():
            break;
        print("Nie podano wartosci");

    while True:
        expDrop = input("Podaj ilość doświadczenia za pokonanie: ");
        if expDrop.strip().isdigit():
            break;
        print("Nie podano wartosci");

    with open("enemy.txt", "a") as file:
        file.write(f"{name},{hitPoints},{attack},{defence},{expDrop}\n");

def new_game():
    print("Nowa gra została rozpoczęta!");
    save_files = glob.glob('save*.txt');
    save_number = len(save_files) + 1;
    save_name = f"save{save_number}.txt";
    with open(save_name, "w") as file:
        file.write("");  # Tworzenie pustego pliku zapisu
    print(f"Utworzono nowy zapis: {save_name}");

def load():
    print("Wybierz zapis do wczytania:");
    save_files = glob.glob('save*.txt');
    if not save_files:
        print("Brak dostępnych zapisów.");
        return;

    for idx, save_file in enumerate(save_files, start=1):
        print(f"{idx}. {save_file}");

    while True:
        choice = input("Wybierz opcję lub wpisz 'exit' aby wyjść: ");
        if choice.lower() == 'exit':
            break;

        if choice.isdigit() and 1 <= int(choice) <= len(save_files):
            selected_save = save_files[int(choice) - 1];
            print(f"Wybrano {selected_save}");
            # Tutaj dodać kod do wczytania danych z wybranego pliku zapisu
            break;
        else:
            print("Nieprawidłowy wybór");
