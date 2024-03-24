def arrify(file_path):
    iArr = []
    with open(file_path, 'r') as file:
        for line in file:
            # Assuming each line contains elements separated by spaces
            array = line.strip().split()
            iArr.append(array)
    return iArr

# Example usage:
#file_path = 'itemList.txt'  # Replace 'input.txt' with the path to your text file
#itemArray = arrify(file_path)
#print(itemArray)