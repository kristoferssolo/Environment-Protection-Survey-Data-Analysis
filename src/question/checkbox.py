from pathlib import Path
from typing import Optional

import matplotlib.pyplot as plt
import pandas as pd


def draw(
    df: Optional[pd.DataFrame] = None,
    /,
    question: Optional[str] = None,
    show: bool = False,
    filename: Optional[Path] = None,
) -> None:
    if df is None or question is None:
        return

    data: pd.DataFrame = df[question].str.split(";").explode()
    answer_count = data.value_counts().sort_values(ascending=True)

    plt.figure(figsize=(16, 9))
    plt.subplots_adjust(left=0.25)

    tick_len = 30
    for i, (answer, count) in enumerate(answer_count.items()):
        if len(answer) > tick_len:
            half_line_len = len(answer) // 2
            answer = "\n".join([answer[:half_line_len], answer[half_line_len:]])
        plt.barh(answer, count, label=answer, color="teal")

    plt.title(question)
    plt.xlabel("Skaits")
    plt.ylabel("")

    if filename:
        plt.savefig(filename)

    if show:
        plt.show()
