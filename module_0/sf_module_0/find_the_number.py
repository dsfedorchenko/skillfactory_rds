def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = np.random.randint(1,100)
    while number != predict:
        count+=1
        if number > 50:
            
            if number > 75:
                predict = np.random.randint(76,100)
                count+=1
                if number > predict: 
                    predict += 1
                elif number < predict: 
                    predict -= 1
            else:
                predict = np.random.randint(51,75)
                count+=1
                if number > predict: 
                    predict += 1
                elif number < predict: 
                    predict -= 1
        else:
            if number > 25:
                predict = np.random.randint(26,50)
                count+=1
                if number > predict: 
                    predict += 1
                elif number < predict: 
                    predict -= 1
            else:
                predict = np.random.randint(1,25)
                count+=1
                if number > predict: 
                    predict += 1
                elif number < predict: 
                    predict -= 1
    return(count) # выход из цикла, если угадали

# Проверяем: Ваш алгоритм угадывает число в среднем за 19 попыток
score_game(game_core_v2)