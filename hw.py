import dictionary

print (dictionary.d)

text = "Salam"
translate = " "
words = text.split()
for w in words:
    translate = translate + " " + dictionary.d[w]

print (translate)
