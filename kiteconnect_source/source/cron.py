# from django_cron import CronJobBase, Schedule
# import datetime

# class MyCronJob(CronJobBase):
#     ALLOW_PARALLEL_RUNS = False
#     RUN_EVERY_MINS = 1

#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     code = 'kiteconnect_source.my_cron_job'    # a unique code

#     def do(self):
#         # time = datetime.datetime.now()
#         val = "This is cron job function new testing:"
#         f = open('/Users/hp/Desktop/ETech/set up folder/wetransfer-f37bf3/KiteConnect_API_19oct_backup/kiteconnect_source/dummy.txt','a')
#         f.write(val)
#         f.close()
#         print("demo")

from crontab import CronTab

# cron = CronTab(user='hp')
# command = "python E:/example.py"
#cron = CronTab(tab="*/2 * * * * ")
file_cron = CronTab(tabfile='E:/abc.tab')
print("yo update in e drive file")
# job = cron.new(command='python E:/example.py')

# cron.minute.every(1)
file_cron.write()
