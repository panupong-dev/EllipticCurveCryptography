import math
import operator


class BabyStepGiantStepAttack:
    @staticmethod
    def create_table(n_1, primitive):
        table_st = dict()

        for i in range(n_1 + 1):
            table_st[i] = i * primitive

        return table_st

    @staticmethod
    def primitive_invert(n_1, primitive):
        p_invert = -1 * primitive
        p_n_invert = n_1 * p_invert

        return p_n_invert

    @staticmethod
    def find_table_index_by_gamma(q_a, p_n_invert, table_st, table_nd):
        index, index_table = 0, -1
        flag = True

        while flag:
            gamma = q_a + index * p_n_invert

            if gamma in table_nd:

                for k, v in table_st:

                    if gamma == v:
                        index_table = k

                flag = False

            index += 1

        return index, index_table

    def baby_step_giant_step_attack(self, primitive, q_a, e_ord):
        n_1 = 1 + int(math.floor(math.sqrt(e_ord)))
        table_st = self.create_table(n_1, primitive)
        table_nd = sorted(table_st.items(), key=operator.itemgetter(1))
        p_n_invert = self.primitive_invert(n_1, primitive)
        index, index_table = self.find_table_index_by_gamma(q_a, p_n_invert, table_st, table_nd)
        n_hat = index * n_1 + index_table

        return n_hat
