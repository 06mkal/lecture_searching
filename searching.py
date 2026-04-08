from dataclasses import field
from pathlib import Path
import json
from generators import unordered_sequence
import time

def read_data(file_name, field):
    with open (file_name, "r") as file_obj:
        data = json.load(file_obj)

    if field in data:
        return data[field]
    else:
        return None

    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name


def linear_search(sekvence, number):
    result = {}
    pozice = []

    for i, hodnota in enumerate(sekvence):
        if hodnota == number:
            pozice.append(i)

    result["positions"] = pozice
    result["count"] = sekvence.count(number)
    print(result)



def binary_search(sekvence, number):
    delka_sekvence = len(sekvence)
    left = 0
    right = delka_sekvence - 1
    while left <= right:
        middle = (left + right) // 2
        if sekvence[middle] == number:
            return middle
        elif number > sekvence[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return None


def pattern_search(sekvence, vzor):
    delka_vzoru = len(vzor)




def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

    start = time.perf_counter()
    linear_search(sequential_data, 0)
    end = time.perf_counter()
    duration = end - start
    print(duration)


    sekvence = read_data("sequential.json", "ordered_numbers")
    start = time.perf_counter()
    vysledek = binary_search(sekvence, 70)
    end = time.perf_counter()
    duration = end - start
    print(duration)
    print(vysledek)




if __name__ == "__main__":
    main()
