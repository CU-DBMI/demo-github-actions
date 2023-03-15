"""
Demonstrational tests for demo-github actions
"""

import pandas as pd
from python_app.main import df


def test_df():
    """
    Tests that main.py's 'df' is a Pandas DataFrame
    """

    assert isinstance(df, pd.DataFrame)
