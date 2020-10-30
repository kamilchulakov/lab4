in_file = "Friday.xml"
out_file = "Result.json"
tags = ["day", "lesson", "lesson-format", "place", "room", "address", "studies", "subject", "lecturer", "time", "hour",
        "week"]


def ignore():
    ...


def remove_a(str):
    str = ""
    str = str.replace("<", "")
    return str