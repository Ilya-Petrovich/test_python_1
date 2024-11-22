class Library:
    """
    A class used to represent a library

    Attributes
    ----------
    books : dict
        Dictionary that contains all books
    statuses : list
        List of possible book statuses

    Methods
    -------
    add(title, author, year)
        Adds a book to library
    delete(id)
        Deletes a book from library
    find(arg)
        Finds books by argument (title, author, year)
    list()
        Prints all books in library
    change_status(id, status):
        Changes status of the book
    """

    def add(self, title, author, year):
        """
        Parameters
        ----------
        title : str
            The title of the book
        author : str
            The author of the book
        year : int
            Book publishing year
        """

    def delete(self, id):
        """
        Deletes a book if given id exists, otherwise prints a warning

        Parameters
        ----------
        id : int
            The id of the book
        """

    def find(self, arg):
        """
        Finds books that match given arg otherwise prints a warning

        Parameters
        ----------
        id : int
            The id of the book
        """

    def list(self):
        """
        Prints list of all books
        """


if __name__ == "__main__":
    pass
