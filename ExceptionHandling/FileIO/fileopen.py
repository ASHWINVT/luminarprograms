#create a reference
#f=open

f=open("demo","r")
word=[]
for lines in f:
    words=lines.split(" ")
    for wrd in words:

        words.append(lines.split(" "))
    print(word)