import time


print('Laptop fans aan...')
time.sleep(1)
print('Beginnen met aftellen...')

for tel in range(30):
    print(f'{30-tel}.. ', end='')
    time.sleep(1)

print('\nLaptop lanceren...')
