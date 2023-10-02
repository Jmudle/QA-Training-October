word = input("Enter a word: ")

vowel_count = 0

for char in word:
    if char.lower() in 'aeiou':
        vowel_count += 1

print(f"The word '{word}' contains {vowel_count} vowel(s).")
