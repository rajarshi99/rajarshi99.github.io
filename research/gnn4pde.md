---
title: Solving BVPs using GNN
---

## Solving boundary value problems (BVP)

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
are time tested numericals technique for solving BVP.
PRACTICALITIES;
PUT SOME LINES EXPLAINING APPLICATIONS;
INCLUDE THE TERM REGION OF INTEREST (ROI)

A mesh is generated over the ROI,
to partition the spatial domain into elements.
WRITE THE DEFINITION OF A MESH.
Let us consider 3 node triangular elements.
EXPLAIN THE SPECIAL CASE OF THE P1 FE IN 2D.

The numerical solution of a time-independent BVP
is reduced to solving a system of linear equations Ku = f.
Where K is the global stiffness matirx,
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

1. an indicator for the the node being on the boundary,

1. or if there is data involved then a flag for that

and so on.
Similarly, an edge,
which is the connection between two nodes
sharing an element
may be assigned the attributes

1. the gradient along the edge based on node attributes,

1. or the gradients on the elements of the edge is the boundary of

and so on.

EXPLAIN THE GNN

## Toy Problems

1. Take the Poi 2D problem with only Dirichlet boundary.
Generate a mesh using the Triangle package in python.
Choose a naive guess solution.
Assign the guess solution values at the nodes.
Experiment with GNN with loss being l2 err of Ku - f.
Figure out the metrics and write them.
Provide a link to a python notebook.

1. Do the same as above
but insted tweak the neighbourhood activation function
to a differential function
with the intuition of gradients and attributes.

## Conclusion

Write how good or bad it is.
How is it similar to FEM?
In what aspects can this be used in the real world?
Inverse problems?


