if __name__ == "__main__":
    from graph import Graph
    g = Graph.generate_random_graph(15, 0.5)
    g.debug()
    g.export_json('data/testdata.json')

