from .bd.Selector import Selector
import networkx as nx
import matplotlib.pyplot as plt

name = 'test.db'

def create_df_authors_for_year(year, DB_name=name):
    testDB = Selector(DB_name)
    df = testDB.make_df_for_year(year)
    testDB.closeConnect()
    return df


def create_df_authors_for_period(start, finish, DB_name=name):

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
        if drawG(G, year, type) != 0:
            print('something went wrong!')
    elif type == 'citations':
        ### citations' funcions go here
        pass
    return G

def drawG(G, year, type):
    nx.draw(G)
    plt.figure(figsize=(30, 30))
    plt.axis('off')
    layout = nx.kamada_kawai_layout(G)
    nx.draw_networkx_edges(G, pos=layout)
    nx.draw_networkx_nodes(G, pos=layout, node_color='blue')
    plt.title(type + ' ' + str(year), fontsize=80)
    plt.draw()
    plt.savefig('catalog/static/Graphs/Graph.png')



