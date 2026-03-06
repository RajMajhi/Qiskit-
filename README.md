# Qiskit – Quantum Computing with Python

Quantum Mechanics is  about understanding a world that is hard to see, &lt;br> while Quantum Computing is about harnessing that world for computation. 

Qiskit is an open-source quantum computing framework that allows you to create, simulate, and run quantum circuits using Python.

---

##  Installation

### 1️⃣ Install Python (3.8+)

Check version:

```bash
python --version
```

---

### 2️⃣ (Optional) Create Virtual Environment

```bash
python -m venv qiskit-env
```

Activate:

**Windows**
```bash
qiskit-env\Scripts\activate
```

**Mac/Linux**
```bash
source qiskit-env/bin/activate
```

---

### 3️⃣ Install Qiskit

```bash
pip install qiskit
```

Verify installation:

```bash
python -c "import qiskit; print(qiskit.__version__)"
```

---

##  Using Qiskit with Jupyter Notebook

Install Jupyter:

```bash
pip install notebook
```

Start Jupyter:

```bash
jupyter notebook
```

Create a new Python notebook and begin coding.

---

##  Basic Example: Bell State Circuit

```python
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile

# Create a 2-qubit circuit with 2 classical bits
qc = QuantumCircuit(2, 2)

# Apply gates
qc.h(0)
qc.cx(0, 1)

# Measure
qc.measure([0, 1], [0, 1])

print(qc)

# Simulate
simulator = Aer.get_backend('aer_simulator')
compiled = transpile(qc, simulator)
result = simulator.run(compiled).result()

counts = result.get_counts()
print(counts)
```

Expected Output (approximate):

```python
{'00': ~50%, '11': ~50%}
```

---

##  Basic Concepts

### Qubit
A quantum bit that can exist in superposition.

### Common Gates

| Gate | Description |
|------|-------------|
| `H`  | Hadamard (superposition) |
| `X`  | Bit flip |
| `Z`  | Phase flip |
| `CX` | Controlled-NOT |
| `RY` | Rotation around Y-axis |

Example:

```python
qc.x(0)
qc.z(1)
qc.ry(1.57, 0)
```

---

##  Visualizing Circuits

```python
qc.draw('mpl')
```

Install matplotlib if needed:

```bash
pip install matplotlib
```

---

##  Statevector Simulation

```python
from qiskit.quantum_info import Statevector

state = Statevector.from_instruction(qc)
print(state)
```

---

##  Running on Real Hardware

Install IBM Runtime:

```bash
pip install qiskit-ibm-runtime
```

Authenticate and run jobs using IBM Quantum services.

---
@RajMajhi

## 📚 Resources

- Official Documentation: https://qiskit.org/documentation/
- Tutorials: https://qiskit.org/learn/
