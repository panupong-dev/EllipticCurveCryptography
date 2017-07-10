import math
import operator

from attack_algorithm.baby_step_giant_step_attack import BabyStepGiantStepAttack as Baby


class BabyStepGiantStepAttackWithHash:
    @staticmethod
    def create_hash_table(n_1, primitive):
        table_st = dict()

        for i in range(n_1 + 1):
            table_st[i] = hash(i * primitive)

        return table_st

    def baby_step_giant_step_attack(self, primitive, q_a, e_ord):
        n_1 = 1 + int(math.floor(math.sqrt(e_ord)))
        table_st = self.create_hash_table(n_1, primitive)
        table_nd = sorted(table_st.items(), key=operator.itemgetter(1))
        p_n_invert = Baby.primitive_invert(n_1, primitive)
        index, index_table = Baby.find_table_index_by_gamma(q_a, p_n_invert, table_st, table_nd)
        n_hat = index * n_1 + index_table

        return n_hat
