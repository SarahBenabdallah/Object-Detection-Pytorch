def in_polygon(poly, point):
    lats = []
    longs = []
    res = []
    xp = point[0]
    yp = point[1]
    for i in range(len(poly)):
        lats.append(poly[i][0])
        longs.append(poly[i][1])
    for i in range(len(lats)):
        # result = (yp - y1) * (x2 - x1) - (xp - x1) * (y2 - y1)
        result = (yp - longs[i]) * (
            lats[(i+1) % len(lats)] - lats[i]) - (
            xp - lats[i]) * (
            longs[(i+1) % len(lats)] - longs[i])
        res.append(result)
    if all(i >= 0 for i in res) or all(i <= 0 for i in res):
        return (True)
    else:
        return (False)
