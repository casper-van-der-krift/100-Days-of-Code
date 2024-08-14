import os
import requests


SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/304789e7b10fc09e838317ed05177ab4/flightDeals/prices'
SHEETY_USERS_ENDPOINT = 'https://api.sheety.co/304789e7b10fc09e838317ed05177ab4/flightDeals/users'


class DataManager:

    def __init__(self):
        self._user = os.environ.get("SHEETY_USERNAME")
        self._password = os.environ.get("SHEETY_PW")
        self._authorization = (self._user, self._password)
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(
            url=SHEETY_PRICES_ENDPOINT,
            auth=self._authorization,
        )
        response.raise_for_status()

        data = response.json()

        print(data)

        self.destination_data = data["prices"]

        print(self.destination_data)

        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )

            response.raise_for_status()

            print(response.text)

    def get_customer_emails(self):
        response = requests.get(
            url=SHEETY_USERS_ENDPOINT,
            auth=self._authorization,
        )

        response.raise_for_status()

        data = response.json()

        self.user_data = data['users']

        print(self.user_data)

        return self.user_data


