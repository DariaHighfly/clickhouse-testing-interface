import argparse
import re
import traceback
import sys
import csv
import json

parser = argparse.ArgumentParser(description='Create performance test report')
parser.add_argument('--report', default='main', choices=['main', 'all-queries'],
                    help='Which report to build')
args = parser.parse_args()
report_errors = []


def read_commit_info(f):
    KEYS_ARR = ["commit", "merge:", "author:", "date:"]  # stop-words array

    commit_dict = dict()
    lines = f.readlines()

    for i in range(len(lines)):
        commit_info_array = re.split(r'\s+', lines[i])
        commit_info_array = list(filter(lambda x: x != '', commit_info_array))
        if len(commit_info_array) > 0:
            key = commit_info_array[0].lower()
            if key in KEYS_ARR:
                value = ' '.join(commit_info_array[1:])
                commit_dict[key.replace(':', '')] = value
            else:
                key = "info"
                if not (key in commit_dict.keys()):
                    commit_dict[key] = ' '.join(commit_info_array[0:])
                else:
                    commit_dict[key] = commit_dict[key] + "\n" + ' '.join(commit_info_array[0:])
    return commit_dict


def read_tsv_table(n, headers):
    error_arr = []
    try:
        with open(n, encoding='utf-8') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                commit_dict = dict()
                row = lines[i].split("\t")
                for j in range(len(row)):
                    key = headers[j]
                    try:
                        value = float(row[j].replace("\n", ""))
                    except:
                        # Find elem-string list
                        res = re.findall(r'^\[[.,;\s\w]+\]', row[j])
                        if len(res) > 0:
                            # If elem-string is list, make new list
                            real_list = res[0].replace("[", "").replace("]", "").split(",")
                            try:
                                for k in range(len(real_list)):
                                    real_list[k] = float(real_list[k])
                            except:
                                continue
                            value = real_list
                        else:
                            value = row[j].replace("\n", "")
                    commit_dict[key] = value
                error_arr.append(commit_dict)
        return error_arr
    except:
        report_errors.append(
            traceback.format_exception_only(
                *sys.exc_info()[:2])[-1].replace("\n", ""))
        pass
    return error_arr


def read_report_errors():
    # Add the errors reported by various steps of comparison script
    report_errors.extend([l.replace("\n", "").strip() for l in open('report-errors.rep')])
    return report_errors


if args.report == 'main':
    # Create dict for json to send from backend to frontend
    json_as_dict = dict()

    # Read old and new commits
    left_commit_info = open('left-commit.txt')
    right_commit_info = open('right-commit.txt')

    # Save old and new commits' information in json
    json_as_dict["commits"] = {"leftCommit": read_commit_info(left_commit_info),
                               "rightCommit": read_commit_info(right_commit_info)}

    # Save information about changes,unstable queries in json
    headers = ["oldTime", "newTime", "relativeDifference", "quantiles", "testName", "query"]
    json_as_dict["changes"] = read_tsv_table('changed-perf.tsv', headers)
    json_as_dict["unstableQueries"] = read_tsv_table('unstable-queries.tsv', headers)

    # Save errors in json
    headers = ["testName", "error"]
    json_as_dict["runErrors"] = read_tsv_table('run-errors.tsv', headers)

    # Save skipped test in json
    headers = ["testName", "reason"]
    json_as_dict["skipped"] = read_tsv_table('skipped-tests.tsv', headers)

    # Save tests with most unstable queries test in json
    headers = ["testName", "unstable", "changedPerf", "total"]
    json_as_dict["badTests"] = read_tsv_table('bad-tests.tsv', headers)

    # Save test times in json
    headers = ["testName",
               "wallClockTime",
               "clientTime",
               "total",
               "ignoredQueries",
               "longestQuery",
               "avgWallClockTime",
               "shortestQuery"]
    json_as_dict["testTimes"] = read_tsv_table('test-times.tsv', headers)

    # Save slow on client queries in json
    headers = ["clientTime", "serverTime", "ratio", "query"]
    json_as_dict["slowOnClient"] = read_tsv_table('slow-on-client.tsv', headers)

    # Save all queries in json
    headers = ["oldTime", "newTime", "relativeDifference", "timeSpeed", "quantiles", "testName", "query"]
    json_as_dict["allQueries"] = len(read_tsv_table('all-queries.tsv', headers))

    # Generate array for time performance
    # time_performance_arr = []
    time_performance_arr = dict()
    all_queries = read_tsv_table('all-queries.tsv', headers)
    for elem in all_queries:
        # print(elem)
        key = elem['testName']
        diff = round(elem['newTime'] - elem['oldTime'], 4)
        if not (key in time_performance_arr.keys()):
            time_performance_arr[key] = dict()
            time_performance_arr[key]["difference"] = [diff]
            time_performance_arr[key]["newTime"] = [elem["newTime"]]
        else:
            time_performance_arr[key]["difference"].append(diff)
            time_performance_arr[key]["newTime"].append(elem["newTime"])
    json_as_dict["timePerformance"] = time_performance_arr

    # Save errors while forming json in json
    json_as_dict["reportErrors"] = read_report_errors()

    # Convert dict to json
    json_to_send = json.dumps(json_as_dict)

    # Save json into file
    json_file = open('../../clickhouse-testing-interface/static/test_data/commit_3/json_to_send.json', 'w')
    print(json_to_send, file=json_file)
    json_file.close()
