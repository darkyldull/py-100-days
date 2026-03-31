#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



with open("D:\\Projects\\py-100-days\\Day24\\mail-merge\\Input\\Names\\invited_names.txt", mode = "r") as file:
    contents = file.readlines()

list_of_names = []

for content in contents:
    list_of_names.append(content.strip())

with open("D:\\Projects\\py-100-days\\Day24\\mail-merge\\Input\\Letters\\starting_letter.txt", mode = "r") as file:
    letter = file.read()

for name in list_of_names:
    new_letter = letter.replace("[name]", name)
    with open(f"D:\\Projects\\py-100-days\\Day24\\mail-merge\\Output\\letter_for_{name}.txt", mode = "w") as file:
        file.write(new_letter)
