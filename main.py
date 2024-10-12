from books import Books
from library import Library

fnac = Library([
    Books("Les misérables", "Victor Hugo", 1862),
    Books("Le Seigneur des anneaux", "J.R.R. Tolkien", 1954),
    Books("1984", "George Orwell", 1949),
    Books("Candide", "Voltaire", 1759)
])

def user_action(number):
    
    match number:
        case 1:
            fnac.show_all_books()
        case 2:
            new_book = create_book()
            fnac.add_book(new_book)
        case 3:
            selected_book = fnac.search_book()
            selected_book.loan_book()
        case 4:
            selected_book = fnac.search_book()
            selected_book.return_book()
        case 5:
            fnac.search_book()
        case 6:
            return
        
def create_book():
    
    all_info = False

    while not all_info:
        
        book_title = input('Veuillez saisir le nom du livre: ')

        if book_title == "":
            print("Erreur, le titre du livre ne peut pas être vide")
        else:
            book_author = input("Veuillez saisir l'auteur du livre: ")

            if book_author == "":
                print("Erreur, le titre du livre ne peut pas être vide")
            else:
                
                try:
                    book_year = int(input("Veuillez saisir l'année de parrution du live: "))
                except ValueError:
                    print("Erreur: Vous devez entrer une année")
            
            all_info = True
    
    new_book = (book_title, book_author, book_year)

    return new_book



print("Bienvenue à la bibliothèque")
print("---------------------------")
print()

print("Vous pouvez:")
print("     1. Voir la liste des livres disponibles dans la bibliothèque")
print("     2. Ajouter un livre")
print("     3. Emprunter un livre")
print("     4. Rendre un livre")
print("     5. Chercher un livre")
print("     6. Partir")

good_input = False

while not good_input:

    try:
        user_choice = int(input("Que souhaitez-vous faire? "))

        if user_choice <= 0 or user_choice > 6:
            print("Erreur: cette option n'est pas disponible.")
        else:
            good_input = True
    except ValueError:
        print("Erreur: Veuillez saisie invalide")

user_action(user_choice)





# fnac.add_book()
# print(fnac.show_available_books())
# print(fnac.search_book("les misérables"))