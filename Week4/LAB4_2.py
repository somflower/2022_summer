"""reverse_sentence = input()

for char in reverse_sentence[-1::-1]:
    print(char)"""

sentence = input()
reverse_sentence = " "

for char in sentence:
    reverse_sentence = char + reverse_sentence
print(reverse_sentence)

for i in range(len(sentence) - 1, -1, -1):
    print(sentence[i], end = "")
print()

#두칸씩 띄어 출력하기
for i in range(0, len(sentence), 2) :
    print(sentence[i])