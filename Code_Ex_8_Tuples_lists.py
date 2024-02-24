connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]

number = 0
total = 0
    
for city in connections:
    if city[1] == 'Rome':
        number += 1
        total += city[2]

print(number, 'connections lead to Rome with an average flight time of', total/number, 'minutes')
