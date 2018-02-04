Modelling HII Regions With Cloudy
=================================

This repository includes all of the information you will need to reproduce the
mini-CLOUDY project that I performed as part of my PhD course at Durham
University.

The course was taught by Prof. Tom Theuns and Prof. Michele Fumagalli.

The CLOUDY parameterfile, `hii_coolstar.in`, was adapted from the one given in
the CLOUDY examples folder.

To run this you will need:

+ `python3.6.0` or higher,
+ some python packages (`pip3 install -r requirements.txt`)
+ cloudy installed in your machine.

The run scripts in `cloudy/` assume that you are using the machine in Durham,
COSMA, but should be easily changed to run anywhere.

To produce the plots, please run the `python` scripts from the `analysis`
directory. They assume that your ouputs are in the top-level directory.

To make the text, you will need:

+ pandoc
+ pandoc-crossref

These can be found through many package managers or built from source.

