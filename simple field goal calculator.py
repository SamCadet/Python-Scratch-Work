# Field goal percentage and evaluation calculator

name1 = 'Spencer Dinwiddie'
fgm1 = 6
fga1 = 13


name2 = 'Caris LeVert'
fgm2 = 5
fga2 = 12

name3 = 'D\'Angelo Russell'

fgm3 = 8
fga3 = 18

name4 = 'Jarrett Allen'

fgm4 = 4
fga4 = 7

name5 = 'Taurean Prince'
fgm5 = 3
fga5 = 9

name6 = 'Joe Harris'
fgm6 = 4
fga6 = 9


def fg_percentage_calculator(name, fgm, fga):
    fg_percentage = (fgm / fga) * 100
    print(name + "'s " + 'field goal percentage:')
    print(fg_percentage)
    print(end='\n')
    if fg_percentage <= 40:
        return name + " has a poor field goal percentage."
    elif fg_percentage < 46:
        return name + " has a field goal percentage that's below average."
    elif fg_percentage >= 50:
        return name + " has an excellent field goal percentage."
    else:
        for fg_percentage in range(46, 49):
            return name + " has an average to above average field goal percentage."


result1 = fg_percentage_calculator(name1, fgm1, fga1)
result2 = fg_percentage_calculator(name2, fgm2, fga2)
result3 = fg_percentage_calculator(name3, fgm3, fga3)
result4 = fg_percentage_calculator(name4, fgm4, fga4)
result5 = fg_percentage_calculator(name5, fgm5, fga5)
result6 = fg_percentage_calculator(name6, fgm6, fga6)

print(result1, end='\n\n')
print(result2, end='\n\n')
print(result3, end='\n\n')
print(result4, end='\n\n')
print(result5, end='\n\n')
print(result6, end='\n\n')
