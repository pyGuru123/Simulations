import math

radius = 160

def toRadian(theta):
    return theta * math.pi / 180

def toDegrees(theta):
    return theta * 180 / math.pi

def getGradient(p1, p2):
    if p1[0] == p2[0]:
        m = toRadian(90)
    else:
        m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    return m

def getAngleFromGradient(gradient):
    return math.atan(gradient)

def getAngle(pos, origin):
    m = getGradient(pos, origin)
    thetaRad = getAngleFromGradient(m)
    theta = round(toDegrees(thetaRad), 2)
    return theta

def getPosOnCircumeference(theta, origin):
    theta = toRadian(theta)
    x = origin[0] + radius * math.cos(theta)
    y = origin[1] + radius * math.sin(theta)
    return (x, y)