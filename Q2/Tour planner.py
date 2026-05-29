class TravelPlanner:

    def __init__(self):

        self.places = {
            "Hyderabad": {
                "History": ["Charminar", "Golconda Fort", "Salar Jung Museum"],
                "Food": ["Paradise Biryani", "Shadab Restaurant"]
            },
            "Goa": {
                "Beach": ["Baga Beach", "Calangute Beach", "Anjuna Beach"],
                "Food": ["Fisherman's Wharf", "Vinayak Family Restaurant"]
            },
            "Delhi": {
                "History": ["Red Fort", "India Gate", "Qutub Minar"],
                "Food": ["Karim's", "Paranthe Wali Gali"]
            }
        }

        self.hotels = {
            "Hyderabad": [
                ("Hotel Abode", 2500),
                ("Taj Krishna", 6000)
            ],
            "Goa": [
                ("Resort Rio", 4500),
                ("Taj Exotica", 8000)
            ],
            "Delhi": [
                ("The Lalit", 5000),
                ("Hotel City Star", 2500)
            ]
        }

        self.travel_cost = {
            "Hyderabad": 3000,
            "Goa": 5000,
            "Delhi": 4000
        }

    def recommend_places(self, city, interest):

        if city not in self.places:
            return []

        return self.places[city].get(interest, [])

    def recommend_food(self, city):

        if city not in self.places:
            return []

        return self.places[city].get("Food", [])

    def recommend_hotel(self, city, budget):

        if city not in self.hotels:
            return None

        for hotel, cost in sorted(self.hotels[city], key=lambda x: x[1]):
            if cost <= budget:
                return hotel, cost

        return self.hotels[city][0]

    def estimate_cost(self, city, days, hotel_cost):

        transport = self.travel_cost[city]
        accommodation = hotel_cost * days
        food = 1000 * days

        total = transport + accommodation + food

        return total

    def generate_itinerary(self, city, places, days):

        itinerary = {}

        index = 0

        for day in range(1, days + 1):

            if index < len(places):
                itinerary[f"Day {day}"] = places[index]
                index += 1
            else:
                itinerary[f"Day {day}"] = "Free Exploration"

        return itinerary


planner = TravelPlanner()

print("\n===== AI TRAVEL PLANNER =====\n")

city = input("Enter Destination City (Hyderabad/Goa/Delhi): ")
interest = input("Enter Interest (History/Beach): ")
budget = int(input("Enter Budget (INR): "))
days = int(input("Enter Number of Days: "))

places = planner.recommend_places(city, interest)
food = planner.recommend_food(city)

hotel, hotel_cost = planner.recommend_hotel(city, budget)

total_cost = planner.estimate_cost(
    city,
    days,
    hotel_cost
)

itinerary = planner.generate_itinerary(
    city,
    places,
    days
)

print("\n===== TRAVEL PLAN =====\n")

print("Destination:", city)

print("\nRecommended Places:")
for place in places:
    print("-", place)

print("\nFood Recommendations:")
for item in food:
    print("-", item)

print("\nRecommended Hotel:")
print(hotel)
print("Cost Per Night: ₹", hotel_cost)

print("\nEstimated Total Cost:")
print("₹", total_cost)

print("\nItinerary:")

for day, activity in itinerary.items():
    print(day + ":", activity)

print("\n===== END OF PLAN =====")
