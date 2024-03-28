our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

shared_destinations = our_routes.intersection(competitor_routes)
print(f"Both airlines fly to {shared_destinations}")

unique_to_us = our_routes.difference(competitor_routes)
print(f"Only our airline flies to {unique_to_us}")

unique_to_each = our_routes.symmetric_difference(competitor_routes)
print(f"These are the destinations that neither airline shares: {unique_to_each}")