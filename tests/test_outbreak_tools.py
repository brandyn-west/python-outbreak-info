from outbreak_tools import outbreak_tools
import pytest
import pandas as pd

def _test_lookup_table():
    output = outbreak_tools.id_lookup([''], table=True)
    assert isinstance(output, pd.core.frame.DataFrame), 'When table is true should return dataframe'

def _test_uniqueness_analysis():
    output = outbreak_tools.uniqueness(
        ['S:E484K', 'S:DEL69/70'],
        'b.1.1.7'
    )
    assert type(output) == float
    assert 0.0 <= output <= 1.0

def test_id_lookup():
    _test_lookup_table()
    _test_uniqueness_analysis()