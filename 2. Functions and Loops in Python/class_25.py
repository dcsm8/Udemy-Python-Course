

cars = ['ok', 'ok', 'ok', 'ok', 'faulty', 'ok', 'ok']

for car_status in cars:
    if car_status == 'faulty':
        print('Stopping the production line!')
        break
    print(f'This car is {car_status}.')

for num in range(2, 10):
    if num % 2 == 0:
        print(f'Found an even number, {num}')
        continue
    print(f'Found a number, {num}')

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f'{n} equals {x} * {n//x}')
            break
    else:
        print(f'{n} is a prime number')
