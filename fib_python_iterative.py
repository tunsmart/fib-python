def fib(position):
    start_position_minus_one = 1
    start_position_minus_two = 0
    fib_num = 0
    if position == 1:
        return start_position_minus_two
    elif position == 2:
        return start_position_minus_one
    for i in range(1, position + 1):
        if i <= 2:
            continue
        else:
            fib_num = start_position_minus_one + start_position_minus_two
            start_position_minus_two = start_position_minus_one
            start_position_minus_one = fib_num
    return fib_num
fib_seq = []
for i in range(1,16):
    fib_seq.append(fib(i))
print(fib_seq)
