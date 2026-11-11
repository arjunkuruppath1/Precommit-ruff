from app.user_service import create_user, get_user


def main():
    user = create_user("Arjun", "arjun@example.com")

    print("Created User:", user)

    user_details = get_user(101)

    print("User Details:", user_details)


if __name__ == "__main__":
    main()
