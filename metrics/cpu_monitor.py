import psutil
from utils.logger import setup_logger

class CPUMonitor:
    def __init__(self):
        self.logger = setup_logger(__name__)
        
    def get_usage(self):
        """Получить использование CPU"""
        try:
            usage = psutil.cpu_percent(interval=1)
            return {
                'percent': usage,
                'cores': psutil.cpu_count(),
                'load_avg': psutil.getloadavg() if hasattr(psutil, 'getloadavg') else None
            }
        except Exception as e:
            self.logger.error(f"Error getting CPU usage: {e}")
            return None
