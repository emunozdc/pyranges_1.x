from typing import cast

import numpy as np
import pandas as pd
from sorted_nearest import maketiles, makewindows  # type: ignore[import-untyped]

from pyranges.names import END_COL, START_COL, TEMP_END_COL, TEMP_START_COL, RangeFrameType


def _windows(
    df: "RangeFrame",
    *,
    window_size: int,
    **_,
) -> "RangeFrame":
    idxs, starts, ends = makewindows(
        df.index.values,
        df.Start.values,
        df.End.values,
        window_size,
    )

    _df = df.reindex(idxs)
    _df.loc[:, START_COL] = starts
    _df.loc[:, END_COL] = ends

    return _df


def _tiles(
    df: "RangeFrame",
    *,
    tile_size: int,
    overlap_column: str | None,
    **_,
) -> "RangeFrame":
    if overlap_column is not None:
        df = df.copy()
        df.insert(df.shape[1], TEMP_START_COL, df.Start)
        df.insert(df.shape[1], TEMP_END_COL, df.End)

    idxs, starts, ends = maketiles(
        df.index.values,
        df.Start.values,
        df.End.values,
        tile_size,
    )

    _df = df.reindex(idxs)
    _df.loc[:, START_COL] = starts
    _df.loc[:, END_COL] = ends

    if overlap_column is not None:
        overlap = np.minimum(_df.End, _df[TEMP_END_COL]) - np.maximum(_df.Start, _df[TEMP_START_COL])
        _df.insert(_df.shape[1], overlap_column, overlap)
        _df = _df.drop_and_return([TEMP_START_COL, TEMP_END_COL], axis=1)

    return _df
