pip install qiskit

from qiskit import QuantumCircuit

#Initialize quantum circuit
bell= QuantumCircuit(2)
#Apply gates
bell.h(0)
bell.cx(0,1) # Controlled qubit & Target qubit

#Measure qubits
bell.measure_all()

#Visualize circuit
print(bell)

# Custom rotations
import numpy as np

circuit = QuantumCircuit(1)
circuit.u(np.pi/2,np.pi/2,np.pi/2,0) # U gate

print(circuit)

# Parameterised Circuit - Variational Algorithm

from qiskit.circuit import Parameter

#Define a variable theta to be a parameter with name 'theta'
theta = Parameter('theta')

#Initialize a quantum circuit with one qubit 
quantum_circuit = QuantumCircuit(1)

#Add a parameterised RX rotation on the qubit 
quantum_circuit.rx(theta, 0)

print(quantum_circuit)

#Binding parameter values
import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter

theta = Parameter('0')
quantum_circuit = QuantumCircuit(1)
quantum_circuit.rx(theta, 0)
#Set the value of the parameter
theta_value = np.pi

#Bind the value to the parameterised circuit
qc= quantum_circuit.assign_parameters({theta: theta_value})
print(qc)

#Binding parameter values
#Set the value of the parameter
theta_value = np.pi

#Bind the value to the parameterised circuit
qc= quantum_circuit.assign_parameters({theta: theta_value})
print(quantum_circuit)

#Dynamic Circuits 
'''
if/else statements
while loops
for loops
'''
qc= QuantumCircuit(1, 2)
qc.h(0)
qc.measure(0, 0)

#if q0 == 1, reset and flip it
with qc.if_test((0, True)):
    qc.reset(0)
    qc.x(0)

qc.measure(0, 1)
qc.draw()

#results: (either '00': 0.5, or '11': 0.5)

#while loop , loop until we get success

qc = QuantumCircuit(1, 2)
qc.h(0)
qc.measure(0, 0)

#  as long as q0==0; reset, add h and measure again until q0==1
with qc.while_loop((0, False)):
    qc.reset(0)
    qc.h(0)
    qc.measure(0, 0)
qc.measure(0, 1)

qc.draw()

#results: ('11': 1)

#switch case
from qiskit import QuantumRegister, ClassicalRegister

qreg = QuantumRegister(2)
creg = ClassicalRegister(2)
qc = QuantumCircuit(qreg, creg)
qc.h ([0, 1])
qc.measure([0, 1],[0, 1])

with qc.switch(creg) as case:
    with case(0):
        qc.z(0)
    with case(1, 2):
        qc.cs(0, 1)
    with case(case.DEFAULT):
        qc.h(0)

qc.draw()

!pip install matplotlib pylatexenc

from qiskit import QuantumCircuit
from IPython.display import display

qc = QuantumCircuit(1, 1)
qc.measure(0, 0)
print(qc.draw('text'))

import qiskit 
print(qiskit.__version__)

import sys
!{sys.executable} -m pip install qiskit-aer

from qiskit_aer import Aer
from qiskit import transpile

backend = Aer.get_backend('qasm_simulator')

compiled = transpile(qc, backend)

job= backend.run(compiled, shots=1000)
result = job.result()
counts = result.get_counts()
print(counts)

#hadamard gate (H) 
'''
|0> -> (|0> + |1>)/√2 
'''
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
backend = Aer.get_backend('qasm_simulator')
compiled = transpile(qc, backend)
job = backend.run(compiled, shots=1000)
counts = job.result().get_counts()
print(counts) # 50% 0, 50% 1 -> superposition

from qiskit.visualization import plot_circuit_layout
qc.draw('text')

from qiskit.visualization import plot_circuit_layout
qc.draw('mpl')

# Multiple Qubits
qc= QuantumCircuit(2, 2)
qc.draw('mpl')

#CNOT gate (Entanglement starts here)
'''
Control qubit controls target qubit
if control = 1 target flips
'''
qc = QuantumCircuit(2, 2)

qc.h(0)        # Put qubit 0 in superposition
qc.cx(0, 1)    # CNOT (control=0, target=1)

qc.measure([0,1], [0,1])

backend = Aer.get_backend('qasm_simulator')
compiled = transpile(qc, backend)
job = backend.run(compiled, shots=1000)

print(job.result().get_counts())

from qiskit import QuantumCircuit
qc= QuantumCircuit(2, 2)
qc.x(1)
qc.measure([0,1],[0,1])
qc.draw('mpl')

print(qc.draw('text'))
