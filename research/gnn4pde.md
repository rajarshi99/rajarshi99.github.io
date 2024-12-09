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

## What is GNN?

## First problem

## Propositions


