import requests
from bs4 import BeautifulSoup

URL = "https://hdmn.cloud/en/demo/success"
EMAIL = "hatgpt575@gmail.com"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
})

resp = session.post(
    URL,
    data={"demo_mail": EMAIL},
    allow_redirects=True,
    timeout=15,
)
resp.raise_for_status()

# сохранить сырой ответ
with open("response.html", "w", encoding="utf-8") as f:
    f.write(resp.text)

# извлечь видимый текст
soup = BeautifulSoup(resp.text, "html.parser")
for tag in soup(["script", "style", "noscript"]):
    tag.decompose()

text = "\n".join(
    line.strip() for line in soup.get_text("\n").splitlines() if line.strip()
)

with open("response.txt", "w", encoding="utf-8") as f:
    f.write(text)

print(text)
