tweet = "hellow my name is python and i am a programming language ."
print(tweet[0:5])
print(tweet[6:8])
print(tweet[11:15])
print(tweet[0:5] + " " + tweet[6:8] + " " + tweet[11:15])
print(tweet[0:5] + " " + tweet[6:8] + " " + tweet[11:15] + " " + tweet[16:18] + " " + tweet[19:21] + " " + tweet[22:28])
print("end of tweet :", tweet[-8:])
print("start of tweet :", tweet[:5])
print("middle of tweet :", tweet[6:28])
print("end of tweet :", tweet[-8:])
print(tweet[::2])
print(tweet[1::2])
print(tweet[::-1])
print(tweet[1:28:2])

# messy
messy = "hellow my name is python and i am a programming language . % $#@!&*() . hi !!!!!!!"
cleaned = messy.replace("!!!!!!!", "nazmul")
print(cleaned)
cleaned = cleaned.replace("%", "")
cleaned = cleaned.replace("$", "")
cleaned = cleaned.replace("#", "")
cleaned = cleaned.replace("@", "")
cleaned = cleaned.replace("!", "")
cleaned = cleaned.replace("&", "")
cleaned = cleaned.replace("*", "")
cleaned = cleaned.replace("(", "")
cleaned = cleaned.replace(")", "")
print(cleaned)
print(cleaned.split())
print(cleaned.capitalize())
print(cleaned.title())
print(cleaned.upper())
print(cleaned.lower())





