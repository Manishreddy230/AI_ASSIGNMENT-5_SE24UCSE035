# Assignment 5 - Q2 - AI Based Travel Planner

## Aim

To design an AI based Travel Planner that reuses existing knowledge bases such as tourist places, food recommendations, drink recommendations, hotel information, transport information, and cost assessment to generate personalized travel plans.

---

# Introduction

Travel planning involves selecting destinations, accommodation, transportation, food options, and estimating expenses. This process can be time-consuming when done manually.

The AI Based Travel Planner simplifies travel planning by using existing knowledge bases and user preferences to generate personalized travel recommendations. The system suggests tourist places, food options, drinks, and estimates the overall trip cost based on the user's budget and interests.

---

# Knowledge Bases Used

### 1. Tourist Places Knowledge Base

Contains information about tourist attractions.

Examples:

```text
Hyderabad → Charminar
Hyderabad → Golconda Fort
Goa → Baga Beach
Goa → Fort Aguada
```

### 2. Food Recommendation Knowledge Base

Contains food recommendations based on user preference.

Examples:

```text
Vegetarian
Non-Vegetarian
```

### 3. Drink Recommendation Knowledge Base

Contains drink suggestions based on food preference.

Examples:

```text
White Wine
Red Wine
Fresh Fruit Juice
Mocktails
```

### 4. Hotel Cost Knowledge Base

Contains estimated hotel costs.

Examples:

```text
Budget Hotel
Standard Hotel
Luxury Hotel
```

### 5. Transport Cost Knowledge Base

Contains transportation cost information.

Examples:

```text
Public Transport
Cab
Private Transport
```

---

# Methodology

The system works in the following steps:

### Step 1: User Input

The user enters:

- Destination
- Number of Days
- Budget
- Interest
- Food Preference
- Hotel Type
- Transport Type

### Step 2: Knowledge Retrieval

The planner retrieves information from the available knowledge bases.

### Step 3: Recommendation Generation

Based on user preferences, suitable tourist places, food options, and drinks are recommended.

### Step 4: Cost Assessment

The system estimates:

- Hotel Cost
- Food Cost
- Transport Cost
- Tourist Place Expenses

### Step 5: Travel Plan Generation

A personalized day-wise travel plan is generated.

---

# Sample Input

```text
Destination: Hyderabad
Days: 3
Budget: 15000
Interest: Heritage
Food Preference: Vegetarian
Hotel Type: Budget
Transport Type: Public
```

---

# Sample Output

```text
Generated Travel Plan

Destination: Hyderabad
Number of Days: 3

Recommended Places:
- Charminar
- Golconda Fort

Food Recommendations:
- Chutneys
- Santosh Dhaba
- Minerva Coffee Shop

Wine / Drink Recommendation:
- Light white wine or fresh fruit juice

Total Estimated Cost: 9350

Budget Check:
The plan is within the given budget.
```

---

# Conclusion

The AI Based Travel Planner successfully uses existing knowledge bases related to tourist places, food recommendations, drinks, hotel costs, and transportation costs. Based on user preferences and budget, the system generates personalized travel plans and performs cost assessment to assist in travel decision making.

The implementation was tested successfully using different user inputs.
