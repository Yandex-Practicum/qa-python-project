BASE_URL = "https://stellarburgers.education-services.ru"

REGISTER_ENDPOINT = "/api/auth/register"
LOGIN_ENDPOINT = "/api/auth/login"
USER_ENDPOINT = "/api/auth/user"
INGREDIENTS_ENDPOINT = "/api/ingredients"
ORDERS_ENDPOINT = "/api/orders"

REQUEST_TIMEOUT = 30

# Это точные значения поля message в ответах API, поэтому они не переведены.
USER_ALREADY_EXISTS_MESSAGE = "User already exists"
REQUIRED_FIELDS_MESSAGE = "Email, password and name are required fields"
INVALID_CREDENTIALS_MESSAGE = "email or password are incorrect"
INGREDIENTS_REQUIRED_MESSAGE = "Ingredient ids must be provided"
UNAUTHORIZED_MESSAGE = "You should be authorised"

