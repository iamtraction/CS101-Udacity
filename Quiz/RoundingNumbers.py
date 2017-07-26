x = 5.78

round_no = x + 0.5
number_string = str(round_no)
decimal_position = number_string.find('.')

print number_string[:decimal_position]
