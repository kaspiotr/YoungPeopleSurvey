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

        heavy_drinkers_by_age = dict()
        total_by_age = dict()
        percentage_of_heavy_drinkers = []

<<<<<<< HEAD
        for i in range (15,31):
=======
        for i in range(15, 31):
>>>>>>> 5809d9d00f0bab3f4fac2c44a55a88dfa97b99e0
            heavy_drinkers_by_age[i] = 0
            total_by_age[i] = 0

        for row in read_csv:
            if not headers_read:
                headers = row
                headers_read = True
                continue

            try:
                age = int(row[headers.index("Age")])
                how_much = row[headers.index("Alcohol")]
                if how_much == "drink a lot":
                    heavy_drinkers.append(age)
                    heavy_drinkers_by_age[age] = heavy_drinkers_by_age[age] + 1
                if how_much == "social drinker":
                    social_drinkers.append(age)
                if how_much == "never":
                    non_drinkers.append(age)
                total_by_age[age] = total_by_age[age] + 1

            except ValueError:
                pass

<<<<<<< HEAD
        for i in range (15,31):
            percentage_of_heavy_drinkers.append(( heavy_drinkers_by_age[i] / total_by_age[i] ) * 100)
=======
        for i in range(15, 31):
            percentage_of_heavy_drinkers.append((heavy_drinkers_by_age[i] / total_by_age[i]) * 100)
>>>>>>> 5809d9d00f0bab3f4fac2c44a55a88dfa97b99e0

        plt.subplot(231)
        plt.xlabel("Age")
        plt.title("Non drinkers")
        plt.ylim(0, 150)
<<<<<<< HEAD
        plt.hist(non_drinkers, 40, range=(15,30))
=======
        plt.hist(non_drinkers, 40, range=(15, 30))
>>>>>>> 5809d9d00f0bab3f4fac2c44a55a88dfa97b99e0

        plt.subplot(232)
        plt.title("Social drinkers")
        plt.ylim(0, 150)
<<<<<<< HEAD
        plt.hist(social_drinkers, 40, range=(15,30))
=======
        plt.hist(social_drinkers, 40, range=(15, 30))
>>>>>>> 5809d9d00f0bab3f4fac2c44a55a88dfa97b99e0

        plt.subplot(233)
        plt.xlabel("Age")
        plt.title("Heavy drinkers")
        plt.ylim(0, 150)
<<<<<<< HEAD
        plt.hist(heavy_drinkers, 40, range=(15,30))
=======
        plt.hist(heavy_drinkers, 40, range=(15, 30))
>>>>>>> 5809d9d00f0bab3f4fac2c44a55a88dfa97b99e0

        plt.subplot(235)
        plt.xlabel("Age")
        plt.title("Percentage of heavy drinkers")
<<<<<<< HEAD
        ages = range(15,31)
=======
        ages = range(15, 31)
>>>>>>> 5809d9d00f0bab3f4fac2c44a55a88dfa97b99e0
        plt.bar(ages, percentage_of_heavy_drinkers)

        plt.suptitle("Alcohol consumption by age and amount")

        print(percentage_of_heavy_drinkers)
<<<<<<< HEAD
        plt.show()

        

=======
        plt.rcParams['figure.figsize'] = [30, 15]
        plt.show()

>>>>>>> 5809d9d00f0bab3f4fac2c44a55a88dfa97b99e0

alcohol_consumption()
