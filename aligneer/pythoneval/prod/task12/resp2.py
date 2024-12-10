import pytest
import cv2
import numpy as np
from main import process_frame

@pytest.fixture
def sample_frame():
    # Create a simple 100x100 test frame
    return np.ones((100, 100, 3), dtype=np.uint8) * 255

def test_normal_processing(sample_frame):
    """Test normal case with valid frame"""
    result = process_frame(sample_frame)
    assert result is not None
    assert isinstance(result, np.ndarray)
    assert result.shape[:2] == sample_frame.shape[:2]  # Output should maintain dimensions

def test_null_frame():
    """Test handling of None input"""
    with pytest.raises(TypeError):
        process_frame(None)

def test_empty_frame():
    """Test handling of empty frame"""
    empty_frame = np.array([])
    with pytest.raises(cv2.error):
        process_frame(empty_frame)

def test_large_frame():
    """Test processing of large images"""
    large_frame = np.ones((4000, 4000, 3), dtype=np.uint8)
    result = process_frame(large_frame)
    assert result.shape == (4000, 4000)

def test_invalid_dimensions():
    """Test handling of frames with invalid dimensions"""
    invalid_frame = np.ones((100, 100), dtype=np.uint8)  # Missing channel dimension
    with pytest.raises(cv2.error):
        process_frame(invalid_frame)

def test_invalid_dtype():
    """Test handling of frames with invalid data types"""
    invalid_frame = np.ones((100, 100, 3), dtype=np.float64)  # Wrong dtype
    with pytest.raises(cv2.error):
        process_frame(invalid_frame)

@pytest.mark.performance
def test_processing_time(sample_frame):
    """Test processing time is within acceptable limits"""
    import time
    start_time = time.time()
    process_frame(sample_frame)
    processing_time = time.time() - start_time
    assert processing_time < 0.1  # Should process within 100ms
