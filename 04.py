class characters:

    def __init__(self, title, character_name, power_score, biography):
        self.title = title
        self.character_name = character_name
        self.power_score = '| ' + 'Power score - ' + power_score + ' -\n'
        self.biography = biography

    def title_name(self):
        print('{} {}'.format(self.title,self.character_name))

    def characters_data(self):
        print('{} {} {} {}'.format(self.title, self.character_name, self.power_score, self.biography))


B_Cider = characters('Barbarian', 'Cider', '4854', 'Not much is known about this character')
L_Cido = characters('Lord', 'Cido', '7910', 'Not much is known about this character' )

# Y(Height) of ascii-art
z = 12
for x in range(z):
	print("-" * (z-x) + "*" * x + " " * x + "-" * (z-x))
# ...............

answer = input('Are you ready to play? (Yes/No or Enter) : ').lower().strip()
first_selection = "Do you want to be a Hero? (Yes/No or Enter) : "
not_Ahero = "\nYou have selected not to be a hero\n____\nYour characters profile:"
Ahero = "\nYou have selected to be a hero\n____\nYour characters profile:"
error = 'ERROR'
yesAnswers = {'yes', 'y', 'sure!', 'yea', 'yeah', 'ye', 'si', ''}
noAnswers = {'no', 'n', 'nope', 'nah', 'not'}

if answer in yesAnswers:
    answer = input(first_selection).lower().strip()
    if answer in yesAnswers:
        print(Ahero)
        print(characters.characters_data(B_Cider))
    if answer in noAnswers:
        print(not_Ahero)
        print(characters.characters_data(L_Cido))
else:
    print(error)
