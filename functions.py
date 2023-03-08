FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Opens the tod file and returns the list
    """
    with open(filepath, 'r') as file2:
        todos2 = file2.readlines()
    return todos2


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == '__main__':
    print('not in main')
