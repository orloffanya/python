pig_latin = input("lets speak Pig Latin. Type a word (use lower case) ")
first = pig_latin[0]
length = len(pig_latin)
no_first = pig_latin[1:length]
if first == "a":
    print(pig_latin+"way")
elif first == "e":
    print(pig_latin + "way")
elif first == "o":
    print(pig_latin + "way")
elif first == "i":
    print(pig_latin + "way")
elif first == "u":
    print(pig_latin + "way")
else:
    print(no_first+first+"ay")