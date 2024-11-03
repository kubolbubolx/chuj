import matplotlib.pyplot as plt
from functions import PearsonsLinearCorrelation, linearRegressionEquation, roundToSpecifiedPlace


def scatterPlotGen(list_x, list_y, xlabel, ylabel):

    r = roundToSpecifiedPlace(PearsonsLinearCorrelation(list_x, list_y), 2)
    a, b = linearRegressionEquation(list_x, list_y)

    A = roundToSpecifiedPlace(a, 1)
    B = roundToSpecifiedPlace(b, 1)

    plt.scatter(list_x, list_y, color='blue')

    regression_line = [a * x + b for x in list_x]
    plt.plot(list_x, regression_line, color='red')

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(f'r = {r}; y = {A}x + {B}')

    plt.show()

def scatterPlots(list):
    ddk = []
    sdk = []
    dp = []
    sp = []

    for line in list:
        ddk.append(line[0])
        sdk.append(line[1])
        dp.append(line[2])
        sp.append(line[3])

    scatterPlotGen(ddk, sdk, 'Długość działki kielicha (cm)', 'Szerokość działki kielicha (cm)')
    scatterPlotGen(dp, ddk, 'Długość płatka (cm)', 'Długość działki kielicha (cm)')
    scatterPlotGen(sp, ddk, 'Szerokość płatka (cm)', 'Długość działki kielicha (cm)')
    scatterPlotGen(dp, sdk, 'Długość płatka (cm)', 'Szerokość działki kielicha (cm)')
    scatterPlotGen(sp, sdk, 'Szerokość płatka (cm)', 'Szerokość działki kielicha (cm)')
    scatterPlotGen(sp, dp, 'Szerokość płatka (cm)', 'Długość płatka (cm)')
