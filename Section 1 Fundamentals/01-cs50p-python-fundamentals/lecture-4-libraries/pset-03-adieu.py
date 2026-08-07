"""
In The Sound of Music, there’s a song sung largely in English, So Long, Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:

Adieu, adieu, to yieu and yieu and yieu

Of course, the line isn’t grammatically correct, since it would typically be written (with an Oxford comma) as:

Adieu, adieu, to yieu, yieu, and yieu

To be fair, “yieu” isn’t even a word; it just rhymes with “you”!

In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. 
Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, 
three names with two commas and one and, and 𝑛 names with 𝑛 −1 commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
"""

import inflect

p = inflect.engine()


def main():
    names = get_name()
    result = adieu(names)
    print()
    print(result)

def get_name():
    name_list = []
    while True:
        try:
            user_input = input("Name: ")
            name_list.append(user_input)
        except EOFError:
            return name_list
            
                
# From a list of names we return the result we need 
def adieu(name_list):
    start = "Adieu, adieu, to "
    result = p.join(name_list)
    return start + result

# print(adieu(name_list))

main()

