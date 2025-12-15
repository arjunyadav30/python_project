import requests
import os

def fetch_news(api_key, keyword="example", lang="en"):
    url = f"https://gnews.io/api/v4/search?q={keyword}&lang={lang}&country=in&max=50&apikey={api_key}"
    response = requests.get(url).json()
    return [
        f"{a['title']}\n{a['description']}\n{a['url']}\n"
        for a in response.get("articles", [])
    ]

def save_news(articles, filename="news.txt"):
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    file_path = os.path.join(downloads_path, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(("\n" + "-"*50 + "\n").join(articles))
    return file_path

def main():
    api_key = "9b957555f9381d94444ea468a1d311db"

    choice = input("Press 1 for Hindi news, 2 for English news: ")
    lang = "hi" if choice == "1" else "en"

    keyword = input("Enter a topic (default: example): ") or "example"

    print(f"Fetching {('Hindi' if lang=='hi' else 'English')} news about '{keyword}'...")
    articles = fetch_news(api_key, keyword, lang)

    if not articles:
        print("No articles found. Try another keyword.")
        return

    print("Saving news to Downloads folder...")
    file_path = save_news(articles)
    print(f"Done! Your news file is saved at:\n{file_path}")
main()