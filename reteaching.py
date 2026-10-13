def how_many_seconds():
    minutes_to_convert = int(input("Enter how many minutes you want to convert: "))# Convert minutes to seconds
    seconds_to_add = int(input("Enter how many seconds you want to add: "))
    total = (minutes_to_convert * 60) + seconds_to_add
    return total

def kilometers_to_miles():
    kilometers_input = float(input("Enter how many kilometers you want to convert: "))
    miles = kilometers_input * 1.6
    return miles

print(how_many_seconds())
print(kilometers_to_miles())

