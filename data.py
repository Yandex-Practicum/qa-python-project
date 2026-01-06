from unittest.mock import Mock


class BunsandOtherIngredients:
    """Добавление моков булочек"""
    mock_buns=[]
    mock_bun1=Mock()
    mock_bun1.get_name.return_value ="red bun"
    mock_bun1.get_price.return_value =300.0
    mock_bun2=Mock()
    mock_bun2.get_name.return_value ="black bun"
    mock_bun2.get_price.return_value =100.0
    mock_bun3=Mock()
    mock_bun3.get_name.return_value ="white bun"
    mock_bun3.get_price.return_value =200.0
    mock_buns.append(mock_bun1)
    mock_buns.append(mock_bun2)
    mock_buns.append(mock_bun3)

    """Добавление моков ингредиентов"""
    mock_ingredients=[]
    mock_ingredient1=Mock()
    mock_ingredient1.get_name.return_value ="sour cream"
    mock_ingredient1.get_price.return_value =200.0
    mock_ingredient1.get_type.return_value ='SAUCE'
    mock_ingredient2=Mock()
    mock_ingredient2.get_name.return_value ="sausage"
    mock_ingredient2.get_price.return_value =300.0
    mock_ingredient2.get_type.return_value ='FILLING'
    mock_ingredient3=Mock()
    mock_ingredient3.get_name.return_value ="dinosaur"
    mock_ingredient3.get_price.return_value =200.0
    mock_ingredient3.get_type.return_value ='FILLING'
    mock_ingredients.append(mock_ingredient1)
    mock_ingredients.append(mock_ingredient2)
    mock_ingredients.append(mock_ingredient3)
    
    """Вывод сформированного рецепта для 1 булки и 1 ингредиента"""
    @staticmethod
    def get_receipt(bun, ingredient):
        receipt = f'(==== {bun.get_name()} ====)\n'
        receipt += f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =\n'
        receipt += f'(==== {bun.get_name()} ====)\n\n'
        receipt += f'Price: {bun.get_price() *2+ingredient.get_price()}'
        return receipt
        
 
class TestData:
    buns_available=[["black bun", 100], ["white bun", 200], ["red bun", 300]]
    ingredients_available=[["SAUCE", "hot sauce", 100], ["SAUCE", "sour cream", 200], ["SAUCE", "chili sauce", 300],
                         ["FILLING", "cutlet", 100], ["FILLING", "dinosaur", 200], ["FILLING", "sausage", 300]]
 
