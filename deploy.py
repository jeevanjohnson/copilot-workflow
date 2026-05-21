from pathlib import Path
import sys
import os
from dataclasses import dataclass
import shutil

# allows for subfolders in this repo of skills and instructions for better
# organization, but then we change it so it fits copilot's file structure


@dataclass
class Resource:
    path: Path
    pattern: str
    type: str


SKILLS = Resource(
    path=Path("./skills"),
    pattern="**/SKILL.md",
    type="skills"
)
INSTRUCTIONS = Resource(
    path=Path("./instructions"),
    pattern="**/**.md",
    type="instructions"
)
AGENTS = Resource(
    path=Path("./agents"),
    pattern="**/AGENT.md",
    type="agents"
)


def get_copilot_folder() -> str:
    assert len(sys.argv) == 2, \
        "Please provide the path to the copilot folder as an argument"
    dest = sys.argv[1]

    if not os.path.exists(dest):
        raise ValueError(f"Destination {dest} does not exist")

    return dest


def build_copilot_path(local_folder: Path, type: str) -> None:
    folder_parts = local_folder.parts[
        local_folder.parts.index(type) + 1:
    ]
    copilot_folder_name = ""
    for part in folder_parts:
        if part == folder_parts[-1]:
            copilot_folder_name += f"{part}"
        else:
            copilot_folder_name += f"{part.upper()}-"

    shutil.copytree(
        local_folder,
        Path(f"./copilot/{type}") / copilot_folder_name,
        dirs_exist_ok=True
    )


if __name__ == "__main__":
    copilot_folder = get_copilot_folder()

    if os.path.exists("./copilot"):
        shutil.rmtree("./copilot")

    for local_folder in (SKILLS, INSTRUCTIONS, AGENTS):
        for file in local_folder.path.rglob(local_folder.pattern):
            build_copilot_path(
                file.parent,
                local_folder.type
            )

        converted_folder = Path("./copilot") / local_folder.type

        copilot_folder_destination = Path(copilot_folder) / local_folder.type
        if copilot_folder_destination.exists():
            shutil.rmtree(copilot_folder_destination)

        if not converted_folder.exists():
            continue

        shutil.copytree(
            Path("./copilot") / local_folder.type,
            copilot_folder_destination,
            dirs_exist_ok=True
        )

        print(f"Copied {local_folder.type} to {copilot_folder_destination}")

    if os.path.exists("./copilot"):
        shutil.rmtree("./copilot")

    print("All done!")
