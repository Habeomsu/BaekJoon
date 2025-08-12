def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = remove2(new_id)
    new_id = remove3(new_id)
    new_id = remove4(new_id)
    new_id = remove5(new_id)
    new_id = remove6(new_id)
    new_id = remove7(new_id)
    answer = new_id
    return answer


def remove2(string):
    new_string = ""
    for i in range(len(string)):
        if string[i].isalpha():
            new_string += string[i]
        elif string[i].isdigit():
            new_string += string[i]
        elif string[i] in ['-', '_', '.']:
            new_string += string[i]
    return new_string


def remove3(string):
    new_string = string
    while True:
        if ".." in new_string:
            new_string = new_string.replace("..", ".")
        else:
            break
    return new_string


def remove4(string):
    if string and string[0] == '.':
        new_string = string[1:]
    else:
        new_string = string

    if new_string and new_string[-1] == '.':
        new_string = new_string[:-1]

    return new_string


def remove5(string):
    if string == "":
        return "a"
    return string


def remove6(string):
    new_string = string
    if len(string) >= 16:
        new_string = new_string[:15]
    if new_string[-1] == '.':
        new_string = new_string[:-1]
    return new_string


def remove7(string):
    new_string = string
    while len(new_string) < 3:
        new_string = new_string + new_string[-1]
    return new_string


'''





'''