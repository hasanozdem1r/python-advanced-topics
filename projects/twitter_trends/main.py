"""
Cron job is created to instantiate class automatically daily once
@Hasan Özdemir 2021
"""

# create cron job
from crontab import CronTab

if '__main__' == __name__:
    print('Process Started')
    cron_obj=CronTab()
    # create a new cron
    job=cron_obj.new(command='python twitter_trends.py')
    # run job daily
    job.day.every(1)
    cron_obj.write('cron_jobs.txt')
    print('Process Stopped')
