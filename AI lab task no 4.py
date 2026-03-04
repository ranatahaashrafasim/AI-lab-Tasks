print("Part 1: LUHN Algorithm")

num = input("Enter card number: ")

digits = []
for d in num:
    digits.append(int(d))

check_digit = digits[-1]
digits = digits[:-1]
digits.reverse()

for i in range(len(digits)):
    if i % 2 == 0:
        digits[i] = digits[i] * 2
        if digits[i] > 9:
            digits[i] = digits[i] - 9

total = sum(digits) + check_digit

if total % 10 == 0:
    print("Valid card number")
else:
    print("Invalid card number")


print("\nPart 2: Remove Punctuations")

text = input("Enter a string: ")

punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
result = ""

for ch in text:
    if ch not in punct:
        result = result + ch

print(result)


print("\nPart 3: Sort Sentence Alphabetically")

sentence = input("Enter a sentence: ")

words = sentence.split()
words.sort()

for w in words:
    print(w)