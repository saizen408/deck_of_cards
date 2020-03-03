class GrumpyDict(dict):
    def __repr__(self):
        print("None of your business")
        return super().__repr__()
        # prints the dicts version of repr

    def __missing__(self, key):
        print(f"YOU WANT {key}? WELL IT AINT HERE!")

    def __setitem__(self, key, value):
        print("YOU WANT TO CHANGE THE DICTIONARY?, OK FINE...")
        super().__setitem__(key, value)
        # calls the dict version of __setitem__

    def __contains__(self, item):
        print("No it aint in here!!!!!")
        return False


data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data)
data['city'] = 'Tokyo'
print(data)
