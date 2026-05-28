from typing import List, Dict


def calculate_fps(frames: int, elapsed_time: float) -> float:
    """Calculate frames per second.

    Args:
        frames (int): Number of frames rendered.
        elapsed_time (float): Time taken to render frames in seconds.

    Returns:
        float: Calculated frames per second.
    """
    if elapsed_time <= 0:
        return 0.0
    return frames / elapsed_time


def average_frame_time(fps: List[float]) -> float:
    """Calculate average frame time from FPS list.

    Args:
        fps (List[float]): List of frames per second values.

    Returns:
        float: Average frame time in milliseconds.
    """
    if not fps:
        return 0.0
    avg_fps = sum(fps) / len(fps)
    return (1000.0 / avg_fps) if avg_fps > 0 else 0.0


def log_performance_metrics(metrics: Dict[str, float]) -> None:
    """Log performance metrics to console.

    Args:
        metrics (Dict[str, float]): Dictionary containing performance metrics.
    """
    for key, value in metrics.items():
        print(f"{key}: {value}")
