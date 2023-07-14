# basic/test_introspection.py
def test_assert_introspection():
    x = y = 0              # with unittest.py
    assert x               # self.assertTrue(x)
    assert x == 1          # self.assertEqual(x, 1)
    assert x != 2          # self.assertNotEqual(x, 2)
    assert not x           # self.assertFalse(x)
    assert x < 3 or y > 5  # ?
