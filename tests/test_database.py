import data
import pytest

class TestDatabase:
    @pytest.mark.parametrize('av_buns', data.AVAILABLE_BUNS)
    def test_available_buns(self, av_buns, database):
        assert (database.available_buns()[av_buns.get('id')].get_name() == av_buns.get('name') and 
                database.available_buns()[av_buns.get('id')].get_price() == av_buns.get('price'))
        
    @pytest.mark.parametrize('av_ingr', data.AVAILABLE_INGREDIENTS)
    def test_available_ingredients(self, av_ingr, database):
        assert (database.available_ingredients()[av_ingr.get('id')].get_type() == av_ingr.get('type') and 
                database.available_ingredients()[av_ingr.get('id')].get_name() == av_ingr.get('name') and 
                database.available_ingredients()[av_ingr.get('id')].get_price() == av_ingr.get('price'))
