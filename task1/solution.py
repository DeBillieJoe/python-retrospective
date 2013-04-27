SIGNS = {1: ("Козирог", 19), 2: ("Водолей", 18), 3: ("Риби", 20),
         4: ("Овен", 20), 5: ("Телец", 20), 6: ("Близнаци", 20),
         7: ("Рак", 21), 8: ("Лъв", 22), 9: ("Дева", 22),
         10: ("Везни", 22), 11: ("Скорпион", 21),
         12: ("Стрелец", 21)}


def what_is_my_sign(day, month):
    if day <= SIGNS[month][1]:
        return SIGNS[month][0]

    elif month == 12:
        return SIGNS[1][0]

    else:
        return SIGNS[month+1][0]