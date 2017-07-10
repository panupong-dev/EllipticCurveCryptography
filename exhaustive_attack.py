class ExhaustiveAttack:
    @staticmethod
    def exhaustive_attack(primitive, q_a, e_ord):
        n_hat = 1

        while n_hat <= e_ord:
            q_hat = n_hat * primitive

            if q_hat == q_a:
                return n_hat

            n_hat += 1

        return -1
