import re


def email_parse(email_address):
    EMAIL_CHECK = re.compile(r'\w+@\w+\.\w+')
    if not re.match(EMAIL_CHECK, email_address):
        return 'Email is not correct'
    username = re.findall(r'\w*[^@]', email_address)
    domain = re.findall(r'@\w*\.\w*', email_address)
    result = (username[0], domain[0])
    return result


print(email_parse('students@mail.ru'))
