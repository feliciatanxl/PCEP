temperatures_day1_day30 = [25, 20, 21, 26, 23, 22, 18, 27, 28, 30, 31, 33, 34, 36, 36, 37, 38, 40, 39, 37, 35, 34, 32, 31, 30, 28, 26, 21, 23, 24]

# 3a
day1_day7 = temperatures_day1_day30[:7]
print("Week 1 temperatures:", day1_day7)

highest_temp = day1_day7[0]
for temp in day1_day7:
    if temp > highest_temp:
        highest_temp = temp
print("Highest temperature in week 1:", highest_temp)

# 3b
day26_day30 = temperatures_day1_day30[-5:]
print("Temperatures for last 5 days:", day26_day30)

lowest_temp = day26_day30[0]
for temp in day26_day30:
    if temp < lowest_temp:
        lowest_temp = temp
print("Lowest temperature for the last 5 days:", lowest_temp)

# 3c
alternate_days = temperatures_day1_day30[::2]
print("Alternate day temperatures:", alternate_days)

total_temp = 0
for temp in alternate_days:
    total_temp += temp
print("Average temperature for these days:", round(total_temp / len(alternate_days), 2))