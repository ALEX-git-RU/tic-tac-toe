class Ship:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        if start[0] == end[0]:
            self.orientation = 'horizontal'
            self.length = abs(start[1] - end[1]) + 1

        else:
            self.orientation = 'vertical'
            self.length = abs(start[0] - end[0]) + 1

ship = Ship((1, 1), (1, 3))



class Board:

    def __init__(self):
        self.grid = [[' ' for _ in range(6)] for _ in range(6)]


    def print_board(self):

        for now in self.grid:
            print(' '.join(","))

    def place_ships(self, ships):
        for ship in ships:

            start = ship.start

            end = ship.end

            if start[0] == end[0]:
                for j in range(start[1], end[1] + 1):
                    self.grid[start[0]][j] = 'S'

            else:
                for i in range(start[0], end[0] + 1):

                    self.grid[i][start[1]] = 'S'


board = Board()

ships = [Ship((1, 1), (1, 3)), Ship((2, 4),(3,4)), Ship((4, 2), (4, 3))]

board.place_ships(ships)

board.print_board()

def check_hit(guess, ships):

    for ship in ships:

        if ship.start[0] <= guess[0] <= ship.end[0] and ship.start[1] <= guess[1] <= ship.end[1]:

            return True

    return False


def computer_move(used_moves):

    import random

    x = random.randint(0, 5)
    y = random.randint(0, 5)

    while (x, y) in used_moves:
        x = random.randint(0, 5)
        y = random.randint(0, 5)

    return x, y



guess = (2, 4)
if check_hit(guess, ships):
    print('HIT;)')

else:
    print('Miss:(')




used_moves = [(3, 2), (4, 4)]

comp_move = computer_move(used_moves)

print("Computer's move:", comp_move)




def main():
    player_board = Board()
    computer_board = Board()
    player_ships = [Ship((1, 1), (1, 3)), Ship((2, 4), (3, 4)), Ship((4, 2), (4, 3))]
    computer_ships = [Ship((0, 0),(0, 2)), Ship((0,4), (1, 4)), Ship((3,1), (3, 2))]


    player_moves = []
    computer_moves = []


    while True:
        player_guess = (int(input("Enter row (0-5): ")), int(input("Enter column (0-5): ")))

        player_moves.append(player_guess)

        if check_hit(player_guess, computer_ships):

            print("Player's Hits!")

        else:

            print("Player's Miss.")


        if all(check_hit(guess, computer_ships) for guess in player_moves):
            print("Player wins!")

            break



        comp_guess = computer_move(computer_moves)
        computer_moves.append(comp_guess)
        if check_hit(comp_guess, player_ships):
            print("Computer's Hit!")

        else:
            print("Computer's miss.")


        if all(check_hit(guess, player_ships) for guess in computer_moves):
             print("Computer WINS!!!")

             break



if __name__ == "__main__":

    main()