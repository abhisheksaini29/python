# Ask User to input a String of min 10 words and max 19 words and perform the following:
# 1. Print full string and length of string
# 2. Tell String is palindrome or not mean
# 3. Tell middle word in the string.
# 4. Print Second last word in the String.

def main():

    # Ask user for input

    user_input = input("Please enter a string of minimum 10 words and maximum 19 words: ")

    

    # Split the input into words

    words = user_input.split()

    

    # Check the number of words

    if len(words) < 10 or len(words) > 19:

        print("Error: The input must contain between 10 and 19 words.")

        return

    

    # 1. Print full string and length of string

    print(f"Full string: {user_input}")

    print(f"Length of string: {len(user_input)} characters")

    

    # 2. Check if the string is a palindrome

    cleaned_string = ''.join(filter(str.isalnum, user_input)).lower() 
    is_palindrome = cleaned_string == cleaned_string[::-1]

    print(f"The string is {'a palindrome' if is_palindrome else 'not a palindrome'}.")

    

    # 3. Tell the middle word in the string

    middle_index = len(words) // 2

    middle_word = words[middle_index] if len(words) % 2 != 0 else words[middle_index - 1] 

    print(f"The middle word is: '{middle_word}'")

    

    # 4. Print the second last word in the string

    second_last_word = words[-2]

    print(f"The second last word is: '{second_last_word}'")


# Run the main function 
if __name__ == "__main__":
    main()