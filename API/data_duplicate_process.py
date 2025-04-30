import pandas as pd

def remove_duplicate_words(text):
    words = text.split()
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return ' '.join(result)

def remove_repeated_suffix(text):
    # 뒤에서부터 앞부분과 같은 부분이 있으면 한 번만 남김
    for i in range(1, len(text)//2 + 1):
        if text.endswith(text[:i]) and len(text) > i:
            return text[:-i]
    return text

df = pd.read_csv('food_modified.csv')
df['식품명'] = df['식품명'].apply(remove_duplicate_words).apply(remove_repeated_suffix)
df.to_csv('food_final.csv', index=False)
