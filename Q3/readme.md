# Assignment 5 - Q3 - Knowledge Graphs and Tools Used to Build Them

## Aim

To study Knowledge Graphs and explore the tools used for building and managing Knowledge Graphs.

---

# Introduction

A Knowledge Graph (KG) is a way of representing information using entities, relationships, and attributes. It helps connect related pieces of information so that machines can understand how different concepts are linked together.

Knowledge Graphs are widely used in Artificial Intelligence, recommendation systems, search engines, semantic web applications, and chatbots because they allow information to be organized in a structured and connected form.

---

# Components of a Knowledge Graph

### 1. Entities

Entities represent real-world objects or concepts.

Examples:

```text
City
Tourist Place
Restaurant
Person
Product
```

### 2. Relationships

Relationships connect entities together.

Examples:

```text
has_place
located_in
has_food
belongs_to
```

### 3. Attributes

Attributes provide additional information about entities.

Examples:

```text
Location
Category
Rating
Cost
```

---

# Tools Used to Build Knowledge Graphs

### 1. Neo4j

Neo4j is a graph database that stores information as nodes and relationships. It is widely used for creating and managing Knowledge Graphs.

### 2. Protégé

Protégé is an ontology development tool used for designing and managing knowledge structures. It is commonly used in semantic web applications.

### 3. GraphDB

GraphDB is a semantic graph database that supports RDF data storage and querying.

### 4. Apache Jena

Apache Jena is a Java framework used for building semantic web and linked data applications.

### 5. RDF (Resource Description Framework)

RDF is a standard model used to represent information in the form of subject-predicate-object triples.

Example:

```text
Delhi → has_place → India Gate
```

### 6. SPARQL

SPARQL is a query language used to retrieve information from RDF-based Knowledge Graphs.

### 7. NetworkX

NetworkX is a Python library used to create, analyze, and visualize graph structures.

---

# Example Used in this Assignment

A simple Knowledge Graph was implemented using Python dictionaries.

The graph stores information about cities, tourist places, and food items.

Examples:

```text
Delhi → India Gate
Delhi → Red Fort
Kerala → Munnar
Kerala → Alleppey
```

The Knowledge Graph also stores food recommendations and place categories.

The program performs simple queries such as:

- Retrieving tourist places of a city
- Retrieving food recommendations
- Retrieving the category of a place

This demonstrates how connected information can be represented and queried using a Knowledge Graph.

---

# Conclusion

Knowledge Graphs provide a structured way of representing connected information using entities, relationships, and attributes. Various tools such as Neo4j, Protégé, GraphDB, Apache Jena, RDF, SPARQL, and NetworkX can be used to build and manage Knowledge Graphs.

The implementation was tested successfully using multiple graph queries.
