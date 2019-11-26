import random

points = {
    'A':1, 'B':3, 'C':3,'D':2, 'E':1,'F':4, 'G':2, 'H':4, 'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1, 'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1, 'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10
}
count = {
    'A':9, 'B':2,'C':2,'D':4, 'E':12,'F':2, 'G':3, 'H':2, 'I':9, 'J':1, 'K':1, 'L':4, 'M':2, 'N':6, 'O':8, 'P':2, 'Q':1, 'R':6, 'S':4, 'T':6, 'U':4, 'V':2, 'W':2, 'X':1, 'Y':2, 'Z':1
}

# part 4(a)
def get_points(word):
    total = 0
    for letter in word:
        total += points[letter]
    return total

# part 4(b)
def is_valid(word, player_tiles):
    if len(word) == 0 or len(word) > len(player_tiles):
        return False
    for letter in word:
        if letter not in player_tiles:
            return False
        elif player_tiles.count(letter) < word.count(letter):
            return False
    return True

# part 4(c)
def select_tiles(player_tiles):
  for i in range(7 - len(player_tiles)):
    if len([player_tiles]) != 0:
      ch = random.choice(list(count.keys()))
      player_tiles.append(ch)
      if count[ch] <= 1:
        del count[ch]
      else:
        count[ch] -= 1
  return player_tiles

# part 4(d)
player_tiles = []
total_scores = 0
while True:
    player_tiles = select_tiles(player_tiles)
    print("Your tiles are:", player_tiles)
    word = input("Enter your word: ")
    word = word.upper()

    if is_valid(word, player_tiles):
        current_points = get_points(word)
        total_scores += current_points
        print("You earned", current_points, "points")
        print("Your total points is", total_scores)
        for letter in word:
            player_tiles.remove(letter)

        if len(count) == 0 and len(player_tiles) == 0:
            print("No more tiles")
            break;
        else:
            cont = input("Do you want to continue? (Y/N) ")
            if cont.upper() != 'Y':
                break;
    else:
        print("Your word is invalid. Please enter again")
print("End of game")
