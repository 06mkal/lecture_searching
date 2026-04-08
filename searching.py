from dataclasses import field
from pathlib import Path
import json


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
        middle = delka_sekvence // 2
        if sekvence[middle] == number:
            return middle
        elif number > sekvence[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return None



def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

    linear_search(sequential_data, 0)

    sekvence = read_data("sequential.json", "ordered_numbers")
    vysledek = binary_search(sekvence, 72)
    print(vysledek)




if __name__ == "__main__":
    main()
