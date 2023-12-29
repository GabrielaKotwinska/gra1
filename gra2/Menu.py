import Data


def show_menu():
    print("Witaj! Wybierz opcję");
    print("1. Nowa gra");
    print("2. Wczytaj");
    print("3. Dodaj wroga");
    print("4. Opcje");
    print("5. Wyjście");

def new_game():
    print("Nowa gra została rozpoczęta!");

def add_enemy():
    print("Dodajemy wroga! Wrrrr!");

def main():
    while True:
        show_menu()
        choice = input("Wybierz opcję (1-5): ");

        if choice == '1':
            print("Wybrałeś opcję Nowa gra.");
            Data.new_game();
        elif choice == '2':
            Data.load();
        elif choice == '3':
            Data.AddEnemyToFile();
        elif choice == '4':
            print("Wybrałeś opcję Opcje.");
        elif choice == '5':
            print("Wychodzę z programu.");
            exit()
            break
        else:
            print("Nieprawidłowy wybór. Wprowadź liczbę od 1 do 5.");



if __name__ == "__main__":
    main();