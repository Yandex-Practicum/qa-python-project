from database import Database

class TestDatabaseAvailableBuns:
    
    def setup_method(self):
        self.database = Database()
    
    def test_available_buns_returns_three_buns(self):
        buns = self.database.available_buns()
        assert len(buns) == 3
    
    def test_available_buns_first_bun_is_black_bun(self):
        buns = self.database.available_buns()
        assert buns[0].get_name() == "black bun"
    
    def test_available_buns_first_bun_price_is_100(self):
        buns = self.database.available_buns()
        assert buns[0].get_price() == 100
    
    def test_available_buns_second_bun_is_white_bun(self):
        buns = self.database.available_buns()
        assert buns[1].get_name() == "white bun"
    
    def test_available_buns_second_bun_price_is_200(self):
        buns = self.database.available_buns()
        assert buns[1].get_price() == 200
    
    def test_available_buns_third_bun_is_red_bun(self):
        buns = self.database.available_buns()
        assert buns[2].get_name() == "red bun"
    
    def test_available_buns_third_bun_price_is_300(self):
        buns = self.database.available_buns()
        assert buns[2].get_price() == 300
    
    def test_available_buns_returns_same_reference(self):
        buns1 = self.database.available_buns()
        buns2 = self.database.available_buns()
        assert buns1 is buns2