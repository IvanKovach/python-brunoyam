speed = int(input("Введите скорость Василия:"))
time = int(input("Введите время движения:"))
length = 109
position = (speed * time) % length
print("Вася остановился на " + str(position) + " километре МКАД")