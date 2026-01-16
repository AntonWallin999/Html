import os

ROOT_DIR = "Html"
OUTPUT_FILE = os.path.join(ROOT_DIR, "index.html")

def main():
    if not os.path.isdir(ROOT_DIR):
        os.makedirs(ROOT_DIR, exist_ok=True)

    files = []

    for root, _, filenames in os.walk(ROOT_DIR):
        for name in filenames:
            if not name.lower().endswith(".html"):
                continue
            if name.lower() == "index.html":
                continue

            full_path = os.path.join(root, name)
            rel = os.path.relpath(full_path, ROOT_DIR).replace("\\", "/")
            files.append(rel)

    files.sort()

    html = [
        "<!DOCTYPE html>",
        "<html>",
        "<head>",
        "<meta charset='utf-8'>",
        "<title>HTML-index</title>",
        "<style>",
        "body{background:#000;color:#e0e0e0;font-family:monospace;padding:16px}",
        "h1{color:#6cf;margin-bottom:12px}",
        "ul{list-style:none;padding:0}",
        "li{margin:6px 0}",
        "a{color:#9cf;text-decoration:none}",
        "a:hover{text-decoration:underline}",
        "</style>",
        "</head>",
        "<body>",
        "<h1>Index</h1>",
        "<ul>"
    ]

    if not files:
        html.append("<li>(inga HTML-filer i Html/ ännu)</li>")
    else:
        for f in files:
            html.append("<li><a href='" + f + "'>" + f + "</a></li>")

    html += ["</ul>", "</body>", "</html>"]

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("\n".join(html))

if __name__ == "__main__":
    main()
