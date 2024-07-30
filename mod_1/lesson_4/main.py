import speed_calculator

running_distance = float(input("ile km przebiegłeś? "))
running_time = float(input("ile godzin ci to zajeło? "))

average_speed = speed_calculator.avg_speed(running_distance, running_time)
print(f'Twoja predkosc srednia biegu to {average_speed} km/h')