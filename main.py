import numpy as np

def random_predict(number:int=1) -> int:


    count =0
    num_list=[]
    a=1
    b=101
    while True:
        count += 1
        predict_number = np.random.randint(a, b)
        num_list.append(predict_number)
        if number == predict_number:
            break

        if number > predict_number:
            count += 1
            predict_number_m = np.random.randint(predict_number, 101)
            num_list.append(predict_number_m)
            a=predict_number_m
            if number == predict_number_m:
                break

        if number < predict_number:
            count += 1
            predict_number_l = np.random.randint(1, predict_number)
            num_list.append(predict_number_l)
            b=predict_number_l
            if number == predict_number_l:

                break

    #print(num_list)
    print(f'Варианты подбора: {num_list}')
    return(count)

print(f'Количество попыток: {random_predict()},')

