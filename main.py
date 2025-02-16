def num_words(str):
    return len(str.split())

def count_char(str):
    char_count = {}
    chars = set()
    words = str.split()
    all_chars = []

    # Put individual characters into a set to make sure they are unique
    for word in words:
        temp_list = list(word)
        for char in temp_list:
            char = char.lower()
            all_chars.append(char) 
            chars.add(char)

    # Loop through all chars while counting how many of each char and saving results to dictionary char_count
    # Temp value to hold character count
    for char in chars:
        count = 0
        for i in range(len(all_chars)):
            if all_chars[i] == char:
                count += 1
        char_count[char] = count

    # Need to account for spaces
    char_count[' '] = str.count(" ")

    # Return the dict
    return char_count


def main():
    # Read file contents
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    
    # # Print file contents to the console
    # print(file_contents)

    # # Print number of words in file
    # print(num_words(file_contents))

    # Get count of each character in the file and store in dictionary 
    char_count = count_char(file_contents)
    print(char_count)



main()