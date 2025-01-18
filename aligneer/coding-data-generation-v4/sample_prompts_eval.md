Given the following existing code, there is a bug with in, please generate the proper working code: from the following user complaint.

Objective: Proper way to get unsigned angles between 0 and 180 for histogram of gradients.

Description:

Currently I have code that computes the magnitude and orientation from the Sobel dervatives.
```python
mag, ang = cv2.cartToPolar(gx, gy, angleInDegrees=True)
ang = ang.clip(min=0, max=179.99999)
```
Long story short, how can I force angles to be unsigned and between [0, 180) degrees without clipping which seems to screw up the histogram distribution.

Is there a numpy function that would take a angle greater than 180, for example 200, and split out 160 or do I have to code something like that up myself.

Would it be possibly to makes the numpy array only contain values from -180 to 180 and then I could just take the abs value.