
#   Реализовать 2 функции
import imageio


def getGraph(year, graph):
    df = str(year) + str(graph)
    return df


def drowG(y):
    im = imageio.imread('~/Desktop/imgs/' + str(y) + '.png')
    imageio.imwrite('~/Downloads/graph/GroupProj/Group_3_Proj/website/catalog/static/Graphs/Graph.png', im[:, :, :])
    #save(.static/Graphs/graph.png)
    return 0
