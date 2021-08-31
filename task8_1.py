import re

EMAIL = re.compile(r'([a-z0-9]+)@([a-z0-9]+\.[a-z]+)')
def email_parse(email):
    dict_1 = {}
    info  = EMAIL.findall(email)[0]
    if info:
        name, addres = info
    else:
        raise ValueError(f'wrong email: {email}')
    dict_1[name] = addres
    return dict_1
print(email_parse('alexandr@mail.ru'))
print(email_parse('alexandr@mailru'))
print(email_parse('alex@mail.ru'))