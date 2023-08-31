import json


class FlashCard:  # Class names are typically in CamelCase
    def __init__(self, number, frontCard, backCard):
        self.number = number
        self.frontCard = frontCard
        self.backCard = backCard
    
    def to_dict(self):
        return {
            "number": self.number,
            "frontCard": self.frontCard,
            "backCard": self.backCard 
        }
       
head = 1

def addCard(flashCardList):
    
    adding = True
    while adding:
        frontCard = input("Front: ")
        backCard = input("Back: ")

        newCard = FlashCard(cardCount() + 1, frontCard, backCard)

        with open("flashcards.txt", "w") as file:
            json.dump(newCard.to_dict(), file, indent=4)

def removeCard():
    viewFlashcards()
    delete = True


def viewFlashcards():
    with open("flashcards.txt", "r") as file:
        for line in file:
            card = json.loads(line)
            print (f"Front: {card['frontCard']} Back: {card['backCard']}")
    

def cardCount():
    count = 0
    with open("flashcards.txt", "r") as file:
        for line in file:
            count +=1
    return count
            

def main():
    flashCardList = []
    choiceLoop = True
    while choiceLoop:
        choice = input("What do you want to do? Add, remove or view Flashcards or exit application: ").upper
        if choice == "ADD":
            addCard()
        elif choice == "REMOVE":
            removeCard()
        elif choice == "VIEW":
            viewFlashcards()
        elif choice == "EXIT":
            choiceLoop == False
        else:
            print("Not a valid option.")