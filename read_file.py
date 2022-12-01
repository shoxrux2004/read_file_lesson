#Rread file and convert to list
def read_file(filename: str) -> list:
    """
    Reads a file and returns a list of lines.
    
    Args:
        filename (str): The name of the file to read.
    
    Returns:
        data (list): A list of lines from the file.
    """
    # Open the file
    data = list(map(int,open(filename, "r").read().split(',')))
    # Read the file
    return data

#Print list from file
print(read_file("read_file_2.txt"))