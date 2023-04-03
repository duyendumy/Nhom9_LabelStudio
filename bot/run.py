from login.login import Login

with Login() as bot:
    bot.land_first_page()
    bot.login_by_user()
