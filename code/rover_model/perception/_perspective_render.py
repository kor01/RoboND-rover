import numpy as np
import matplotlib.pyplot as plt


class PerspectiveRender(object):

  def __init__(self, scale, resolution):

    self._scale = scale
    self._resolution = resolution

  def render(self, particles, inplace=False):
    particles = particles * self._scale
    particles[:, 1] *= -1
    particles[:, 1] += self._resolution / 2
    particles = np.around(particles).astype('uint32')
    particles[:, 0] = self._resolution - particles[:, 0]
    particles = particles.clip(0, self._resolution - 1)
    render = np.zeros([self._resolution, self._resolution], dtype=np.uint8)
    render[particles[:, 0], particles[:, 1]] += 1
    if inplace:
      plt.imshow(render)
      plt.show()
    return render


def highlight_position(mp : np.ndarray, x, y):
    mp = np.asarray(mp).copy()
    x = int(np.around(x))
    y = int(np.around(y))
    y_max = mp.shape[0]
    x_max = mp.shape[1]
    xs = [max(x-1, 0), x, min(x+1, y_max - 1)]
    ys = [max(y-1, 0), y, min(y+1, x_max - 1)]
    for x in xs:
        for y in ys:
            mp[y_max - y, x, 0] = 128
    return mp
