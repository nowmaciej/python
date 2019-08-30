# class Reference for handling user dictionary, checking for type errors, repeats, adding value and calculating result
# it takes empty dictionary as init, not empty dictionary is cleaned on init to avoid wrong answers

class Reference:
    def __init__(self):
        self.references = {}
        
    def add(self,name_value_pair):
        name, value = name_value_pair
# check for repeated reference key or value

        if name in self.references:
            print('Name {} already exists!'.format(name))
        elif value in self.references.values():
            print('Value {} already exists!'.format(value))

# check if given value is number        
        
        elif not str(value).isdigit():
            print('Value must be number, {} was given!'.format(type(value)))

# if OK then add new name/value to dictionary (changing value to integer)

        else:
            self.references[name] = int(value)

        return self.references
            
    def parse_units(self, to_parse):
        self.references = dict(sorted(self.references.items(), key=lambda x: x[1], reverse=True))
        if not str(to_parse).isdigit():
            print('I can only parse numbers, please type in an integer')
        else:
            to_parse = int(to_parse)
            result = ''
            for i in self.references:
                if to_parse >= self.references[i]:
                    result += str(int(to_parse/self.references[i])) + ' ' + i + ' '
                    to_parse = to_parse%self.references[i]
            result += '({} rest)'.format(to_parse)
        return result
    

references = Reference()

# --------------------------------------------- get reference units to parse ---------------------------------------------

print('Input units as reference in form of [str]NAME,[int]VALUE. Empty input = END. [Example: Banana,32]:\n')

i=1    

while True:
    try:
        in_data = input('Input reference no {}: '.format(i))
            
        if in_data == '':
            break
            
        in_data=in_data.split(',')
        references.add(in_data)
        i+=1

    except:
        print('\nERROR: Keep input format: [str],[int] or empty for END\n')
    
# -----------------------------------------------------------------------------------------------------------

# --------------------------------------------- get number to parse ---------------------------------------------

while True:
    in_toparse = input("Input number to parse: ")
    if in_toparse.isdigit():
        print('\nNumber {} parsed is: {}\n'.format(in_toparse,references.parse_units(in_toparse)))
        break

# --------------------------------------------------------------------------------------------------------------