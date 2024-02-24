#!/usr/bin/env python
from pathlib import Path
from typing import Optional

import matplotlib.pyplot as plt
import pandas as pd
from question import checkbox

BASE_DIR = Path(__file__).resolve().parent.parent
FILE_PATH = BASE_DIR / "data" / "responses.csv"
EXPORT_DIR = BASE_DIR / "export"


def read_data(filename: Path) -> pd.DataFrame:
    return pd.read_csv(filename)


QUESTIONS = {
    "b": "Es plānoju samazināt pārtikas atkritumus mājsaimniecībā",
    "c": "Kādā veidā Jūs samaziniet savu atkritumu daudzumu?",
    "d": "Ražotu dzērienu vietā (limonādes, ūdens pudelēs, alkoholiskie dzērieni) es dzeršu krāna ūdeni.",
    "e": "Kāda ir Jūsu uztura izvēle?",
    "f": "Kuras no sekojošām rīcībām Jūs būtu gatavi veikt?",
    "h": "Kāda veida transportlīdzekļus Jūs izmantojat?",
    "i": "Ja esat automašīnas īpašnieks, kuru no minētajām iespējām Jūs izvēlētos, lai būtu videi draudzīgāks?",
    "k": "Kurš no sekojošiem apgalvojumiem Jums ir tuvāks?",
    "l": "Kuras no sekojošām darbībām Jūs pārsvarā veicat ar informācijas un komunikācijas tehnoloģiju (IKT) ierīcēm (telefona, datora, televizora u.c.) un to lietošanu?",
    "m": "Kādas darbības Jūs mēģinat veikt, lai samazinātu enerģijas patēriņu?",
    "o": "Kādā mājokļa tipā Jūs dzīvojat?",
    "q": "Vai Jūs atteiktos no liekas mājokļa platības?",
    "s": "Vai Jūsu dzīvesvieta ir papildus nosiltināta?",
    "u": "Kurš no apgalvojumiem atbilst Jūsu dzīves situācijai?",
    "v": "Kurš no šiem apgalvojumiem ir patiess par Jūsu mājdzīvniekiem?",
    "w": "Kurš no apgalvojumiem par pārvietošanos brīvdienās un atvaļinājumos Jums ir patiess?",
    "y": "Kurš no šiem apgalvojumiem par apģērbu un apavu iegādi attiecas uz Jums?",
    "z": "Kurš no apgalvojumiem par Jums ir patiess?",
}


def individual_charts(data: pd.DataFrame) -> None:
    for column, question in QUESTIONS.items():
        checkbox.draw(data, question=question, filename=EXPORT_DIR / "individual" / f"{column}.png")


def main() -> None:
    data = read_data(FILE_PATH)
    individual_charts(data)


if __name__ == "__main__":
    main()
