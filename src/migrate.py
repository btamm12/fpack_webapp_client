import shutil

from src import constants


def migrate():

    # Path to old repository.
    OLD_REPO = constants.DIR_PROJECT.parent.joinpath("fpack_webapp_client_old")
    if not OLD_REPO.exists():
        print("Cannot find project to migrate from: 'fpack_webapp_client_old'.")
        exit(1)

    # Copy subject mapping.
    print("Copying subject_mapping.txt.")
    src_path = OLD_REPO.joinpath("subject_mapping.txt")
    dst_path = constants.SUBJECT_MAPPING_PATH
    if src_path.exists():
        shutil.copy(src_path, dst_path)
    else:
        print("> subject_mapping.txt does not exist.")

    # Copy collaboration.
    print("Copying collaboration/my_name.txt.")
    src_path = OLD_REPO.joinpath("collaboration", "my_name.txt")
    dst_path = constants.DIR_COLLABORATION.joinpath("my_name.txt")
    if src_path.exists():
        shutil.copy(src_path, dst_path)
    else:
        print("> collaboration/my_name.txt does not exist.")

    print("Copying collaboration/my_sections.txt.")
    src_path = OLD_REPO.joinpath("collaboration", "my_sections.txt")
    dst_path = constants.DIR_COLLABORATION.joinpath("my_sections.txt")
    if src_path.exists():
        shutil.copy(src_path, dst_path)
    else:
        print("> collaboration/my_sections.txt does not exist.")

    # Copy data.
    print("Copying data...")
    items_copied = 0
    for folder in OLD_REPO.joinpath("data").iterdir():
        if not folder.is_dir():
            print(f"data/{folder.name} not copied.")
            continue
        dst_folder = constants.DIR_DATA.joinpath(folder.name)
        if not dst_folder.exists():
            print(
                f"data/{folder.name}/ not copied since it does not exist in the new project."
            )
            continue
        for item in folder.iterdir():
            dst_path = dst_folder.joinpath(item.name)
            shutil.copy(item, dst_path)
            items_copied += 1
    print(f"{items_copied} items copied.")

    # Copy app data.
    print("Copying app data: src/state.pkl.")
    src_path = OLD_REPO.joinpath("src", "state.pkl")
    dst_path = constants.STATE_PATH
    if src_path.exists():
        shutil.copy(src_path, dst_path)
    else:
        print("> src/state.pkl does not exist.")

    print("Migration finished.")


if __name__ == "__main__":
    migrate()
