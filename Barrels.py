import random
import logging

logging.basicConfig(filename = "lg.log", level = logging.INFO)

while True: # Цикл обработки ввода количества бочонков
    try:
        number = int (input("Введите число больше 1: "))
        if number <= 0:
            print('Неверный ввод.\nПовторите попытку:')
        else:
            logging.info(f'Barrels count:  {number}') # Передача информации о количестве в log
            break
    
    except ValueError:
        print('Неверный ввод.\nПовторите попытку:')

number_list = [i+1 for i in range(number)] # Заполнение списка номеров 

random.shuffle(number_list) # Перемешивание номеров в списке 


for i in range(number): # Цикл вывода номеров по одному
    input('Нажмите Enter для вывода следующего числа: ')
    logging.info("Button pressed") # Передача информации о нажатии на кнопку в log
    print(number_list[i])
    logging.info(f"Number is: {number_list[i]}") # Передача информации о выпавшем числе в log

logging.info("Program finished")