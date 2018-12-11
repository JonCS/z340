#python
import random

print("\n** Begin Script **\n")

MAX_CHARS = 136
MIN_WORDS = 48
NUM_SAMPLES = 1000

# dictionary of words
f = open("alice_oz.txt", "rt")

print("\nreading 'alice_oz.txt'...\n")

for x in f:
  #print(x)
  x.strip()
f.close()

wordList = x.split(' ')
#print(wordList[0])

out = open("word_salad.txt", "a")
out2 = open("space_salad.txt", "a")

print("\noutput1 appends to 'word_salad.txt'\n")
print("\noutput2 appends to 'space_salad.txt'\n")

random.seed()

for i in range(NUM_SAMPLES):
  salad = random.sample(wordList,MIN_WORDS)
  #print(salad)

  s2 = ""
  s3 = ""
  s3Offset = 0 

  while (len(salad) > 0):
    word = salad.pop();
    s2 += word;
    s3 += word + ' ' 

    #to avoid re-counting letters
    if (len(s2) < MAX_CHARS):  
      s3Offset += 1 
  #print(s2)
  #print("\n")
  #print(len(s2))
  #print("\n")
  s2 = s2[0:MAX_CHARS]
  s3Offset += MAX_CHARS
  s3 = s3[0:s3Offset]
  #print(s2)
  #print("\n")
  #print(len(s2))
  #print("\n")
  out.write(s2 + "\n")
  out2.write(s3 + "\n")

out.close()
out2.close()
print("\n** End Script **\n")

