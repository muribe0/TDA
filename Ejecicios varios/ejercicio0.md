Si tenemos un algoritmo cuya ecuacion de recurrencia es:
$$
T(n) = AT(\frac{n}{B}) + O(n^c)
$$
**A**: cantidad de llamados recursivos

**B**: proporcion del tamano original con el que llamamos recursivamente

**$O(n^c)$**: el costo de *partir y juntar* (todo lo que no son llamados recursivos)

### Solucion

* $\text{ Si } \log_{B}{A} < C \rightarrow T(n) = O(n^{c})$
* $\text{ Si } \log_{B}{A} = C \rightarrow T(n) = O(n^{c}\log_{B}{n}) = O(n^{c}\log{n})$
* $\text{ Si } \log_{B}{A} > C \rightarrow T(n) = O(n^{\log_{B}{A}})$


$$
\begin{align}
T(n) &= 2T\left(\frac{n}{2}\right) + O(1)  \\
\end{align}
$$
