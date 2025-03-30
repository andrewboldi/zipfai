import random
inp = open("all.txt", encoding="latin-1").readlines()

pd = {}
for i, x in enumerate(inp):
  inp[i] = x.split("\n")[0]
  prob = float(inp[i].split("% ")[0]) / 100
  word = inp[i].split("% ")[1].split(" ")[0]
  pd[word] = prob


n = int(input("Enter number of words to generate: ") or 100)
words = random.choices(list(pd.keys()), weights=list(pd.values()), k=n)
for word in words:
  print(word, end=" ")
 
print("\n")
