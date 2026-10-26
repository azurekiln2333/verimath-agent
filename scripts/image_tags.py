"""Validate a release against pyproject.toml and print its immutable/moving tags."""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import tomllib


def release_tags(image: str, tag: str, revision: str = "") -> list[str]:
    project_file = Path(__file__).resolve().parents[1] / "pyproject.toml"
    version = tomllib.loads(project_file.read_text(encoding="utf-8"))["project"]["version"]
    if tag != f"v{version}":
        raise ValueError(f"Release tag must be v{version}, received {tag!r}")
    if not re.fullmatch(r"[a-z0-9][a-z0-9._/-]+", image):
        raise ValueError("Image must be a lowercase registry/repository path without a tag")
    tags = [f"{image}:{tag}"]
    if revision:
        if not re.fullmatch(r"[0-9a-f]{7,40}", revision):
            raise ValueError("Revision must be a Git commit hash")
        tags.append(f"{image}:sha-{revision[:12]}")
    # Packaging versions can spell prereleases as 0.2.0rc1 as well as 0.2.0-rc.1.
    if re.fullmatch(r"\d+\.\d+\.\d+", version):
        tags.append(f"{image}:latest")
    return tags


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", required=True)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--revision", default="")
    args = parser.parse_args()
    try:
        print("\n".join(release_tags(args.image, args.tag, args.revision)))
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
