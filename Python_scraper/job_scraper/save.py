import csv

def save_to_csv(jobs):
    with open("jobs.csv", mode='w', encoding="UTF-8", newline='') as file:
        # 위 newline 옵션 미적용 시 아래 csv파일에 빈 줄이 생김
        # 위 encoding 옵션 미적용 시 오류 발생(UnicodeEncodeError: 'cp949' codec can't encode character '\xe3' in position 46: illegal multibyte sequence)
        write = csv.writer(file)
        write.writerow(jobs[0].keys())
        for job in jobs:
            write.writerow(list(job.values()))