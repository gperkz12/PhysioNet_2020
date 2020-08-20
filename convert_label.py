import numpy as np

def convert_label(label,classes):
    newlabel = []
    for i in range(len(label)):
        # First remove the trailing newline characters
        label[i] = label[i].rstrip()
        # Now compare with the possible classes
        tmpidx = classes.index(label[i])
        newlabel.append(tmpidx)

    return newlabel
