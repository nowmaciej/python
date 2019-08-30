# class Reference for handling user dictionary, checking for type errors, repeats, adding value and calculating result
# it takes empty dictionary as init, not empty dictionary is cleaned on init to avoid wrong answers

class Reference:
    def __init__(self,references):
        references = {} # in case not empty dictionary was given
        self.references = references
        
    def add(self,name,value):
        
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
        
        return dict(sorted(self.references.items(), key=lambda x: x[1], reverse=True))
            
    def parse_units(self, to_parse):
        if not str(to_parse).isdigit():
            print('I can only parse numbers, please type in an integer')
        else:            
            result = ''
            for i in self.references:
                if to_parse >= self.references[i]:
                    result += str(int(to_parse/self.references[i])) + ' ' + i + ' '
                    to_parse = to_parse%self.references[i]
                    print(to_parse)
            result += '({} rest)'.format(to_parse)
        return result
        
references = {}
x = Reference(references)
x.add('ala',5)
x.add('miska',2)
x.add('asd',9)

print(x.parse_units(7))