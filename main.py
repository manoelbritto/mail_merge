# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(".\input\letters\starting_letter.txt") as file:
    text = file.readlines()

with open(".\input\\Names\invited_names.txt") as name:
    name = name.readlines()

for name_text in name:
    name_text = name_text.replace("\n", "")
    with open(f".\output\ReadyToSend\\{name_text}.txt", "w") as letter:
        for replace_text in text:
            # print(replace_text)
            if replace_text.strip() == 'Dear [name],':
                header = replace_text.strip()
                replace_text = header.replace("[name]", name_text)

            letter.write(replace_text)
