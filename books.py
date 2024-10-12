class Books: 

    def __init__(self, title, author, year, available = True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    # Affiche les info du bouquin
    def show_information(self):
        if self.available == True:
            string_available = "est disponible"
        elif self.available == False:
            string_available = "n'est pas disponible"

        return f'"{self.title}" de {self.author} ({self.year}) {string_available}'

    # Change l'état disponible à False si le livre est dispo, sinon affiche un message indiquant qu'il n'est pas dispo
    def loan_book(self):
        if self.available == False:
            return f'Le livre "{self.title}" de {self.author} ({self.year}) n\' est pas disponible en prêt.'
        else:
            self.available = False
            return f'Vous venez d\'emprunter le livre "{self.title}" de {self.author} ({self.year}).'

    # Change l'état disponible à True
    def return_book(self):
        self.available = True
        return f'Vous venez de ramener le livre "{self.title}" de {self.author} ({self.year}).'
