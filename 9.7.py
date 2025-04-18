def ispalindrome(text):
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]
input_str = input("Enter a string: ")
if ispalindrome(input_str):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")