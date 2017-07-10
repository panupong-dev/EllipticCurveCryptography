from attack_algorithm.baby_step_giant_step_attack_with_hash import BabyStepGiantStepAttackWithHash as babyHash
from attack_algorithm.exhaustive_attack import ExhaustiveAttack as Exhaustive
from attack_algorithm.baby_step_giant_step_attack import BabyStepGiantStepAttack as babyStepGiantStep
from elliptic.create_elliptic import CreateElliptic as Elliptic

if __name__ == '__main__':
    key_size = 128
    primitive_value, e_curve, e_ord = Elliptic.gen_elliptic_cha2(key_size)
    n_a, q_a = Elliptic().ecdlp_problem(primitive_value, e_ord)

    exhaustive_result = Exhaustive().exhaustive_attack(primitive_value, q_a, e_ord)
    baby_result = babyStepGiantStep().baby_step_giant_step_attack(primitive_value, q_a, e_ord)
    baby_hash_result = babyHash().baby_step_giant_step_attack(primitive_value, q_a, e_ord)
