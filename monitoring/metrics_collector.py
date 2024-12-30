import psutil
import time
from typing import Dict, Any
from dataclasses import dataclass
from datetime import datetime

@dataclass
class PerformanceMetrics:
    cpu_percent: float
    memory_percent: float
    disk_usage_percent: float
    timestamp: datetime

class MetricsCollector:
    """Collects various system and application metrics"""
    
    def __init__(self):
        self.last_api_stats = {}
        self.plugin_stats = {}
    
    def collect_memory_usage(self) -> Dict[str, float]:
        """Collect memory usage statistics"""
        vm = psutil.virtual_memory()
        return {
            'total': vm.total,
            'available': vm.available,
            'percent': vm.percent,
            'used': vm.used,
            'free': vm.free
        }
    
    def collect_performance_metrics(self) -> PerformanceMetrics:
        """Collect system performance metrics"""
        return PerformanceMetrics(
            cpu_percent=psutil.cpu_percent(interval=1),
            memory_percent=psutil.virtual_memory().percent,
            disk_usage_percent=psutil.disk_usage('/').percent,
            timestamp=datetime.now()
        )
    
    def collect_api_stats(self) -> Dict[str, Any]:
        """Collect API usage statistics"""
        # Placeholder - integrate with actual API tracking
        return {
            'total_requests': 0,
            'success_rate': 100.0,
            'avg_response_time': 0.0,
            'active_connections': 0
        }
    
    def collect_plugin_usage(self) -> Dict[str, Any]:
        """Collect plugin usage statistics"""
        # Placeholder - integrate with plugin system
        return {
            'active_plugins': 0,
            'plugin_errors': 0,
            'plugin_load_time': 0.0
        }
    
    def collect_all_metrics(self) -> Dict[str, Any]:
        """Collect all available metrics"""
        perf_metrics = self.collect_performance_metrics()
        return {
            'timestamp': datetime.now().isoformat(),
            'memory': self.collect_memory_usage(),
            'performance': {
                'cpu_percent': perf_metrics.cpu_percent,
                'memory_percent': perf_metrics.memory_percent,
                'disk_usage_percent': perf_metrics.disk_usage_percent
            },
            'api': self.collect_api_stats(),
            'plugins': self.collect_plugin_usage()
        }
