#!/usr/bin/env python
import itertools
from pathlib import Path
from typing import Optional

import matplotlib.pyplot as plt
import pandas as pd
from question import checkbox, correlation
from question.correlation import Combination

BASE_DIR = Path(__file__).resolve().parent.parent
FILE_PATH = BASE_DIR / "data" / "responses.csv"
EXPORT_DIR = BASE_DIR / "export"


def read_data(filename: Path) -> pd.DataFrame:
    return pd.read_csv(filename)


def individual_charts(data: pd.DataFrame) -> None:
    QUESTIONS: dict[str, str] = {
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
    export_path = EXPORT_DIR / "individual"

    if not export_path.exists():
        export_path.mkdir()

    for column, question in QUESTIONS.items():
        checkbox.draw(data, question=question, filename=export_path / f"{column}.png")


def create_combinations() -> dict[str, Combination]:
    QUESTIONS = {
        "Es plānoju samazināt pārtikas atkritumus mājsaimniecībā",
        "Kāda ir Jūsu uztura izvēle?",
        "Kurš no sekojošiem apgalvojumiem Jums ir tuvāks?",
        "Kādā mājokļa tipā Jūs dzīvojat?",
        "Vai Jūs atteiktos no liekas mājokļa platības?",
        "Vai Jūs būtu ar mieru dzīvot koplietojamā mājoklī?",
        "Vai Jūsu dzīvesvieta ir papildus nosiltināta?",
    }

    DEMOGRAPHIC = {
        "Kāds ir Jūsu dzimums?",
        "Kāds ir Jūsu vecums?",
        "Kāds ir augstākais Jūsu iegūtais izglītības līmenis?",
        # "Kurš no šiem variantiem atspoguļo Jūsu mājsaimniecības ikmēneša neto ienākumus?",
        "Kāds ir Jūsu pašreizējais nodarbinātības statuss?",
        "Kāda ir Jūsu dzīvesvieta?",
    }
    return {
        f"{i + 1}": Combination(str(pair[0]), str(pair[1]))
        for i, pair in enumerate(itertools.product(QUESTIONS, DEMOGRAPHIC))
    }


def correlation_charts(data: pd.DataFrame) -> None:
    export_path = EXPORT_DIR / "correlation"

    if not export_path.exists():
        export_path.mkdir()

    for filename, comb in create_combinations().items():
        correlation.draw(data, comb, filename=export_path / f"{filename}.png")


def main() -> None:
    data = read_data(FILE_PATH)
    individual_charts(data)
    correlation_charts(data)


if __name__ == "__main__":
    main()
