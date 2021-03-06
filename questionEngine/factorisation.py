from questionEngine.base_question_engine import BaseQuestionEngine
from sympy import *
import random


class FactorisationQuestions(BaseQuestionEngine):
    def __init__(self):
        super().__init__()

    def gen_quad_factorisation_x_only(self, coeff_range=None, follower_range=None, **kwargs):
        if coeff_range is None:
            coeff_range = [-2, 2]
        if follower_range is None:
            follower_range = [-8, 8]
        pre_gen_eq = 1 * \
            (random.randint(*coeff_range) * self.x + random.randint(*follower_range)) * \
            (random.randint(*coeff_range) * self.x + random.randint(*follower_range))

        return [pre_gen_eq.expand(), pre_gen_eq]

    def gen_quad_factorisation_complete_square_x_only(self, **kwargs):
        coeff_range = [1, 3]
        bracket_follower_range = [-6, 6]
        external_follower_range = [-10, 10]
        pre_gen_eq = random.randint(*coeff_range) * (
            (random.randint(*coeff_range) * self.x + random.randint(*bracket_follower_range))**2 +
            random.randint(*external_follower_range))

        return [pre_gen_eq.expand(), pre_gen_eq]

    def gen_question(self, diff=0, **kwargs):
        if diff == 0:
            return self.gen_quad_factorisation_x_only(**kwargs)
        elif diff == 1:
            return self.gen_quad_factorisation_complete_square_x_only(**kwargs)
        elif diff == 4:
            return random.choice([
                self.gen_quad_factorisation_x_only,
                self.gen_quad_factorisation_complete_square_x_only
            ])(**kwargs)


if __name__ == "__main__":
    test_fac_engine = FactorisationQuestions()
    print(test_fac_engine.gen_question_set(10, diff=0))
    print(test_fac_engine.gen_question_set(10, diff=1))
    print(test_fac_engine.gen_question_set(10, diff=4))
