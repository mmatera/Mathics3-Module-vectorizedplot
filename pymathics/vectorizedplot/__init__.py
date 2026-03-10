"""
Plotting, Graphing, and Drawing

Showing something visually can be done in a number of ways:

<ul>
  <li>Starting with complete images and modifying them using the 'Image' \
      Built-in function.
  <li>Use pre-defined 2D or 3D objects like <url>
  :'Circle':
  /doc/reference-of-built-in-symbols/drawing-graphics/circle</url> and <url>
  :'Cuboid':
/doc/reference-of-built-in-symbols/plotting-graphing-and-drawing/three-dimensional-graphics/cuboid/</url> \
  and place them in a coordinate space.
  <li>Compute the points of the space using a function. This is done using functions \
  like <url>
  :'Plot':
  /doc/reference-of-built-in-symbols/plotting-graphing-and-drawing/general-graphical-plots/plot</url> \
  and <url>
  :'ListPlot':
  /doc/reference-of-built-in-symbols/plotting-graphing-and-drawing/list-plots/listplot</url>.
</ul>
"""


from pymathics.vectorizedplot.version import __version__
try:
    from pymathics.vectorizedplot.plot_plot3d import ContourPlot3D, ParametricPlot3D, SphericalPlot3D

    __all__ = (
        "ContourPlot3D",
        "ParametricPlot3D",
        "SphericalPlot3D",
        "__version__",
        "pymathics_version_data"
    )
except Exception:
    __all__ = (
        "__version__",
        "pymathics_version_data"
    )

# To be recognized as an external mathics module, the following variable
# is required:
#
pymathics_version_data = {
    "author": "The Mathics3 Team",
    "version": __version__,
    "requires": ["scikit-image"],
}

# This tells documentation how to sort this module
sort_order = "mathics.builtin.plotting-graphing-and-drawing"


