def main():
    #Asking the user for the greetings
    greeting = input("Greetings: ")
    print(f"${value(greeting)}")

def value(greeting):
    # Checking either user greeted with word starts with h and it is not hello
    greeting=greeting.title()
    if greeting.startswith("H") and "Hello" not in greeting:
        return 20
    #checking either the greeting have hello
    elif "Hello" in greeting:
        return 0
    #All other conditions
    else:
        return 100
    # Calling the main  function
if __name__=="__main__":
    main()
