import numberOfSpecies
import traitCharacteristics
import histograms
import dotPlot_linearRegresionLine

def convertData(file):
    data = open(file, 'r')
    list = []
    for line in data:
        line = line.strip()
        line = line.split(",")
        data_converted = [float(value) for value in line[:-1]] + [int(line[-1])]
        list.append(data_converted)
    data.close()
    return list


def main():
    list = convertData("data/data1.csv")

    print(numberOfSpecies.numberOfSpecies(list))
    print(traitCharacteristics.traitCharacteristics(list))
    histograms.hists(list)
    histograms.boxplots(list)
    dotPlot_linearRegresionLine.scatterPlots(list)

if __name__ == '__main__':
    main()