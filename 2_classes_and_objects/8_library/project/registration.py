class Registration:
    def add_user(self, user, library):
        if user not in library.user_records:
            library.user_records.append(user)
            return
        return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user, library):
        if user in library.user_records:
            library.user_records.remove(user)
            return
        return "We could not find such user to remove!"

    def change_username(self, user_id, new_username, library):
        for user in library.user_records:
            if user.user_id == user_id and user.username != new_username:
                user.username = new_username
                for u in library.rented_books:
                    if u == user.username:
                        library.rented_books[u] = library.rented_books[new_username]
                        del library.rented_books[u]
                return f"Username successfully changed to: {new_username} for user id: {user_id}"

            if user.user_id == user_id and user.username == new_username:
                return "Please check again the provided username - it should be different than " \
                       "the username used so far!"

            return f"There is no user with id = {user_id}!"

