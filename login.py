import create_user

user = create_user.CreateUser()
logged_user, session = user.login_user()
print(logged_user.text)
