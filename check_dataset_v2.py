import json

file_path = "c:\\Users\\Enes\\Desktop\\Yeni klasör\\emotion_data.json"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    print(f"{'Duygu':<15} | {'Sayı':<10}")
    print("-" * 30)
    
    counts = {}
    for item in data:
        label = item.get("label")
        counts[label] = counts.get(label, 0) + 1
        
    total_count = 0
    for emotion, count in counts.items():
        total_count += count
        print(f"{emotion:<15} | {count:<10}")
    print("-" * 30)
    print(f"{'TOPLAM':<15} | {total_count:<10}")
    
    # Show a few examples
    print("\nÖrnekler:")
    for i in range(5):
        print(data[i])

except Exception as e:
    print(f"Hata: {e}")
