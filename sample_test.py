import csv
import matplotlib.pylab as plt
import random
import math


def sample_test():
    with open('resources/young-people-survey/responses.csv') as csv_file:
        read_csv = csv.reader(csv_file, delimiter=',')
        headers = []
        headers_read = False
        
        heavy_drinkers = 0
        total = 0
        all_drinkers = []

        for row in read_csv:
            if not headers_read:
                headers = row
                headers_read = True
                continue

            try:
                how_much = row[headers.index("Alcohol")]
                if how_much == "drink a lot":
                    heavy_drinkers = heavy_drinkers + 1
                all_drinkers.append(how_much)
                total = total + 1

            except ValueError:
                pass

        heavy_drinkers_percentage = ( heavy_drinkers / total ) * 100

        print(str(heavy_drinkers_percentage) + "% of responders declared themselves as heavy drinkers")

        sample_size = 100
        sample = random.sample(all_drinkers, sample_size)

        heavy_drinkers_sample = 0

        for how_much in sample:
            if how_much == 'drink a lot':
                heavy_drinkers_sample = heavy_drinkers_sample + 1

        heavy_drinkers_sample_percentage = ( heavy_drinkers_sample / sample_size ) * 100

        print(str(heavy_drinkers_sample_percentage) + "% of responders from the sample ("+str(sample_size)+" random responders) declared themselves as heavy drinkers")

        standard_error = math.sqrt( heavy_drinkers_sample_percentage * (100 - heavy_drinkers_sample_percentage)/sample_size)

        print("Standard error: " + str(standard_error) + "%")

        a = heavy_drinkers_sample_percentage - 2 * standard_error
        b = heavy_drinkers_sample_percentage + 2 * standard_error

        c = heavy_drinkers_sample_percentage - standard_error
        d = heavy_drinkers_sample_percentage + standard_error

        print("We can be 95% sure that between " + str(a) + " and " + str(b) + " of the total population are heavy drinkers.")
        print("We can be 68% sure that between " + str(c) + " and " + str(d) + " of the total population are heavy drinkers.")


sample_test()