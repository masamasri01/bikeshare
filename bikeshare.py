import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def print_section(title):
    print(f"\n{'='*10} {title} {'='*10}\n")

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city
        (str) month
        (str) day
    """
    cities = ['chicago', 'new york city', 'washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

    while True:
        city = input("Enter a city (Chicago, New York City, Washington): ").strip().lower()
        if city in cities:
            break
        print("Invalid input. Please choose a valid city.")

    while True:
        month = input("Enter a month (January to June) or 'all': ").strip().lower()
        if month in months:
            break
        print("Invalid input. Please choose a valid month or 'all'.")

    while True:
        day = input("Enter a day of the week or 'all': ").strip().lower()
        if day in days:
            break
        print("Invalid input. Please choose a valid day or 'all'.")

    print('-'*40)
    return city, month, day

def add_time_columns(df):
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour
    return df

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df = add_time_columns(df)

    if month != 'all':
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    print_section("Most Frequent Times of Travel")
    start_time = time.time()

    print("Most Frequent Month:", df['month'].mode()[0].title())
    print("Most Frequent Day:", df['day_of_week'].mode()[0].title())
    print("Most Frequent Hour:", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    print_section("Most Popular Stations and Trip")
    start_time = time.time()

    print("Most Popular Start Station:", df['Start Station'].mode()[0])
    print("Most Popular End Station:", df['End Station'].mode()[0])
    df['Trip Combination'] = df['Start Station'] + " to " + df['End Station']
    print("Most Popular Trip:", df['Trip Combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    print_section("Trip Duration")
    start_time = time.time()

    print("Total Travel Time:", df['Trip Duration'].sum(), "seconds")
    print("Average Travel Time:", df['Trip Duration'].mean(), "seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    print_section("Statistics On Bikeshare Users")
    start_time = time.time()

    print("User Type Counts:")
    print(df['User Type'].value_counts())

    if 'Gender' in df.columns:
        print("\nGender Counts:")
        print(df['Gender'].value_counts())

    if 'Birth Year' in df.columns:
        print("\nEarliest Birth Year:", int(df['Birth Year'].min()))
        print("Most Recent Birth Year:", int(df['Birth Year'].max()))
        print("Most Common Birth Year:", int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df, rows=5):
    i = 0
    while True:
        raw = input(f"\nWould you like to see {rows} rows of raw data? Enter yes or no: ").lower()
        if raw != 'yes':
            break
        print(df.iloc[i:i+rows])
        i += rows
        if i >= len(df):
            print("\nNo more data to display.")
            break

def main_menu():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        if input('\nDo you want to restart? Enter yes or no: ').lower() != 'yes':
            break

if __name__ == "__main__":
    main_menu()
