import sqlite3


class TableCreator():
    def __init__(self, DB):
        self.connector = sqlite3.connect(DB)
        self.c = self.connector.cursor()
        self.c.execute("PRAGMA foreign_keys = ON")
        self.connector.commit()

    def createArticle(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS Article'
                       '(ID TEXT PRIMARY KEY NOT NULL,'
                       ' ArticleName TEXT,'
                       ' Year INTEGER,'
                       ' Volume INTEGER,'
                       ' Issue INTEGER,'
                       ' Pages INTEGER,'
                       ' KeyWords TEXT,'
                       ' Abstract TEXT)')
        self.connector.commit()

    def createAuthor(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS Author'
                       '(Name TEXT PRIMARY KEY)')
        self.connector.commit()

    def createHas(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS Has'
                       '(Article_ID TEXT REFERENCES Article(ID) ON UPDATE CASCADE ON DELETE CASCADE, '
                       'Author_Name TEXT REFERENCES Author(Name) ON UPDATE CASCADE ON DELETE CASCADE, '
                       'PRIMARY KEY(Article_ID, Author_Name))')
        self.connector.commit()

    def createCitation(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS Citation'
                       '(Article_FID TEXT REFERENCES Article(ID) ON UPDATE CASCADE ON DELETE CASCADE, '
                       'Article_SID TEXT REFERENCES Article(ID) ON UPDATE CASCADE ON DELETE CASCADE, '
                       'PRIMARY KEY(Article_FID, Article_SID))')
        self.connector.commit()

    def closeConnect(self):
        self.connector.close()
