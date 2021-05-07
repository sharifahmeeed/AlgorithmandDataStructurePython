numbers = [10, 20, 30, 40, 50]
numbers[1] = "Adam"

print('Standard')
for num in numbers:
    print(num)

print('\n \nNot standard')
for i in range(len(numbers)):
    print(numbers[i])

print('first 2 items item: ', numbers[0:2])
print('without last one  item: ', numbers[:-1])
print('without last two  item: ', numbers[:-2])
print('for all  item: ', numbers[:])

#for next part
numbers = [10, 20, 30, 40, 50]

#linear search
#O(N) search running time
#linear time complexity

maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print(maximum)
