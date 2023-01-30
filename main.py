def search_word(file_path):
    search_word = input("Enter the word to search for: ")
    with open(file_path, "r") as file:
        lines = file.readlines()

    for line in lines:
        if search_word in line:
            print(line)

file_path = "path/to/textfile.txt"
search_word(file_path)
