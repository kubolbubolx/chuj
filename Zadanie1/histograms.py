import matplotlib.pyplot as plt

def histGen(histType, list, bins, title, xlabel, ylabel):
    plt.hist(list, bins, alpha=0.7, color='blue', edgecolor='black', histtype=histType)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.show()

def boxplotGen(list, labels, title, xlabel, ylabel):
    plt.boxplot(list, labels=labels)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.show()

def hists(list):
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

    histGen('bar', ddk, [4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0], 'Długość działki kielicha', 'Długość (cm)', 'Liczebność')
    histGen('bar', sdk, [2.0,2.5,3.0,3.5,4.0,4.5], 'Szerokość działki kielicha', 'Szerokość (cm)', 'Liczebność')
    histGen('bar', dp, [1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0], 'Długość płatka', 'Długość (cm)', 'Liczebność')
    histGen('bar', sp, [0.0,0.5,1.0,1.5,2.0,2.5], 'Szerokość płatka', 'Szerokość (cm)', 'Liczebność')

def boxplots(list):
    setosa_ddk = []
    setosa_sdk = []
    setosa_dp = []
    setosa_sp = []
    versicolor_ddk = []
    versicolor_sdk = []
    versicolor_dp = []
    versicolor_sp = []
    virginica_ddk = []
    virginica_sdk = []
    virginica_dp = []
    virginica_sp = []

    for line in list:
        if line[4] == 0:
            setosa_ddk.append(line[0])
            setosa_sdk.append(line[1])
            setosa_dp.append(line[2])
            setosa_sp.append(line[3])
        elif line[4] == 1:
            versicolor_ddk.append(line[0])
            versicolor_sdk.append(line[1])
            versicolor_dp.append(line[2])
            versicolor_sp.append(line[3])
        else:
            virginica_ddk.append(line[0])
            virginica_sdk.append(line[1])
            virginica_dp.append(line[2])
            virginica_sp.append(line[3])

    boxplotGen([setosa_ddk, versicolor_ddk, virginica_ddk], ['setosa', 'versicolor', 'virginica'], 'Długość działki kielicha', 'Gatunek', 'Długość (cm)')
    boxplotGen([setosa_sdk, versicolor_sdk, virginica_sdk], ['setosa', 'versicolor', 'virginica'], 'Szerokość działki kielicha', 'Gatunek', 'Szerokość (cm)')
    boxplotGen([setosa_dp, versicolor_dp, virginica_dp], ['setosa', 'versicolor', 'virginica'], 'Długość płatka', 'Gatunek', 'Długość (cm)')
    boxplotGen([setosa_sp, versicolor_sp, virginica_sp], ['setosa', 'versicolor', 'virginica'], 'Szerokość płatka', 'Gatunek', 'Szerokość (cm)')