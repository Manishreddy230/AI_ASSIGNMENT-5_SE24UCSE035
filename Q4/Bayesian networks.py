from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ("Burglary", "Alarm"),
    ("Earthquake", "Alarm"),
    ("Alarm", "JohnCalls"),
    ("Alarm", "MaryCalls")
])

cpd_burglary = TabularCPD(
    variable="Burglary",
    variable_card=2,
    values=[[0.999], [0.001]]
)

cpd_earthquake = TabularCPD(
    variable="Earthquake",
    variable_card=2,
    values=[[0.998], [0.002]]
)

cpd_alarm = TabularCPD(
    variable="Alarm",
    variable_card=2,
    values=[
        [0.999, 0.71, 0.06, 0.05],
        [0.001, 0.29, 0.94, 0.95]
    ],
    evidence=["Burglary", "Earthquake"],
    evidence_card=[2, 2]
)

cpd_john = TabularCPD(
    variable="JohnCalls",
    variable_card=2,
    values=[
        [0.95, 0.10],
        [0.05, 0.90]
    ],
    evidence=["Alarm"],
    evidence_card=[2]
)

cpd_mary = TabularCPD(
    variable="MaryCalls",
    variable_card=2,
    values=[
        [0.99, 0.30],
        [0.01, 0.70]
    ],
    evidence=["Alarm"],
    evidence_card=[2]
)

model.add_cpds(
    cpd_burglary,
    cpd_earthquake,
    cpd_alarm,
    cpd_john,
    cpd_mary
)

print("Model Valid:", model.check_model())

inference = VariableElimination(model)

print("\nProbability of Burglary:")
result1 = inference.query(
    variables=["Burglary"]
)
print(result1)

print("\nProbability of Alarm:")
result2 = inference.query(
    variables=["Alarm"]
)
print(result2)

print("\nProbability of Burglary given JohnCalls and MaryCalls:")
result3 = inference.query(
    variables=["Burglary"],
    evidence={
        "JohnCalls": 1,
        "MaryCalls": 1
    }
)
print(result3)
