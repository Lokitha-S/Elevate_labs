import logging

logging.basicConfig(filename="errors.log", level=logging.ERROR,filemode='w',format="%(asctime)s - %(levelname)s - %(message)s")

def simple_calculator():
    print("--- Simple Division Tool ---")
    
    try:
        num = int(input("Enter a number: "))
        result = 100 / num
        
    except ValueError:
        msg = "Error: Please enter numbers only, not text!"
        print(msg)
        logging.error(msg)

    except ZeroDivisionError:
        msg = "Error: You cannot divide by zero!"
        print(msg)
        logging.error(msg)

    else:

        print(f"Success! 100 divided by {num} is {result}")

    finally:
        print("Task 9 simulation finished.")

simple_calculator()