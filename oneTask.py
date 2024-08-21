from datetime import datetime

action = "Press Enter to move to next item.\n"

step1 = "Wake up at least 1 hours before you have to look at a screen (no email)\n"

step2 = "Cup of tea and sit down with pen and paper (in this case, you are sitting in front of a terminal)\n"

step3 = ("List up to 5 things that are making you anxious and uncomfortable (things you have put off.)\n"
         "Most important usually means most uncomfortable.\n"
         "If you only have 3 things, leave the other two blank.\n")

print("Efficacy > Efficiency\n")
# Wake up
print(step1)
input(action)

# Get tea
print(step2)
input(action)

# List to-dos
puttingOff = []
print(step3)
# try catch. If null, seems like nothing is bothering you. Take the day off. End program.
for i in range(5):
    item = input(f"Item number {i+1}: ")
    if item != '':
        puttingOff.append(item)
print(puttingOff)

yesList = []

for i in range(len(puttingOff)):
    todoItem = puttingOff[i]
    print(todoItem)
    answer1 = input("If this was the only thing I accomplished today, would I be satisfied with my day?(y/n)\n")
    answer2 = input("Will moving this forward make other to-dos easier or irrelevant later?(y/n)\n")
    print(f"Answer 1: {answer1}. Answer 2: {answer2}")
    if answer1 == 'y' or answer2 == 'y':
        yesList.append(todoItem)


print("Look only at items you have answered YES to.")

for index, item in enumerate(yesList):
    row = f"{index + 1}) {item}"
    print(row)

print("Block out 2 - 3 hours to focus on ONE OF THEM for today.\n")
focusItem = int(input("Which item are you going to focus on?\n")) - 1

print(f"Today you're going to focus on {yesList[focusItem]}\n")
timeFormat = '%I:%M %p'

startTime_string = input("When will that 2 - 3 hour block start? HH:MM AM/PM format (ex. 01:00 AM, 11:45 PM)\n")
startTime = datetime.strptime(startTime_string, timeFormat)
print(f"Chosen start time: {startTime}")

endTime_string = input("When will that 2 - 3 hour block end? HH:MM AM/PM format (ex. 01:00 AM, 11:45 PM)\n")
endTime = datetime.strptime(endTime_string, timeFormat)
print(f"Chosen end time: {endTime}")

blockedTime = endTime - startTime
print(blockedTime)

# TRY-CATCH TODO: If blocked time is less than 2 hours, ask for start and end time again.
print("BLOCK OUT 2 - 3 HOURS TO FOCUS ON ONE OF THEM. Single block.\n \n")

print("If procrastinate, it is ok. Do not spiral. Just come back to that one item.\n\n")

print(f"Your task for today: {yesList[focusItem]}\n"
      f"You're going to work on it from {startTime} to {endTime}")

# TODO: Add functionality for user to put in their number.