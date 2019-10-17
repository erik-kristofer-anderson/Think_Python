# write a definition for a class name Kangaroo,

class Kangaroo:
    """This class represents a Kangaroo, apparently
    attribute: name
    attribute: pouch_contents
    """

    def __init__(self, name = "", obj = None):
        self.pouch_contents = []
        if obj != None:
            self.pouch_contents.append(obj)
        self.name = name

    def print_kangaroo(self): #done (didn't need change)
        """Prints a string representation of the Kangaroo."""
        print(str(self))


    def put_in_pouch(self, obj):
        self.pouch_contents.append(obj)

    def __str__(self):
        s = self.name + ' is a Kangaroo with pouch contents: ' + str(self.pouch_contents)
        return s
