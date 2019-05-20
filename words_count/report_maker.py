import json
import csv

class ReportMaker:
    def __init__(self):
        pass

    def makeReport(self, data):
        raise NotImplementedError

class ScreenReportMaker(ReportMaker):
    def __init__(self):
        super().__init__()

    def makeReport(self, data):
        headers = data["headers"]
        body = data["body"]
        max_len_keys = max(len(x) for x in body.keys())
        if len(headers[0]) > max_len_keys:
            max_len_keys = len(headers[0])
        max_len_counts = max(len(str(x)) for x in body.values())
        if len(headers[1]) > max_len_counts:
            max_len_counts = len(headers[1])
        maxlen = max_len_counts + max_len_keys + 2
        print(headers[0] + " " * (maxlen - len(headers[0]) - len(headers[1])) + headers[1])
        for key, val in body.items():
            print(key + " " * (maxlen - len(key) - len(str(val))) + str(val))

class JsonReportMaker(ReportMaker):
    def __init__(self, out_file):
        super().__init__()
        self.out_file = out_file

    def makeReport(self, data):
        with open(self.out_file, "w", encoding="UTF-8") as fp:
            json.dump(data, fp)

class CsvReportMaker(ReportMaker):
    def __init__(self, out_file, delimeter=";"):
        super().__init__()
        self.out_file = out_file
        self.delimeter = delimeter

    def makeReport(self, data):
        headers = data["headers"]
        body = data["body"]
        with open(self.out_file, "w", encoding="UTF-8", newline="") as fp:
            writer = csv.writer(fp, delimiter=self.delimeter)
            writer.writerow([headers[0], headers[1]])
            for key, val in body.items():
                writer.writerow([key, val])
