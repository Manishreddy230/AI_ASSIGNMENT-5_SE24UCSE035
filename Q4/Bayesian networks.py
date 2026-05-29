class BayesianNetwork:

    def __init__(self):

        self.P_Burglary = {
            True: 0.001,
            False: 0.999
        }

        self.P_Earthquake = {
            True: 0.002,
            False: 0.998
        }

        self.P_Alarm = {
            (True, True): 0.95,
            (True, False): 0.94,
            (False, True): 0.29,
            (False, False): 0.001
        }

        self.P_JohnCalls = {
            True: 0.90,
            False: 0.05
        }

        self.P_MaryCalls = {
            True: 0.70,
            False: 0.01
        }

    def show_network(self):

        print("\nBAYESIAN NETWORK STRUCTURE\n")

        print("Burglary ------>")
        print("                  Alarm ------> JohnCalls")
        print("Earthquake ---->")
        print("                  Alarm ------> MaryCalls")

    def display_probabilities(self):

        print("\nPRIOR PROBABILITIES\n")

        print("P(Burglary=True)  =", self.P_Burglary[True])
        print("P(Burglary=False) =", self.P_Burglary[False])

        print("\nP(Earthquake=True)  =", self.P_Earthquake[True])
        print("P(Earthquake=False) =", self.P_Earthquake[False])

    def calculate_joint_probability(
            self,
            burglary,
            earthquake):

        p_b = self.P_Burglary[burglary]
        p_e = self.P_Earthquake[earthquake]

        p_a = self.P_Alarm[
            (burglary, earthquake)
        ]

        p_j = self.P_JohnCalls[True]
        p_m = self.P_MaryCalls[True]

        joint = (
            p_b *
            p_e *
            p_a *
            p_j *
            p_m
        )

        return joint

    def show_joint_table(self):

        print("\nJOINT PROBABILITY TABLE\n")

        cases = [
            (True, True),
            (True, False),
            (False, True),
            (False, False)
        ]

        for burglary, earthquake in cases:

            probability = self.calculate_joint_probability(
                burglary,
                earthquake
            )

            print(
                "Burglary =",
                burglary,
                " Earthquake =",
                earthquake,
                " Joint Probability =",
                round(probability, 8)
            )

    def probability_of_alarm(self):

        total = 0

        cases = [
            (True, True),
            (True, False),
            (False, True),
            (False, False)
        ]

        for burglary, earthquake in cases:

            total += (
                self.P_Burglary[burglary]
                *
                self.P_Earthquake[earthquake]
                *
                self.P_Alarm[
                    (burglary, earthquake)
                ]
            )

        return total

    def probability_of_burglary_given_calls(self):

        numerator = 0
        denominator = 0

        cases = [
            (True, True),
            (True, False),
            (False, True),
            (False, False)
        ]

        for burglary, earthquake in cases:

            joint = self.calculate_joint_probability(
                burglary,
                earthquake
            )

            denominator += joint

            if burglary:
                numerator += joint

        return numerator / denominator

    def probability_of_earthquake_given_calls(self):

        numerator = 0
        denominator = 0

        cases = [
            (True, True),
            (True, False),
            (False, True),
            (False, False)
        ]

        for burglary, earthquake in cases:

            joint = self.calculate_joint_probability(
                burglary,
                earthquake
            )

            denominator += joint

            if earthquake:
                numerator += joint

        return numerator / denominator

    def inference_report(self):

        print("\nINFERENCE RESULTS\n")

        alarm_probability = self.probability_of_alarm()

        print(
            "Probability of Alarm =",
            round(alarm_probability, 6)
        )

        burglary_probability = (
            self.probability_of_burglary_given_calls()
        )

        print(
            "Probability of Burglary given JohnCalls and MaryCalls =",
            round(burglary_probability, 6)
        )

        earthquake_probability = (
            self.probability_of_earthquake_given_calls()
        )

        print(
            "Probability of Earthquake given JohnCalls and MaryCalls =",
            round(earthquake_probability, 6)
        )


bn = BayesianNetwork()

print("\n====================================")
print(" BAYESIAN NETWORK IMPLEMENTATION ")
print("====================================")

bn.show_network()

bn.display_probabilities()

bn.show_joint_table()

bn.inference_report()

print("\n====================================")
print(" EXECUTION COMPLETED ")
print("====================================")
