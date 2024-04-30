import re 

def main():
    print(convert(input("Hours: ")))

def convert(time):
    if match := re.search(r"^(([\d][0-2]*):*([0-5][\d])*) ([A-P]M) to (([\d][0-2]*):*([0-5][\d])*) ([A-P]M)$",time):
        hours = match.groups()

        if int(hours[1]) > 12 or int(hours[5]) > 12:
            raise ValueError

        time_1, time_2 = conv_hour(hours[1],hours[2], hours[3]), conv_hour(hours[5],hours[6], hours[7])
        return time_1 + " to " + time_2
    else:
        raise ValueError


def conv_hour(hour, min, merid):
    if merid == 'PM':
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    if min == None:
        new_min = ':00'
        new_time = f"{new_hour:02}" + new_min
    else:
        new_time = f"{new_hour:02}" + ':' + min
    return new_time


if __name__ == "__main__":
    main()