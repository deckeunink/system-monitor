#!/usr/bin/env python3
"""
Основной модуль системы мониторинга
"""

import time
import schedule
from metrics.cpu_monitor import CPUMonitor
from metrics.memory_monitor import MemoryMonitor
from metrics.disk_monitor import DiskMonitor
from alerts.alert_manager import AlertManager
from utils.logger import setup_logger

class SystemMonitor:
    def __init__(self):
        self.logger = setup_logger(__name__)
        self.cpu_monitor = CPUMonitor()
        self.memory_monitor = MemoryMonitor()
        self.disk_monitor = DiskMonitor()
        self.alert_manager = AlertManager()
        
    def collect_metrics(self):
        """Сбор всех метрик системы"""
        try:
            metrics = {
                'timestamp': time.time(),
                'cpu': self.cpu_monitor.get_usage(),
                'memory': self.memory_monitor.get_usage(),
                'disk': self.disk_monitor.get_usage()
            }
            
            self.alert_manager.check_alerts(metrics)
            self.logger.info(f"Metrics collected: {metrics}")
            return metrics
            
        except Exception as e:
            self.logger.error(f"Error collecting metrics: {e}")
            
    def run(self):
        """Запуск мониторинга"""
        self.logger.info("Starting System Monitor...")
        
        # Запускаем сбор метрик каждую минуту
        schedule.every(1).minutes.do(self.collect_metrics)
        
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    monitor = SystemMonitor()
    monitor.run()
