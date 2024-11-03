import pandas as pd

def numberOfSpecies(list):
    setosa = 0
    versicolor = 0
    virginica = 0
    sum = 0
    for i in list:
        sum += 1
        if int(i[4]) == 0:
            setosa += 1
        elif int(i[4]) == 1:
            versicolor += 1
        else:
            virginica += 1

    data_frame = pd.DataFrame(
        {
            'Gatunek': ['Setosa', 'Versicolor', 'Virginica', 'Suma'],
            'Liczebność': [
                f'{setosa} ({round(setosa / sum * 100, 1)}%)',
                f'{versicolor} ({round(versicolor / sum * 100, 1)}%)',
                f'{virginica} ({round(virginica / sum * 100, 1)}%)',
                f'{sum} ({round(sum / sum * 100, 1)}%)'
            ]
        }
    )
    return data_frame.to_string(index=False)