import csv
from pathlib import Path

FILE_PATH = "MOCK_DATA.csv"

def parse_csv():
	"""Parse the CSV into a list of dictionaries keyed by its headers."""
	with Path(FILE_PATH).open(newline="", encoding="utf-8") as csv_file:
		return list(csv.DictReader(csv_file))
