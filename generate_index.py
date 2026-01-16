import os

ROOT_DIR = "Html"
OUTPUT_FILE = "index.html"

def main():
    files = []

    for root, _, filenames in os.walk(ROOT_DIR):
        for name in filenames:
            if not name.lower().endswith(".html"):
                continue
            path = os.path.join(root, name).replace("\\", "/")
            files.append(path)

    files.sort()

    html = [
        "<!DOCTYPE html>",
        "<html>",
        "<head>",
        "<meta charset='utf-8'>",
        "<title>HTML Index</title>",
        "<style>",
        "body{background:#000;color:#e0e0e0;font-family:monospace}",
        "h1{color:#6cf}",
        "a{color:#9cf;text-decoration:none}",
        "a:hover{text-decoration:underline}",
        "</style>",
        "</head>",
        "<body>",
        "<h1>Index</h1>",
        "<ul>"
    ]

    for f in files:
        html.append(f"<li><a href='{f}'>{f}</a></li>")

    html += [
        "</ul>",
        "</body>",
        "</html>"
    ]

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("\n".join(html))

if __name__ == "__main__":
    main()
