from enum import Enum
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from datetime import datetime
import logging

class AlertLevel(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"

@dataclass
class Alert:
    level: AlertLevel
    message: str
    timestamp: datetime
    metrics: Dict[str, Any]

class AlertChannel:
    def send_alert(self, alert: Alert) -> bool:
        raise NotImplementedError

class EmailAlertChannel(AlertChannel):
    def send_alert(self, alert: Alert) -> bool:
        # Placeholder for email implementation
        logging.info(f"Email alert: {alert.level.value} - {alert.message}")
        return True

class SlackAlertChannel(AlertChannel):
    def send_alert(self, alert: Alert) -> bool:
        # Placeholder for Slack implementation
        logging.info(f"Slack alert: {alert.level.value} - {alert.message}")
        return True

class AlertManager:
    def __init__(self):
        self.channels: List[AlertChannel] = []
        self.thresholds = {
            'cpu_percent': 80.0,
            'memory_percent': 85.0,
            'disk_usage_percent': 90.0,
            'api_error_rate': 5.0
        }
    
    def add_channel(self, channel: AlertChannel):
        """Add a new alert channel"""
        self.channels.append(channel)
    
    def check_thresholds(self, metrics: Dict[str, Any]) -> Optional[Alert]:
        """Check if metrics exceed defined thresholds"""
        alerts = []
        
        # Check CPU usage
        if metrics.get('performance', {}).get('cpu_percent', 0) > self.thresholds['cpu_percent']:
            alerts.append(Alert(
                level=AlertLevel.WARNING,
                message=f"High CPU usage: {metrics['performance']['cpu_percent']}%",
                timestamp=datetime.now(),
                metrics=metrics
            ))
        
        # Check memory usage
        if metrics.get('performance', {}).get('memory_percent', 0) > self.thresholds['memory_percent']:
            alerts.append(Alert(
                level=AlertLevel.WARNING,
                message=f"High memory usage: {metrics['performance']['memory_percent']}%",
                timestamp=datetime.now(),
                metrics=metrics
            ))
        
        # Return most severe alert if any
        return max(alerts, key=lambda x: x.level.value) if alerts else None
    
    def send_alert(self, alert_type: AlertLevel, message: str, metrics: Dict[str, Any] = None):
        """Send alert through all configured channels"""
        alert = Alert(
            level=alert_type,
            message=message,
            timestamp=datetime.now(),
            metrics=metrics or {}
        )
        
        for channel in self.channels:
            try:
                channel.send_alert(alert)
            except Exception as e:
                logging.error(f"Failed to send alert through channel {channel.__class__.__name__}: {e}")
