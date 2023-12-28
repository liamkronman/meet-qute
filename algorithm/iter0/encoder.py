from qiskit import QuantumCircuit

def encode_response(response):
    '''
    Encoding the response to the question: Are you single?
    '''
    qc = QuantumCircuit(1) # one qubit circuit
    if response == 1:
        qc.x(0) # apply X gate if response is 'Yes'
    return qc


# test cases
if __name__ == '__main__':
    qc = encode_response(1)
    print(qc.draw())
    qc = encode_response(0)
    print(qc.draw())