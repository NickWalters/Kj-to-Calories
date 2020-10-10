foodCount = int(input("How many items of food did you eat today? :  "))
gender = str(input("What is your Gender? M or F ? : "))
foodList = []
foodListCalories = []

for food in range(foodCount):
    tempFood = int(input("Enter KJ of food item: "))
    foodList.append(tempFood)

for item in foodList:
    foodListCalories.append(item * 0.238845897)


netLossGain = 0
    # gender is male (kj)
if(gender.find("M") >= 0 or gender.find("m") >= 0):
    netLossGain = 7100
else:
    # gender is female (kj)
    netLossGain = 5900


totalCalories = sum(foodListCalories)
totalKg = (round(totalCalories) / 7700)
print("\n\n\n")
print("______________________________________________________")
print("Total Calories Consumed: ")
print("______________________________________________________")
print("\n")
print("Calories: ")
print(round(totalCalories))
print()
print("Kg: ")
print(round(totalKg, 3))
print("\n")
print("Net Loss/Gain: ")
print("calculated based on basal metabolic rate of the average male/female \n The human body consumes a certain amount of calories/energy per day")
print("______________")
nlgCalories = netLossGain * 0.238845897
nlgKg = (round(nlgCalories) / 7700)
print("Calories: " + str(totalCalories - nlgCalories))
print("Kg: " + str(totalKg - nlgKg))
print()
print("______________________________________________________")
print("______________________________________________________")
