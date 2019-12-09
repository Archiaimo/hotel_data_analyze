def get_zodiac(year):
    zodiac = ("猴", "鸡", "狗","猪", "鼠", "牛", "虎", "兔", "龙", "蛇", "马","羊")
    return zodiac[year % 12]

print(get_zodiac(1965))