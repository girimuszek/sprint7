intro='''*******************************************************************
         * Welcome to my BMI calculator! In order to see what your BMI is, * 
         *                 please fill out the parameters!                 *                                           
         *******************************************************************
         '''

print(intro)

# WEIGHT VVV
while True:
    try:
        weightPoundsInput = int(input("Please enter your weight in pounds -->"))
    except ValueError:
        print("Please make sure that you're only typing in numbers only!")
        continue
        
    if weightPoundsInput <= 70 or weightPoundsInput >500: 
        print("Either your weight is too severe to be measured by this test, or you made a typo. Please try again!")
        continue
    else:
        print("Weight successfully added!")
        break

# HEIGHT VVV
while True:
    try:
         heightInchesInput= int(input("Please enter your height in inches -->"))
    except ValueError:
        print("Please make sure that you're only typing in numbers only!")
        continue
        
    if heightInchesInput <25 or heightInchesInput >96: 
        print("There is no way that that's your height. Please type in the correct height (in inches)")
        continue
    else:
        print("Height succesfully added!")
        break

# AGE VVV    
print("Okay, now that that's out of the way, let me ask you your age! What is it?")

while True:
    try:
        ageInput = int(input("Please enter your age -->"))
    except ValueError:
        print("Please make sure that you're typing in numbers only!")
        continue
        
    if  ageInput <2  or ageInput >105: 
        print("Improper age. Try again")
        continue
    else:
        print("Age successfully added!")
        break

# BLOOD PRESSURE VVV
bloodPressurePrompt = '''What is your blood pressure like? Pick from the following options:
                         
                         1 = normal
                         2 = elevated
                         3 = stage 1
                         4 = stage 2
                         5 = crisis
                         
                         Type out an answer between 1-5 -->'''   
while True:
    try:
        bloodPresInput = int(input(bloodPressurePrompt))
    except ValueError:
        print("Please make sure that you're typing in numbers only!")
        continue
        
    if  bloodPresInput <1 or bloodPresInput >5: 
        print("Please choose between 1-5 only. Please try again.")
        continue
    else:
        print("Blood pressure status added!")
        break

# FAMILY DISEASE VVV
famDiseasePrompt = '''Does your family have a history of some of these diseases below? 
                         
                         1 = diabetes
                         2 = cancer
                         3 = Alzheimers
                         4 = None of the above
                         
                         Type out an answer between 1-4 -->'''   

while True:
    try:
        famDiseaseInput = int(input(famDiseasePrompt))
    except ValueError:
        print("Please make sure that you're typing in numbers only!")
        continue
        
    if  famDiseaseInput <1 or famDiseaseInput >4: 
        print("Please choose between 1-4 only. Please try again.")
        continue
    else:
        print("Family disease status added!")
        break 

# Calculations Stuff VVV
 


kilos = weightPoundsInput * 0.453

meters = heightInchesInput * 0.0254



bmi = kilos / meters**2

print("bmi is", bmi)

totalScore = 0

bmiScoreDict = {
    'normal': 0,
    'overweight': 30,
    'else': 75
}

if bmi >=18.5 and bmi<=24.9:
    totalScore += bmiScoreDict['normal']

if bmi >=25.0 and bmi<=29.9:
    totalScore += bmiScoreDict['overweight']

if bmi >=30.0:
    totalScore += bmiScoreDict['else']

print(totalScore)


    
    
    
    
    
    
print("PRINTING RESULTS")



