import sys
from words_count.words_count_core import WordsCount
from words_count.repository_worker import Repository, RepositoryException
from words_count.report_maker import ReportMaker, CsvReportMaker, JsonReportMaker, ScreenReportMaker

def parse_args(args):
    outs = []
    if "-json" in args:
        outs.append("-json")
    if "-csv" in args:
        outs.append("-csv")
    if (len(outs) > 1):
        return ["Параметры {0} не могут использоваться вместе.".format(", ".join(outs))]

    repo_url = ""
    local_path = "/tmp/tmp_repo"
    pos = "noun"
    name_type = "functions"
    language = "python"
    out_type = "screen"
    out_file = ""

    i = 1
    while i < len(args):
        if args[i] == "-repo":
            if i < len(args) - 1:
                i += 1
                repo_url = args[i]
            else:
                return ["Пропущен параметр: путь к репозиторию."]
            continue

        if args[i] == "-local":
            if i < len(args) - 1:
                i += 1
                local_path = args[i]
            else:
                return ["Пропущен параметр: локальный путь для клонирования репозитория."]
            continue

        if args[i] == "-pos":
            if i < len(args) - 1:
                i += 1
                pos = args[i]
            else:
                return ["Пропущен параметр: часть речи."]
            continue

        if args[i] == "-nametype":
            if i < len(args) - 1:
                i += 1
                name_type = args[i]
            else:
                return ["Пропущен параметр: часть речи."]
            continue

        if args[i] == "-json":
            if i < len(args) - 1:
                i += 1
                out_file = args[i]
                out_type = "json"
            else:
                return ["Пропущен параметр: путь к формируемому файлу JSON."]
            continue

        if args[i] == "-csv":
            if i < len(args) - 1:
                i += 1
                out_file = args[i]
                out_type = "csv"
            else:
                return ["Пропущен параметр: путь к формируемому файлу CSV."]
            continue

        i += 1

    if repo_url == "":
        return ["Не задан путь к репозиторию."]

    return [repo_url, local_path, pos, name_type, language, out_type, out_file]

def main():
    args = parse_args(sys.argv)
    if len(args) == 1:
        print("Ошибка: " + args[0])
        return 1

    repo_url, local_path, pos, name_type, language, out_type, out_file = args

    try:
        Repository.clone(repo_url, local_path)
    except RepositoryException as e:
        print("Ошибка: " + str(e))
        return 1

    wc = WordsCount(pos, name_type, language)
    stats = wc.get_stats(local_path)

    if out_type == "json":
        report_maker = JsonReportMaker(out_file)
    elif out_type == "csv":
        report_maker = CsvReportMaker(out_file)
    else:
        report_maker = ScreenReportMaker()

    report_maker.makeReport(stats)

    return 0
