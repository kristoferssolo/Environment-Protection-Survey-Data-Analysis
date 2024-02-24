from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import matplotlib.pyplot as plt
import pandas as pd


@dataclass
class Combination:
    q1: str
    q2: str


def draw(
    df: pd.DataFrame,
    comb: Combination,
    /,
    show: bool = False,
    filename: Optional[Path] = None,
) -> None:
    chart = pd.crosstab(df[comb.q1], df[comb.q2])
    chart.plot(kind="bar")
    plt.figure(figsize=(16, 9))
    plt.title(comb.q1)
    plt.xlabel("")
    plt.ylabel("")

    if filename:
        plt.savefig(filename)

    if show:
        plt.show()
