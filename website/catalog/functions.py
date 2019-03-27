from Selector import Selector
from Tablecreator import TableCreator
from Inserter import Inserter

import networkx as nx
import matplotlib.pyplot as plt


def create_df_authors_for_year(year, DB_name='test.db'):
    testDB = Selector(DB_name)
    df = testDB.make_df_for_year(year)
    testDB.closeConnect()
    return df


def create_df_authors_for_period(start, finish, DB_name='test.db'):
    df = create_df_authors_for_year(start, DB_name)
    for year in range(start + 1, finish + 1):
        df = df.append(create_df_authors_for_year(year, DB_name))
    return df


def create_graph_from_pandas_df(df):
    """ Takes pandas dataframe and create networkx graph. We suggest every row in df
        is an article with next columns: 'list of authors' (list of strings)
    """
    G = nx.Graph()

    for num, row in df.iterrows():
        authors_list = row['authors_list']
        # connect every one and update edges
        for i in range(len(authors_list)):
            for j in range(i + 1, len(authors_list)):
                from_, to_ = authors_list[i], authors_list[j]
                new_weight = (G[from_][to_]['weight'] if G.has_edge(from_, to_) else 0) + 1
                G.add_edge(from_, to_, weight=new_weight)

    return G


def getGraph(year, type):
    if type == 'co-authorship':
        df = create_df_authors_for_year(year)
        G = create_graph_from_pandas_df(df)
        if drawG(G) != 0:
            print('something went wrong!')
    elif type == 'citations':
        ### citations' funcions go here
        pass
    return G

def drawG(G):
    nx.draw(G)
    plt.draw()
    plt.savefig('.static/Graphs/graph.png', format="PNG")
    #save('.static/Graphs/graph.png')

    return 0

