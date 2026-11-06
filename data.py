class Data:
    def expect_burger(number):
        lst = []
        lst.append("(==== black bun ====)\n"+
                   "= sauce hot sauce =\n"+
                   "= filling cutlet =\n"+
                   "(==== black bun ====)\n\n"+
                   "Price: 400")

        lst.append("(==== white bun ====)\n"+
                   "= sauce sour cream =\n"+
                   "= filling dinosaur =\n"+
                   "(==== white bun ====)\n\n"+
                   "Price: 800")
        
        lst.append("(==== red bun ====)\n"+
                   "= sauce chili sauce =\n"+
                   "= filling sausage =\n"+
                   "(==== red bun ====)\n\n"+
                   "Price: 1200")        

        return lst[number]

    def expect_bun(number):
        lst = [ 'black bun',
                'white bun',
                'red bun' ]
        return lst[number]    

    def expect_ingredient(number):
        lst = [ 'hot sauce',
                'sour cream',
                'chili sauce',
                'cutlet',
                'dinosaur',
                'sausage' ]
        return lst[number] 
