# Input parameters
1. complex vector $w$ with dimension of 256x1.
2. $\alpha(\theta, \phi)$ with dimension 256x361x91.
3. target binary coding matrix $F_0(\theta, \phi)$ with dimension 361x91

$F_0(\theta, \phi) = w^H * \alpha(\theta, \phi)$

$\alpha(\theta, \phi) = f(\theta, \phi) * e^-jk0(x_i * \sin{\theta} * cos{\phi} + y_i * sin{\theta} * sin{\phi})$

- **Hermitian of $w$:** Since $w$ is 256×1, $w^H$ will be 1×256.
- **Tensor $\alpha(\theta, \phi):$** This is a 3-dimensional tensor of size 256x361x91.
- To compute $F_0(\theta, \phi)$, the following is considered:
  1. 
  2. 

# 1
### What is the Complex Vector
- https://chatgpt.com/share/5909bf82-1c5e-4749-8853-567f2a4e9590
- Complex vectors have elements that are complex numbers. 
- A complex number is typically written as $a+bi$, where $a$ and $b$ are real numbers, and $i$ is the imaginery unit $(i^2 = -1
)$.
- The complex vector $w$ with dimensions 256x1 refers to a column vector composed of 256 complex numbers arranged vertically. 
- Each element of this vector can be expressed as $w_i$ where $i$ ranges between from 1 to 256.
- *Complex Vector Space*: 
    - A space consisting of all possible complex vectors of a given dimension. 
    - It is similar to a real vector space, but with complex numbers as the scalar field.
- *Complex Vector Operations*: 
    - Vector-addition
    - Vector-subtraction
    - Scalar-multiplication
    - Scalar-division
    - Similar to those real vector spaces, but they follow the rules of complex arithmetic.
    - To visulaise, a complex vector $w$ with dimensions 256x1 can be represented as
    $$\mathbf{w} = \begin{bmatrix} w_1 \\ w_2 \\ w_3 \\ \vdots \\ w_{256} \end{bmatrix}$$
    - Each element $w_i$ (for $i=1, ,2, 3, ..., 256$) is a complex number.
    - Each element $w_i$ can be expressed as $w_i = a_i + b_i \cdot i$, where $a$ and $b$ are real numbers.

# 2
### What is the Three-dimensional Array
- The Notaion $\alpha(\theta, \phi)$ with 256x31x91 refers to a three-dimensional array or *tensor*.
- First dimension: any discrete unit
- Second dimension: set of values or parameters associated with each entity from the first dimension.
- Third dimension: another set of values or parameters associated with each entity and each value or parameter from the second dimension.
- Therefore, $\alpha(\theta, \phi)$ is a 3D structure where each element $\alpha(i, j, k)$ 
  - $i=1,2,3,\cdots, 256$ 
  - $j=1,2,3,\cdots, 31$ 
  - $k=1,2,3,\cdots, 91$

# 3
### What is the Target Binary Coding Matrix
- A Binary Coding Matrix represents data in a binary (0 and 1) format. 
- Each element in $F_0(\theta, \phi)$ is either 0 or 1.

