---
title: Research Proposal
---

## Problem Statement

Given a Boundary Value Problem (BVP)
and a mesh over its computational domain,
optimise the coordinates of the mesh
to obtain a high accuracy Finite Element Methods (FEM) solution,
while utilising the underlying physics of the problem.

## Origin of the problem

In Science and Engineering,
quantities which are continuous functions of space and time
are modelled as a BVP.
In a BVP,
we are given a domain,
Partial Differential Equations (PDEs) to be solved
and the constraints to be imposed at the boundary of the domain.
As an example,
simulation of the airflow around an airfoil is modelled by a BVP.
Airfoils are objects of shapes which can,
for favourable airflow,
generate lift
(countering the gravitational forces)
like the wings of a turbine or aircraft.
For airflow simulation,
the Navier-Stokes Equations (NSE)
describe the physics
at each point in the domain
in the form of PDEs.
To specify the inflow, outflow
and the friction of the air with the airfoil
we impose boundary conditions
on the velocity and pressure
at the surface of the airfoil
and a rectangle around the airfoil
marking the region of interest
as described in figure \ref{bvp_airfoil}.
The first step for numerically solving such PDEs,
is to generate a mesh over the region of interest.
The FEM with nodal basis functions
for a good quality mesh and appropriate element sizes
provide accurate and reliable solutions,
but computational power can be a limiting factor
in obtaining solutions of the desired accuracy.
Our research is focused on balancing the computational cost and accuracy
to find an optimal mesh while exploiting the parallel computing possibilities.

Time-independent BVPs capture the steady state of the system,
while time-dependent ones capture the evolution.
A steady state occurs when the system no longer changes significantly with time
and the transience has died down.
The Reynolds number,
a dimensionless quantity representing the ratio of inertial to viscous forces,
is a measure of turbulence in the system.
Higher Reynolds numbers often necessitate finer grids and smaller time steps
to resolve turbulent features like eddies and vortices
while maintaining numerical stability.

## Proposed Methodologies

The goal is to begin with a coarse mesh
and optimise the mesh coordinates
to obtain solutions of enhanced accuracy.
First, we will develop the algorithm
for the 2 dimensional Poisson's problem
with [manufactured solutions](notes/mms.pdf)
as it will be good way to understand if our methods
improves accuracy.

The basic plan to be implemented
for time-independent BVP is given below.

1. To generate the initial coarse mesh,
the Triangle package in Python will be used.

2. After the assembly of the stiffness matrix and the consistent load vector
the FEM solution will be computed
using the linear solver in the Numpy or Scipy package in Python.

3. A loss function will be defined
based on a-posteriori error estimates,
like the element residual method,
which will take as inputs
the mesh coordinates and the FEM solution on the mesh.

4. An iteration of a gradient based method,
using the TensorFlow package,
will applied to tweak the mesh coordinates to reduce the loss value.
  
5. Another method which utilises the TensorFlow package
will be used corect the FEM solution for the tweaked mesh.
This will be possible as only the coordinates of the nodes have changed
and not the connections between them.

6. We have to loop through steps 4 and 5
to achieve a desirable mesh and a solution on it.

Starting from the Poisson's problem,
we will move to singularly perturbed problems,
convection-diffusion problem,
lid driven cavity problem,
channel flow problem,
flow past circular cylinder problem,
and then finally
the airfoil problem.
The airfoil specifications will be
chosen from the
National Advisory Committee for Aeronautics (NACA)
[database.](http://airfoiltools.com/search/index?m%5Bgrp%5D=naca4d&m%5Bsort%5D=1)

## On optimising mesh coordinates

Find the descripation and result
of [one of the simple ways](mesh_optim1.pdf)
of forming a mesh
by formulating a rule
based on which the node positions will be decided.
Here, the total potential is calculated
using the pairwise Morse potential between all pairs of nodes.
In my implementation,
using TensorFlow,
for finding the pairwise distances
I have used the concept of sparse matirces in the following way.
```
import tensorflow as tf

N = 65                      # Number of points

row_id = 0
indices = []
values = []
for i in range(N-1):
    for j in range(i+1,N):
        # print(i,j)
        indices.append([row_id,i])
        indices.append([row_id,j])
        values.append(1.0)
        values.append(-1.0)
        row_id += 1

diff_tf = tf.sparse.SparseTensor(indices, values, [row_id,N])
```
This sparse matrix is used
to evaluate the total potential,
defined as loss in the following code.
```
def loss(x,y):
    diffx = tf.sparse.sparse_dense_matmul(diff_tf, x)
    diffy = tf.sparse.sparse_dense_matmul(diff_tf, y)
    # Using the Morse potential
    d = tf.sqrt(diffx**2 + diffy**2) - re
    return tf.reduce_sum(tf.square(1 - tf.exp(-a*d)))
```
Note that here any type of boundary is not considered.

Another [toy problem](mesh_optim2.pdf)
shows how mesh coordinates can be optimised
using a gradient descent stratergy.
As an example, the objective function
considered is the variation in the area of the elements.
Here the boundary nodes are not moved
as the gradients are not applied on them.
