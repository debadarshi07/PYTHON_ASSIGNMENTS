score = float(input("Enter your numeric score: "))

if score >= 90 :
    print("Grade: 'A' \nExcellent!")
elif 80 <= score < 90 :
    print("Grade: 'B' \nGood!")
elif 70 <= score < 80 :
    print("Grade: 'C' \nAverage!")
elif 60 <= score < 70 :
    print("Grade: D \nNeeds Improvement!")
else :
    print("Grade: 'F' \nFailing!")