import datetime
import requests

from urllib.parse import urljoin


class STACProbe:
    _root_url: str
    _collection: str
    _threshold_ok: int
    _threshold_warn: int

    def __init__(
            self,
            root_url: str = None, collection: str = None,
            threshold_ok: int = 24, threshold_warn: int = 168
    ):
        if root_url is not None:
            self._root_url = root_url
        else:
            self._root_url = "https://stac.cesnet.cz"

        if collection is None:
            raise Exception("STAC collection is required!")
        else:
            self._collection = collection

        self._threshold_ok = threshold_ok
        self._threshold_warn = threshold_warn

    def check_last_entry_date(self) -> tuple[int, str]:
        collection_url = urljoin(self._root_url, f"collections/{self._collection}")

        response = requests.get(collection_url)

        if response.status_code != 200:
            if response.status_code == 404:
                return 3, f"Collection {self._collection} not found!"
            else:
                return 3, f"STAC Server {self._root_url} responds unexpectedly! Code HTTP/{response.status_code}."

        json_dict = response.json()

        max_date = json_dict['summaries']['datetime']['maximum']
        last_entry_date = datetime.datetime.strptime(max_date, "%Y-%m-%dT%H:%M:%S.%fZ").date()
        yesterday = datetime.date.today() - datetime.timedelta(hours=self._threshold_ok)
        if last_entry_date >= yesterday:
            return 0, f"The last entry in collection {self._collection} is from {last_entry_date}."

        last_week = datetime.date.today() - datetime.timedelta(hours=self._threshold_warn)
        if last_entry_date >= last_week:
            return 1, (f"The last entry in collection {self._collection} is from {last_entry_date}. "
                       f"OK threshold: {self._threshold_ok} hours.")

        return 2, (f"The last entry in collection {self._collection} is from {last_entry_date}. "
                   f"WARN threshold: {self._threshold_warn} hours.")
