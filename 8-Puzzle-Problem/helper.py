import pydot
def draw_legend(graph):
    graphlegend = pydot.Cluster(graph_name="legend", label="Legend", fontsize="20", color="red",
                                fontcolor="blue", style="filled", fillcolor="white")

    legend1 = pydot.Node('Start Node', shape="plaintext")
    graphlegend.add_node(legend1)
    legend2 = pydot.Node("Intermediate Nodes", shape="plaintext")
    graphlegend.add_node(legend2)
    legend3 = pydot.Node('Goal Node', shape="plaintext")
    graphlegend.add_node(legend3)
    legend4 = pydot.Node('Leaf Nodes', shape="plaintext")
    graphlegend.add_node(legend4)


    node1 = pydot.Node("1", style="filled", fillcolor="cyan", label="")
    graphlegend.add_node(node1)
    node2 = pydot.Node("2", style="filled", fillcolor="green", label="")
    graphlegend.add_node(node2)
    node3 = pydot.Node("3", style="filled", fillcolor="gold", label="")
    graphlegend.add_node(node3)
    node4 = pydot.Node("4", style="filled", fillcolor="red", label="")
    graphlegend.add_node(node4)
    


    graph.add_subgraph(graphlegend)
    graph.add_edge(pydot.Edge(legend1, legend2, style="invis"))
    graph.add_edge(pydot.Edge(legend2, legend3, style="invis"))
    graph.add_edge(pydot.Edge(legend3, legend4, style="invis"))

    graph.add_edge(pydot.Edge(node1, node2, style="invis"))
    graph.add_edge(pydot.Edge(node2, node3, style="invis"))
    graph.add_edge(pydot.Edge(node3, node4, style="invis"))