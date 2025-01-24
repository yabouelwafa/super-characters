import check
import load_data

__author__ = "Yusuf Abouelwafa"

def test_return_correct_dict_inside_list():
    test_file = "characters-test.csv"
    
    #test that character_occupation_list returns a correct dictionary inside the list (3 different test cases required)
    occupation_case1 = load_data.character_occupation_list(test_file, "AT")
    occupation_case2 = load_data.character_occupation_list(test_file, "H")
    occupation_case3 = load_data.character_occupation_list(test_file, "SDF")

    check.equal([occupation_case1[0], occupation_case1[-1]], [{'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'}, 
                                        {'Strength': 19, 'Agility': 9, 'Stamina': 9, 'Personality': 10, 'Intelligence': 12, 'Luck': 0.39, 'Armor': 10, 'Weapon': 'Dagger'}])
    check.equal([occupation_case2[0], occupation_case2[-1]], [{'Strength': 19, 'Agility': 11, 'Stamina': 8, 'Personality': 6, 'Intelligence': 12, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Shortbow'}, 
                                        {'Strength': 14, 'Agility': 11, 'Stamina': 13, 'Personality': 12, 'Intelligence': 8, 'Luck': 0.72, 'Armor': 11, 'Weapon': 'Longsword'}])
    check.equal(occupation_case3, [])

    #test that character_strength_list returns a correct dictionary inside the list  (3 different test cases required)
    strength_case1 = load_data.character_strength_list(test_file, (0, 20))
    strength_case2 = load_data.character_strength_list(test_file, (19, 19))
    strength_case3 = load_data.character_strength_list(test_file, (15, 3))

    check.equal([strength_case1[0], strength_case1[-1]], [{'Occupation': 'AT', 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'},
                                                          {'Occupation': 'WA', 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'}])
    check.equal([strength_case2[0], strength_case2[-1]], [{'Occupation': 'AT', 'Agility': 9, 'Stamina': 9, 'Personality': 10, 'Intelligence': 12, 'Luck': 0.39, 'Armor': 10, 'Weapon': 'Dagger'}, 
                                                          {'Occupation': 'H', 'Agility': 11, 'Stamina': 8, 'Personality': 6, 'Intelligence': 12, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Shortbow'}])
    check.equal(strength_case3, [])
    
    #test that character_luck_list returns a correct dictionary inside the list  (3 different test cases required)
    luck_case1 = load_data.character_luck_list(test_file, 1)
    luck_case2 = load_data.character_luck_list(test_file, 0.55)
    luck_case3 = load_data.character_luck_list(test_file, 0)

    check.equal([luck_case1[0], luck_case1[-1]], [{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Armor': 10, 'Weapon': 'Staff'},
                                                  {'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Armor': 11, 'Weapon': 'Spear'}])
    check.equal([luck_case2[0], luck_case2[-1]], [{'Occupation': 'AT', 'Strength': 13, 'Agility': 10, 'Stamina': 5, 'Personality': 11, 'Intelligence': 7, 'Armor': 10, 'Weapon': 'Club'},
                                                  {'Occupation': 'WA', 'Strength': 16, 'Agility': 10, 'Stamina': 6, 'Personality': 9, 'Intelligence': 9, 'Armor': 10, 'Weapon': 'Club'}])
    check.equal(luck_case3, [])
    
    #test that character_weapon_list returns a correct dictionary inside the list (3 different test cases required)
    weapon_case1 = load_data.character_weapon_list(test_file, 'Spear')
    weapon_case2 = load_data.character_weapon_list(test_file, '')
    weapon_case3 = load_data.character_weapon_list(test_file, 'dfgfd')
    
    check.equal([weapon_case1[0], weapon_case1[-1]], [{'Occupation': 'VF', 'Strength': 14, 'Agility': 6, 'Stamina': 4, 'Personality': 12, 'Intelligence': 14, 'Luck': 0.56, 'Armor': 9},
                                                      {'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11}])
    check.equal(weapon_case2, [])
    check.equal(weapon_case3, [])
    
    #test that load_data returns a correct dictionary inside the list (6 different test cases required)
    load_case1 = load_data.load_data(test_file, ('Occupation', 'H'))
    load_case2 = load_data.load_data(test_file, ('Strength', (13, 15)))
    load_case3 = load_data.load_data(test_file, ('Luck', 0.54))
    load_case4 = load_data.load_data(test_file, ('Weapon', 'Sling'))
    load_case5 = load_data.load_data(test_file, ('All', 0.5))
    load_case6 = load_data.load_data(test_file, ('Agility', 10))
    
    check.equal([load_case1[0], load_case1[-1]], [{'Strength': 19, 'Agility': 11, 'Stamina': 8, 'Personality': 6, 'Intelligence': 12, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Shortbow'},
                                                  {'Strength': 14, 'Agility': 11, 'Stamina': 13, 'Personality': 12, 'Intelligence': 8, 'Luck': 0.72, 'Armor': 11, 'Weapon': 'Longsword'}])
    check.equal([load_case2[0], load_case2[-1]], [{'Occupation': 'AT', 'Agility': 10, 'Stamina': 5, 'Personality': 11, 'Intelligence': 7, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Club'}, 
                                                  {'Occupation': 'WA', 'Agility': 12, 'Stamina': 7, 'Personality': 13, 'Intelligence': 7, 'Luck': 0.67, 'Armor': 11, 'Weapon': 'Dagger'}])
    check.equal([load_case3[0], load_case3[-1]], [{'Occupation': 'AT', 'Strength': 13, 'Agility': 10, 'Stamina': 5, 'Personality': 11, 'Intelligence': 7, 'Armor': 10, 'Weapon': 'Club'},
                                                  {'Occupation': 'WA', 'Strength': 16, 'Agility': 10, 'Stamina': 6, 'Personality': 9, 'Intelligence': 9, 'Armor': 10, 'Weapon': 'Club'}])
    check.equal([load_case4[0], load_case4[-1]], [{'Occupation': 'EB', 'Strength': 13, 'Agility': 8, 'Stamina': 8, 'Personality': 14, 'Intelligence': 15, 'Luck': 0.83, 'Armor': 10},
                                                  {'Occupation': 'HG', 'Strength': 12, 'Agility': 7, 'Stamina': 12, 'Personality': 10, 'Intelligence': 7, 'Luck': 0.83, 'Armor': 10}])
    check.equal([load_case5[0], load_case5[-1]], [{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'},
                                                  {'Occupation': 'WA', 'Strength': 8, 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'}])
    check.equal(load_case6, [])

    #test that calculate_health returns a correct dictionary inside the list  (3 different test cases required)
    health_case1 = load_data.calculate_health([{'Occupation': 'HG', 'Strength': 17, 'Agility': 9, 'Stamina': 8, 'Personality': 14, 'Intelligence': 9, 'Luck': 0.5, 'Armor': 10, 'Weapon': 'Club'}])
    health_case2 = load_data.calculate_health([{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'},
                                               {'Occupation': 'EB', 'Strength': 13, 'Agility': 13, 'Stamina': 12, 'Personality': 8, 'Intelligence': 9, 'Luck': 0.67, 'Armor': 11, 'Weapon': 'Dart'}])
    health_case3 = load_data.calculate_health([{'Occupation': 'HG', 'Strength': 12, 'Agility': 7, 'Stamina': 12, 'Personality': 10, 'Intelligence': 7, 'Luck': 0.83, 'Armor': 10, 'Weapon': 'Sling'}, 
                                               {'Occupation': 'M', 'Strength': 17, 'Agility': 9, 'Stamina': 11, 'Personality': 5, 'Intelligence': 7, 'Luck': 0.61, 'Armor': 10, 'Weapon': 'Longsword'}, 
                                               {'Occupation': 'WA', 'Strength': 16, 'Agility': 10, 'Stamina': 6, 'Personality': 9, 'Intelligence': 9, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Club'}])
    
    check.equal(health_case1, [{'Occupation': 'HG', 'Strength': 17, 'Agility': 9, 'Stamina': 8, 'Personality': 14, 'Intelligence': 9, 'Luck': 0.5, 'Armor': 10, 'Weapon': 'Club', 'Health': 107.0}])
    check.equal(health_case2, [{'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff', 'Health': 115.0}, 
                               {'Occupation': 'EB', 'Strength': 13, 'Agility': 13, 'Stamina': 12, 'Personality': 8, 'Intelligence': 9, 'Luck': 0.67, 'Armor': 11, 'Weapon': 'Dart', 'Health': 136.07}])
    check.equal(health_case3, [{'Occupation': 'HG', 'Strength': 12, 'Agility': 7, 'Stamina': 12, 'Personality': 10, 'Intelligence': 7, 'Luck': 0.83, 'Armor': 10, 'Weapon': 'Sling', 'Health': 131.0}, 
                               {'Occupation': 'M', 'Strength': 17, 'Agility': 9, 'Stamina': 11, 'Personality': 5, 'Intelligence': 7, 'Luck': 0.61, 'Armor': 10, 'Weapon': 'Longsword', 'Health': 110.0}, 
                               {'Occupation': 'WA', 'Strength': 16, 'Agility': 10, 'Stamina': 6, 'Personality': 9, 'Intelligence': 9, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Club', 'Health': 94.0}])
    
    
    check.summary()

print(test_return_correct_dict_inside_list())
