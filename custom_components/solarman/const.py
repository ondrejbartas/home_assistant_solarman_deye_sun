from datetime import timedelta

DOMAIN = 'solarman'

DEFAULT_PORT_INVERTER = 8899
DEFAULT_INVERTER_MB_SLAVEID = 1
DEFAULT_LOOKUP_FILE = 'deye_hybrid_fast.yaml'
LOOKUP_FILES = ['deye_hybrid_fast.yaml', 'deye_hybrid.yaml', 'deye_string.yaml', 'sofar_lsw3.yaml', 'sofar_wifikit.yaml', 'solis_hybrid.yaml', 'sofar_g3hyd.yaml', 'custom_parameters.yaml']

MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=60)
MIN_TIME_BETWEEN_REALTIME_UPDATES = timedelta(seconds=10)

CONF_INVERTER_HOST = 'inverter_host'
CONF_INVERTER_PORT = 'inverter_port'
CONF_INVERTER_SERIAL = 'inverter_serial'
CONF_INVERTER_MB_SLAVEID = 'inverter_mb_slaveid'
CONF_LOOKUP_FILE = 'lookup_file'

SENSOR_PREFIX = 'Solarman'
