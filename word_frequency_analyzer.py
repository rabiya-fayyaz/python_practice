# Problem:
# User enters a paragraph.

# Display:
# • Frequency of every word
# • Most common word
# • Total unique words

# Concepts:
# • Dictionaries
# • Loops
# • Strings
# • Functions
# learn collection.counter *new concept*
from collections import Counter
def get_paragraph():
  paragraph= input("Enter a paragraph:")
  words = paragraph.lower().split()
  c = Counter(words)

  total_words = len(words)
  print("Total words :", total_words)

  unique_words = len(set(words))
  print("Total unique words:", unique_words)

  print("Longest word:", max(words, key=len))
  print("Shortest word:", min(words, key=len))

  for word, frequency in c.items():
    print(word, ":", frequency) 

  most_word, count = c.most_common(1)[0]
  print("Most common word:", most_word)
  print("Frequency:", count)
  
  total = 0
  for word in words:
    total += len(word)
    
  average = total / len(words)
  print("average word length :",average)

get_paragraph()