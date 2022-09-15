class RangeError(Exception):
    pass


class InvalidUserError(Exception):
    def __init__(self, name):
        super().__init__(f'{name} is not a valid username')


def get_int():
    val = int(input('Enter an integer: '))
    if not val in range(1, 11):
        raise RangeError(f'{val} is out of range - must be between 1 and 10')

    return val


def get_username():
    valid_users = ['alice', 'toby']
    name = input('Username: ')
    if not name in valid_users:
        raise InvalidUserError(name)

    return name


def main():
    while True:
        try:
            x = get_int()
            print(1 / x)
            break
        except RangeError as err:
            print(err)
        except ValueError:
            print('Input must be an integer')
        except ZeroDivisionError:
            print('Input cannot be zero')


    print(f'You entered {x}')


if __name__ == '__main__':
    main()
