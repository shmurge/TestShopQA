class CreateAccountPage:
    INPUT_LOGIN = ('css selector', '[id="login"]')
    INPUT_USERNAME = ('css selector', '[id="name"]')
    INPUT_PASSWORD = ('css selector', '[id="password"]')
    INPUT_PASSWORD_CONFIRM = ('css selector', '[id="confirm_password"]')
    BUTTON_SUBMIT = ('css selector', '[class="btn btn-primary"]')
    ALERT_PASSWORDS_MISSMATCH = ('css selector', '[class="alert alert-danger"]')