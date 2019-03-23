import sqlite3
import numpy as np
import pandas as pd
from Tablecreator import TableCreator
from Inserter import Inserter


def _exec(DB, statement):
    DB.c.execute(statement)


def createDB(DB_name):
    testDB = TableCreator(DB_name)
    testDB.createArticle()
    testDB.createAuthor()
    testDB.createHas()
    testDB.createCitation()
    testDB.closeConnect()
    return


def insert_paper(DB_name, article, authors, citations, citated, keywords, pages, year, volume, issue, abstract = ''):
    testDB = Inserter(DB_name)
    testDB.insertArticle(article, keywords, pages, year, volume, issue, abstract)

    for author in authors:
        testDB.insertAuthor(author)
        testDB.insertHas(article, author)

    for cit in citations:
        testDB.insertCitations(article, cit)
    for cit in citated:
        testDB.insertCitations(cit, article)
    testDB.closeConnect()
    return



name = 'test.db'
createDB(name)
insert_paper(name, article, authors, citations, citated, keywords, pages, year, volume, issue, abstract)