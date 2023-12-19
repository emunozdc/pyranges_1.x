from typing import TYPE_CHECKING

import pandas.core.groupby  # type: ignore[name-defined]

from pyranges.names import return_pyranges_if_possible

if TYPE_CHECKING:
    import pandas as pd

    import pyranges as pr


class PyRangesDataFrameGroupBy(pandas.core.groupby.DataFrameGroupBy):

    def __init__(self, pandas_groupby):
        self._pandas_groupby = pandas_groupby

    def __getattr__(self, item):
        # Handle attribute access, e.g., g.some_method()
        if item in (pd_grpby := self.__dict__["_pandas_groupby"]).__dict__:
            attr = getattr(pd_grpby, item)
            if callable(attr):
                def wrapper(*args, **kwargs):
                    result = attr(*args, **kwargs)
                    return return_pyranges_if_possible(result)

                return wrapper
            else:
                return attr

    def __getitem__(self, key):
        # Handle item access, e.g., g['column_name']
        result = self._pandas_groupby[key]
        return return_pyranges_if_possible(result)

    @return_pyranges_if_possible
    def agg(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().agg(*args, **kwargs)

    @return_pyranges_if_possible
    def aggregate(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().aggregate(*args, **kwargs)

    @return_pyranges_if_possible
    def all(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: A003, D102
        return super().all(*args, **kwargs)

    @return_pyranges_if_possible
    def any(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: A003, D102
        return super().any(*args, **kwargs)

    @return_pyranges_if_possible
    def apply(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().apply(*args, **kwargs)

    @return_pyranges_if_possible
    def bfill(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().bfill(*args, **kwargs)

    @return_pyranges_if_possible
    def cumcount(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().cumcount(*args, **kwargs)

    @return_pyranges_if_possible
    def cummax(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().cummax(*args, **kwargs)

    @return_pyranges_if_possible
    def cummin(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().cummin(*args, **kwargs)

    @return_pyranges_if_possible
    def cumprod(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().cumprod(*args, **kwargs)

    @return_pyranges_if_possible
    def cumsum(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().cumsum(*args, **kwargs)

    @return_pyranges_if_possible
    def describe(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().describe(*args, **kwargs)

    @return_pyranges_if_possible
    def diff(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().diff(*args, **kwargs)

    @return_pyranges_if_possible
    def ewm(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().ewm(*args, **kwargs)

    @return_pyranges_if_possible
    def expanding(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().expanding(*args, **kwargs)

    @return_pyranges_if_possible
    def ffill(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().ffill(*args, **kwargs)

    @return_pyranges_if_possible
    def fillna(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().fillna(*args, **kwargs)

    @return_pyranges_if_possible
    def filter(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: A003, D102
        return super().filter(*args, **kwargs)

    @return_pyranges_if_possible
    def first(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().first(*args, **kwargs)

    @return_pyranges_if_possible
    def get_group(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().get_group(*args, **kwargs)

    @return_pyranges_if_possible
    def head(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().head(*args, **kwargs)

    @return_pyranges_if_possible
    def idxmax(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().idxmax(*args, **kwargs)

    @return_pyranges_if_possible
    def idxmin(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().idxmin(*args, **kwargs)

    @return_pyranges_if_possible
    def last(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().last(*args, **kwargs)

    @return_pyranges_if_possible
    def max(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: A003, D102
        return super().max(*args, **kwargs)

    @return_pyranges_if_possible
    def mean(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().mean(*args, **kwargs)

    @return_pyranges_if_possible
    def median(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().median(*args, **kwargs)

    @return_pyranges_if_possible
    def min(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: A003, D102
        return super().min(*args, **kwargs)

    @return_pyranges_if_possible
    def ngroup(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().ngroup(*args, **kwargs)

    @return_pyranges_if_possible
    def nunique(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().nunique(*args, **kwargs)

    @return_pyranges_if_possible
    def ohlc(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().ohlc(*args, **kwargs)

    @return_pyranges_if_possible
    def pct_change(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().pct_change(*args, **kwargs)

    @return_pyranges_if_possible
    def pipe(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().pipe(*args, **kwargs)

    @return_pyranges_if_possible
    def prod(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().prod(*args, **kwargs)

    @return_pyranges_if_possible
    def quantile(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().quantile(*args, **kwargs)

    @return_pyranges_if_possible
    def rank(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().rank(*args, **kwargs)

    @return_pyranges_if_possible
    def resample(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().resample(*args, **kwargs)

    @return_pyranges_if_possible
    def rolling(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().rolling(*args, **kwargs)

    @return_pyranges_if_possible
    def sample(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().sample(*args, **kwargs)

    @return_pyranges_if_possible
    def sem(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().sem(*args, **kwargs)

    @return_pyranges_if_possible
    def shift(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().shift(*args, **kwargs)

    @return_pyranges_if_possible
    def size(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().size(*args, **kwargs)

    @return_pyranges_if_possible
    def skew(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().skew(*args, **kwargs)

    @return_pyranges_if_possible
    def std(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().std(*args, **kwargs)

    @return_pyranges_if_possible
    def sum(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: A003, D102
        return super().sum(*args, **kwargs)

    @return_pyranges_if_possible
    def tail(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().tail(*args, **kwargs)

    @return_pyranges_if_possible
    def take(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().take(*args, **kwargs)

    @return_pyranges_if_possible
    def transform(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().transform(*args, **kwargs)

    @return_pyranges_if_possible
    def value_counts(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().value_counts(*args, **kwargs)

    @return_pyranges_if_possible
    def var(self, *args, **kwargs) -> "pr.PyRanges | pd.DataFrame | pd.Series":  # noqa: D102
        return super().var(*args, **kwargs)
