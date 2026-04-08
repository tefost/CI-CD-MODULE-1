import re

def count_sentences(text: str) -> int:
    if not text or not text.strip():
        return 0
    # Розділяємо по три крапки або по одному із знаків . ! ?
    sentences = re.split(r'\.\.\.|[.!?]', text)
    # Відфільтровуємо порожні рядки, які утворюються в кінці
    return len([s for s in sentences if s.strip()])