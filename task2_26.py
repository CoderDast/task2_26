def odd_and_even(numbers):
    ''' Считает количество четных и нечетных чисел в списке'''
    odd = 0 
    even = 0
    for number in numbers:
        try:               # если введен не integer, пропускает элемент списка
            if int(number) % 2 == 0 or int(number)% -2 == 0:
                even += 1
            else:
                odd += 1
        except ValueError:
            pass
    return even, odd


numbers_list = input('Type numbers divided by space\n').split(' ')

even_numbers, odd_numbers = odd_and_even(numbers_list)
print (f'There are {even_numbers} even numbers and {odd_numbers} odd numbers')