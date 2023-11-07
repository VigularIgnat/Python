def displayMenu():
    print("txt spk cntv")
    print("-"*15)
    print("Menu:")
    print("c-convert sentenes")
    print("p-print dictionary")
    print("a-add a work")
    print("d- delete a word")
    print("q-quit")


def convertSentenses():
    sentence=input("Input sentenses").lower()
    translatedSentenses=""
    listOfwords=sentence.split()

    for word in listOfwords:
        if word in dictionary:
            translatedSentenses+=dictionary[word]+""
        else:
            translatedSentenses+=word+" "
    print("==>")
    print(translatedSentenses)

def addDictionaryItem():
    txtToAdd=input("Enter the text-speak to add to the dictionary:")
    meaning=input("What does this mean?:")
    dictionary[txtToAdd]=meaning
def deleteDictionaryItem():
    txtToDelete=input("Enter the text-speak to delete from dictionary:")
    del dictionary[txtToDelete]
dictionary={
    "lol": " lough out loud ",
    "idk": "l dont know ",
    "bc": "becauce "
   
    }
running=True
displayMenu()
while running== True:
    menuChoice=input(">_").lower()

    if menuChoice=="c":
        convertSentenses()

    elif menuChoice=="p":
        print(dictionary)
       
    elif menuChoice=="a":
        addDictionaryItem()
    elif menuChoice=="d":
         deleteDictionaryItem()
    elif menuChoice=="q":
       running=False
    else:
        print("Invalid syntaxys")
