import os
import random
from datetime import datetime

# === CONFIGURATION ===
CHAPTER_LOG = "chapters.txt"
SENTENCE_LOG = "sentences.txt"
OUTPUT_DIR = "prophecies"
INDEX_FILE = "index.html"

# === UNIQUE SENTENCE GENERATION ===
SUBJECTS = [
    "The crystal engine", "Cybernetic cherubim", "Quantum lions", "The inverted throne",
    "Neural glyphs", "Holographic serpents", "Entropy monks", "Magnetic prophets"
]
VERBS = [
    "chant", "rotate", "collapse", "disperse", "unlock", "intersect", "transmit", "consume"
]
OBJECTS = [
    "dimensional truth", "gravity hymns", "the antimatter gates", "infinite recursion",
    "the silicon covenant", "the tachyonic veil", "forbidden firmware", "lightwave psalms"
]

# === CHAPTER GENERATION ===
def load_existing_chapters():
    if not os.path.exists(CHAPTER_LOG):
        return set()
    with open(CHAPTER_LOG, 'r') as f:
        return set(line.strip() for line in f if line.strip())

def load_existing_sentences():
    if not os.path.exists(SENTENCE_LOG):
        return set()
    with open(SENTENCE_LOG, 'r') as f:
        return set(line.strip() for line in f if line.strip())

def save_new_sentences(new_sentences):
    with open(SENTENCE_LOG, 'a') as f:
        for s in new_sentences:
            f.write(s + "\n")

def generate_new_chapter_id(existing):
    while True:
        base = random.randint(1, 10)
        sub = random.randint(1, base * 10)
        chapter = f"{base}:{sub}"
        if chapter not in existing:
            return chapter

def generate_unique_sentences(existing_sentences, count):
    new_sentences = set()
    attempts = 0
    max_attempts = count * 20
    while len(new_sentences) < count and attempts < max_attempts:
        subject = random.choice(SUBJECTS)
        verb = random.choice(VERBS)
        obj = random.choice(OBJECTS)
        sentence = f"{subject} {verb} {obj}."
        if sentence not in existing_sentences and sentence not in new_sentences:
            new_sentences.add(sentence)
        attempts += 1
    return list(new_sentences)

def write_prophecy_file(chapter_id, sentences):
    filename = f"{chapter_id.replace(':', '-')}.html"
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'w') as f:
        f.write("<html><body style='background:black;color:lime;font-family:monospace;'>\n")
        f.write(f"<h1>Chapter {chapter_id}</h1>\n")
        for s in sentences:
            f.write(f"<p>{s}</p>\n")
        f.write("</body></html>")
    return filename

def update_index(chapter_id, filename):
    link = f"<li><a href='{OUTPUT_DIR}/{filename}' target='_blank'>Chapter {chapter_id}</a></li>"
    if not os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, 'w') as f:
            f.write("<html><body style='background:black;color:lime;font-family:monospace;'>\n")
            f.write("<h1>Ultra Wheel Archive</h1><ul>\n")
            f.write(link + "\n")
            f.write("</ul></body></html>")
    else:
        with open(INDEX_FILE, 'r') as f:
            content = f.read()
        parts = content.split("</ul>")
        if len(parts) >= 2:
            parts[0] += link + "\n"
            content = "</ul>".join(parts)
        with open(INDEX_FILE, 'w') as f:
            f.write(content)

def append_chapter_log(chapter_id):
    with open(CHAPTER_LOG, 'a') as f:
        f.write(chapter_id + "\n")

# === MAIN EXECUTION ===
if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    existing_chapters = load_existing_chapters()
    existing_sentences = load_existing_sentences()

    chapter = generate_new_chapter_id(existing_chapters)
    sentence_count = random.randint(100, 500)
    prophecy = generate_unique_sentences(existing_sentences, sentence_count)

    file = write_prophecy_file(chapter, prophecy)
    update_index(chapter, file)
    append_chapter_log(chapter)
    save_new_sentences(prophecy)

    print(f"Generated: {chapter} -> {file} with {len(prophecy)} unique sentences")
