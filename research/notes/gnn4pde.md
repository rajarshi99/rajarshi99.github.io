---
title: Solving BVPs using GNN
author: Rajarshi
---

## Solving Boundary Value Problems (BVPs)

A BVP is posed
by specifying a

1. domain,

1. boundary conditions to be imposed
for an unknown function
defined on the domain

1. and the partial differential equations (PDE)
to be satisfied by the function.

The solution for the BVP
entails finding the unknown function.
Finite element methods (FEM)
are time tested numerical techniques for solving BVPs.
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
marking the
[region of interest](notes/roi.pdf)
(ROI).

A mesh is generated over the ROI,
to partition the spatial domain into elements.
For a point in a 3 node triangular element,
the mesh consists of nodes,
with coordinates and an indicator of being on the boundary,
and triplets of nodes forming a triangular cells (or elements)
which partition the domain.
The value of the unknown function
for a point inside a cell
is found by interpolating the values on the nodes of the cell
serving as degrees of freedom.
By applying the weak form of the PDE for each element
we arrive at the element level undetermined system
of 3 linear equations in 3 unknowns,
which are the values of the unknown function at the nodes (of the element).
Once we assemble all the equations
for the free nodes (free of the Dirichlet boundary),
the numerical solution of a time-independent BVP
is reduced to solving a system of linear equations Ku = f.
Where K is the global stiffness matrix,
f is consistent load vector
and u is the unknown vector.
The i-th entry of u
is the value of the function to be found
at the i-th free node.

WRITE ABOUT LINEAR SOLVER;
DIRECT AND ITERATIVE

## Graph Neural Network

A [Graph](https://en.wikipedia.org/wiki/Graph_theory)
is a mathematical construct
defined by a set of vertices and edges.
Several real world scenarios can be modelled by graphs,
by assigning meaning,
or attributes,
to the vertices (or nodes) and edges.
The underlying mesh of an FEM solver
can be thought of as Graph,
where each node may be assigned attributes like

1. the coordinates,

1. proposed value of the unknown function u,

1. an indicator for the node being on the boundary,

1. or if there is data involved then a flag for that

and so on.
Similarly, an edge,
which is the connection between two nodes
sharing an element
may be assigned the attributes

1. the gradient along the edge based on node attributes,

1. or the gradients on the elements of the edge is the boundary of

and so on.

Graph Convolution Network (GCN)
is a type of GNN.
Here we only work with node attributes.

## Toy Problems

1. Take a Poisson's 2D problem with only Dirichlet boundary.
Generate a mesh using the Triangle package in python.
Choose a naive guess solution.
Assign the guess solution values at the nodes.
Experiment with Graph Convolution Network (GCN)
with loss being a norm of Ku - f.

## Conclusion

Write how good or bad it is.
How is it similar to FEM?
In what aspects can this be used in the real world?
Inverse problems?


