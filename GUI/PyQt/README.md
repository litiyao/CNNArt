# CNNArtGUI

This GUI is designed with PyQt5 and works for Python >2.7 and >3.5.

## GUI calling
`Qt_main.py`<br/>
to open the GUI. This GUI can be run independent from CNNArt.

### Requirements
`pip3 install matplotlib PyQt5 dicom pyyaml scipy numpy dicom_numpy h5py pandas sklearn keras tensorflow`

## GUI features
- data viewing (DICOM, natural scene images)
- preprocessing: labeling/annotation, patching, data augmentation, data splitting
- network training: hyperparameter setting and network selection
- test data evaluation: online accuracy/loss plots, confusion matrix, derived test metrics
- network visualization: architecture, feature maps, kernel weights, deep visualization

### Data viewing
- image viewing: flexible layout, 2D/3D mode, images can be loaded from python workspace
- prediction overlay: colors and hatches can be modified
- labeling: 3 selector(rectangle, ellipse, lasso), the name and color of the labels can be modified

### Network training
- data preprocessing, parameter setting
- accuracy/loss curves can be dynamically plotted

### Network visualization 
- network structure: the network structure can be loaded from h5 file
- view feature maps and kernels
- envoke deep visualization from a test data image
