import csv


def read_lines_from_csv(limit=999):
    result = []
    with open("/Users/otus/PycharmProjects/feb24_api_testing/users.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            result.append(row)
            if len(result) == limit:
                break
    return result


print(read_lines_from_csv())
