from typing import Dict, Set


class FSM:
    """
    Finite State Machine implementation
    """

    def __init__(self, init_state: str, trans_table: Dict, final_states: Set, output_map: Dict = None):
        """
        :param init_state: Initial state of the FSM
        :param trans_table: A dictionary mapping (current_state, symbol) to next_state
        :param final_states: Accepted final states
        :param output_map: (Optional) A dictionary mapping states to output values
        """
        self.init_state = init_state
        self.trans_table = trans_table
        self.final_states = final_states
        self.output_map = output_map
        self.current_state = init_state

    def reset(self):
        """
        Reset the FSM to the initial state
        """
        self.current_state = self.init_state

    def process_symbol(self, symbol: str):
        """
        Process a single symbol and update the current state
        :param symbol: The input symbol
        """
        key = (self.current_state, symbol)
        if key not in self.trans_table:
            raise ValueError(f"No transition defined for state {self.current_state} with symbol {symbol}")

        self.current_state = self.trans_table[key]

    def compute(self, input_string):
        """
        Process an entire input string symbol by symbol

        :param input_string: The input string to process
        :return: The output value corresponding to the final state if output_map defined, otherwise return the current state directly.
        """
        for symbol in input_string:
            self.process_symbol(symbol)

        if self.current_state not in self.final_states:
            raise ValueError("The current state is an unaccepted final state.")

        return self.output_map[self.current_state] if self.output_map is not None else self.current_state


def create_mod_three_fsm() -> FSM:
    """
    Create a specific FSM for computing the mod 3 task
    :return: A FSM instance
    """
    trans_table = {
        ('S0', '0'): 'S0',
        ('S0', '1'): 'S1',
        ('S1', '0'): 'S2',
        ('S1', '1'): 'S0',
        ('S2', '0'): 'S1',
        ('S2', '1'): 'S2',
    }

    output_map = {
        'S0': 0,
        'S1': 1,
        'S2': 2,
    }

    return FSM(
        init_state='S0',
        trans_table=trans_table,
        final_states={'S0', 'S1', 'S2'},
        output_map=output_map
    )


if __name__ == '__main__':
    test_cases = [
        ('1101', 1),
        ('1110', 2),
        ('1111', 0),
        ('110', 0),
        ('1010', 1),
    ]

    fsm = create_mod_three_fsm()

    for input_str, expected_out in test_cases:
        fsm.reset()
        output = fsm.compute(input_str)
        print(f"Input: {input_str} -> Output: {output}, Expected Output: {expected_out}")
