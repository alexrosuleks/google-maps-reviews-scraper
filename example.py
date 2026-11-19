"""Google Maps Reviews Scraper with the Scrapely Python SDK (scrapely-client-python).

Install: pip install scrapely-client-python
Run:     SCRAPELY_TOKEN=your_token python example.py
"""
import json
import os

from scrapely_client import ScrapelyClient


def main() -> None:
    client = ScrapelyClient(os.environ['SCRAPELY_TOKEN'])

    run_input = {
        "startUrls": [
            {
                "url": "https://www.google.com/maps/place/Eiffel+Tower/@48.8583701,2.2944813,17z/data=!3m1!4b1!4m6!3m5!1s0x47e66e2964e34e2d:0x8ddca9ee380ef7e0!8m2!3d48.8583701!4d2.2944813"
            }
        ],
        "maxPlacesPerSearch": 20,
        "maxReviews": 10,
        "reviewsSort": "mostRelevant",
        "language": "en",
        "personalData": True,
        "proxyConfiguration": {
            "useScrapelyProxy": True,
            "scrapelyProxyGroups": [
                "DATACENTER"
            ]
        }
    }

    # Start the scraper on Scrapely and wait for it to finish.
    run = client.actor('cornerledger/google-maps-reviews-scraper').call(run_input=run_input)
    if run is None:
        raise RuntimeError('Run was not found')

    # Read the scraped results from the run's dataset.
    items = list(client.dataset(run.default_dataset_id).iterate_items())
    print(f'Scraped {len(items)} results')
    print(json.dumps(items, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
