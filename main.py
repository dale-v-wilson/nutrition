# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def getGenderInput():
    try:
        return str(input("What is your gender?: "))
    except:
        print("Invalid entry")
        return getGenderInput()

gender = getGenderInput()
while str(gender) != "male" and str(gender) != "female":
    print("Enter male or female")
    gender = getGenderInput()
print("Your selected gender is", gender)
def getInput(prompt):
    try:
        return float(input(prompt))
    except:
        print("Invalid entry, please enter a number")
        return getInput(prompt)


age = getInput("Please enter your age?: ")
while age <= 0 or age > 120:
    print("Please enter a valid age between 0 and 120")
    age = getInput("Please enter your age?: ")
print("Your selected age is", age)

height = getInput("What is your height in cm?: ")
while height <= 50 or height > 300:
    print("Please enter a valid height between 50cm and 300cm")
    height = getInput("What is your height in cm?: ")
print("Your selected height is", height, "cm")

weight = getInput("What is your weight in kg?: ")
while weight <= 0 or weight > 300:
    print("Please enter a valid weight between 0kg and 300kg")
    weight = getInput("What is your weight in kg?: ")
print("Your selected weight is", weight, "kg")


def calcbmi(height, weight):
    bmi = float(weight) / ((float(height) / 100) ** 2)
    return bmi


bmi = calcbmi(height, weight)
print("Your BMI is: ", round(bmi, 2))
if float(bmi) < 18.5:
    print("You are underweight")
elif 18.5 <= float(bmi) <= 24.9:
    print("You are at a healthy weight")
elif 25 <= float(bmi) <= 29.9:
    print("You are overweight")
elif float(bmi) >= 30:
    print("You are obese")


def calcbmr(gender, height, weight, age):
    if str(gender) == "male":
        bmr = (88.4 + 13.4 * weight) + (4.8 * height) - (5.68 * age)
        return bmr
    else:
        bmr = (447.6 + 9.25 * weight) + (3.10 * height) - (4.33 * age)
        return bmr


bmr = calcbmr(gender, height, weight, age)
print("Your BMR is: ", round(bmr, 2), "calories per day")
print("Basal metabolic rate (BMR) is the rate of energy expenditure per unit time by endothermic animals at rest")


def getActivityInput():
    try:
        return str(input("What is your activity level?: "))
    except:
        print("Invalid entry")
        return getActivityInput()


print("What activity level are you:\nsedentary(little to no exercise\nlightly active(exercise 1–3 days/week))")
print("moderately active(exercise 3–5 days/week)")
print("active(exercise 5–7 days/week)\nvery active(hard exercise 5–7 days/week)")


activity_options = [
    "sedentary",
    "lightly active",
    "moderately active",
    "active",
    "very active"
]

activity = getActivityInput()
while activity not in activity_options:
    print("Enter sedentary, lightly active, moderately active, active, very active")
    activity = getActivityInput()

print("Your selected activity level is", activity)


def calcCaloricBurn(bmr, activity):
    if activity == "sedentary":
        burn = float(bmr) * 1.2
        return burn
    elif activity == "lightly active":
        burn = float(bmr) * 1.375
        return burn
    elif activity == "moderately active":
        burn = float(bmr) * 1.55
        return burn
    elif activity == "active":
        burn = float(bmr) * 1.725
        return burn
    elif activity == "very active":
        burn = float(bmr) * 1.9
        return burn


burn = calcCaloricBurn(bmr, activity)
print("Your caloric burn is approximately", burn, "per day")

def getInput(prompt):
    try:
        return float(input(prompt))
    except:
        print("Invalid entry, please enter a number")
        return getInput(prompt)


protein = getInput("How much protein did you eat today?: ")
carbs = getInput("How much carbs did you eat today?: ")
fats = getInput("How much fats did you eat today?: ")
sugar = getInput("How much sugar did you eat today?: ")

print("You ate ", protein, "proteins, ", carbs, "carbs, ", fats, "fats and ", sugar, "sugars today.")
totalEnergy = (protein * 4) + (carbs * 4) + (fats * 9) + (sugar * 4)
print("That's ", totalEnergy, "calories in total!")
print("Protein should be 10-35% of your caloric intake, yours is", round(float((protein*4)/totalEnergy) * 100, 2), "%")
proteinreq = round(float(weight) * 0.8, 2)
print("You should be eating at least", proteinreq, "g of protein per day")
print("Carbohydrates should be 45-65% of your caloric intake", round(float((carbs*4)/totalEnergy) * 100, 2), "%")
print("Fats and oils should be 20-35% of your caloric intake, yours is", round(float((fats*9)/totalEnergy) * 100, 2), "%")



