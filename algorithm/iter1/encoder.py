from qiskit import QuantumCircuit

def encode_user_profile(answers):
    """
    Encodes a user's answers into a quantum circuit.
    answers: List of binary answers to the 3 questions.
    """
    qc = QuantumCircuit(3)
    for i, answer in enumerate(answers):
        if answer == 1:
            qc.x(i)
    return qc


# test cases
if __name__ == '__main__':
    qc = encode_user_profile([1, 0, 1])
    print(qc.draw())
    qc = encode_user_profile([0, 1, 0])
    print(qc.draw())