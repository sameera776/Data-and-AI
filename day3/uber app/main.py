import random
from ride_ops import create_ride, view_rides, calculate_fare,feedback
from driver_ops import assign_driver, complete_ride

ride_id = random.randint(1000, 9999)
name = input("Enter Customer Name: ")
pickup = input("Enter Pickup Location: ")
drop = input("Enter Drop Location: ")

distance = random.randint(1, 30)        
time = random.randint(5, 60)             
fare = calculate_fare(distance)

location = (pickup, drop)   

create_ride(
    ride_id=ride_id,
    name=name,
    location=location,
    distance=distance,
    time=time,
    fare=fare,
    driver=None,
    status="Booked",
    feedback=None
)

view_rides()

assign_driver(ride_id)

print("⏳ Driver is on the way...")
print(f"📍 Distance: {distance} km")
print(f"⏱ Estimated Time: {time} minutes")
print(f"💰 Estimated Fare: ₹{fare}")

complete_ride(ride_id)
feedback(ride_id)
view_rides()
