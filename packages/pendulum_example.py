# https://pendulum.eustace.io/docs/
import pendulum
import pandas as pd

# common functions
print(f'Now: {pendulum.now()}')
print(f'Yesterday: {pendulum.yesterday()}')
print(f'Today: {pendulum.today()}')
print(f'Tomorrow: {pendulum.tomorrow()}')

# get local time of given time zone
moscow_time = pendulum.now(tz='Europe/Moscow')
warsaw_time = pendulum.now(tz='Europe/Warsaw')
tokyo_time = pendulum.now(tz='Asia/Tokyo')
toronto_time = pendulum.now('America/Toronto')

# Pendulum enforces timezone aware datetimes, and using them is the preferred and recommended way of using the library.
print(pendulum.naive(2024, 2, 5).timezone)

print('BEFORE PANDAS', moscow_time, 'AFTER PANDAS', pd.Timestamp(moscow_time))

# parsing date
print(pendulum.parse(pendulum.now(tz='Asia/Tokyo')))
