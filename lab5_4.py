import json

def read_json(filename="people.json"):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def main():
    data = read_json()
    print("Записи з файлу people.json:")
    for surname, info in data.items():
        name, patronymic, year = info
        print(f"{surname} — {name} {patronymic}, рік народження: {year}")

if __name__ == "__main__":
    main()