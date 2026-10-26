"""Build the skills-only PMP Coach ZIP. Python 3.10+, standard library only."""
import hashlib
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
# Explicit allowlist: never ship learner data, evals, Git state, or build helpers.
FILES = (
    "plugin.json",
    "LICENSE",
    "skills/explain-pmp-questions/SKILL.md",
    "skills/explain-pmp-questions/agents/openai.yaml",
    "skills/explain-pmp-questions/references/pmp-exam-content-outline.md",
    "skills/explain-pmp-questions/references/pmp-principles.md",
)


def build():
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    if manifest.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        raise ValueError("Unexpected plugin schema")
    if manifest.get("name") != "pmp-coach":
        raise ValueError("Unexpected plugin name")
    version = manifest.get("version", "")
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
        raise ValueError("Expected a numeric major.minor.patch version")
    if not manifest.get("description"):
        raise ValueError("Missing description")
    payload = {}
    for name in FILES:
        path = ROOT / name
        if path.is_symlink() or not path.resolve().is_relative_to(ROOT):
            raise ValueError(f"File must stay inside repository: {name}")
        data = path.read_bytes()
        if not data or not data.decode("utf-8").strip():
            raise ValueError(f"Empty UTF-8 file: {name}")
        payload[name] = data
    skill_name = "skills/explain-pmp-questions/SKILL.md"
    skill = payload[skill_name].decode("utf-8")
    frontmatter = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", skill, re.S)
    if not frontmatter:
        raise ValueError("Missing skill frontmatter")
    for field in ("name", "description"):
        if not re.search(rf"^{field}:\s*\S.+$", frontmatter[1], re.M):
            raise ValueError(f"Missing skill {field}")
    if not re.search(r"^name: explain-pmp-questions$", frontmatter[1], re.M):
        raise ValueError("Skill name and directory differ")
    for target in re.findall(r"\]\((references/[^)#]+)(?:#[^)]*)?\)", skill):
        if f"skills/explain-pmp-questions/{target}" not in payload:
            raise ValueError(f"Unbundled reference: {target}")
    output = ROOT / "dist" / f"pmp-coach-{version}.zip"
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w") as archive:
        for name, data in sorted(payload.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    with zipfile.ZipFile(output) as archive:
        if archive.testzip() or set(archive.namelist()) != set(FILES):
            raise ValueError("Archive validation failed")
        for name, data in payload.items():
            if archive.read(name) != data:
                raise ValueError(f"Archive content differs: {name}")
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    print(f"Built {output.name}: {len(payload)} files, {output.stat().st_size} bytes")
    print(f"SHA256 {digest}")
    print("Local structure checks passed; portal validation and installation are separate.")
    return output


if __name__ == "__main__":
    build()
