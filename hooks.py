import re
from pathlib import Path

SNIPPET_RE = re.compile(r'^--8<--\s+["\']([^"\']+)["\']\s*$', re.MULTILINE)
HEADING_RE = re.compile(r'^(#{1,5})(\s+.+)$', re.MULTILINE)


def _demote_headings(text):
    return HEADING_RE.sub(lambda match: "#" + match.group(1) + match.group(2), text)


def on_page_markdown(markdown, page, config, files):
    if not SNIPPET_RE.search(markdown):
        return markdown

    docs_dir = Path(config["docs_dir"]).resolve()
    project_dir = docs_dir.parent

    def replace(match):
        source = (project_dir / match.group(1)).resolve()
        try:
            source.relative_to(project_dir)
        except ValueError:
            return match.group(0)
        if not source.is_file():
            return match.group(0)
        return _demote_headings(source.read_text(encoding="utf-8").rstrip())

    return SNIPPET_RE.sub(replace, markdown)
