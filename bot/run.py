from tests.signin.test_signin import SignIn
from tests.invite.invite import Invite
from tests.signup.signup import SignUp


with SignIn() as bot1:
    bot1.test_land_first_page()
    bot1.test_login_by_valid_user()
    # bot1.login_by_incorrect_password()
    # bot1.login_by_incorrect_email()
    # bot1.login_by_invalid_email()
    # bot1.not_fill_field_login()


# with SignUp() as bot2:
#     bot2.land_first_page()
#     # bot2.signup_by_existing_account()
#     bot2.not_fill_out_sign_up()

# with Invite() as bot3:
#     bot3.land_first_page()
#     # bot3.get_invite_link()
#     bot3.reset_invite_link()
    

