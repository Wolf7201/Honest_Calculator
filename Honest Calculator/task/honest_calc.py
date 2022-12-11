MSG_0 = "Enter an equation\n"
MSG_1 = "Do you even know what numbers are? Stay focused!"
MSG_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
MSG_3 = "Yeah... division by zero. Smart move..."
MSG_4 = "Do you want to store the result? (y / n):\n"
MSG_5 = "Do you want to continue calculations? (y / n):\n"
MSG_6 = " ... lazy"
MSG_7 = " ... very lazy"
MSG_8 = " ... very, very lazy"
MSG_9 = "You are"
MSG_10 = "Are you sure? It is only one digit! (y / n)\n"
MSG_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)\n"
MSG_12 = "Last chance! Do you really want to embarrass yourself? (y / n)\n"

operations = {
    "+": (lambda x, y: x + y),
    "-": (lambda x, y: x - y),
    "*": (lambda x, y: x * y),
    "/": (lambda x, y: x / y),
}

msg_ = {
    10: MSG_10,
    11: MSG_11,
    12: MSG_12
}


def is_one_digit(v):
    return bool(-10 < v < 10 and v.is_integer())


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += MSG_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += MSG_7
    if (v1 == 0 or v2 == 0) and v3 != '/':
        msg += MSG_8
    if msg != '':
        msg = MSG_9 + msg
        print(msg)


def main():
    memory = 0.0

    while True:
        x, oper, y = input(MSG_0).split()
        try:
            x = memory if x == "M" else float(x)
            y = memory if y == "M" else float(y)
            check(x, y, oper)
            result = operations[oper](x, y)
            print(result)
            if input(MSG_4) == "y":

                if is_one_digit(result):
                    msg_index = 10
                    while msg_index in msg_.keys() and input(msg_[msg_index]) != 'n':
                        msg_index += 1
                    if msg_index not in msg_.keys():
                        memory = result
                else:
                    memory = result

            if input(MSG_5) == "n":
                break
        except ValueError:
            print(MSG_1)
        except KeyError:
            print(MSG_2)
        except ZeroDivisionError:
            print(MSG_3)


if __name__ == '__main__':
    main()
