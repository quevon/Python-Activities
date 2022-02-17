#Quevon M. Galang
import re
print("---------------------------------------------------")
noun1 = input("Noun1: ")
noun2 = input("Noun2: ")
adj1 = input("Adjective1: ")
adj2 = input("Adjective2: ")

print("<--------------------Original--------------------->")
poem = """Candy,
Candy,
Candy,
Gummi candy,
Pop rock candy,
Ring pop tootsie roll skittles candy,
Razzles gum fun dip candy,
Sour patch candy,
Twix candy,
Pixy stix tootsie roll snickers candy,
Spree nerds starburst candy,
Milky way candy,
Mint candy,
Hot Tamale candy,
Don’t forget mike and ike candy,
Last of all best of all I like Kit Kat candy.
"""
print(poem)
print("<----------------------New----------------------->")

replaces = {"candy": noun1.upper(),"Candy": noun1.upper(), "rock": noun2.upper(), "Sour": adj1.upper(), "Mint": adj2.upper()}

regex = re.sub("|".join(replaces.keys()), lambda match: replaces[match.string[match.start():match.end()]], poem)

print(regex)