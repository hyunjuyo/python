import csv


def save_brands(list_total, brands):
    brands["company"] = brands["company"].replace("/", "_")
    with open(f"./csv_files/{brands['company']}.csv", mode='w', encoding="UTF-8", newline="") as file:
        write = csv.writer(file)
        write.writerow(list_total[0].keys())
        for list_a in list_total:
            write.writerow(list_a.values())
