import os

EXCLUDE_DIRS = {".git", ".github", "__pycache__"}
EXCLUDE_FILES = {"index.html", "generate_index.py"}

def main():
    files = []

    for root, dirs, filenames in os.walk("."):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for name in filenames:
            if name in EXCLUDE_FILES:
                continue
            path = os.path.join(root, name).replace("./", "")
            files.append(path)

    files.sort()

    html = [
        "<!DOCTYPE html>",
        "<html>",
        "<head>",
        "<meta charset='utf-8'>",
        "<title>Repo Index</title>",
        "<style>",
        "body{background:#0b0b0b;color:#e0e0e0;font-family:monospace}",
        "a{color:#6cf;text-decoration:none}",
        "a:hover{text-decoration:underline}",
        "</style>",
        "</head>",
        "<body>",
        "<h1>Auto-index</h1>",
        "<ul>"
    ]

    for f in files:
        html.append(f"<li><a href='{f}'>{f}</a></li>")

    html += ["</ul>", "</body>", "</html>"]

    with open("index.html", "w", encoding="utf-8") as out:
        out.write("\n".join(html))

if __name__ == "__main__":
    main()
