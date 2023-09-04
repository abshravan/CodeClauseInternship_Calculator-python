import re

def calculate(expression):
    try:
        expression = re.sub(r'[^0-9+\-*/() ]', '', expression)
        result = eval(expression)
        return result
    except Exception as e:
        return "Error: " + str(e)

def main():
    print("Python Calculator")
    while True:
        user_input = input("Enter an expression (or 'q' to quit): ")
        
        if user_input.lower() == 'q':
            break
        
        if user_input.lower() == 'clear':
            print("Cleared.")
            continue
        
        result = calculate(user_input)
        print("Result:", result)

if __name__ == "__main__":
    main()
