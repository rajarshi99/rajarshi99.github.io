# Literature Review

In academia,
people at times encounter research happening
in various different frontiers.
Specialists of similar fields,
working at their own respective frontiers,
are able to communicate
with surprising ease and efficiency.
Naturally,
knowing and understanding complicated words
and their scientific or mathematical meaning
is important.
But it is commonplace,
as a newcomer in a research domain,
to be lost in the jargon.
I begin the documentation
to give the motivation and background
in a simple and friendly manner.

## Meshing Net

Title
: [MeshingNet: A New Mesh Generation Method based on Deep Learning](https://arxiv.org/abs/2004.07016)

Authors
: Zheyan Zhang
: Yongxing Wang
: Peter K. Jimack
: and He Wang

Date
: April 2020


Let us first look into the example of
[2D linear elasticity](notes/lin_elasc_2d.pdf) problem in the paper.
A neural network is trained which has inputs

1. Boundary geometry:
Chosen from a set of polygons of 6-8 edges

2. Boundary condition:
Each edge can have only one of the following
three types of boundary conditions.
- BC1: zero displacement
- BC2: specified uniform traction in a given range
- BC3: unconstrained; which means zero traction

3. Material parameters:
Poisson's ratio and density in a given range

4. Point in the domain

The output of the NN is the target area upper bound A.
The training is carried out in a supervised fashion
the key steps to be followed are given below.

1. Create a list of problems by choosing the
boundary geometry, boundary condition, Poisson' ratio etc
and parameterise them.
So, each problem can be assigned a set of numbers.

2. Numerically solve each problem for a
Low Density Uniform Mesh (LDUM) to get a Low Accuracy Solution (LAS)
and a High Density Uniform Mesh (HDUM) to get a High Accuracy Solution (HAS).

3. Let P_i be the parameters of the i-th problem.
x_j be the center of the j-th element in the LDUM of the i-th problem
and E_ij be the error approximate for the j-th element in the LDUM of the i-th problem.
To find E_ij the HAS and LAS are used.
The NN is trained to minimise the loss

> mean square (NN(P_i, x_j) - 1/E_ij).

Now for an unseen problem we can get the
target area upper bound A.
This is used by the Triangle package
to form the non-uniform mesh.

## Turbulence Modelling

### Reynolds-averaged Navier-Stokes Equation (RANS)

### Large Eddy Simulation (LES)

### Variational Multiscale (VMS)

## ALE framework
