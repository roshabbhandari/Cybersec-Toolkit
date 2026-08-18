"""Recommended HTTP response headers for defensive audits."""

RECOMMENDED_HEADERS = {
    "content-security-policy": "Restrict executable and embedded content sources",
    "strict-transport-security": "Force HTTPS for supporting clients",
    "x-content-type-options": "Prevent MIME type sniffing",
    "referrer-policy": "Limit referrer information leakage",
    "permissions-policy": "Restrict browser capabilities by default",
}
