import json

file_path = "c:\\Users\\Enes\\Desktop\\Yeni klasör\\emotion_data.json"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    print(f"{'Duygu':<15} | {'Sayı':<10}")
    print("-" * 30)
    total_count = 0
    for emotion, items in data.items():
        count = len(items)
        total_count += count
        print(f"{emotion:<15} | {count:<10}")
    print("-" * 30)
    print(f"{'TOPLAM':<15} | {total_count:<10}")

except Exception as e:
    print(f"Hata: {e}")
