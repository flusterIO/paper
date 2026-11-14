# Derivations and Current Status

## Status Key

| Status                         | Meaning                                                                                      |
| ------------------------------ | -------------------------------------------------------------------------------------------- |
| **Derived**                    | Algebraically follows from the stated starting equations.                                    |
| **Conditional**                | Mathematically derived, but depends on an assumption not yet independently established.      |
| **Standard result reproduced** | Reproduces an established result, but has not yet been independently derived from our model. |
| **Incomplete**                 | Partially developed; important steps or justification remain.                                |
| **Needs correction**           | Contains a mathematical, dimensional, or conceptual problem that must be resolved.           |
| **Not yet derived**            | Identified as a necessary result, but no complete derivation exists.                         |

## 1. Lorentz Transformations and Spatial Displacement

| Derivation                                                 | Principal Result                                                                      | Current Status                                                                                                                      |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Lorentz factor from relative velocity                      | $\gamma=\frac{1}{\sqrt{1-v^2/c^2}}$                                                   | **Derived** — standard Lorentz relation.                                                                                            |
| Velocity as a function of $\gamma$                         | $v=c\sqrt{1-\gamma^{-2}}$                                                             | **Derived** — algebraic rearrangement.                                                                                              |
| Additional spatial displacement                            | $dy=\tau v\sqrt{\gamma^2-1}=\frac{\tau v^2}{\sqrt{c^2-v^2}}$                          | **Conditional** — follows from the Pythagorean displacement construction and our coordinate definitions.                            |
| Spatial gradient of the additional coordinate              | $\frac{\partial y}{\partial x}=\frac{v}{\sqrt{c^2-v^2}}$                              | **Derived** — follows from the displacement relations.                                                                              |
| Lorentz factor expressed through the additional coordinate | $\gamma=\sqrt{1+\left(\frac{\partial y}{\partial x}\right)^2}$                        | **Derived** — direct consequence of the preceding gradient.                                                                         |
| Additional-coordinate displacement rate                    | $\frac{\partial y}{\partial\tau}=\frac{v^2}{\sqrt{c^2-v^2}}$                          | **Derived** — under the constant-velocity construction.                                                                             |
| Instantaneous Lorentz interval comparison                  | $ds'^2=-dx^2=ds^2$                                                                    | **Conditional** — the instantaneous limit has been examined, but this does not establish invariance of the full spacetime interval. |
| Transformation between coordinate systems                  | Spatial and temporal displacement transformations between $\mathbf S$ and $\mathbf U$ | **Incomplete** — the full transformation and its physical interpretation need further development.                                  |

## 2. Gravitational Parameters and Characteristic Velocities

| Derivation                                             | Principal Result                                                                       | Current Status                                                                                                          |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Radial gradient of gravitational acceleration          | $\delta(M,R)=\left                                                                     | \frac{dg}{dR}\right                                                                                                     | =\frac{2GM}{R^3}$ | **Derived** — provided $\delta$ is explicitly defined as the magnitude of the gradient. |
| Cube root of the gravitational gradient                | $\omega=\left(\frac{2GM}{R^3}\right)^{1/3}$                                            | **Derived** — algebraically established; physical interpretation remains open.                                          |
| Earth gravitational parameter comparison               | Numerical comparison between $\omega_\oplus$ and $\alpha(2-\alpha)$                    | **Incomplete** — numerical agreement does not independently establish the relationship.                                 |
| Electromagnetic characteristic velocity                | Expression involving $e$, $\mu_0$, $\epsilon_0$, and $h$, leading to $\gamma_{\rm em}$ | **Incomplete** — requires dimensional analysis and an independent derivation of the electromagnetic relationship.       |
| Earth kinematic velocity                               | $v=c\sqrt{1-\gamma_{\rm em}^{-2}}$                                                     | **Conditional** — follows from the proposed electromagnetic Lorentz factor, whose physical basis remains unestablished. |
| Cosmological velocity                                  | $v_{\rm cosmo}=c\sqrt{1-\varphi^{-2}}$                                                 | **Needs correction** — the definition of $\varphi$ has unresolved dimensional and integration-limit problems.           |
| Kinematic velocity from the trigonometric construction | Numerical result near $371{,}580\ \mathrm{m/s}$                                        | **Needs correction** — the derivation contains unresolved dimensional inconsistencies.                                  |
| Solar and planetary gravitational relationships        | Proposed relationships involving $\Gamma(\sigma)$, spin, and gravitational parameters  | **Incomplete** — the functional dependence has not yet been derived.                                                    |

## 3. Orbital Motion

| Derivation                                       | Principal Result                                                          | Current Status                                                                                                                          |
| ------------------------------------------------ | ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Trigonometric orbital construction               | Geometric relationship between radial displacement and tangential motion  | **Incomplete** — the starting equation and its dimensions need to be reconciled.                                                        |
| Galactic orbital velocity                        | $v_{\rm orbit}(M,R)=\frac{\sqrt{GM(GM+2R^3)}}{R^2}$                       | **Needs correction** — the expression appears dimensionally inconsistent as currently written.                                          |
| Milky Way solar-neighborhood velocity comparison | Numerical estimate of approximately $216{,}874\ \mathrm{m/s}$             | **Conditional** — depends on the proposed orbital formula and enclosed mass.                                                            |
| Stable circular orbit interpretation             | Relationship between gravitational displacement and stable orbital motion | **Incomplete** — the distinction between escape velocity, circular velocity, and the model's proposed velocity needs to be established. |

## 4. Fifth-Dimensional Geometry and the Metric

| Derivation                                         | Principal Result                                                           | Current Status                                                                                                                      |
| -------------------------------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Fifth-dimensional displacement                     | $dy=v\tau\sqrt{\gamma^2-1}$                                                | **Derived** — within the proposed geometric construction.                                                                           |
| Five-dimensional line element                      | $dS^2=g_{\mu\nu}dx^\mu dx^\nu+G_{44}dy^2$                                  | **Conditional** — a metric ansatz, not yet derived from the displacement construction.                                              |
| Five-dimensional metric tensor                     | $G_{AB}=\begin{pmatrix}g_{\mu\nu}&0\\0&G_{44}\end{pmatrix}$                | **Conditional** — assumes a diagonal metric with no mixed components.                                                               |
| Fifth-dimensional Christoffel symbol               | $\Gamma^R_{44}=-\frac12g^{RR}\frac{\partial G_{44}}{\partial R}$           | **Derived** — for the diagonal metric ansatz and radial dependence of $G_{44}$.                                                     |
| Fifth-dimensional metric in the co-moving frame    | $G_{44}^{(U)}=1$                                                           | **Conditional** — obtained through the proposed line-element comparison; the transformation between frames needs to be established. |
| Fifth-dimensional metric in the stationary frame   | $G_{44}^{(S)}=0$                                                           | **Needs correction** — this would make the metric degenerate if interpreted as an actual metric component.                          |
| Radial dependence of $G_{44}$                      | Gravitationally dependent fifth-dimensional metric component               | **Incomplete** — our immediate next derivation.                                                                                     |
| Relationship between $G_{44}$ and the radion field | Interpretation of the extra-dimensional metric component as a scalar field | **Incomplete** — physical identification and normalization have not been established.                                               |
| Five-dimensional geodesic equations                | Equations governing motion through the additional coordinate               | **Incomplete** — must be derived from the full metric, with conserved quantities identified where applicable.                       |

## 5. Radial Embedding and Relativistic Orbital Motion

| Derivation                                          | Principal Result                                                      | Current Status                                                                                                                   |
| --------------------------------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Radial embedding in an additional spatial dimension | $d\ell^2=dR^2+R^2d\phi^2+dy^2$                                        | **Derived** — under the assumed flat ambient spatial geometry.                                                                   |
| Induced radial metric                               | $A(R)=1+\left(\frac{dy}{dR}\right)^2$                                 | **Derived** — follows directly from the embedding.                                                                               |
| Induced spatial line element                        | $d\ell_{\rm ind}^2=A(R)dR^2+R^2d\phi^2$                               | **Derived** — follows from the radial embedding.                                                                                 |
| Spatial geodesic equation                           | Orbit equation derived from the induced spatial metric                | **Derived** — for spatial geodesics; this alone does not establish spacetime geodesics.                                          |
| Schwarzschild spatial embedding                     | $A(R)=\frac{1}{1-r_s/R}$                                              | **Standard result reproduced** — matches the Schwarzschild spatial metric but has not been independently derived from our model. |
| Embedded radial coordinate                          | $y(R)=\pm2\sqrt{r_s(R-r_s)}+C$                                        | **Derived** — follows from matching the induced metric to the Schwarzschild spatial slice.                                       |
| Static spacetime metric                             | $ds^2=-N(R)^2c^2dt^2+A(R)dR^2+R^2d\phi^2$                             | **Conditional** — assumes a static, diagonal spacetime metric.                                                                   |
| Schwarzschild temporal metric relation              | $N^2(R)=\frac{1}{A(R)}$                                               | **Standard result reproduced** — imposed through the Schwarzschild metric, not derived from our embedding.                       |
| Conserved energy and angular momentum               | First integrals of the static spacetime geodesic equations            | **Derived** — conditional on the assumed metric symmetries.                                                                      |
| Schwarzschild radial first integral                 | Radial motion expressed through conserved energy and angular momentum | **Standard result reproduced** — follows from the Schwarzschild metric.                                                          |
| Relativistic orbital equation                       | $u''+u=\frac{GM}{L^2}+\frac{3GM}{c^2}u^2$                             | **Standard result reproduced** — the Schwarzschild orbit equation.                                                               |
| Perihelion precession                               | $\Delta\phi=\frac{6\pi GM}{a(1-e^2)c^2}$                              | **Standard result reproduced** — the standard GR result, not yet an independent prediction of our model.                         |

## 6. The Precession and $G_{44}(R)$ Investigation

| Derivation                                      | Principal Result                                                           | Current Status                                                                                                                                            |
| ----------------------------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fifth-coordinate conserved momentum             | $q=G_{44}\frac{dy}{d\lambda}$                                              | **Conditional** — valid if the metric is independent of $y$, making $y$ a cyclic coordinate.                                                              |
| Radial force from the fifth-dimensional metric  | Radial contribution proportional to $\partial_R G_{44}$                    | **Incomplete** — must be derived carefully from the five-dimensional geodesic Lagrangian.                                                                 |
| Five-dimensional orbital equation               | Orbit equation containing $G_{44}(R)$ and its radial derivative            | **Incomplete** — the previous expression must be re-derived with all assumptions explicit.                                                                |
| Radial dependence required for precession       | Candidate $G_{44}(R)$ containing both $R^{-1}$ and $R^{-3}$ terms          | **Conditional** — obtained by matching the desired relativistic orbital correction.                                                                       |
| Candidate metric component                      | $G_{44}(R)=\left[1-\frac{2GM}{q^2R}-\frac{2GML^2}{q^2c^2R^3}\right]^{-1}$  | **Needs correction** — dependence on the test particle's angular momentum $L$ is a serious problem for interpreting this as a universal spacetime metric. |
| Independent prediction of perihelion precession | Deriving the correction without inserting the Schwarzschild orbit equation | **Not yet derived** — the key test of the model.                                                                                                          |

## 7. Recommended Next Derivations

The immediate objective is to determine whether our five-dimensional metric can produce the relativistic orbital correction without making the metric depend on the angular momentum of an individual test particle.

The work should proceed in this order:

1. Establish the exact five-dimensional metric and its coordinate assumptions.
2. Derive the five-dimensional geodesic Lagrangian.
3. Derive the radial equation and eliminate the affine parameter.
4. Obtain the orbital equation in terms of $u=1/R$.
5. Determine whether a universal $G_{44}(R)$ produces the $u^2$ relativistic correction.
6. Determine whether the resulting orbit predicts perihelion precession independently.

**The objective is to derive the relativistic correction from our geometry, not to build the correction into the metric by matching Schwarzschild.**
