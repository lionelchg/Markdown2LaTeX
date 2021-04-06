# Linear Algebra Exercices

## Reduction

### Exercice 1

Solve in $\mc{M}_3(\mathbb{C})$ the following equation in $X$:

$$
\begin{equation}
    X^2 = A = \begin{pmatrix}
        1 & 3 & - 7 \\
        2 & 6 & - 14 \\
        1 & 3 & - 7
    \end{pmatrix}
\end{equation}
$$

#### Solution

Computing first the characteristic polynomial of $A$

$$
\begin{aligned}
    \chi(A) &= \begin{vmatrix}
    1 - x & 3 & - 7 \\
    2 & 6 - x & - 14 \\
    1 & 3 & - 7 - x
    \end{vmatrix} = \begin{vmatrix}
    - x & 0 & x \\
    2 & 6 - x & - 14 \\
    1 & 3 & - 7 - x
    \end{vmatrix} \\ &= x \begin{vmatrix}
    - 1 & 0 & 1 \\
    2 & 6 - x & - 14 \\
    1 & 3 & - 7 - x
    \end{vmatrix} = x \begin{vmatrix}
    - 1 & 0 & 1 \\
    2 & 6 - x & - 14 \\
    1 & 3 & - 7 - x
    \end{vmatrix} = \\
    &= x \left[-\begin{vmatrix}
    6 - x & - 14 \\
    3 & - 7 - x 
    \end{vmatrix} + x \right] = - x^3
\end{aligned}
$$

Hence $S_p(A) = {0}$. The matrice needs to be trigonalized. It is obvious that:

$$
\begin{align}
    \dim(\ker(A)) = 2
\end{align}
$$

Moreover $A^2 = 0$ and hence $\mrm{Im}(A) \subset \mrm{Ker}(A)$. Let us 
first take a vector $e_3$ that is not in $\mrm{Ker}(A)$ and 
$e_2 = A e_3$. We complete $e_2$ with $e_1$ such that $(e_1, e_2)$ is a
basis of $\mrm{Ker}(A)$. That way:

$$
    A = P\begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}P^{-1}
$$

Let us find a suitable form for $P$:

$$
    P = \begin{pmatrix} 3 & - 7 & 0 \\ -1 & - 14 & 0 \\ 0 & - 7 & 1 \end{pmatrix}
$$

and we have an equation for $\ker(A)$:

$$
    x + 3 y - 7 z = 0
$$

$X$ now needs to be simplified. We search for the decomposition of $X$ in the basis $(e_1, e_2, e_3)$:

$$
    X' = P^{-1} X P
$$

$X$ and $A$ commute, so that $\mrm{Im}(A)$ and $\mrm{Ker}(A)$ are stable by X:

$$
    X' = \begin{pmatrix} a & 0 & d  \\ b & c & e  \\ 0 & 0 & f \end{pmatrix}
$$

And since $X$ is also nilpotent, $\mrm{Sp}(X) = \{0\}$ and $a = c = f = 0$. Finally:

$$
    X' = \begin{pmatrix} 0 & 0 & b  \\ a & 0 & c  \\ 0 & 0 & 0 \end{pmatrix}
$$

Solving the equation:

$$
    X'^2 = \begin{pmatrix} 0 & 0 & 0  \\ 0 & 0 & ab  \\ 0 & 0 & 0 \end{pmatrix}
$$

Comparing with the reduced form of $A$:

$$
    ab = 1 \implies 
    X' = \begin{pmatrix} 0 & 0 & 1 / a  \\ a & 0 & b  \\ 0 & 0 & 0 \end{pmatrix}
$$