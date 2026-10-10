import csv
import json

##############################################################

def save_test_ids(test_ids):
    with open("tests.txt", "w", encoding="utf-8") as file:
        for test_id in test_ids:
            file.write(test_id + "\n")


def add_test_id(test_id):
    with open("tests.txt", "a", encoding="utf-8") as file:
        file.write(test_id + "\n")


def load_test_ids(filename):
    test_ids = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            test_id = line.strip()
            if test_id:
                test_ids.append(test_id)
    return test_ids

save_test_ids(["QA-1001", "QA-1002", "QA-1003"])

add_test_id("QA-1004")

print(load_test_ids("tests.txt"))

####################################################################################

def get_test_statistics(filename):
    total = 0
    passed = 0
    failed = 0
    total_duration_ms = 0
    failed_ids = []

    with open(filename, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += 1
            total_duration_ms += int(row["duration_ms"])

            if row["status"] == "PASSED":
                passed += 1

            if row["status"] == "FAILED":
                failed += 1
                failed_ids.append(row["test_id"])

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "total_duration_ms": total_duration_ms,
        "failed_ids": failed_ids
    }


print(get_test_statistics("results.csv"))

####################################################################################

def save_test_config(environment, base_url, timeout):
    config = {
        "environment": environment,
        "base_url": base_url,
        "timeout": timeout
    }

    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)


def load_test_config(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

save_test_config("staging", "https://example.com", 30)
config = load_test_config("config.json")
print(config["timeout"])