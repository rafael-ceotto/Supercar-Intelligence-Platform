import csv
from typing import List, Dict

def load_csv(path: str) -> List[Dict[str, str]]:
    with open(path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]
