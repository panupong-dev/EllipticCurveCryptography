from random import randrange


class CreateElliptic:
    @staticmethod
    def gen_elliptic_cha2(keysize):
        field. < V >= GF(2 ^ keysize, "s")
        s_gen = field.gen()
        s_ord = field.order()
        a_point = field(V ^ 16 + V ^ 14 + V ^ 13 + V ^ 12 + V ^ 11 + V ^ 10 + V ^ 7 + V ^ 5 + V ^ 3 + V ^ 2)
        b_point = s(1)
        e_curve = EllipticCurve(S, [1, a_point, 0, 0, b_point])
        primitive_value = e_curve \
            (V ^ 17 + V ^ 16 + V ^ 15 + V ^ 13 + V ^ 10 + V ^ 8 + V ^ 3 + V ^ 2 + 1,
             V ^ 16 + V ^ 10 + V ^ 8 + V ^ 6 + V ^ 3 + V ^ 2 + V + 1)
        e_ord = primitive_value.order()

        return primitive_value, e_curve, e_ord

    @staticmethod
    def ecdlp_problem(primitive_value, e_ord):
        n_a = randrange(1, e_ord - 1)
        q_a = n_a * primitive_value

        return n_a, q_a
