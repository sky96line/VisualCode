class Seet:
    CPI = 1
    count = 0

    def __init__(self, subject, mark):
        self.subject = subject
        self.mark = mark
        Seet.CPI += mark
        Seet.count += 1

    def getSubject(self):
        return self.subject

    def getMark(self):
        return self.mark

    def getCPI(self):
        return Seet.CPI / Seet.count


for i in range(0, 3):

    s = raw_input("Enter subject : ")

    m = int(raw_input("Enter mark : "))
    ss = Seet(s, m)
    print(ss.getMark())

print("CPI is {}", ss.getCPI())
