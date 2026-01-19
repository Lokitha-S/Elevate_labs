try:
    maths   = int(input("Enter Math mark: "))
    science = int(input("Enter Science mark: "))
    social  = int(input("Enter Social mark: "))
    english = int(input("Enter English mark: "))

    total_marks = maths + science + social + english
    average = total_marks / 4
    
    print(f"Total Score: {total_marks}")
    print(f"Average: {average}")
    
    if total_marks >= 35 or total_marks == 40:
        print("Result: Excellent")
        
    elif 20 < total_marks < 35: # Refactor: Used chained comparison for readability
        print("Result: Average")
        
    else:
        # Nested condition for specific pass rule
        if total_marks == 10:
            print("Result: Just Pass")
        else:
            print("Result: Fail")

except ValueError:
    print("Invalid Input: Please enter numbers only.")
