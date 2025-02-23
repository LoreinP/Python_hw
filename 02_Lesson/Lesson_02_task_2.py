def is_year_leap(year):


    if year % 4== 0:
        return True
    else:
        return False


year = int(input('Введите год: '))


leap_year = is_year_leap(year)
print(f"год{year}:{leap_year}")


