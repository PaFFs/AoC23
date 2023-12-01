with open('input.txt') as file:
    lines = file.readlines()

# task 1
nums = 0
for line in lines:
    for char in line:
        if char.isnumeric():
            left = char
    for char in line[::-1]:
        if char.isnumeric():
            right = char
    doubleNum = int(right + left)
    nums += doubleNum
print(nums)


# task 2
numbers = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

numbersDict = {
    "1":"1",
    "2":"2",
    "3":"3",
    "4":"4",
    "5":"5",
    "6":"6",
    "7":"7",
    "8":"8",
    "9":"9",
    "0":"0",
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}
nums = 0
for line in lines:
    for subString in range(0, len(line)+1):
        for number in numbers:
            if number in line[0:subString]:
                left = numbersDict[number]
                break
            else:
                continue
            break
        else:
            continue
        break
    for subString in range(len(line), 0-1, -1):
        for number in numbers:
            if number in line[subString:len(line)]:
                right = numbersDict[number]
                break
            else:
                continue
            break
        else:
            continue
        break
    num = int(left + right)
    nums += num
print(nums)


