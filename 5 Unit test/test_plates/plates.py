def main():
    # Prompt user to input license plate number
    plate = input("Plate: ")

    # Check if the plate is valid
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if the length of the plate number is within the valid range
    if 2 <= len(s) <= 6:
        s1, s2 = "", ""

        # Separate letters and numbers
        for i in range(len(s)):
            if s[i].isnumeric():
                s2 += s[i::]
                break
            else:
                s1 += s[i]

        # Conditions for validity: at least 2 letters, all numeric part and not starting with 0, or if there's no numeric part
        if len(s1) >= 2 and s1.isalpha() and s2.isdigit() and s2[0] != "0" or s2 == "":
            return True
        else:
            return False
    else:
        return False  # Length of plate number is not within the valid range

if __name__=="__main__":
    main()
