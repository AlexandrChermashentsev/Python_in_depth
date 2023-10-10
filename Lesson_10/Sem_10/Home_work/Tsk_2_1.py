class Triangle:
    
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        
    def get_info(self):
        return f'{self.side_a} {self.side_b} {self.side_c}'
        
    def status_triangle(self):
        if (self.side_a > self.side_b + self.side_c or 
            self.side_b > self.side_a + self.side_c or 
            self.side_c > self.side_a + self.side_b):
            return 'Такого треугольника не существует'
        elif self.side_a == self.side_b == self.side_c:
            return 'РавноСТОРОННИЙ'
        elif (self.side_a == self.side_b) or (self.side_a == self.side_c) or (self.side_c == self.side_b):
            return 'РавноБЕДРЕННЫЙ'
        else:
            return 'РАЗНОсторонний'
        
triangle_1 = Triangle(2, 2, 2)
triangle_2 = Triangle(4, 5, 2)
triangle_3 = Triangle(3, 2, 2)
triangle_4 = Triangle(6, 2, 2)
for tr in [triangle_1, triangle_2, triangle_3, triangle_4]:
    print(f'{tr.get_info()} -', tr.status_triangle())
        

                