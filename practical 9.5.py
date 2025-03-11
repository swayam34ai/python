def ispangram(input_string):
    a_set = set('abcdefghijklmnopqrstuvwxyz')
    i_set = set(c.lower() for c in input_string if c.isalpha())
    return i_set >= a_set
sample1 = "The quick brown fox jumps over the lazy dog"
sample2 = "Crazy Fredrick bought many very exquisite opal jewels"
print(f"Is the first sentence a pangram? {ispangram(sample1)}")
print(f"Is the second sentence a pangram? {ispangram(sample2)}")
    
