class KnowledgeGraph:

    def __init__(self):
        self.graph = {}

    def add_entity(self, entity):
        if entity not in self.graph:
            self.graph[entity] = []

    def add_relationship(self, source, relation, target):
        self.add_entity(source)
        self.add_entity(target)
        self.graph[source].append((relation, target))

    def display(self):
        print("\n===== KNOWLEDGE GRAPH =====\n")

        for entity in self.graph:
            for relation, target in self.graph[entity]:
                print(
                    entity,
                    "--(" + relation + ")-->",
                    target
                )

    def find_connections(self, entity):

        if entity not in self.graph:
            print("\nEntity not found.")
            return

        print("\nConnections for", entity)

        for relation, target in self.graph[entity]:
            print(
                entity,
                "--(" + relation + ")-->",
                target
            )


kg = KnowledgeGraph()

kg.add_relationship(
    "Alice",
    "studies_at",
    "University"
)

kg.add_relationship(
    "University",
    "located_in",
    "New York"
)

kg.add_relationship(
    "Professor Smith",
    "teaches",
    "Artificial Intelligence"
)

kg.add_relationship(
    "Alice",
    "learns",
    "Artificial Intelligence"
)

kg.add_relationship(
    "Artificial Intelligence",
    "includes",
    "Machine Learning"
)

kg.add_relationship(
    "Alice",
    "intern_at",
    "Google"
)

kg.display()

kg.find_connections("Alice")
