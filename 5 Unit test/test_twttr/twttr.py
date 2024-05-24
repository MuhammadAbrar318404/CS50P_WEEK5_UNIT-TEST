def main():
    # Prompt the user to input a string 
    word = input("Input: ")
    # Print the shortened version of the string 
    print(shorten(word))
# Function to eliminate the vowels from the provided string 
def shorten(word):
    # Define a string containing all vowels (both uppercase and lowercase)
    vowels = "aAeEiIoOuU"
    # Initialize an empty string to store the result
    user_str1 = ""
    # Iterate over each character in the input word
    for i in word:
        # If the character is not a vowel, add it to the result string
        if i not in vowels:
            user_str1 = user_str1 + i
        else:
            pass  # If the character is a vowel, do nothing
    # Return the result string with vowels removed
    return user_str1

# Ensure the main function is called only when the script is executed directly
if __name__ == "__main__":
    main()
