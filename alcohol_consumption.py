import csv
import matplotlib.pylab as plt


def alcohol_consumption():
    with open('resources/young-people-survey/responses.csv') as csv_file:
        read_csv = csv.reader(csv_file, delimiter=',')
        headers = []
        headers_read = False
        heavy_drinkers = []
        social_drinkers = []
        non_drinkers = []

        for row in read_csv:
            if not headers_read:
                headers = row
                headers_read = True
                continue

            try:
                if row[headers.index("Alcohol")] == "drink a lot":
                    heavy_drinkers.append(int(row[headers.index("Age")]))
                if row[headers.index("Alcohol")] == "social drinker":
                    social_drinkers.append(int(row[headers.index("Age")]))
                if row[headers.index("Alcohol")] == "never":
                    non_drinkers.append(int(row[headers.index("Age")]))

            except ValueError:
                pass

        plt.subplot(131)
        plt.xlabel("Age")
        plt.title("Non drinkers")
        plt.ylim(0, 150)
        plt.hist(non_drinkers, 40, range=(15,30))

        plt.subplot(132)
        plt.xlabel("Age")
        plt.title("Social drinkers")
        plt.ylim(0, 150)
        plt.hist(social_drinkers, 40, range=(15,30))

        plt.subplot(133)
        plt.xlabel("Age")
        plt.title("Heavy drinkers")
        plt.ylim(0, 150)
        plt.hist(heavy_drinkers, 40, range=(15,30))

        plt.suptitle("Alcohol consumption by age and amount")

        plt.show()


alcohol_consumption()
