from books import Books
from library import Library

fnac = Library([
    Books("Les misérables", "Victor Hugo", 1862),
    Books("Le Seigneur des anneaux", "J.R.R. Tolkien", 1954),
    Books("1984", "George Orwell", 1949),
    Books("Candide", "Voltaire", 1759)
])

# Permet de gérer l'appel des fonctions selon le choix de l'utilisateur
def user_action(number):
    
    match number:
        case 1:
            fnac.show_all_books()
            print()
        case 2:
            new_book = create_book()
            fnac.add_book(new_book)
            print()
        case 3:
            selected_book = looking_for_book()
            print(selected_book.loan_book())
            print()
        case 4:
            selected_book = looking_for_book()
            selected_book.return_book()
            print()
        case 5:
            looking_for_book()
            print()
        case 6:
            print(fnac.show_available_books())
            print()

# Fonction permettant de créer un livre. Renvoie un objet Livre
def create_book():
    
    all_info = False

    while not all_info:
        
        book_title = input('Veuillez saisir le nom du livre: ')
        print()

        if book_title == "":
            print("Erreur, le titre du livre ne peut pas être vide")
        else:
            book_author = input("Veuillez saisir l'auteur du livre: ")
            print()

            if book_author == "":
                print("Erreur, le titre du livre ne peut pas être vide")
            else:
                
                try:
                    book_year = int(input("Veuillez saisir l'année de parrution du live: "))
                    print()
                except ValueError:
                    print("Erreur: Vous devez entrer une année")
            
            all_info = True
    
    new_book = Books(book_title, book_author, book_year)

    return new_book

# Fonction permettant de chercher un livre d'après le titre. Sert pour la recherche, le prêt et le retour d'un livre
def looking_for_book():

    book_title = input('Veuillez saisir le nom du livre: ')
    print()

    if book_title == "":
        print("Erreur, le titre du livre ne peut pas être vide")
    else:
        book_searched = fnac.search_book(book_title)

    return book_searched

end_of_program = False

print("Bienvenue à la bibliothèque")
print("---------------------------")
print()

# Boucle d'action
while not end_of_program:
    print("Vous pouvez:")
    print("     1. Voir la liste des livres disponibles dans la bibliothèque")
    print("     2. Ajouter un livre")
    print("     3. Emprunter un livre")
    print("     4. Rendre un livre")
    print("     5. Chercher un livre")
    print("     6. Voir le nombre de livre disponible")
    print("     7. Partir")
    print()

    good_input = False

    while not good_input:

        try:
            user_choice = int(input("Que souhaitez-vous faire? "))
            print()

            if user_choice <= 0 or user_choice > 7:
                print("Erreur: cette option n'est pas disponible.")
            else:
                good_input = True
        except ValueError:
            print("Erreur: Veuillez saisie invalide")

    if user_choice == 7:
        end_of_program = True
    else:
        user_action(user_choice)