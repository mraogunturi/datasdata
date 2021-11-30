from . import *
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'DEBUG': {
            'level': 'DEBUG',
            # 'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': 'logs/DEBUG.log',
        },
        'INFO': {
            'level': 'INFO',
            # 'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': 'logs/INFO.log',
        },
        'WARNING': {
            'level': 'WARNING',
            # 'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': 'logs/WARNING.log',
        },
        'ERROR': {
            'level': 'ERROR',
            # 'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': 'logs/ERROR.log',
        },
        'CRITICAL': {
            'level': 'CRITICAL',
            # 'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': 'logs/CRITICAL.log',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['DEBUG'],
            'propagate': True,
            'level': 'DEBUG'
        },
        'django': {
            'handlers': ['INFO'],
            'propagate': True,
            'level': 'INFO'
        },
        'django': {
            'handlers': ['WARNING'],
            'propagate': True,
            'level': 'WARNING'
        },
        'django': {
            'handlers': ['ERROR'],
            'propagate': True,
            'level': 'ERROR'
        },
        'django': {
            'handlers': ['CRITICAL'],
            'propagate': True,
            'level': 'CRITICAL'
        }
    }
}