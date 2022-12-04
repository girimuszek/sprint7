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


ageScoreDict = {
    
	'<30' :	0, 
	'<45' :	10, 
	'<60' :	20, 
	'else':	30 
}

if ageInput >=2 and ageInput<=30:
    totalScore += ageScoreDict['<30']

if ageInput >=31 and ageInput<=45:
    totalScore += ageScoreDict['<45']

if ageInput >=46 and ageInput<=60:
    totalScore += ageScoreDict['<60']

if ageInput >60:
    totalScore += ageScoreDict['<60']


bloodPressureDict = {
	'normal': 0,
	'elevated': 15,
	'stage 1': 30,
	'stage 2': 75,
	'crisis': 100  
}    

if bloodPresInput == 1:
    totalScore += bloodPressureDict['normal']

if bloodPresInput == 2:
    totalScore += bloodPressureDict['elevated']

if bloodPresInput == 3:
    totalScore += bloodPressureDict['stage 1']

if bloodPresInput == 4:
    totalScore += bloodPressureDict['stage 2']

if bloodPresInput == 5:
    totalScore += bloodPressureDict['crisis']

familyPressureDict = {
	'diabetes': 10, 
	'cancer' : 10, 
	'Alzheimers': 10, 
    'none': 0
}

if famDiseaseInput == 1:
    totalScore += familyPressureDict['diabetes']

if famDiseaseInput == 2:
    totalScore += familyPressureDict['cancer']

if famDiseaseInput == 3:
    totalScore += familyPressureDict['Alzheimers']

if famDiseaseInput == 4:
    totalScore += familyPressureDict['none']
    


totalScoreDict = {
    '<=20': 'low risk',
	'<=50': 'moderate risk',
	'<=75': 'high risk',
	'else': 'uninsurable'
}
    


print("LOADING TEST RESULTS!!!")



if totalScore <=20:
    print("You are a", totalScoreDict['<=20'])

if totalScore >20 and totalScore <=50:
    print("You are a", totalScoreDict['<=50'])

if totalScore >50 and totalScore <=75:
    print("You are a", totalScoreDict['<=75'])

if totalScore >75:
    print("You are a", totalScoreDict['else'])
    


