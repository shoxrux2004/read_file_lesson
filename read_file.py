#Rread file and convert to list
def read_file(filename: str) -> list[int]:
    """
    Reads a file and returns a list of integers.
    Args:
        filename (str): The name of the file to read.
    Returns:
        data (list): A list of integers from the file.
#     """
#     # Open the file
#     # Read the file
#     return 0 
# #Print list from file
    list1=[]
    f=open(filename)
    a=f.read()
    t=a.split(',')
    for i in t:
        list1.append(int(i))
    return list1
print(read_file("data.txt"))
