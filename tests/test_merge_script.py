import sys, os
sys.path.insert(0, os.path.abspath(os.getcwd()))

import json
import pytest
from merge_script import merge_directory

def create_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f)

def test_merge_directory_json(tmp_path):
    d = tmp_path / "data"
    d.mkdir()
    create_json(d / "a.json", {"x": 1})
    create_json(d / "b.json", {"y": 2})
    result = merge_directory(str(d))
    assert result["x"] == 1
    assert result["y"] == 2
