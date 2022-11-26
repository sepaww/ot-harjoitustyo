import sqlite3


class Databaseop:
    def __init__(self):
        self.db = sqlite3.connect("highscore.db")
        self.db.isolation_level = None
        self.names = 0
        self.days = 0
        self.exist()
        self.geths()

    def cleartable(self):
        self.db.execute("DROP table IF EXISTS hs")
        self.db.commit()

    def namechange(self):
        while self.scorelist[self.ind][0][-1:] == "_":
            self.scorelist[self.ind][0] = self.scorelist[self.ind][0][:-1]
        if self.scorelist[self.ind][0] == "":
            self.scorelist[self.ind][0] = "anon"
        self.cleartable()
        self.insertintable()

    def insertintable(self):
        self.db.execute("CREATE TABLE hs (name varchar(255), days int)")
        for i in range(10):
            name = self.scorelist[i][0]
            day = self.scorelist[i][1]
            self.db.execute(
                "INSERT INTO hs(name,days) VALUES(?,?)", (name, day))
        self.db.commit()

    def exist(self):
        text = "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='hs'"
        cur = self.db.cursor()
        cur.execute(text)

        if cur.fetchone()[0] != 1:
            print("lisataantaulu")
            self.db.execute("CREATE TABLE hs (name varchar(255), days int)")
            for i in range(10):
                self.db.execute(
                    "INSERT INTO hs(name,days) VALUES(?, ?)", ("anon", 0))
                self.db.commit()

    def geths(self):
        print("et")
        self.days = self.db.execute("SELECT days FROM hs").fetchall()
        self.days = [i[0] for i in self.days]
        self.names = self.db.execute("SELECT name FROM hs").fetchall()
        self.names = [i[0] for i in self.names]
        #print(self.names, self.days)
        self.scorelist = [(self.names[i], self.days[i])
                          for i in range(len(self.days))]
        print(self.scorelist)
