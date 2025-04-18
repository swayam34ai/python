def frequency(text):
    words = text.split()
    freq_dict = {}  
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    sorted_freq = dict(sorted(freq_dict.items())) 
    return sorted_freq
input_str = input("Enter a sentence: ")
word_frequencies = frequency(input_str)
print("Word Frequencies:")
for word, count in word_frequencies.items():
    print(f"{word}: {count}")