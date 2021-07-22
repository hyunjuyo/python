import csv


def save_jobs(word, jobs):
    with open(f"jobs_{word}.csv", mode='w') as file:
        write = csv.writer(file)
        write.writerow(jobs[0].keys())
        for job in jobs:
            write.writerow(job.values())
