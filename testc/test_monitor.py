import unittest
from unittest.mock import Mock, patch
from src.monitor import SystemMonitor

class TestSystemMonitor(unittest.TestCase):
    
    def setUp(self):
        self.monitor = SystemMonitor()
        
    @patch('src.monitor.CPUMonitor')
    @patch('src.monitor.MemoryMonitor')
    def test_collect_metrics(self, mock_memory, mock_cpu):
        # Mock the metrics
        mock_cpu.return_value.get_usage.return_value = {'percent': 50}
        mock_memory.return_value.get_usage.return_value = {'percent': 60}
        
        metrics = self.monitor.collect_metrics()
        
        self.assertIsNotNone(metrics)
        self.assertIn('cpu', metrics)
        self.assertIn('memory', metrics)

if __name__ == '__main__':
    unittest.main()
