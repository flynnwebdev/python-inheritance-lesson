# from calculator import square

nums = [10, 14, 21, 50, 5, -6]

# def square(x):
#     return x * x

squared = map(lambda x: x * x, nums)
# squared = [square(x) for x in nums if x < 20]

# for num in nums:
#     squared.append(square(num))

print(list(squared))

def add_prefix(index, value):
    # index, value = tuple
    return f'{index + 1}. {value.strip()}'

with open('shopping-list.txt') as f:
    # items = list(enumerate(f))
    # numbered = map(add_prefix, items)
    numbered = [add_prefix(index, value) for index, value in enumerate(f) if index % 2 == 0]

print(list(numbered))


students = [
    {'name': 'Hermione', 'house': 'Gryffindor'},
    {'name': 'Ron', 'house': 'Gryffindor'},
    {'name': 'Harry', 'house': 'Gryffindor'},
    {'name': 'Draco', 'house': 'Slytherin'}
]

# print([student['name'] for student in students if student['house'] == 'Gryffindor'])

# def is_gryffindor(student):
#     return student['house'] == 'Gryffindor'

print(list(filter(lambda student: student['house'] == 'Gryffindor', students)))

