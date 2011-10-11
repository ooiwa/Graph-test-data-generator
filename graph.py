class Graph(object):
    def __init__(self):
        self.nodes = []
        self.edges = []

    @classmethod
    def generate_complete_graph(cls, node_num):
        graph = cls()

        for i in range(node_num):
            graph.add_node()

        for i in range(node_num):
            for j in range(i+1, node_num):
                graph.add_edge(i, j)

        return graph

    @classmethod
    def generate_random_graph(cls, node_num, rate):
        graph = cls()

        for i in range(node_num):
            graph.add_node()

        import random
        for i in range(node_num):
            for j in range(i+1, node_num):
                if random.random() < rate:
                    graph.add_edge(i, j)
        
        return graph

    def add_node(self):
        node = {"id": self.get_number_of_nodes()}
        self.nodes.append(node)

    def add_edge(self, i, j):
        #edge = {"source":i, "target":j}
        edge = [i, j]
        self.edges.append(edge)

    def get_number_of_nodes(self):
        return len(self.nodes)

    def get_number_of_edges(self):
        return len(self.edges)

    def export_json(self, path):
        print "writing data: " + path
        f = open(path, "w")
        data = {"nodes": self.nodes, "edges":self.edges}
        import simplejson
        jsondata = simplejson.dumps(data)
        f.write(jsondata)
        f.close()
        print "writing completed"

    def debug(self):
        print self.nodes
        print self.edges

    # about node attribute
    
    def add_node_value(self, node_id, value):
        self.nodes[node_id]["value"] = value

    def add_node_attrs(self, node_id, **attrs):
        # UNDONE
        pass 
    

    

