#!/usr/bin/env python3
"""Define a CSV serialization module"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV to JSON"""

    try:
        data_list = []
        with open(csv_filename, 'r', encoding="utf-8") as csv_file:
            read = csv.DictReader(csv_file)
            for row in read:
                data_list.append(row)

        with open("data.json", 'w', encoding="utf-8") as json_file:
            json.dump(data_list, json_file)

        return True

    except FileNotFoundError:
        return False
