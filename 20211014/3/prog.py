line = input()
width = len(line)
height = 1
liquid_count = 0
gas_count = 0
while (line := input()) != ('#'*width):
    height += 1
    for symbol in line:
        if symbol == '.':
            gas_count += 1
        elif symbol == '~':
            liquid_count += 1
height += 1  # нижнюю грань ящика не посчитали            
# округление в большую сторону без дополнительных импортов         
liquid_lines = round(liquid_count / (height - 2))
if liquid_lines * (height - 2) < liquid_count:
    liquid_lines += 1    
gas_lines = width - 2 - liquid_lines


print('#' * height)
for i in range(gas_lines):
    print('#' + '.' * (height - 2) + '#')
for i in range(liquid_lines):
    print('#' + '~' * (height - 2) + '#')
print('#' * height)

# статичтика выводится по изначальным данным
max_len = max(gas_count, liquid_count)
print('{:<21}'.format('.'* round(20*gas_count/max_len)), gas_count, '/', gas_count + liquid_count, sep='')
print('{:<21}'.format('~'* round(20*liquid_count/max_len)), liquid_count, '/', gas_count + liquid_count, sep='')
