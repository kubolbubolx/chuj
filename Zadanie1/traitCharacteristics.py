import pandas as pd
from functions import arithmeticMean, standardDeviation, median, quartile, roundToSpecifiedPlace


def traitCharacteristics(list):
    ddk = []
    sdk = []
    dp = []
    sp = []

    for line in list:
        ddk.append(line[0])
        sdk.append(line[1])
        dp.append(line[2])
        sp.append(line[3])

    ddk.sort()
    sdk.sort()
    dp.sort()
    sp.sort()

    min_ddk = roundToSpecifiedPlace(min(ddk), 2)
    min_sdk = roundToSpecifiedPlace(min(sdk), 2)
    min_dp = roundToSpecifiedPlace(min(dp), 2)
    min_sp = roundToSpecifiedPlace(min(sp), 2)

    max_ddk = roundToSpecifiedPlace(max(ddk), 2)
    max_sdk = roundToSpecifiedPlace(max(sdk), 2)
    max_dp = roundToSpecifiedPlace(max(dp), 2)
    max_sp = roundToSpecifiedPlace(max(sp), 2)


    data_frame = pd.DataFrame(
        {
            'Cecha': ['Długość działki kielicha (cm)', 'Szerokość działki kielicha (cm)', 'Długość płatka (cm)', 'Szerokość płatka (cm)'],
            'Minimum': [min_ddk, min_sdk, min_dp, min_sp],
            'Śr. arytm. (± odch. stand.)': [f'{arithmeticMean(ddk)} (±{standardDeviation(ddk)})',
                                            f'{arithmeticMean(sdk)} (±{standardDeviation(sdk)})',
                                            f'{arithmeticMean(dp)} (±{standardDeviation(dp)})',
                                            f'{arithmeticMean(sp)} (±{standardDeviation(sp)})'],
            'Mediana (Q1 - Q3)': [f'{median(ddk)} ({quartile(ddk, 0.25)} - {quartile(ddk, 0.75)})',
                                  f'{median(sdk)} ({quartile(sdk, 0.25)} - {quartile(sdk, 0.75)})',
                                  f'{median(dp)} ({quartile(dp, 0.25)} - {quartile(dp, 0.75)})',
                                  f'{median(sp)} ({quartile(sp, 0.25)} - {quartile(sp, 0.75)})'],
            'Maximum': [max_ddk, max_sdk, max_dp, max_sp],
        }
    )
    return data_frame.to_string(index=False)