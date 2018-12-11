#python
import random

print("\n** Begin Script **\n")

MAX_CHARS = 136
MIN_WORDS = 48
NUM_SAMPLES = 1000

# dictionary of words
f = open("alice_oz.txt", "rt")

print("\reading 'alice_oz.txt'...\n")

for x in f:
  #print(x)
  x.strip()
f.close()

wordList = x.split(' ')

out = open("english_text.txt", "a")
out2 = open("space_english.txt", "a")

print("\noutput1 appends to 'english_text.txt'\n")
print("\noutput2 appends to 'space_english.txt'\n")

random.seed()


for x in range(NUM_SAMPLES):
  n = random.randint(0,(len(wordList) - MIN_WORDS))
  s2 = ""
  s3 = ""
  s3Offset = 0

  #print(n)
  #print(wordList[n])

  for i in range(MIN_WORDS):
    s2 += wordList[n]
    s3 += wordList[n] + ' '
    n += 1
    if (len(s2) < MAX_CHARS):
      s3Offset += 1

  #print("\n")
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

