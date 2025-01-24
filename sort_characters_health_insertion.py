__author__ = "Yusuf Abouelwafa"

#==========================================#
def  sort_characters_health_insertion(characters_list: list[dict], order: str) -> list[dict]:
    """ Return the list character_list with the dictionaires inside sorted based on the Health key dpending on the 
    the order that the user chooses, "A" for ascending and "D" for ascending. Return the original list if Health key is not present.
    
    Preconditions = character_list is a list of dictionaries 

    >>> sort_characters_health_insertion([{'Occupation': 'EB', 'Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}], "A") 
    [{'Occupation': 'EB', 'Health': 62.37}, {'Occupation': 'H', 'Health': 62.71}]

    >>> sort_characters_health_insertion([{'Occupation':'EB'}, {'Occupation': 'M'}], "A")
    Health key is not present
    [{'Occupation': 'EB'}, {'Occupation': 'M'}]

    >>> sort_characters_health_insertion([{"Occupation": "AT", "Health": 42.3}, {"Occupation": "AT", "Health": 89}, {"Occupation": "AT", "Health": 50}], 'D')
    [{'Occupation': 'AT', 'Health': 89}, {'Occupation': 'AT', 'Health': 50}, {'Occupation': 'AT', 'Health': 42.3}]
    """
    if len(characters_list) > 0 and "Health" in characters_list[0]:
        for i in range(1, len(characters_list)):
            #Sets up keys
            dict_health_key = characters_list[i]
            index_key = i - 1

            #Checks wanted order 
            if order.lower() == "a":
                #Checks if key is less than the values before it untill it reaches a greater value 
                while dict_health_key["Health"] < (characters_list[index_key])["Health"] and index_key >= 0:
                    #Moves the values in the list over one 
                    characters_list[index_key + 1] = characters_list[index_key]
                    index_key -= 1
                #Places the key in it's correct spot 
                characters_list[index_key + 1] = dict_health_key
            elif order.lower() == "d":
                #Checks if key is more than the values before it untill it reaches a lesser value 
                while dict_health_key["Health"] > (characters_list[index_key])["Health"] and index_key >= 0:
                    #Moves the values in the list over one 
                    characters_list[index_key + 1] = characters_list[index_key]
                    index_key -= 1
                #Places the key in it's correct spot 
                characters_list[index_key + 1] = dict_health_key
    else:
        print("Health key is not present")
    
    return characters_list
