Members: Ryan Danehy, and Brandon Fisher

We propose a neural network that is trained to count the number of cells in a
image of a eye. We will be in collaboration with Dr Donald Miller of the IU
School of Optometry, who specializes in detailed imaging of the human retina.
Currently Dr. Miller manually counts each cell which is very time consuming. We
believe we can save him tons of time by implementing a service that counts for
him.

The idea behind using the neural network is that it can be used to find the
optimal combination of filters to use to detect the edges, delimit, and count
the cells. Assuming Dr Miller has a nice dataset handy with precounted images
(or images that we can count ourselves), there should be a sufficient amount of
training data to create a nice model. It will also be very important for us to
consider the end product's ease of use by a group who may have vastly different
technical skills from those of us in engineering. Therefore, this project will
likely also include the creation of some kind of encapsulating program and GUI
to allow the users to interface with our cloud hosted REST service.
