Sent="Hi My Name is the Rohith"
Words=Sent.split()
# Big=Words[0]
Big=""
for word in Words:
    if len(word) > len(Big):
        Big=word
print(Big)
