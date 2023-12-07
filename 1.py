file = open('1_input')
sum = 0
for line in file:
    # leave only digits in each line
    string = ''.join(filter(str.isdigit, line))
    # take first and last one
    value = int(string[0] + string[-1])
    # add it up
    sum += value
# i gotta see my man
print(sum)