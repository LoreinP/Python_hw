def month_to_season(month):
    if month in [12, 1, 2]:
        return 'зима'
    if month in [3, 4, 5]:
        return 'весна'
    if month in [6, 7, 8]:
        return 'лето'
    if month in [9, 10, 11]:
        return 'осень'
    else:
        return 'Неверный номер месяца'

if __name__ == "__main__":
    month = int(input('Введите номер месяца: (1-12): '))
    season = month_to_season(month)
    print(f"Месяц {month} относится к сезону: {season}")
