from datetime import date
from dateutil.relativedelta import relativedelta

"""Output sample
   1982-05-08 No merit or demerit points.
   1983-06-06 2 demerit point(s).
   1987-06-07 1 merit point(s).

   InputSample
   19820508
   19830606 2"""


"""
* Class to manage driver points *
"""


class DriverPoints:

    def __init__(self, dt):
        self.points = 0
        self.lastDate = dt
        self.printString = ""+str(dt.year)+"-"+str(dt.month)+"-"+str(dt.day)+" No merit or demerit points.\n"

    def demerit(self, dem_dt, dem_points):
        assert isinstance(dem_dt, date)
        assert isinstance(dem_points, int)
        diff = int(relativedelta(dem_dt, self.lastDate).years)

        """If a new offense occurs on the same day as a demerit point reduction or merit point award, the
                    reduction/award is done before the new demerit points are given.
           Se o dia e o mes de lastDate e dem_dt forem iguais, incrementar diff"""

        i = 0
        while (i < diff) and (self.points < 5):
            if self.points < 0:
                self.lastDate = date((self.lastDate.year + 1), self.lastDate.month, self.lastDate.day)
                line = "" + str(self.lastDate.year) + "-" + str(self.lastDate.month) + "-" + str(self.lastDate.day)
                if self.points == -2:
                    self.points = 0
                else:
                    self.points = int(self.points/2)
                if self.points == 0:
                    line += " No merit or demerit points.\n"
                else:
                    line += " " + str(abs(self.points)) + " demerit point(s).\n"
                i += 1
            else:
                if (diff - i) > 1:
                    self.points += 1
                    self.lastDate = date((self.lastDate.year + 2), self.lastDate.month, self.lastDate.day)
                    line = "" + str(self.lastDate.year) + "-" + str(self.lastDate.month) + "-" + str(self.lastDate.day)
                    line += " " + str(self.points) + " merit point(s).\n"
                    i += 2
                else:
                    break
            self.printString += line

        line = "" + str(dem_dt.year) + "-" + str(dem_dt.month) + "-" + str(dem_dt.day)
        if self.points > 0:
            if dem_points > (self.points*2):
                dem_points -= (self.points*2)
                self.points = (0-dem_points)
                line += " " + str(abs(self.points)) + " demerit point(s).\n"
            else:
                self.points = int(self.points-(dem_points/2))
                if self.points == 0:
                    line += " No merit or demerit points.\n"
                else:
                    line += " " + str(self.points) + " merit point(s).\n"
        else:
            self.points -= dem_points
            line += " " + str(abs(self.points)) + " demerit point(s).\n"

        self.printString += line
        self.lastDate = dem_dt

    def end_points_score(self):
        while self.points < 5:
            if self.points < 0:
                self.lastDate = date((self.lastDate.year + 1), self.lastDate.month, self.lastDate.day)
                line = "" + str(self.lastDate.year) + "-" + str(self.lastDate.month) + "-" + str(self.lastDate.day)
                if self.points == -2:
                    self.points = 0
                else:
                    self.points = int(self.points/2)
                if self.points == 0:
                    line += " No merit or demerit points.\n"
                else:
                    line += " " + str(abs(self.points)) + " demerit point(s).\n"
            else:
                self.points += 1
                self.lastDate = date((self.lastDate.year + 2), self.lastDate.month, self.lastDate.day)
                line = "" + str(self.lastDate.year) + "-" + str(self.lastDate.month) + "-" + str(self.lastDate.day)
                line += " " + str(self.points) + " merit point(s).\n"
            self.printString += line

    def print_output(self):
        self.end_points_score()
        print(self.printString)

"""
* function to get date from string *
"""


def get_date_from_string(buffer=""):
    assert isinstance(buffer, str)
    year = int(buffer[:4])
    month = int(buffer[4:6])
    day = int(buffer[6:])

    return date(year, month, day)

"""
def get_date_from_string(buffer=""):
    assert isinstance(buffer, str)
    year = int(buffer.split('-')[0])
    month = int(buffer.split('-')[1])
    day = int(buffer.split('-')[2])

    return date(year, month, day)
"""

"""
* START *
"""
nInput = int(input())

driverPoints = None

i = 0
while True:
    try:
        dem_str = input()
        if dem_str == "":
            """print("*** blank line ****")"""
            if driverPoints is not None:
                driverPoints.print_output()
            driverPoints = DriverPoints(get_date_from_string(input()))
            i += 1
        else:
            dem_date = get_date_from_string(dem_str.split(' ')[0])
            demPoints = int(dem_str.split(' ')[1])
            driverPoints.demerit(dem_date, demPoints)
    except EOFError:
        pass
        break

"""driverPoints.print_output()"""



