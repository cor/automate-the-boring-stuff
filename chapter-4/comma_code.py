def comma_code(list):
    if not list:
        return ''
    elif len(list) == 1:
        return list[0]
    elif len(list) == 2:
        return f'{list[0]} and {list[1]}'
    else:
        return ', '.join(list[:-1]) + f', and {list[-1]}'


print(comma_code(['Apples']))
print(comma_code(['Apples', 'Bananas']))
print(comma_code(['Apples', 'Bananas', 'Carrots']))