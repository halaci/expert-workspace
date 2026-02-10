"""
Unit Tests for Calculator Module
"""
import pytest
import sys
sys.path.insert(0, '../src')

from calculator import add, subtract, multiply, divide


class TestAdd:
    """Összeadás tesztek - US-001"""
    
    def test_add_positive_numbers(self):
        """AC-1: add(2, 3) == 5"""
        assert add(2, 3) == 5
    
    def test_add_negative_and_positive(self):
        """AC-2: add(-1, 1) == 0"""
        assert add(-1, 1) == 0
    
    def test_add_floats(self):
        """AC-3: add(1.5, 2.5) == 4.0"""
        assert add(1.5, 2.5) == 4.0


class TestSubtract:
    """Kivonás tesztek - US-002"""
    
    def test_subtract_basic(self):
        """AC-1: subtract(5, 3) == 2"""
        assert subtract(5, 3) == 2
    
    def test_subtract_negative_result(self):
        """AC-2: subtract(1, 5) == -4"""
        assert subtract(1, 5) == -4
    
    def test_subtract_floats(self):
        """AC-3: subtract(2.5, 1.5) == 1.0"""
        assert subtract(2.5, 1.5) == 1.0


class TestMultiply:
    """Szorzás tesztek - US-003"""
    
    def test_multiply_positive_numbers(self):
        """AC-1: multiply(2, 3) == 6"""
        assert multiply(2, 3) == 6
    
    def test_multiply_negative(self):
        """AC-2: multiply(-2, 3) == -6"""
        assert multiply(-2, 3) == -6
    
    def test_multiply_floats(self):
        """AC-3: multiply(2.5, 4) == 10.0"""
        assert multiply(2.5, 4) == 10.0
    
    def test_multiply_by_zero(self):
        """AC-4: multiply(0, 100) == 0"""
        assert multiply(0, 100) == 0


class TestDivide:
    """Osztás tesztek - US-004"""
    
    def test_divide_even(self):
        """AC-1: divide(6, 2) == 3"""
        assert divide(6, 2) == 3
    
    def test_divide_with_remainder(self):
        """AC-2: divide(7, 2) == 3.5"""
        assert divide(7, 2) == 3.5
    
    def test_divide_negative(self):
        """AC-3: divide(-6, 2) == -3"""
        assert divide(-6, 2) == -3
    
    def test_divide_by_zero(self):
        """AC-4: divide(5, 0) raises ValueError"""
        with pytest.raises(ValueError, match="Division by zero"):
            divide(5, 0)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
