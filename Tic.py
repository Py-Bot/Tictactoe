# Tic Tac Toe

# Spielfeld initialisieren
board = [' ' for _ in range(9)]

# Funktion zum Anzeigen des Spielfelds
def display_board():
    print("-------------")
    for i in range(3):
        print("| {} | {} | {} |".format(board[i*3], board[i*3+1], board[i*3+2]))
        print("-------------")

# Funktion zum Überprüfen, ob das Spielfeld komplett gefüllt ist
def is_board_full():
    return ' ' not in board

# Funktion zum Überprüfen, ob ein Spieler gewonnen hat
def check_winner(player):
    # Überprüfen der Reihen
    for i in range(3):
        if board[i*3] == board[i*3+1] == board[i*3+2] == player:
            return True
    # Überprüfen der Spalten
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Überprüfen der Diagonalen
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Funktion zum Ausführen eines Spielzugs
def make_move(player, position):
    board[position] = player

# Funktion zum Ausführen des Spiels
def play_game():
    player = 'X' # Spieler X beginnt
    
    while not is_board_full():
        display_board()
        
        # Spielzug vom Spieler erhalten
        position = int(input("Spieler {}: Gib eine Position (0-8) ein: ".format(player)))
        
        if position < 0 or position > 8 or board[position] != ' ':
            print("Ungültige Position! Versuche es erneut.")
            continue
        
        # Spielzug ausführen
        make_move(player, position)
        
        # Überprüfen, ob der Spieler gewonnen hat
        if check_winner(player):
            display_board()
            print("Spieler {} hat gewonnen!".format(player))
            return
        
        # Zum anderen Spieler wechseln
        player = 'O' if player == 'X' else 'X'
    
    # Wenn das Spielfeld voll ist und keiner gewonnen hat, endet das Spiel unentschieden
    display_board()
    print("Das Spiel endet unentschieden.")

# Spiel starten
play_game()