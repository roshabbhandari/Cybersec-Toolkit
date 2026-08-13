# Error Handling

Modules should return useful errors instead of terminating the entire application. File-not-found, permission, malformed-input, and network failures should be handled at the module boundary when practical.

CLI code should turn those results into concise messages for the user.
