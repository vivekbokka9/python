starting_position = 5
#def move_player():
    #by_amount = 2
    #global position
    #position += by_amount
def move_player(current_position, by_amount):
    return current_position + by_amount
print(starting_position)
new_postion = move_player(starting_position, 2)
print(new_postion)
newest_postion = move_player(starting_position, -5)
print(newest_postion)
print('difference between positions is', starting_position - newest_postion)
#print(new_position)
#move_player()
#print(position)
