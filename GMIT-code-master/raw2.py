# question 2
letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def shift(word):
    new_word=""
    shift=int(input("enter shift number :"))
    for i in range(0,len(word)):
        if word[i]==" ":
            new_word=new_word+" "
        else:
            index=letter.index(word[i])
            new_idex=index+shift
            if new_idex >25:
                new_idex=new_idex-26
                new_word=new_word+letter[new_idex]
            else:
                new_word=new_word+letter[new_idex]
    print(new_word)


def decode(word):
    new_word=""
    shift=int(input("enter shift number :"))
    for i in range(0,len(word)):
        if word[i]==" ":
            new_word=new_word+" "
        else:
            index=letter.index(word[i])
            new_idex=index-shift
            if new_idex <0:
                new_idex=new_idex+26
                new_word=new_word+letter[new_idex]
            else:
                new_word=new_word+letter[new_idex]
    print(new_word)

cont=True
while cont==True:
    word=input("enter the message :")

    coder=int(input("1 :encode or 2 :decode :"))
    if coder==1:
        shift(word)
    else:
        decode(word)
    c=input("Do you want to continue [y/n]")
    if c=="n":
        print("Okay! Good Bye")
        cont=False
