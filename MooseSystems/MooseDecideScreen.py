def importFiles():
    import sys
    import pathlib

    current = pathlib.Path(__file__).parent.absolute()
    sys.path.append(str(current)+'/Kernels/')
    import kernels
