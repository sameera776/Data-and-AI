
from data import drivers
from ride_ops import search_ride

def assign_driver(ride_id):
    if not drivers:
        print("⏳ Waiting for driver...")
        return

    ride = search_ride(ride_id)
    if ride and ride["status"] == "Booked":
        driver = drivers.pop()
        ride["driver"] = driver
        ride["status"] = "Driver Assigned"
        print(f"🚗 Driver {driver} assigned!")


def complete_ride(ride_id):
    ride = search_ride(ride_id)
    if ride:
        drivers.add(ride["driver"])
        ride["status"] = "Completed"
        print("🏁 Ride completed successfully!")
