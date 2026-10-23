with open ("notes.txt", "r") as file:
    content = file.read()
    words = content.split()
    
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
print(count)        