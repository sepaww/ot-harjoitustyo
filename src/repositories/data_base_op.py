import sqlite3
import os


class Data_base_op:
    """Class for operating the highscore database
    """

    def __init__(self):
        """initiator
        """
        dir_name = os.path.dirname(__file__)
        database_spot = os.path.join(dir_name, "..", "highscore.db")
        self.data = sqlite3.connect(database_spot)
        self.data.isolation_level = None
        self.names = 0
        self.days = 0
        self.exist()
        self.get_hs()
        self.ind = -1

    def clear_table(self):
        """clears the database of highscore table before updating it
        """
        self.data.execute("DROP table IF EXISTS hs")
        self.data.commit()

    def namechange(self):
        """modefies the given player name by removing excess
        underscores and replaces and empty name with
        'anon' anonymous
        """
        while self.score_list[self.ind][0][-1:] == "_":
            self.score_list[self.ind][0] = self.score_list[self.ind][0][:-1]
        if self.score_list[self.ind][0] == "":
            self.score_list[self.ind][0] = "anon"
        self.clear_table()
        self.insert_in_table()

    def insert_in_table(self):
        """creates the highscore table and saves the current scoreboard to it
        """
        self.data.execute("CREATE TABLE hs (name varchar(255), days int)")
        for i in range(10):
            name = self.score_list[i][0]
            day = self.score_list[i][1]
            self.data.execute(
                "INSERT INTO hs(name,days) VALUES(?,?)", (name, day))
        self.data.commit()

    def exist(self):
        """checks whether the hs table already exists in the database.
        if not: adds a table hs to it and fills it with anon 0 values
        """
        text = "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='hs'"
        cur = self.data.cursor()
        cur.execute(text)

        if cur.fetchone()[0] != 1:

            self.data.execute("CREATE TABLE hs (name varchar(255), days int)")
            for _ in range(10):
                self.data.execute(
                    "INSERT INTO hs(name,days) VALUES(?, ?)", ("anon", 0))
                self.data.commit()

    def get_hs(self):
        """takes the highscore data from database and adds it to class values.
        """
        self.days = self.data.execute("SELECT days FROM hs").fetchall()
        self.days = [i[0] for i in self.days]
        self.names = self.data.execute("SELECT name FROM hs").fetchall()
        self.names = [i[0] for i in self.names]
        self.score_list = [(self.names[i], self.days[i])
                          for i in range(len(self.days))]
