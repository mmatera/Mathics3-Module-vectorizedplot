This is a Mathics3 Python Module that implements some of the Plot routines used in Mathics3 using the faster vectorized routines proposed by @bdlucas1.

By now, it is a proof of concept, which implements `ContourPlot3D`, `Spherical3D` and `ParametricPlot3D`.

To make these routines available:

      $ mathicsscript
      In[1]:= LoadModule["pymathics.vectorizedplot"]
      Out[1]= pymathics.vectorizedplot

      In[2]:= ContourPlot[x, {x, -2, 2}, {y, -1, 1}, Contours->{0, 0.5}, AspectRatio->Automatic]
      Out[2]:= ...

You can test with ``py.test``::

     $ pytest test

or simply::

     $ make check
