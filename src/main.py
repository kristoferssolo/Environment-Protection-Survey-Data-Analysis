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


def main() -> None:
    data = read_data(FILE_PATH)
    checkbox.draw(
        data, question="Kādā veidā Jūs samaziniet savu atkritumu daudzumu?", show=True, filename=EXPORT_DIR / "c.png"
    )


if __name__ == "__main__":
    main()
