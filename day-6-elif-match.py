# percentage = 83

# if percentage >= 95:
#     print("A+")
# elif percentage >= 90:
#     print("A")
# elif percentage >= 85:
#     print("B+")
# elif percentage >= 80:
#     print("B")
# else:
#     print("PASS")

# day = 4

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")

# holiday = [4, 5]

# match day:
#     case 1 | 2 | 3:
#         print("Workday")
#     case 4 | 5 if day in holiday:
#         print("WFH")
#     case 6 | 7:
#         print("Weekend")


isOnline = True
isTyping = False
speaking = True

if isOnline and (isTyping or speaking):
    print("User is typing")
elif isOnline:
    print("User is online")
