
def suggest_itinerary(days):
    itinerary = {
        1: ["Visit local landmarks", "Try famous local food", "Sunset walk at a popular spot"],
        2: ["City sightseeing", "Museum or cultural tour", "Evening shopping market"],
        3: ["Beach or nature visit", "Adventure activity", "Dinner at a recommended restaurant"],
        4: ["Day trip to nearby town", "Local experience (like cooking class)", "Photography tour"],
        5: ["Relax day with spa or chill", "Final shopping", "Sunset cruise"]
    }

    return itinerary.get(days, ["Explore freely, no strict plan needed!"])          