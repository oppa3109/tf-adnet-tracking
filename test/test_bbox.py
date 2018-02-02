import unittest

from boundingbox import BoundingBox
from configs import ADNetConf


class TestCommons(unittest.TestCase):
    def test_iou(self):
        a = BoundingBox(253, 66, 30, 30)
        b = BoundingBox(251, 67, 32, 32)
        iou = a.iou(b)
        iou2 = b.iou(a)
        self.assertEqual(iou, iou2)
        self.assertGreater(iou, 0.8)

    def test_do_action(self):
        ADNetConf.conf = ADNetConf(None)
        ADNetConf.conf.conf = {
            'action_move': {
                'x': 0.03, 'y': 0.03, 'w': 0.03, 'h': 0.03
            },
            'predict': {
                'stop_iou': 0.93
            }
        }

        a = BoundingBox(253, 66, 30, 30)
        b = BoundingBox(251, 67, 32, 32)
        lb = BoundingBox.get_action_label(b, a)
        self.assertIn(lb, [4, 5])
        pass
