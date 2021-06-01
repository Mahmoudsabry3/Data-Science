import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june','all']
week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    global city 
    city= input('please choose the city : chicago or new york city or washington ? ').lower()
    while city not in CITY_DATA.keys():
        city= input('please type a valid name (chicago or new york city or washington) ').lower()

        
    
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month  = input('which month ? january, february, march , april , may , june or all ? ').lower()
    while month not in months:
        month =  input('please type a valid month (january, february, march , april , may , june or all) ').lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day  = input('which day in the week ? monday tuesday wednesday thursday friday saturday sunday or all ?').lower()
    while day not in week:
        day =  input('please type a valid day (sunday ,monday,..., or all) ').lower()
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df
def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']

    common_month_num = df['month'].mode()[0]
    common_month_str = months[common_month_num-1]
    print(common_month_str)
    
     # TO DO: display the most common day of week
    
    print(' the most common day of week ', df['day_of_week'].value_counts().idxmax())


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('the most start hour ', df['hour'].mode()[0])



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    start_station = df['Start Station'].value_counts().idxmax()
    print('the most common used start station: ',start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('the most common used end station: ',end_station)


    # TO DO: display most frequent combination of start station and end station trip
    #start =  df['Start Station'].value_counts()
    #end =  df['Start Station'].value_counts()

    print('the most common combination of start station and end station trip: ',end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
 #   """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('the total travel time  = '+str(total_time/(60*60))+ ' Hour\n')

    # TO DO: display mean travel time
    average_time = df['Trip Duration'].mean()
    print('the average_time  = '+str(average_time/(60*60))+ ' Hour\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    if city == 'washington':
        print(' no user stats for washington city ')
    else :
        
        """Displays statistics on bikeshare users."""

        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # TO DO: Display counts of user types

        users = df['User Type'].value_counts()
        print('the counts of users :\n\n',users)
        # TO DO: Display counts of gender
        print('\n')
        gender = df['Gender'].value_counts()
        print('the counts of gender :\n\n',gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        print('\n')
        birth_year_min = df['Birth Year'].min()
        print('the earliest year : ',birth_year_min)

        most_recent = df['Birth Year'].max()
        print('the most recent year of birth : ',most_recent)

        most_common = df['Birth Year'].mode()[0]
        print('the most common year of birth : ',most_common)


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
def show_row_data(df):

    answer = input('do you want to see the raw data ? please choose yes or no ').lower()

    if  answer == 'yes':

        no_of_rows = int (input('how many row you want to see? '))
        print(df.iloc[:no_of_rows-1])

    else :
        print("Exiting.....")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_row_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
