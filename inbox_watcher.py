"""
Inbox Watcher - Copies new files from Inbox to Needs_Action as markdown.
Usage: python inbox_watcher.py
"""

import time
import shutil
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

INBOX = Path(__file__).parent / "Inbox"
NEEDS_ACTION = Path(__file__).parent / "Needs_Action"


class InboxHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        src = Path(event.src_path)

        # Wait briefly for file to finish writing
        time.sleep(0.5)

        # Create markdown filename
        dest_name = src.stem + ".md"
        dest = NEEDS_ACTION / dest_name

        # Handle duplicates
        counter = 1
        while dest.exists():
            dest_name = f"{src.stem}_{counter}.md"
            dest = NEEDS_ACTION / dest_name
            counter += 1

        # Read source and write as markdown
        try:
            content = src.read_text(encoding="utf-8", errors="replace")
            dest.write_text(f"# {src.name}\n\n{content}", encoding="utf-8")
            print(f"[+] {src.name} -> {dest_name}")
        except Exception as e:
            print(f"[!] Error processing {src.name}: {e}")


if __name__ == "__main__":
    print(f"Watching: {INBOX}")
    print("Press Ctrl+C to stop\n")

    observer = Observer()
    observer.schedule(InboxHandler(), str(INBOX), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
