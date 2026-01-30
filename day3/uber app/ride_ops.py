
from data import rides, BASE_FARE, FARE_PER_KM

def calculate_fare(distance):
    return BASE_FARE + (distance * FARE_PER_KM)


def create_ride(**kwargs):
    rides.append(kwargs)
    print("✅ Ride booked successfully!")


def view_rides():
    if not rides:
        print("❌ No rides available")
        return
    for ride in rides:
        print(ride)


def search_ride(ride_id):
    for ride in rides:
        if ride["ride_id"] == ride_id:
            print("🔍 Ride Found:", ride)
            return ride
    print("❌ Ride not found")
    return None

def feedback(ride_id):
    for ride in rides:
        if ride["ride_id"] == ride_id:
            comment = input("Please provide your feedback for the ride: ")
            ride["feedback"] = comment
            print("🙏 Thank you for your feedback!")
            return
    print("❌ Ride not found")
