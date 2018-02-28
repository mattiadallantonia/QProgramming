from qiskit import QuantumProgram, QISKitError, RegisterSizeError

# Create a QuantumProgram object instance.
q_program = QuantumProgram()
backend = 'local_qasm_simulator'
try:
    # Create a Quantum Register called "qr" with 2 qubits.
    quantum_reg = q_program.create_quantum_register("qr", 2)
    # Create a Classical Register called "cr" with 2 bits.
    classical_reg = q_program.create_classical_register("cr", 2)
    # Create a Quantum Circuit called "qc" involving the Quantum Register "qr"
    # and the Classical Register "cr".
    quantum_circuit = q_program.create_circuit("bell", [quantum_reg], [classical_reg])

    # Add the H gate in the Qubit 0, putting this qubit in superposition.
    quantum_circuit.h(quantum_reg[0])
    # Add the CX gate on control qubit 0 and target qubit 1, putting
    # the qubits in a Bell state
    quantum_circuit.cx(quantum_reg[0], quantum_reg[1])

    # Add a Measure gate to see the state.
    quantum_circuit.measure(quantum_reg, classical_reg)

    # Compile and execute the Quantum Program in the local_qasm_simulator.
    result = q_program.execute(["bell"], backend=backend, shots=1024, seed=1)

    # Show the results.
    print(result)
    print(result.get_data("bell"))

except QISKitError as ex:
    print('There was an error in the circuit!. Error = {}'.format(ex))
except RegisterSizeError as ex:
    print('Error in the number of registers!. Error = {}'.format(ex))
