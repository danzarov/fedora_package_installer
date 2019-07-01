from user_selection import ask_user
from app import start


def main():
    selected_packages = ask_user()
    start(selected_packages)


if __name__ == "__main__":
    main()