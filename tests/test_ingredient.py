from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngridients:
    def test_get_price_sause(self, create_sauce):
        sauce = create_sauce
        assert sauce.get_price() == 90

    def test_get_price_filling(self, create_filling):
        filling=create_filling
        assert filling.get_price()==1337

    def test_get_name_sause(self, create_sauce):
        sauce = create_sauce
        assert sauce.get_name() == 'Соус Spicy-X'

    def test_get_name_filling(self, create_filling):
        filling = create_filling
        assert filling.get_name() == 'Мясо бессмертных моллюсков Protostomia'

    def test_get_type_sause(self,create_sauce):
        sauce = create_sauce
        assert sauce.get_type() == INGREDIENT_TYPE_SAUCE

    def test_get_type_filling(self,create_filling):
        filling = create_filling
        assert filling.get_type() == INGREDIENT_TYPE_FILLING
