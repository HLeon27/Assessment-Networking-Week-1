"""Functions that interact with the Postcode API."""

import requests as req
import os
import json

CACHE_FILE = "./postcode_cache.json"


def load_cache() -> dict:
    """Loads the cache from a file and converts it from JSON to a dictionary."""
    # This function is used in Task 3, you can ignore it for now.
    ...


def save_cache(cache: dict):
    """Saves the cache to a file as JSON"""
    # This function is used in Task 3, you can ignore it for now.
    ...


def validate_postcode(postcode: str) -> bool:
    """Function validates postcode passed in as an argument."""
    if not isinstance(postcode, str):
        raise TypeError("Function expects a string.")
    BASE_URL = "https://api.postcodes.io/postcodes/"
    response = req.get(f"{BASE_URL}{postcode}/validate")
    if response.status_code == 500:
        raise req.RequestException("Unable to access API.")
    data = response.json()
    return data["result"]


def get_postcode_for_location(lat: float, long: float) -> str:
    """Function returns the postcode as a str for a given location"""
    if not isinstance(lat, float) or not isinstance(long, float):
        raise TypeError("Function expects two floats.")
    BASE_URL = "https://api.postcodes.io/postcodes"
    query = {
        "lon": long,
        "lat": lat
    }
    response = req.get(BASE_URL, params=query)
    if response.status_code == 500:
        raise req.RequestException("Unable to access API.")
    data = response.json()
    if not data["result"]:
        raise ValueError("No relevant postcode found.")
    results = data['result']
    return results[0]['postcode']


def get_postcode_completions(postcode_start: str) -> list[str]:
    """Function returns a list of auto completed postcode strings."""
    if not isinstance(postcode_start, str):
        raise TypeError("Function expects a string.")
    BASE_URL = "https://api.postcodes.io/postcodes"
    response = req.get(f"{BASE_URL}/{postcode_start}/autocomplete")
    if response.status_code == 500:
        raise req.RequestException("Unable to access API.")
    data = response.json()
    return data['result']


def get_postcodes_details(postcodes: list[str]) -> dict:
    pass
