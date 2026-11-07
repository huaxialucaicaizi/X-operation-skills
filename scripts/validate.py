#!/usr/bin/env python3
"""Validate skill frontmatter, required files, relative Markdown links and README rules."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKILLS = {
    "podcast-teardown": "播客拆解",
    "growth-topics": "增长选题",
    "x-title": "标题",
    "longform-writing": "长文写作",
    "de-ai-tone": "去 AI 味",
    "cover-and-figures": "头图配图",
    "publish-engage": "发布互动",
    "data-review": "数据复盘",
    "x-growth": "X 涨粉",
}

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    ".gitignore",
    "shared/workflow.md",
    "shared/evidence-rules.md",
    "shared/templates/source-register.md",
    "shared/templates/evidence-card.md",
    "shared/templates/approval-log.md",
    "shared/templates/decision-library.md",
    "skills/longform-writing/templates/x-long-post.md",
    "skills/longform-writing/templates/x-article.md",
    "skills/de-ai-tone/references/banned-patterns.md",
    "skills/de-ai-tone/references/meaning-preservation.md",
    "skills/x-growth/templates/growth-config.example.md",
]

# Patterns that must not appear anywhere in tracked text files (except this script).
FORBIDDEN_ANYWHERE = {
    "X--operation-skills": "old repository name",
}

# Patterns that must not appear in README.md.
FORBIDDEN_IN_README = {
    "shields.io": "badge",
    "badgen.net": "badge",
    "star-history": "Star History",
    "Star History": "Star History",
}

LICENSE_MUST_CONTAIN = [
    "华夏路菜菜子",
    "@huaxialucaicaizi",
    "Skill 商店",
    "事先书面许可",
]

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_NAME_LEN = 64
MAX_DESCRIPTION_LEN = 1024
ALLOWED_KEYS = {"name", "description", "license", "metadata", "allowed-tools", "compatibility"}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".py", ".txt", ""}

errors = []


def rel(path):
    return path.relative_to(ROOT).as_posix()


def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{rel(path)}: must start with '---' frontmatter")
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        errors.append(f"{rel(path)}: frontmatter is not closed with '---'")
        return {}
    fields = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        if not sep or line[0].isspace():
            errors.append(f"{rel(path)}: unsupported frontmatter line: {line!r}")
            continue
        fields[key.strip()] = value.strip().strip("'\"")
    return fields


def check_skills():
    skills_dir = ROOT / "skills"
    found = {p.name for p in skills_dir.iterdir() if p.is_dir()} if skills_dir.is_dir() else set()
    for missing in sorted(set(SKILLS) - found):
        errors.append(f"missing skill directory: skills/{missing}")
    for extra in sorted(found - set(SKILLS)):
        errors.append(f"unexpected skill directory (add it to SKILLS in validate.py): skills/{extra}")

    for name in sorted(found & set(SKILLS)):
        base = skills_dir / name
        skill_md = base / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"skills/{name}: missing SKILL.md")
            continue
        fields = parse_frontmatter(skill_md)
        fm_name = fields.get("name", "")
        description = fields.get("description", "")
        if not fm_name:
            errors.append(f"skills/{name}/SKILL.md: missing 'name'")
        elif not NAME_RE.match(fm_name) or len(fm_name) > MAX_NAME_LEN:
            errors.append(f"skills/{name}/SKILL.md: invalid name {fm_name!r}")
        elif fm_name != name:
            errors.append(f"skills/{name}/SKILL.md: name {fm_name!r} must match directory {name!r}")
        if not description:
            errors.append(f"skills/{name}/SKILL.md: missing 'description'")
        elif len(description) > MAX_DESCRIPTION_LEN:
            errors.append(f"skills/{name}/SKILL.md: description is {len(description)} chars (> {MAX_DESCRIPTION_LEN})")
        unknown = set(fields) - ALLOWED_KEYS
        if unknown:
            errors.append(f"skills/{name}/SKILL.md: unexpected frontmatter keys: {sorted(unknown)}")
        for sub in ("references", "templates"):
            if not any((base / sub).glob("*.md")):
                errors.append(f"skills/{name}: {sub}/ must contain at least one .md file")


def check_required_files():
    for path_str in REQUIRED_FILES:
        path = ROOT / path_str
        if not path.is_file():
            errors.append(f"missing required file: {path_str}")
        elif not path.read_text(encoding="utf-8").strip():
            errors.append(f"required file is empty: {path_str}")


def iter_text_files():
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.suffix in TEXT_SUFFIXES:
            yield path


def check_relative_links():
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        for target in LINK_RE.findall(md.read_text(encoding="utf-8")):
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            file_part = target.split("#", 1)[0]
            if file_part and not (md.parent / file_part).exists():
                errors.append(f"{rel(md)}: broken link -> {target}")


def check_forbidden():
    this_script = Path(__file__).resolve()
    for path in iter_text_files():
        if path.resolve() == this_script:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for needle, why in FORBIDDEN_ANYWHERE.items():
            if needle in text:
                errors.append(f"{rel(path)}: contains {needle!r} ({why})")

    readme = ROOT / "README.md"
    if readme.is_file():
        text = readme.read_text(encoding="utf-8")
        for needle, why in FORBIDDEN_IN_README.items():
            if needle in text:
                errors.append(f"README.md: contains {needle!r} ({why} is not allowed)")
        for name, zh in SKILLS.items():
            entry = f"**[{name}](skills/{name}/SKILL.md) {zh}**"
            if entry not in text:
                errors.append(f"README.md: project map must contain {entry!r}")


def check_license():
    path = ROOT / "LICENSE"
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    for needle in LICENSE_MUST_CONTAIN:
        if needle not in text:
            errors.append(f"LICENSE: must contain {needle!r}")


def main():
    check_required_files()
    check_skills()
    check_relative_links()
    check_forbidden()
    check_license()
    if errors:
        for err in errors:
            print(f"ERROR: {err}")
        return 1
    print(
        f"OK: {len(SKILLS)} skills valid, {len(REQUIRED_FILES)} required files present, "
        "relative links resolve, README and LICENSE rules pass"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
