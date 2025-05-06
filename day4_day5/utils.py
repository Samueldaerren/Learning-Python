import json
from functools import reduce
from tabulate import tabulate
from typing import List, Dict
from datetime import datetime
from notes import Note

def load_notes(file_path='data.json') -> List[Note]:
    try:
        with open(file_path, 'r') as f:
            raw = json.load(f)
            return [Note(**note) for note in raw]
    except FileNotFoundError:
        return []

def save_notes(notes: List[Note], file_path='data.json'):
    with open(file_path, 'w') as f:
        json.dump([note.to_dict() for note in notes], f, indent=4)

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"▶ Menjalankan fungsi: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def show_notes(notes: List[Note]):
    table = [[note.date, note.title, note.category] for note in notes]
    print(tabulate(table, headers=["Tanggal", "Judul", "Kategori"]))

@logger
def filter_by_category(notes: List[Note], category: str):
    return list(filter(lambda note: note.category.lower() == category.lower(), notes))

@logger
def get_stats(notes: List[Note]):
    total_notes = len(notes)
    total_words = reduce(lambda acc, n: acc + len(n.content.split()), notes, 0)
    categories = {}
    for note in notes:
        categories[note.category] = categories.get(note.category, 0) + 1

    print(f"\n📊 Statistik Catatan:")
    print(f"- Total Catatan: {total_notes}")
    print(f"- Total Kata: {total_words}")
    print("- Kategori:")
    for cat, count in categories.items():
        print(f"  - {cat}: {count} catatan")
