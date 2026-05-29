import networkx as nx
import matplotlib.pyplot as plt

class KnowledgeGraph:

    def __init__(self):
        self.graph = nx.DiGraph()

    def add_entity(self, entity):
        self.graph.add_node(entity)

    def add_relationship(self, source, target, relation):
        self.graph.add_edge(source, target, relation=relation)

    def display_relationships(self):
        print("\nKnowledge Graph Relationships:\n")

        for source, target, data in self.graph.edges(data=True):
            print(f"{source} --({data['relation']})--> {target}")

    def visualize(self):

        plt.figure(figsize=(10, 7))

        pos = nx.spring_layout(self.graph, seed=42)

        nx.draw(
            self.graph,
            pos,
            with_labels=True,
            node_size=3500,
            node_color="skyblue",
            font_size=10,
            font_weight="bold",
            arrows=True
        )

        edge_labels = nx.get_edge_attributes(
            self.graph,
            "relation"
        )

        nx.draw_networkx_edge_labels(
            self.graph,
            pos,
            edge_labels=edge_labels
        )

        plt.title("Knowledge Graph Example")
        plt.show()


kg = KnowledgeGraph()

kg.add_entity("Alice")
kg.add_entity("University")
kg.add_entity("Artificial Intelligence")
kg.add_entity("Professor Smith")
kg.add_entity("New York")
kg.add_entity("Google")
kg.add_entity("Machine Learning")

kg.add_relationship(
    "Alice",
    "University",
    "studies_at"
)

kg.add_relationship(
    "Alice",
    "Artificial Intelligence",
    "learns"
)

kg.add_relationship(
    "Professor Smith",
    "Artificial Intelligence",
    "teaches"
)

kg.add_relationship(
    "University",
    "New York",
    "located_in"
)

kg.add_relationship(
    "Alice",
    "Google",
    "intern_at"
)

kg.add_relationship(
    "Machine Learning",
    "Artificial Intelligence",
    "part_of"
)

kg.display_relationships()

kg.visualize()
