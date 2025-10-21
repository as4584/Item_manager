"""
Custom exceptions for infrastructure layer.
"""


class LightspeedAPIError(Exception):
    """Base exception for Lightspeed API errors."""
    pass


class LightspeedAuthError(LightspeedAPIError):
    """Raised when authentication fails (401)."""
    pass


class LightspeedRateLimitError(LightspeedAPIError):
    """Raised when rate limit is exceeded (429)."""
    pass


class LightspeedNotFoundError(LightspeedAPIError):
    """Raised when resource is not found (404)."""
    pass


class LightspeedServerError(LightspeedAPIError):
    """Raised for server errors (5xx)."""
    pass
