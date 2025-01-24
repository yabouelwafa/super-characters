__author__ = "Yusuf Abouelwafa"

#==========================================#
def character_luck_list(file_name: str, luck_vaue: float) -> list[dict]:
    """Return a list of characters from the specified file "file_name", with less luck than the specified luck value "luck_value".

    Preconditions: First line of file must be the attribute names.

    >>> character_luck_list('characters-mat.csv', 0.1)
        []
    >>> character_luck_list('characters-mat.csv', 0.2)
        [{'Occupation': 'VF', 'Strength': '12', 'Agility': '4', 'Stamina': '2', 
        'Personality': '14', 'Intelligence': '14', 'Armor': '9', 'Weapon': 'Dagger'}]
    >>> character_luck_list('characters-mat.csv', 0.3)
        [{'Occupation': 'AT', 'Strength': '14', 'Agility': '5', 'Stamina': '6', 
        'Personality': '13', 'Intelligence': '9', 'Armor': '9', 'Weapon': 'Staff'}, 
        {'Occupation': 'DB', 'Strength': '9', 'Agility': '7', 'Stamina': '7', 
        'Personality': '11', 'Intelligence': '5', 'Armor': '10', 'Weapon': 'Staff'}, 
        {'Occupation': 'DB', 'Strength': '15', 'Agility': '7', 'Stamina': '6', 
        'Personality': '7', 'Intelligence': '13', 'Armor': '10', 'Weapon': 'Club'},
        {Rest of charcters}]
    
    """
    characters_final = []
    first_line = True
    in_file = open(file_name)

    for line in in_file:     
        line = line.strip().split(",")

        if first_line:
            first_line = False
            attributes = line
        else:
            if float(line[6]) < luck_vaue:
                character = {}
                for i in range(len(attributes)):
                    try:
                        character[attributes[i]] = int(line[i])
                    except:
                        character[attributes[i]] = str(line[i])

                del character[attributes[6]]
                characters_final.append(character)      
            
    in_file.close()
    return characters_final

