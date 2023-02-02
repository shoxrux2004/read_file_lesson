#Rread file and convert to list
def read_file(filename: str) -> list:
    """
    Reads a file and returns a list of int digits.
    
    Args:
        filename (str): The name of the file to read.
    Returns:
        data (list): A list of list of int digits from the file.
    """
    # Open the file
    f = open(filename).read()
    f = f.split(",")
    list_of_integers = []
    for i in f:
        list_of_integers.append(int(i))
    # Read the file
    return list_of_integers

#Print list from file
print(read_file("data.txt"))