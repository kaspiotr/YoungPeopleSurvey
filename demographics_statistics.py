import csv
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from utils.math_functions import median, mean, stddev

response_no = []
responders_ages = []


def read_age_from_csv():
    with open('resources/young-people-survey/responses.csv') as csv_file:
        read_csv = csv.reader(csv_file, delimiter=',')
        headers = []
        headers_read = False
        response_idx = 0
        for row in read_csv:
            if not headers_read:
                headers = row
                headers_read = True
                continue
            response_no.append(response_idx)
            try:
                responders_ages.append(int(row[headers.index("Age")]))
            except ValueError:
                pass  # or whatever
            response_idx += 1


def show_responders_age_box_plot(data):
    data_median = median(data)
    sub_data_Q1 = list(filter(lambda x: x < data_median, data))
    sub_data_Q3 = list(filter(lambda x: x > data_median, data))
    Q1 = median(sub_data_Q1)
    Q3 = median(sub_data_Q3)
    IQR = Q3 - Q1
    flier_low = max(min(data), Q1 - 1.5 * IQR)
    flier_high = max(min(data), Q3 + 1.5 * IQR)
    fig, ax = plt.subplots()
    ax.boxplot(data, showfliers=True)
    plt.hlines(y=[flier_high, mean(data), Q1, Q3, data_median, flier_low], xmin=0, xmax=1, colors='k',
               linestyles='dashed')
    plt.yticks([flier_high, Q1, Q3, mean(data), data_median, flier_low])
    plt.ylabel("age")
    plt.show()


def show_responders_age_histogram(data, bin_count=40):
    plt.title("Responders age histogram")
    plt.xlabel("age")
    plt.ylabel("number of responders at specified age")
    plt.hist(data, bins=bin_count, range=(15, 30))
    plt.show()


def display_missing_values(df):
    nulls = df.isnull().sum().sort_values(ascending=False)
    nulls.plot(kind='bar', figsize=(23, 5))
    plt.show()


def display_missing_values_info(df):
    print('Number of girls who omitted weight field: {:.0f}'.format(
        df[df['Gender'] == 'female']['Weight'].isnull().sum()))
    print('Number of boys who omitted weight field: {:.0f}'.format(
        df[df['Gender'] == 'male']['Weight'].isnull().sum()))
    print('Number of girls who omitted height field: {:.0f}'.format(
        df[df['Gender'] == 'female']['Height'].isnull().sum()))
    print('Number of boys who omitted height field: {:.0f}'.format(
        df[df['Gender'] == 'male']['Height'].isnull().sum()))


def display_missing_values_further_info(df):
    omitted = df[(df['Weight'].isnull()) | df['Height'].isnull()]
    print('Number of people with omitted weight or height: {:.0f}'.format(omitted.shape[0]))
    nas = omitted.drop(['Weight', 'Height', 'Number of siblings', 'Age'], 1).isnull().sum().sum()
    print('Number of fields that were omitted by people who did not fill Weight or Height: {:.0f}'.format(nas))


def drop_rows_without_values_and_display_village_vs_city_stats(column_name, df):
    interesting_var = column_name
    mapping = {interesting_var: {'city': 0, 'village': 1}}
    df.dropna(subset=[interesting_var], inplace=True)
    # to have ability to use hue parameter in seaborn for better comparison
    df["all"] = ""
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))
    sns.countplot(y=interesting_var, data=df, ax=ax[0])
    sns.countplot(y=interesting_var, hue='Gender', data=df, ax=ax[1])
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.show()


def main():
    read_age_from_csv()
    df = pd.read_csv('resources/young-people-survey/responses.csv')
    df.head(2)
    df.describe()
    print("Average responder age is %f" % mean(responders_ages))
    print("Median of responders age is %d" % median(responders_ages))
    print("Standard deviation of responders age is %f" % stddev(responders_ages))
    show_responders_age_box_plot(responders_ages)
    show_responders_age_histogram(responders_ages)
    display_missing_values(df)
    display_missing_values_info(df)
    display_missing_values_further_info(df)
    drop_rows_without_values_and_display_village_vs_city_stats('Village - town', df)


if __name__ == '__main__':
    main()
