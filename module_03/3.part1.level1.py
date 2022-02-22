investment = float(input("Введите сумму вклада: "))
percent = float(input("Введите процентную ставку: ")) / 100
desire = float(input("Введите желаемую сумму на счету: "))
term = 0

while investment < desire:
    term += 1
    investment = int(investment + investment * percent)

print(f"Желаемая сумма будет на счету через {term} лет")