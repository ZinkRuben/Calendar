def leapyeartester(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return(True)
    else:
        return(False)

days = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
january_first = []
counter = 0


for year in range(0, 400, 1):

#counter reset
    if counter == 7:
        counter = 0
    elif counter == 8:
        counter = 1
    elif counter == 9:
        counter = 2

    january_first.append(days[counter])
    if leapyeartester(year):
        counter += 2
    else:
        counter += 1
print(january_first)
