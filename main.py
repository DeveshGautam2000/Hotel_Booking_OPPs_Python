import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def book(self):
        """Book a hotel by Changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    def view_hotels(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass

    def genrate(self):
        pass


print(df)
hotel_id = input("Enter the id of the Hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    name = input("Enter Your Name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.genrate())
else:
    print("Hotel is not Free")
