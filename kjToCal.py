foodCount = int(input("How many items of food did you eat today? :  "))
foodList = []
foodListCalories = []

for food in range(foodCount):
    tempFood = int(input("Enter KJ of food item: "))
    foodList.append(tempFood)

for item in foodList:
    foodListCalories.append(item * 0.238845897)

totalCalories = sum(foodListCalories)
print("Total Calories Consumed: ")
print("________________________")
print("\n\n")
print(totalCalories)
print("\n\n")
print("________________________")