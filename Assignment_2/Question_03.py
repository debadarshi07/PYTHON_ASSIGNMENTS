score = float(input("Enter your numeric score: "))

if score >= 90 :
    print("Grade: 'A' \nExcellent!")
elif score >= 80 and score < 90 :
    print("Grade: 'B' \nGood!")
elif score >= 70 and score < 80 :
    print("Grade: 'C' \nAverage!")
elif score >= 60 and score < 70 :
    print("Grade: D \nNeeds Improvement!")
else :
    print("Grade: 'F' \nFailing!")