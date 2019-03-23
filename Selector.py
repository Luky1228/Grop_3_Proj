import sqlite3
import numpy as np
import pandas as pd


class Selector():
    def __init__(self, DB):
        self.connector = sqlite3.connect(DB)
        self.c = self.connector.cursor()
        self.c.execute("PRAGMA foreign_keys = ON")
        self.connector.commit()
        np.random.seed(4404)
    
    def make_df_authors(self):
        df = pd.DataFrame({'id':[], 'authors_list':[]})
        statement = 'SELECT Article.ID FROM Article'
        self.c.execute(statement)
        self.connector.commit()
        articlesid = np.array(self.c.fetchall())
        for art in articlesid:
            statement = 'SELECT Has.Author_Name ' \
                        'FROM Has ' \
                        'WHERE Has.Article_ID = ?'
            self.c.execute(statement, art)
            self.connector.commit()
            authors = np.array(self.c.fetchall())
            author_list = []
            for auth in authors:
                author_list.append(auth[0])
            df = df.append({'id':art[0], 'authors_list':author_list}, ignore_index=True)
        return df

    def make_df_for_year(self, year):
        df = pd.DataFrame({'id':[], 'authors_list':[]})
        statement = 'SELECT Article.ID ' \
                    'FROM Article ' \
                    'WHERE Article.Year = ?'
        self.c.execute(statement, [year])
        self.connector.commit()
        articlesid = np.array(self.c.fetchall())
        for art in articlesid:
            statement = 'SELECT Has.Author_Name ' \
                        'FROM Has ' \
                        'WHERE Has.Article_ID = ?'
            self.c.execute(statement, art)
            self.connector.commit()
            authors = np.array(self.c.fetchall())
            author_list = []
            for auth in authors:
                author_list.append(auth[0])
            df = df.append({'id':art[0], 'authors_list':author_list}, ignore_index=True)
        return df

    def closeConnect(self):
        self.connector.close()
