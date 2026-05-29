P_Burglary = {
    True: 0.001,
    False: 0.999
}

P_Earthquake = {
    True: 0.002,
    False: 0.998
}

P_Alarm = {
    (True, True): 0.95,
    (True, False): 0.94,
    (False, True): 0.29,
    (False, False): 0.001
}

P_JohnCalls = {
    True: 0.90,
    False: 0.05
}

P_MaryCalls = {
    True: 0.70,
    False: 0.01
}


def probability_burglary_given_calls():

    numerator = 0
    denominator = 0

    for burglary in [True, False]:
        for earthquake in [True, False]:

            p_b = P_Burglary[burglary]
            p_e = P_Earthquake[earthquake]

            p_a = P_Alarm[(burglary, earthquake)]

            p_j = P_JohnCalls[True]
            p_m = P_MaryCalls[True]

            joint = p_b * p_e * p_a * p_j * p_m

            denominator += joint

            if burglary:
                numerator += joint

    return numerator / denominator


print("Bayesian Network Example")
print("------------------------")

print("P(Burglary=True) =", P_Burglary[True])
print("P(Earthquake=True) =", P_Earthquake[True])

result = probability_burglary_given_calls()

print("\nProbability of Burglary given JohnCalls and MaryCalls:")
print(round(result, 4))
