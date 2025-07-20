import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import pytest
from mnemosphere_merge import load_and_merge_csv

def test_load_and_merge_csv(tmp_path):
    df1 = pd.DataFrame({"a": [1,2]})
    df2 = pd.DataFrame({"a": [3,4]})
    f1 = tmp_path / "1.csv"; df1.to_csv(f1, index=False)
    f2 = tmp_path / "2.csv"; df2.to_csv(f2, index=False)
    merged = load_and_merge_csv(str(tmp_path))
    assert list(merged["a"]) == [1,2,3,4]
