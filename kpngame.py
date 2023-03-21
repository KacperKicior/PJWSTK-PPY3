import getpass
import random

rounds_set = int(input("Do ilu rund?\n"))

gametype = input("Wybierz: AI czy 2 graczy ?\n")


class Points:
    player_score = 0
    ai_score = 0
    player1_name = ""
    player2_name = ""
    player1_score = 0
    player2_score = 0


def ai_gamemode():
    move = input("Wybierz ruch: kamien, papier, nozyce\n")
    if move == "kamien":
        print("Wybrales kamień")
    elif move == "papier":
        print("Wybrales papier")
    elif move == "nozyce":
        print("Wybrales nożyce")
    else:
        print("Niepoprawny ruch")
    ai_move = random.choice(["kamien", "papier", "nozyce"])
    print("AI wybrał", ai_move, "\n")
    if move == "kamien" and ai_move == "nozyce":
        print("Wygrałeś")
        Points.player_score += 1
    elif move == "papier" and ai_move == "kamien":
        print("Wygrałeś")
        Points.player_score += 1
    elif move == "nozyce" and ai_move == "papier":
        print("Wygrałeś")
        Points.player_score += 1
    elif move == ai_move:
        print("Remis")
    else:
        print("Przegrałeś")
        Points.ai_score += 1
    print("Wynik: Gracz: ", Points.player_score, ": AI:", Points.ai_score, "\n")


def two_player_gamemode():
    move = getpass.getpass(f"{Points.player1_name}, wybierz ruch: kamien, papier, nozyce\n")
    move2 = getpass.getpass(f"{Points.player2_name}, wybierz ruch: kamien, papier, nozyce\n")
    if move == "kamien" and move2 == "nozyce":
        print(f"Wygrał {Points.player1_name}\n")
        Points.player1_score += 1
    elif move == "papier" and move2 == "kamien":
        print(f"Wygrał {Points.player1_name}\n")
        Points.player1_score += 1
    elif move == "nozyce" and move2 == "papier":
        print(f"Wygrał {Points.player1_name}\n")
        Points.player1_score += 1
    elif move == move2:
        print("Remis")
    else:
        print(f"Wygrał {Points.player2_name}\n")
        print(f"{Points.player1_name} wybrał {move}, {Points.player2_name} wybrał {move2}\n")
        Points.player2_score += 1
    print(f"Wynik: {Points.player1_name}: ", Points.player1_score, ": ", Points.player2_name, ":",
          Points.player2_score, "\n")


if gametype == "AI":
    rounds_num = 0
    while rounds_set > rounds_num:
        ai_gamemode()
        rounds_num += 1

elif gametype == "2 graczy":
    rounds_num = 0
    Points.player1_name = input("Podaj imię gracza 1\n")
    Points.player2_name = input("Podaj imię gracza 2\n")
    while rounds_set > rounds_num:
        two_player_gamemode()
        rounds_num += 1
