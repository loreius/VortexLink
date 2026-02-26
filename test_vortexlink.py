# test_vortexlink.py
"""
Tests for VortexLink module.
"""

import unittest
from vortexlink import VortexLink

class TestVortexLink(unittest.TestCase):
    """Test cases for VortexLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VortexLink()
        self.assertIsInstance(instance, VortexLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VortexLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
