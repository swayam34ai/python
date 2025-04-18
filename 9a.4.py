lst = ['madam', 'Python', 'malayalam', 12321]
def is_palindrome(s):
    return str(s) == str(s)[::-1]
for item in lst:
    if is_palindrome(item):
        print(item)