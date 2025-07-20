import os
import json
import tempfile
import pytest
from merge_script import merge_directory

def create_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f)

def test_merge_directory_json(tmp_path):
    d = tmp_path / "data"
    d.mkdir()
    
    # Создаём два JSON-файла
    create_json(d / "a.json", {"x": 1, "z": 3})
    create_json(d / "b.json", {"y": 2, "z": 4})
    
    result = merge_directory(str(d))
    assert result["x"] == 1
    assert result["y"] == 2
    assert "z" in result and result["z"] == 3

def test_merge_empty_directory():
    temp_dir = tempfile.mkdtemp()
    result = merge_directory(temp_dir)
    assert result == {}

def test_merge_directory_with_error():
    temp_dir = tempfile.mkdtemp()
    create_json(temp_dir / "a.json", {"x": 1})
    # Создаём директорию с недопустимыми файлами
    os.makedirs(temp_dir / "invalid")
    with pytest.raises(Exception):
        merge_directory(temp_dir)

def test_merge_directory_with_non_json_files(tmp_path):
    d = tmp_path / "data"
    d.mkdir()
    create_json(d / "a.json", {"x": 1})
    create_text_file(d / "b.txt", "some text")
    
    with pytest.raises(Exception):
        merge_directory(str(d))

def create_text_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
