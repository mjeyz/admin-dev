PlaceHolder = "[name]"

with open("./input/names/invited_names.txt") as letter_name:
    names = letter_name.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    content = letter_file.read()
    for name in names:
        striped_name = name.strip()
        new_letter = content.replace(PlaceHolder, striped_name)

        with open(f"./Output/letter_for_{striped_name}.md", mode="w") as completed_letter:
            completed_letter.write(new_letter)