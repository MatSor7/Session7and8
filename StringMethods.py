text = "abcdefghijklmnop"
print(dir(text))
help(text.isupper)
print(text.isupper())
print("ABC".isupper())
print(text.upper())
print(text.upper().isupper())

new_text = text.upper()
print(text, new_text)

print("bannannnana".count("n"))

print("banabababnan".index("ana"))
print("banababanabnana".replace("ana", "XXYYZZ"))

sentence = "Hello, kind-sir; how may I be of service today?"
print(sentence)
print(sentence.replace(",", "").replace("-", "").replace(";", "").replace("?", ""))
punctuation = ".,;!?-"
for p in punctuation:
    sentence = sentence.replace(p, "")
print(sentence)

print("This is a sentence and I want the words".split(" "))
# This is the first one sofar to not return a string, but rather several strings
text = "Bob goes to school. Bob likes to play tennis. I am friends with Bob."
print(text.find("Bob"))
print(text.rfind("Bob"))
i = 0
while i < len(text):
    i = text.find("Bob", i)
    if i == -1:
        break
    print(i)
    i += 1  # Don't understand...
