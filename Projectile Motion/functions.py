import math

def toRadian(theta):
    return theta * math.pi / 180

def toDegrees(theta):
    return theta * 180 / math.pi

def getGradient(p1, p2):
    if p1[0] == p2[0]:
        m = 1.5707963268
    else:
        m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    return m

def getAngleFromGradient(gradient):
    return math.atan(gradient)

def getAngle(pos, origin):
    m = getGradient(pos, origin)
    thetaRad = getAngleFromGradient(m)
    theta = toDegrees(thetaRad)
    return abs(theta)