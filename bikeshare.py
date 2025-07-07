import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
   
    cities = ['chicago', 'new york city', 'washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

    while True:
        city = input("Which city would you like to explore? (Chicago, New York City, Washington): ").lower()
        if city in cities:
            break
        else:
            print("Invalid input. Please choose from: Chicago, New York City, or Washington.")

    while True:
        month = input("Which month? (January to June or enter all): ").lower()
        if month in months:
            break
        else:
            print("Invalid input. Please enter a valid month or enter all.")

    while True:
        day = input("Which day? (Monday to Sunday or enter all): ").lower()
        if day in days:
            break
        else:
            print("Invalid input. Please enter a valid day or all.")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\n Most Frequent Times of Travel\n')
    start_time = time.time()

    print("Most Frequent Month:", df['month'].mode()[0].title())
    print("Most Frequent Day:", df['day_of_week'].mode()[0].title())
    print("Most Frequent Hour:", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\n Most Popular Stations and Trip\n')
    start_time = time.time()

    print("Most Popular Start Station:", df['Start Station'].mode()[0])
    print("Most Popular End Station:", df['End Station'].mode()[0])
    df['Trip Combination'] = df['Start Station'] + " to " + df['End Station']
    print("Most Popular Trip:", df['Trip Combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nTrip Duration: \n')
    start_time = time.time()

    print("Total Travel Time:", df['Trip Duration'].sum(), "seconds")
    print("Average Travel Time:", df['Trip Duration'].mean(), "seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\Statistics On Bikeshare Users:\n')
    start_time = time.time()

    print("User Type Counts:")
    print(df['User Type'].value_counts())

    if 'Gender' in df.columns:
        print("\nGender Counts:")
        print(df['Gender'].value_counts())

    if 'Birth Year' in df.columns:
        print("\n Earliest Birth Year:", int(df['Birth Year'].min()))
        print("Most Recent Birth Year:", int(df['Birth Year'].max()))
        print("Most Common Birth Year:", int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data 5 rows at a time upon user request."""
    i = 0
    while True:
        raw = input("\n Do you want to see 5 lines of raw data? Enter yes or no. \n").lower()
        if raw != 'yes':
            break
        print(df.iloc[i:i+5])
        i += 5
        if i >= len(df):
            print("\nNo more data to show.")
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nDo you want to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
