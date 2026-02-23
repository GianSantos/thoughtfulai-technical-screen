from unittest import TestCase

from package_sorter import sort, Package

class TestPackageSorting(TestCase):
    def test_standard_package(self):
        self.assertEqual(sort(10, 10, 10, 5), Package.STANDARD.value)

    def test_special_package_due_to_dimension(self):
        self.assertEqual(sort(150, 10, 10, 5), Package.SPECIAL.value)

    def test_special_package_due_to_volume(self):
        self.assertEqual(sort(100, 100, 100, 5), Package.SPECIAL.value)

    def test_rejected_package_due_to_heavy_and_bulky(self):
        self.assertEqual(sort(150, 150, 150, 20), Package.REJECTED.value)

    def test_rejected_package_due_to_negative_dimension(self):
        self.assertEqual(sort(-10, 10, 10, 5), Package.REJECTED.value)

    def test_rejected_package_due_to_zero_mass(self):
        self.assertEqual(sort(10, 10, 10, 0), Package.REJECTED.value)