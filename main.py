from price_tracker import AmazonPriceTracker
from src.config import *


if __name__ == '__main__':

    price_tracker = AmazonPriceTracker(
        product_url=LIVE_URL,
        target_price=101.99,
        email_address=os.environ["EMAIL"]
    )

    price_tracker.notify()
