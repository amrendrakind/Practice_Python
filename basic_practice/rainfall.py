days = 8
for day in range(1, days):
    sum_rain_fall = 0
    rain_fall = -1
    while(rain_fall != 0):
        rain_fall = int(input("Enter rain fall for the day "))
        if( rain_fall == -1 ):
            break
        else:
            sum_rain_fall += rain_fall
    print(f'Total rain fall for day {day} is', sum_rain_fall)

