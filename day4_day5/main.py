import argparse
from notes import Note
from utils import load_notes, save_notes, show_notes, filter_by_category, get_stats

def add_note_from_args(args):
    note = Note(args.title, args.content, args.category)
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print(f"✅ Catatan '{args.title}' berhasil ditambahkan.")

def main():
    parser = argparse.ArgumentParser(description="📒 Manajemen Catatan Harian")
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Tambah catatan')
    add_parser.add_argument('--title', required=True)
    add_parser.add_argument('--content', required=True)
    add_parser.add_argument('--category', required=True)

    subparsers.add_parser('list', help='Tampilkan semua catatan')
    filter_parser = subparsers.add_parser('filter', help='Filter berdasarkan kategori')
    filter_parser.add_argument('--category', required=True)

    subparsers.add_parser('stats', help='Tampilkan statistik catatan')

    args = parser.parse_args()
    notes = load_notes()

    if args.command == 'add':
        add_note_from_args(args)
    elif args.command == 'list':
        show_notes(notes)
    elif args.command == 'filter':
        filtered = filter_by_category(notes, args.category)
        show_notes(filtered)
    elif args.command == 'stats':
        get_stats(notes)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
