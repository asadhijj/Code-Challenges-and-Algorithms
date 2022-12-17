class Node:
    def __init__(self, value=None):
        self.value = value
    
    def __str__(self):
        return self.value

class Edge:
    def __init__(self,vertex,weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self,value):
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex

    def add_edge(self,node1,node2,weight=0):
        
        if not node1 in self.adj_list.keys():
            return("this node does not exist")

        if not node2 in self.adj_list.keys():
            return("this node does not exist")
        
        edge1 = Edge(node2,weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1,weight)
        self.adj_list[node2].append(edge2)

    def breadth_first(self,target):
        seen = []
        queue = [target]
        while queue:
            current_node = queue.pop(0)
            if current_node.value not in seen:
                seen.append(current_node.value)
                for edge in self.adj_list[current_node]:
                    queue.append(edge.vertex)
        return seen


if __name__ == "__main__":
    gr = Graph()
    a = gr.add_node('A')
    b = gr.add_node('B')
    c = gr.add_node('C')
    d = gr.add_node('D')
    e = gr.add_node('E')
    f = gr.add_node('F')
    g = gr.add_node('G')
    h = gr.add_node('H')
    i = gr.add_node('I')
    k = gr.add_node('K')


    gr.add_edge(a, c)
    gr.add_edge(a, e)
    gr.add_edge(a, b)
    gr.add_edge(e, f)
    gr.add_edge(e, g)
    gr.add_edge(e, d)
    gr.add_edge(f, i)
    gr.add_edge(h, k)
    gr.add_edge(b, d)
    gr.add_edge(g, h)
    gr.add_edge(i, k)
    gr.add_edge(c, f)
    gr.add_edge(f, h)


    print(gr.breadth_first(c))