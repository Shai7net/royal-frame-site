from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []
        self.ids: list[str] = []
        self.has_title = False
        self.has_description = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.append(values["id"] or "")
        if tag in {"a", "link"} and values.get("href"):
            self.links.append(values["href"] or "")
        if tag in {"img", "script"} and values.get("src"):
            self.links.append(values["src"] or "")
        if tag == "title":
            self.has_title = True
        if tag == "meta" and values.get("name") == "description" and values.get("content"):
            self.has_description = True


def local_target(page: Path, link: str) -> Path | None:
    if not link or link.startswith(("#", "mailto:", "tel:")):
        return None
    parsed = urlsplit(link)
    if parsed.scheme or parsed.netloc:
        return None
    return (page.parent / parsed.path).resolve()


errors: list[str] = []
for page in sorted(ROOT.glob("*.html")):
    text = page.read_text(encoding="utf-8")
    parser = PageParser()
    parser.feed(text)
    if not parser.has_title:
        errors.append(f"{page.name}: missing title")
    if page.name != "404.html" and not parser.has_description:
        errors.append(f"{page.name}: missing meta description")
    if len(parser.ids) != len(set(parser.ids)):
        errors.append(f"{page.name}: duplicate id")
    if "[[" in text or "]]" in text:
        errors.append(f"{page.name}: unresolved placeholder")
    for link in parser.links:
        target = local_target(page, link)
        if target is not None and not target.exists():
            errors.append(f"{page.name}: missing local target {link}")

if errors:
    raise SystemExit("\n".join(errors))

print(f"PASS: {len(list(ROOT.glob('*.html')))} pages, local links, assets and placeholders")
