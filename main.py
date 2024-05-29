from config import *
from satellite_tracker import SatelliteTracker

import time

if __name__ == "__main__":

    satellite_tracker = SatelliteTracker(
        lat=MY_LAT,
        lon=MY_LONG,
        email="berry"
    )

    satellite_tracker.notify()