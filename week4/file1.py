# Open a file in write mode
with open("text_file.txt", "w") as file:
    # Write content to the file
    file.write("Hello, this is a text file.\n")
    file.write("This file is opened in normal mode (text mode).\n")
    
# Open a file in read mode
with open("text_file.txt", "r") as file:
    # Read content from the file
    content = file.read()
    print(content)

#Binary Mode
# Open a file in binary write mode
with open("binary_file.bin", "wb") as file:
    # Write content to the file
    file.write(b'Binary data\x00\x01\x02')
    
# Open a file in binary read mode
with open("binary_file.bin", "rb") as file:
    # Read content from the file
    content = file.read()
    print(content)
