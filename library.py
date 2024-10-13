class Library:

    def __init__(self, books_list = []):
        self.books_list = books_list

    # Permet d'ajouter un livre à la bibliothèque
    def add_book(self, book):
        self.books_list.append(book)

    # Permet de montrer les livres de la bibliothèque
    def show_all_books(self):
        for book in self.books_list:
            print(book.show_information())

    # Liste le nombre de livre disponible en prêt
    def show_available_books(self):
        count = 0

        for book in self.books_list:
            if book.available:
                count +=1

        return f'Il y a {count} livres disponible en prêt.'

    # Permet de chercher un livre avec son titre
    def search_book(self, title):
        
        for book in self.books_list:
            if title == book.title:
                print(book.show_information())
                print()
                return book
            else:
                return f"Aucun livre \"{title}\" n'est présent dans la bibliothèque!"