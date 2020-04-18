import time
import pandas as pd
import numpy as np



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    #get user inouts for city, month and day
    print('Hello! Let\'s explore some US bikeshare data!')
    #city input
    while True :
        city = input("Please select a city filter - New York City, Chicago, Washington  ").lower()
        if city not in("new york city","chicago","washington") :
            print("Invalid Input!")
            continue
        else :
            break
    #mont input
    while True :
        month = input("Do you have a month filter? \n If no, enter all. \n If yes, enter January,February,March,April,May,June,July,August,September,October,November,December \n ").lower()
        if month not in("january","february","march","april","may","june","july","august","september","october","november","december","all") :
            print("Invalid Input!")
            continue
        else :
            break
    #day inout
    while True :
        day = input("Do you have a day filter? \n If no, enter all. \n If yes, enter monday,tuesday,wednesday,thursday,friday,saturday,sunday \n ").lower()
        if day not in("sunday","monday","tuesday","wednesday","thursday","friday","saturday","all") :
            print("Invalid Input!")
            continue
        else :
            break
    print('-'*40)
    return city, month, day


def load_data(city, month, day) :
    #load data and appluy the relevant filters
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # display the most common month
    com_mth = df['month'].mode()[0]
    print('common month is ',com_mth)

    # display the most common day of week
    com_day = df['day_of_week'].mode()[0]
    print('common day is ',com_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    com_hr =df['hour'].mode()[0]
    print('common hour is ',com_hr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    com_start = df['Start Station'].mode()[0]
    print('Most Commonly used start station:', com_start)

    # display most commonly used end station
    com_end = df['End Station'].mode()[0]
    print('Most Commonly used end station:', com_end)

    # display most frequent combination of start station and end station trip
    frequent = df.groupby(['Start Station','End Station'])
    combo_station = frequent['Trip Duration'].count().idxmax()
    print('Most Commonly used combonation :\n', combo_station)
    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time:', total_travel_time/86400, " Days")


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:',mean_travel_time, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = df['User Type'].value_counts()
    print ("User Types : ", user_types)

    # Display counts of gender
    if 'Gender' in df.columns :
        gender_types = df['Gender'].value_counts()
        print('Gender Types:\n', gender_types)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns :
        earliest = df['Birth Year'].min()
        print('\nEarliest Year:',earliest)

        recent = df['Birth Year'].max()
        print('\nMost Recent Year:',recent)

        common_year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year:', common_year)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def print_data(df):
    #display raw data
    start = 0
    end = 5
    input_data = 'yes'
    while input_data == 'yes' :
        print(df[start : end])
        start = start + 5
        end = end + 5
        input_data = input("Do you want to continue? Enter yes or no. \n")
        if input_data != 'yes':
            break
        else :
            continue


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data = input("would you like to see raw data of the table ?Enter yes or no.\n")
        if raw_data == 'yes' :
            print_data(df)
        restart = input('\nWould you like to analyzse again? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

#first refactoring change
#second refactoring change
if __name__ == "__main__":
	main()
