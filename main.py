import math
import random

import numpy as np
import cv2

img = np.zeros((2340, 1080, 1), np.uint8)
img[:, :] = 255


def draw_angled_rec(x0, y0, width, height, angle, img, color, line_w):
    _angle = angle * math.pi / 180.0
    b = math.cos(_angle) * 0.5
    a = math.sin(_angle) * 0.5
    pt0 = (int(x0 - a * height - b * width),
           int(y0 + b * height - a * width))
    pt1 = (int(x0 + a * height - b * width),
           int(y0 - b * height - a * width))
    pt2 = (int(2 * x0 - pt0[0]), int(2 * y0 - pt0[1]))
    pt3 = (int(2 * x0 - pt1[0]), int(2 * y0 - pt1[1]))

    cv2.line(img, pt0, pt1, color, line_w)
    cv2.line(img, pt1, pt2, color, line_w)
    cv2.line(img, pt2, pt3, color, line_w)
    cv2.line(img, pt3, pt0, color, line_w)

    return img


lado_q = img.shape[1] / 13

emb = 0
for y in range(int(lado_q//2), img.shape[0]-int(lado_q), int(lado_q)):
    for x in range(int(lado_q//2), img.shape[1]-int(lado_q), int(lado_q)):
        img = draw_angled_rec(random.randint((x + lado_q // 2) - emb, (x + lado_q // 2) + emb),
                              random.randint((y + lado_q // 2) -
                                             emb, (y + lado_q // 2) + emb),
                              lado_q, lado_q,
                              random.uniform(float(f"-{emb}"), emb),
                              img, 0, 4)
    emb += random.randint(0, 3)

cv2.imwrite("Lindomar Rodrigues, Schotter.png", img)
