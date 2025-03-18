def  c_vowels(n):
    vowels='aeiou'
    if len(n)==0:
        return 0
    else:
        if n[0].lower() in vowels:
            return 1 + c_vowels(n[1:])
        return c_vowels(n[1:])
str1=input("enter string")
print(c_vowels(str1))
