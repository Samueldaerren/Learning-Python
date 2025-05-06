from datetime import datetime

class Note:
    def __init__(self, title: str, content: str, category: str, date: str = None):
        self.title = title
        self.content = content
        self.category = category
        self.date = date or datetime.now().strftime('%Y-%m-%d')

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "category": self.category,
            "date": self.date
        }

    def __str__(self):
        return f"[{self.date}] {self.title} - {self.category}"

    def __eq__(self, other):
        return self.date == other.date

    def __lt__(self, other):
        return self.date < other.date


class ReminderNote(Note):
    def __init__(self, title, content, category, date, remind_at: str):
        super().__init__(title, content, category, date)
        self.remind_at = remind_at

    def to_dict(self):
        data = super().to_dict()
        data["remind_at"] = self.remind_at
        return data
