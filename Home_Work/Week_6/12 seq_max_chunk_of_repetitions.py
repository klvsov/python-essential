previous_number = -1
this_max_rep = 0
max_rep = 0
number = int(input())
while number != 0:
    if previous_number == number:
        this_max_rep += 1
    else:
        previous_number = number
        max_rep = max(max_rep, this_max_rep)
        this_max_rep = 1
    number = int(input())
max_rep = max(max_rep, this_max_rep)
print(max_rep)
