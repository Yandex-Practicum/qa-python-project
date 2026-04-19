class ExpectedResponceCodes:
    #создание пользователя
    CREATE_DUPLICATE_USER=403
    CREATE_USER_WITHOUT_ANY_PARAM=403
    
    #Авторизация
    LOGIN_SUCCESS=200
    LOGIN_WITHOUT_ANY_FIELD=401
    LOGIN_WRONG_AUTORIZATION_DATA=401
    
    #Создание заказа
    CREATE_ORDER_UNAUTORIZED_USER=500
    CREATE_ORDER_INVALID_INGREDIENT_HASH=500
    CREATE_ORDER_EMPTY_INGREDIENTS=400

class ExpectedResponces:
    #создание пользователя
    CREATE_DUPLICATE_USER='User already exists'
    CREATE_USER_WITHOUT_ANY_PARAM='Email, password and name are required fields'
    
    #Авторизация
    LOGIN_WITHOUT_ANY_FIELD="email or password are incorrect"
    LOGIN_WRONG_AUTORIZATION_DATA="email or password are incorrect"

    #Создание заказа
    CREATE_ORDER_EMPTY_INGREDIENTS="Ingredient ids must be provided"