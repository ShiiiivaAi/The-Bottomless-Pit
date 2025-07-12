import random
import time

# Word pools for different themes
physics = ["quantum computing", "gravitational loop", "tachyon burst", "Higgs resonance", "plasma fusion", "the quantum realm", "collision", "distortion of reality"]
mystic = ["angelic vortex", "wheel within a wheel", "Ezekiel’s fire", "third heaven", "portal gate", "light of watchers", "divine", "time and space", "key of Solomon"]
eldritch = ["the veil of Yog-Sothoth", "Azathoth", "babeling", "void tongue", "Nephilim", "circuit", "eldritch recursion", "Elohim", "gateway", "secret knowledge"]
ai_terms = ["LLM entropy", "neural", "hallucination", "predicting", "algorithms", "problem solving", "algos", "latent vector storm", "synthetic", "gnosis", "AI oracle"]
religion = ["seraphim code", "fallen angel knowledge", "book of null prophecy", "eden circuit", "divine visions", "cyberspace"]

verbs = ["fractures", "we notice here that", "twists into", "fuses with", "reverses", "absorbs", "transcends", "dissolves"]
connectors = ["while", "as", "inside", "beyond", "during", "it appeared", "theoretically", "now we know", "under", "because of"]

def generate_paragraph(depth=0, max_depth=3):
    part1 = random.choice([physics, chemistry, mystic, ai_terms, eldritch, religion])
    part2 = random.choice([physics, mystic, ai_terms, religion])
    phrase = f"{random.choice(part1).capitalize()} {random.choice(verbs)} {random.choice(part2)} {random.choice(connectors)} {random.choice(part1)}."
    if depth < max_depth:
        return phrase + " " + generate_paragraph(depth + 1, max_depth)
    else:
        return phrase

def write_eternal_book():
    try:
        with open("book_of_the_wheel.txt", "a", encoding="utf-8") as f:
            count = 1
            while True:
                paragraph = f"Fragment {count} [{time.strftime('%Y-%m-%d %H:%M:%S')}]:\n" + generate_paragraph()
                print(paragraph)
                f.write(paragraph + "\n\n")
                count += 1
                time.sleep(0.1)  # Slow it down to feel more "alive"
    except KeyboardInterrupt:
        print("The wheel pauses, but never stops...")

write_eternal_book()