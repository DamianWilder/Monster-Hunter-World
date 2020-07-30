monster_elements =('Fire','Water','Thunder','Ice','Dragon','Poison','Sleep','Paralysis','Blast','Stun','None')

ele = monster_elements

monsters = {
    'GREAT JAGRAS' : {
        'print_name' : "Great Jagras",
        'immunities' : [1,],
        'resistances' : [4,],
        'normal damage' : [2, 3,],
        'weaknesses' : [0, 4, 5, 6, 7, 8, 9,],
    },
    'PUKEI PUKEI' : {
        'print_name' : "Pukei Pukei",
        'immunities' : [1,],
        'resistances' : [5, 4,],
        'normal damage' : [0, 3, 8, 9,],
        'weaknesses' : [2, 6, 7,],
    },
    'KULU YA KU' : {
        'print_name' : "Kulu Ya Ku",
        'immunities' : [10],
        'resistances' : [10],
        'normal damage' : [0, 2, 3, 4, 5, 6, 7, 8, 9,],
        'weaknesses' : [1],
    },
    'TOBI KADACHI' : {
        'print_name' : "Tobi Kadachi",
        'immunities' : [2,],
        'resistances' : [4,],
        'normal damage' : [0, 3, 6, 7, 8, 9,],
        'weaknesses' : [1, 5,],
    },
    'ANJANATH' : {
        'print_name' : "Anjanath",
        'immunities' : [0,],
        'resistances' : [4, 9,],
        'normal damage' : [2, 3, 5, 6, 7, 9,],
        'weaknesses' : [1,],
    },
    'RATHIAN' : {
        'print_name' : "Rathian",
        'immunities' : [0],
        'resistances' : [1, 3, 5, 8,],
        'normal damage' : [2, 6, 7,],
        'weaknesses' : [4, 9,],
    },
    'BARROTH' : {
        'print_name' : "Barroth",
        'immunities' : [2, 0, 1,],
        'resistances' : [4, 9,],
        'normal damage' : [3, 6,],
        'weaknesses' : [0, 1, 5, 7, 8,],
    },
    'JYURATODUS' : {
        'print_name' : "Jyuratodus",
        'immunities' : [0, 1, 2,],
        'resistances' : [0, 3, 4, 6, 8],
        'normal damage' : [5, 7,],
        'weaknesses' : [1, 2, 9,],    
    },
    'TZITZI-YA-KU' : {
        'print_name' : "Tzitzi-Ya-Ku",
        'immunities' : [10],
        'resistances' : [10],
        'normal damage' : [0, 1, 4, 5, 6, 7, 8, 9],
        'weaknesses' : [2, 3,],
    },
    'PAOLUMU' : {
        'print_name' : "Paolumu",
        'immunities' : [1],
        'resistances' : [3, 4,],
        'normal damage' : [2, 5, 6, 7,],
        'weaknesses' : [0, 8, 9,],
    },
    'GREAT GIRROS' : {
        'print_name' : "Great Jirros",
        'immunities' : [2],
        'resistances' : [4, 7,],
        'normal damage' : [0, 3, 5, 8, 9,],
        'weaknesses' : [1, 6,],
    },
    'RADOBAAN' : {
        'print_name' : "Radobaan",
        'immunities' : [10],
        'resistances' : [0, 1, 2, 6,],
        'normal damage' : [3, 5, 7, 9,],
        'weaknesses' : [4, 8,],
    },
    'LEGIANA' : {
        'print_name' : "Legiana",
        'immunities' : [3,],
        'resistances' : [1, 4,],
        'normal damage' : [0, 6, 7, 8, 9,],
        'weaknesses' : [2, 5,],
    },
    'ODOGARON' : {
        'print_name' : "Odogaron",
        'immunities' : [4,],
        'resistances' : [0, 1, 5],
        'normal damage' : [2, 6, 8, 9,],
        'weaknesses' : [3, 7,]
    },
    'RATHALOS' : {
        'print_name' : "Rathalos",
        'immunities' : [0],
        'resistances' : [1, 3, 5, 8,],
        'normal damage' : [2, 6, 7, 9,],
        'weaknesses' : [4,],
    },
    'DIABLOS' : {
        'print_name' : "Diablos",
        'immunities' : [0,],
        'resistances' : [2, 9,],
        'normal damage' : [1, 4, 5, 6, 8,],
        'weaknesses' : [3, 7,],
    },
    'KIRIN' : {
        'print_name' : "Kirin",
        'immunities' : [2, 7,],
        'resistances' : [4, 5, 9,],
        'normal damage' : [1, 3, 6, 8,],
        'weaknesses' : [0,],
    },
    'ZORAH MAGDAROS' : {
        'print_name' : "Zorah Magdaros",
        'immunities' : [0, 5, 6, 7, 8, 9,],
        'resistances' : [2,],
        'normal damage' : [3,],
        'weaknesses' : [1, 4,],
    },
    'DODOGAMA' : {
        'print_name' : "Dodogama",
        'immunities' : [0,],
        'resistances' : [4, 8,],
        'normal damage' : [1, 3, 6, 7, 9,],
        'weaknesses' : [2, 5,],
    },
    'PINK RATHIAN' : {
        'print_name' : "Pink Rathian",
        'immunities' : [0,],
        'resistances' : [1, 3, 5, 8,],
        'normal damage' : [2, 6, 7,],
        'weaknesses' : [4, 9,],
    },
    'BAZELGEUSE' : {
        'print_name' : "Bazelgeuse",
        'immunities' : [0,],
        'resistances' : [1, 8, 9,],
        'normal damage' : [3, 4, 5, 6, 7,],
        'weaknesses' : [2,],
    },
    'LAVASIOTH' : {
        'print_name' : "Lavasioth",
        'immunities' : [0, 2, 3,],
        'resistances' : [0, 4, 6, 8,],
        'normal damage' : [1, 2, 3, 7, 9,],
        'weaknesses' : [1, 6,],
    },
    'URAGAAN' : {
        'print_name' : "Uragaan",
        'immunities' : [0,],
        'resistances' : [2, 6,],
        'normal damage' : [3, 4, 7, 8,],
        'weaknesses' : [1, 5,],
    },
    'AZURE RATHALOS' : {
        'print_name' : "Azure Rathalos",
        'immunities' : [0,],
        'resistances' : [1, 2, 5, 8,],
        'normal damage' : [3, 6, 7, 9,],
        'weaknesses' : [4,],
    },
    'BLACK DIABLOS' : {
        'print_name' : "Black Diablos",
        'immunities' : [0, 4,],
        'resistances' : [2, 9,],
        'normal damage' : [1, 5, 6, 8,],
        'weaknesses' : [3, 7,],
    },
    'NERGIGANTE' : {
        'print_name' : "Nergigante",
        'immunities' : [10,],
        'resistances' : [0, 1, 3,],
        'normal damage' : [4, 5, 6, 7, 8, 9,],
        'weaknesses' : [2,],
    },
    'TEOSTRA' : {
        'print_name' : "Teostra",
        'immunities' : [0,],
        'resistances' : [2, 4, 6, 7, 8,],
        'normal damage' : [5, 9,],
        'weaknesses' : [1, 3,],
    },
    "KUSHALA DAORA" : {
        'print_name' : "Kushala Daora",
        'immunities' : [1, 3,],
        'resistances' : [0, 6, 7,],
        'normal damage' : [4, 9,],
        'weaknesses' : [2, 5, 8,],
    },
    'VAAL HAZAK' : {
        'print_name' : "Vaal Hazak",
        'immunities' : [1,],
        'resistances' : [2, 5, 6, 7,],
        'normal damage' : [3, 8, 9,],
        'weaknesses' : [0, 4,],
    },
    'XENO\'JIIVA' : {
        'print_name' : "Xeno'Jiiva",
        'immunities' : [6,],
        'resistances' : [7, 9,],
        'normal damage' : [0, 1, 2, 3, 4,],
        'weaknesses' : [5,],
    },       
}

class Monster:
    def __init__(self, name, immunities, resistances, normal_damage, weaknesses):
        self.name = name
        self.immunities = immunities
        self.resistances = resistances
        self.normal_damage = normal_damage
        self.weaknesses = weaknesses


    def monster_format(self, ele_int):
        """Takes the integer from the monster dict and returns the element associated with it
        """
        x = list(map(lambda n: ele[n] , ele_int ))
        return ", ".join(x)
        

    def monster_print(self):
        """Creates a class of Monster with the properties outlined in the dict and prints all the information out
        """
        self.monster_format(self.immunities)
        self.monster_format(self.resistances)
        self.monster_format(self.normal_damage)
        self.monster_format(self.weaknesses)
        print('\n' + underline("Name:") + '\n   ' + self.name + '\n\n' + underline("Immunities:") + '\n   ' + self.monster_format(self.immunities)
             + '\n\n' + underline("Resistances:") + '\n   ' + self.monster_format(self.resistances) + '\n\n' + underline("Normal Damage:") + '\n   ' 
             + self.monster_format(self.normal_damage) + '\n\n' + underline("Weaknesses:") + '\n   ' 
             + self.monster_format(self.weaknesses) +'\n\n')


def monster_maker(monster_name):  #should this be a static?
    """Takes the user input of monster_name and assigns the ints based off the monster dict
    """
    x = monsters[monster_name]
    return Monster(x['print_name'],x['immunities'],x['resistances'],x['normal damage'],x['weaknesses'])


def underline(text):
    """adds a row of underscores under the argument for readability
    """
    return '\n' + text + '\n' + ("=" * len(text))


def show_instructions():
    """Prints main menu options
    """
    print("""
Welcome to the MHW Monster Guide
Type the monster name to display the monster's stats.
Type 'HELP' to view this menu.
Type 'DONE' to close the program. 
""")


show_instructions()

while True:
    monster_name = input('Monster Name?\n').upper()
    if monster_name == 'DONE':
        break
    elif monster_name == 'HELP':
        show_instructions()
        continue
    monster_maker(monster_name).monster_print()
