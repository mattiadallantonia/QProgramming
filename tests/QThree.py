# use QISKit.org
from qiskit import QuantumProgram

# useful additional packages
from tools.visualization import plot_histogram

# Define the QProgram and the Quantum and Classical Registers
qp = QuantumProgram()
q = qp.create_quantum_register("q", 3)
c = qp.create_classical_register("c", 3)

# Define the circuit
threeQ = qp.create_circuit("threeQ", [q], [c])
threeQ.measure(q[0], c[0])
threeQ.measure(q[1], c[1])
threeQ.measure(q[2], c[2])

# Execute the circuit
result = qp.execute(["threeQ"])

# Plot result
plot_histogram(result.get_counts("threeQ"))