import os
import shutil
import platform
from file_menedger import (
    create_folder, delete_file_or_folder, copy_file_or_folder,
    view_os_info, view_creator_info, view_folders, view_files
)


# --------- Тесты для чистых функций ---------

def test_view_os_info(capsys):
    view_os_info()
    captured = capsys.readouterr()
    assert platform.uname().system in captured.out


def test_view_creator_info(capsys):
    view_creator_info()
    captured = capsys.readouterr()
    assert "Создатель программы: Евгений" in captured.out


def test_view_folders(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(os, 'listdir', lambda: ['folder1', 'folder2', 'file.txt'])
        captured_folders = []
        m.setattr(os.path, 'isdir', lambda x: x.startswith('folder'))
        view_folders()
        assert captured_folders == ['folder1', 'folder2']


def test_view_files(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(os, 'listdir', lambda: ['folder1', 'folder2', 'file.txt'])
        captured_files = []
        m.setattr(os.path, 'isfile', lambda x: x.endswith('.txt'))
        view_files()
        assert captured_files == ['file.txt']


# --------- Тесты для грязных функций ---------

def test_create_folder(monkeypatch):
    folder_name = "test_folder"
    monkeypatch.setattr('builtins.input', lambda _: folder_name)
    if os.path.exists(folder_name):
        os.rmdir(folder_name)

    create_folder()
    assert os.path.exists(folder_name)
    os.rmdir(folder_name)  # Очистка после теста


def test_delete_file(monkeypatch):
    file_name = "test_file.txt"
    with open(file_name, "w") as f:
        f.write("Test content")

    monkeypatch.setattr('builtins.input', lambda _: file_name)
    delete_file_or_folder()
    assert not os.path.exists(file_name)


def test_delete_folder(monkeypatch):
    folder_name = "test_folder"
    os.makedirs(folder_name)

    monkeypatch.setattr('builtins.input', lambda _: folder_name)
    delete_file_or_folder()
    assert not os.path.exists(folder_name)


def test_copy_file(monkeypatch):
    src = "test_file.txt"
    dest = "test_copy.txt"
    with open(src, "w") as f:
        f.write("Test content")

    monkeypatch.setattr('builtins.input', lambda prompt: src if 'копирования' in prompt else dest)
    copy_file_or_folder()
    assert os.path.exists(dest)

    os.remove(src)
    os.remove(dest)


def test_copy_folder(monkeypatch):
    src = "test_folder"
    dest = "test_copy_folder"
    os.makedirs(src)

    monkeypatch.setattr('builtins.input', lambda prompt: src if 'копирования' in prompt else dest)
    copy_file_or_folder()
    assert os.path.exists(dest)

    shutil.rmtree(src)
    shutil.rmtree(dest)
