PLACEHOLDER = "[name]"

with open('./Input/Names/invited_names.txt', mode='r') as names_file:
    names = names_file.readlines()

with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_names = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_names)
        with open(f'./Output/ReadyToSend/Invitation_for_{stripped_names}.txt', mode='w') as invitation:
            invitation.write(new_letter)