temp = open("liczby.txt")
file = temp.readlines()
temp.close()
results = open("zadanie6.txt", "w")

even = 0
nums = []
len_nine_counter, len_nine_sum = 0, 0
for lines in file:
    number = lines.rstrip()
    if number[-1] == '0':
        even +=  #6a
    nums.append(int(number, 2)) #6b
    if len(number) == 9: #6c
        len_nine_counter += 1
        len_nine_sum += int(number, 2)
        
results.write(f"6a\n{even}\n\n6b\n{bin(max(nums))[2:]} {max(nums)}\n\n"
              f"6c\nLiczb: {len_nine_counter} Suma: {len_nine_sum}")

results.close()