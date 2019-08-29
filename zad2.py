def get_units():

    units = {}

    print('Input units as reference in form of [str]NAME,[int]VALUE. Empty input = END. [Example: Banana,32]:\n')
    
    i = 1
    while True:
        try:
            in_data = input('Input reference no {}: '.format(i))
            
            if in_data == '':
                break
            
            in_data=in_data.split(',')
            
            if in_data[1].isdigit():
                units[in_data[0]] = int(in_data[1])     
                i+=1
        except:
            print('\nERROR: Keep input format: [str],[int] or empty for END\n')
    
    units = sorted(units.items(), key=lambda x: x[1], reverse=True)
        
    return dict(units)

def parse_units(units, to_parse):
    result = ''
    for i in units:
        if to_parse > units[i]:
            result += str(int(to_parse/units[i])) + ' ' + i + ' '
            to_parse = to_parse%units[i]
    result += '({} rest)'.format(to_parse)
    return result

while True:
    in_toparse = input("Input number to parse: ")
    if in_toparse.isdigit():
        to_parse = int(in_toparse)
        break

print('\nNumber {} parsed is: {}\n'.format(to_parse,parse_units(get_units(),to_parse)))

