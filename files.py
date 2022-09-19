# with open('shopping-list.txt') as f:
#     for index, data in enumerate(f):
#         print(f'{index + 1}. {data.strip()}')

shows = [
    'The Witcher',
    'The X-Files',
    'Star Trek: Strange New Worlds',
    'The Mandalorian'
]

with open('tv-shows.txt', 'a') as f:
    f.write('\nMonty Python\'s Flying Circus')

