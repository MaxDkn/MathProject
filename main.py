class Vector:
    def __init__(self, pos=(0, 0)):
        self.x, self.y = pos
        self.x = float(self.x)
        self.y = float(self.y)

    def __str__(self):
        if self.x == int(self.x):
            x = int(self.x)
        else:
            x = self.x
        if self.y == int(self.y):
            y = int(self.y)
        else:
            y = self.y
        return f'({x}, {y})'


class Orthonormal:
    """
    This object is used to solve a classic problem, generally encountered in geometry problems. The typical problem is
    as follows: We have the coordinates, in an orthonormal coordinate system, of 3 points. We know the distance between
    each point and the unknown point and the question is: where is the unknown point? Generally, you must use a compass,
    and draw circles of radius r, with 1 of the 3 points as the center. Thanks to this method, we can solve this problem
    in a simpler way: enter the coordinates of the points in the arguments of the class, then put the distances in the
    arguments of one of the functions (be careful, in one case you will have to put these distances squared) then the
    function returns us the positions of the unknown point


    In the function "search_z_point", the values are unfortunately approximated due to the fact that they are long
    calculations, with many irrational numbers, or at least, they are numbers that are not decimal numbers but in
    the other function, the precision is better.
    """

    def __init__(self, pos_a: tuple[float, float] or Vector, pos_b: tuple[float, float] or Vector,
                 pos_c: tuple[float, float] or Vector):
        if type(pos_a) is tuple:
            self.posA = Vector(pos_a)
        elif type(pos_a) is Vector:
            self.posA = pos_a
        else:
            raise ValueError

        if type(pos_b) is tuple:
            self.posB = Vector(pos_b)
        elif type(pos_b) is Vector:
            self.posB = pos_b
        else:
            raise ValueError

        if type(pos_c) is tuple:
            self.posC = Vector(pos_c)
        elif type(pos_c) is Vector:
            self.posC = pos_c
        else:
            raise ValueError

    def search_z_point(self, distance_between_a_and_z, distance_between_b_and_z, distance_between_c_and_z):
        #  To simplify the formula
        dA = float(distance_between_a_and_z)
        dB = float(distance_between_b_and_z)
        dC = float(distance_between_c_and_z)

        xA = self.posA.x
        yA = self.posA.y
        xB = self.posB.x
        yB = self.posB.y
        xC = self.posC.x
        yC = self.posC.y

        z = Vector()

        z_x_numerator = (yC-yB)*(dA**2-xA**2-yA**2-dB**2+xB**2+yB**2)-(yB-yA)*(dB**2-xB**2-yB**2-dC**2+xC**2+yC**2)
        z_x_denominator = 2*(yC-yB)*(xB-xA) - 2*(yB-yA)*(xC-xB)

        z_y_numerator = (xC-xB)*(dA**2-xA**2-yA**2-dB**2+xB**2+yB**2)-(xB-xA)*(dB**2-xB**2-yB**2-dC**2+xC**2+yC**2)
        z_y_denominator = 2*(xC-xB)*(yB-yA) - 2*(xB-xA)*(yC-yB)

        z.x = z_x_numerator / z_x_denominator
        z.y = z_y_numerator / z_y_denominator
        return z

    def search_z_point_square_arguments(self, square_distance_between_a_and_z, square_distance_between_b_and_z,
                                        square_distance_between_c_and_z):
        """This function is more precise that search_z_point() because the irrational number are limited"""

        #  To simplify the formula
        dA = float(square_distance_between_a_and_z)
        dB = float(square_distance_between_b_and_z)
        dC = float(square_distance_between_c_and_z)

        xA = self.posA.x
        yA = self.posA.y
        xB = self.posB.x
        yB = self.posB.y
        xC = self.posC.x
        yC = self.posC.y

        z = Vector()

        z_x_numerator = (yC-yB)*(dA-xA**2-yA**2-dB+xB**2+yB**2)-(yB-yA)*(dB-xB**2-yB**2-dC+xC**2+yC**2)
        z_x_denominator = 2*(yC-yB)*(xB-xA) - 2*(yB-yA)*(xC-xB)

        z_y_numerator = (xC-xB)*(dA-xA**2-yA**2-dB+xB**2+yB**2)-(xB-xA)*(dB-xB**2-yB**2-dC+xC**2+yC**2)
        z_y_denominator = 2*(xC-xB)*(yB-yA) - 2*(xB-xA)*(yC-yB)

        z.x = z_x_numerator / z_x_denominator
        z.y = z_y_numerator / z_y_denominator
        return z


class AlgoToSearch:
    the_first_prime_number = [2]

    def __init__(self):
        _list = self.the_fibonacci_sequence(100)
        self.phi = _list[-1] / _list[-2]

    #  For this script I used the famous recursion in Python
    def the_fibonacci_sequence(self, index):
        list_fibonacci = []
        if index <= 0:
            list_fibonacci = [0]
        elif index == 1:
            list_fibonacci = [0, 1]
        else:
            for number in self.the_fibonacci_sequence(index-1):
                list_fibonacci.append(number)
            list_fibonacci.append(list_fibonacci[-1] + list_fibonacci[-2])
        return list_fibonacci

    def the_first_prime_numbers(self, index):
        i = 3
        prime_numbers = self.the_first_prime_number
        while len(prime_numbers) != index:
            divisible = False
            for number in prime_numbers:
                if i % number == 0:
                    divisible = True
                if divisible:
                    break

            if not divisible:
                prime_numbers.append(i)
            i += 2
        return prime_numbers

    def the_first_pairs_prime_numbers(self, index):
        i = 2
        prime_numbers = self.the_first_prime_number
        pairs_numbers = []

        while len(pairs_numbers) != index:
            divisible = False
            for number in prime_numbers:
                if i % number == 0:
                    divisible = True
                    break

            if not divisible:
                prime_numbers.append(i)
                if prime_numbers[-1] - prime_numbers[-2] == 2:
                    #  pairs_numbers.append(f'[{prime_numbers[-2]} | {prime_numbers[-1]}]')
                    pairs_numbers.append((prime_numbers[-2], prime_numbers[-1]))

            i += 1
        return pairs_numbers


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(AlgoToSearch().the_first_prime_numbers(20))
    print(AlgoToSearch().the_first_pairs_prime_numbers(10))
    print(AlgoToSearch().the_fibonacci_sequence(20))
    print(AlgoToSearch().phi)
    print(Orthonormal((0, 0), (4, 2), (1, 4)).search_z_point_square_arguments(5, 5, 10))
