import PyPDF2
from calendar_writer import write_event
import re

file = open('sample_tickets/tt-pp.pdf', 'rb')
# file = open('ZSSK_ITD_20220819104454.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(file)
pageObj = pdfReader.getPage(0)

with open("text.txt", "w") as w:
    w.write(pageObj.extract_text())

train_names = {"os", "r", "rr", "rex", "ex", "ic", "ec"}
tr_name_w_sep = set([i + " " for i in train_names])

class Event:
    def __init__(self):
        self.train_type = ""
        self.start_date = ""
        self.end_date = ""
        self.start_time = ""
        self.end_time = ""
        self.start_station = ""
        self.end_station = ""

    def __repr__(self):
        return repr((self.train_type,
                        self.start_date,
                        self.end_date,
                        self.start_time,
                        self.end_time,
                        self.start_station,
                        self.end_station))

    def __str__(self):
        return str((self.train_type,
                        self.start_date,
                        self.end_date,
                        self.start_time,
                        self.end_time,
                        self.start_station,
                        self.end_station))

def is_date(s):
    s = s.strip().split(".")
    if len(s) != 3: return False

    try: s = list(map(int, s))
    except: return False

    if not (0 < s[0] <= 31): return False
    if not (0 < s[1] <= 12): return False
    if not (0 < s[2] <= 100): return False

    return True

def is_time(s):

    s = s.strip().split(":")
    if len(s) != 2: return False

    try:
        s = list(map(int, s))
    except:
        return False

    if not (0 < s[0] < 24): return False
    if not (0 <= s[1] < 60): return False

    return True

def parse_record(rec):

    # correct form : 0 - type, 1 - date, 2 - time,

    event = Event()

    event.train_type = rec["type"]

    if not is_date(rec["from_date"]): return Event()
    event.start_date = rec["from_date"]

    if not is_time(rec["from_time"]): return Event()
    event.start_time = rec["from_time"]

    event.start_station = rec["from_stat"]

    if not is_date(rec["to_date"]): return Event()
    event.end_date = rec["to_date"]

    if not is_time(rec["to_time"]): return Event()
    event.end_time = rec["to_time"]

    event.end_station += rec["to_stat"]

    return event

with open("text.txt", "r") as r:
    for line in r:

        #print(re.search(".* [ex | os] .* [0-9]{1,2}.[0-9]{1,2}.[0-9]{1,4}.", line))
        x = re.finditer(
            "(?P<type>Ex|Os) (?P<from_date>[0-9]{1,2}.[0-9]{1,2}.[0-9]{1,4}) "
            "(?P<from_time>[0-9]{1,2}:[0-9]{1,2}) (?P<from_stat>.*) "
            "(?P<to_date>[0-9]{1,2}.[0-9]{1,2}.[0-9]{1,4}) "
            "(?P<to_time>[0-9]{1,2}:[0-9]{1,2}) (?P<to_stat>[^\.\*0-9]*)", line)
        for match in x:
            record = parse_record(match.groupdict())
            if record.train_type != "":
                #print(record)
                write_event(record)

file.close()
