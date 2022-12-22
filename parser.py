import PyPDF2
from calendar_writer import write_event

file = open('ZSSK_ITD_20221222183857.pdf', 'rb')
# file = open('ZSSK_ITD_20220819104454.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(file)
pageObj = pdfReader.getPage(0)

with open("text.txt", "w") as w:
    w.write(pageObj.extract_text())

train_names = {"os", "r", "rr", "rex", "ex"}
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

    if not (1 < s[0] <= 31): return False
    if not (1 < s[1] <= 12): return False
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
    if not (0 < s[1] < 60): return False

    return True

def parse_record(rec):

    # correct form : 0 - type, 1 - date, 2 - time,

    event = Event()

    ind = 0

    event.train_type = rec[ind]
    ind += 1

    if not is_date(rec[ind]): return Event()
    event.start_date = rec[ind]
    ind += 1

    if not is_time(rec[ind]): return Event()
    event.start_time = rec[ind]
    ind += 1

    while not is_date(rec[ind]):
        if event.start_station != "" : event.start_station += " "
        event.start_station += rec[ind]
        ind += 1

    if not is_date(rec[ind]): return Event()
    event.end_date = rec[ind]
    ind += 1

    if not is_time(rec[ind]): return Event()
    event.end_time = rec[ind]
    ind += 1

    while ind < len(rec):

        # train number after station name
        try:
            int(rec[ind])
            break
        except: pass

        if event.end_station != "" : event.end_station += " "
        event.end_station += rec[ind]
        ind += 1
    return event

with open("text.txt", "r") as r:
    for line in r:
        if any([tr in line.lower() for tr in tr_name_w_sep]):
            for tr in tr_name_w_sep:
                if tr in line.lower():
                    pos = line.lower().index(tr)
                    #print(line[pos:].split())
                    record = parse_record(line[pos:].split())
                    if record.train_type != "":
                        # print(record)
                        write_event(record)
                    break

file.close()