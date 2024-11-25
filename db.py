from typing import Dict, Optional
import hmac
import hashlib

API_KEYS: Dict[str, str] = {
    "bob_api_key_value": hashlib.sha256(b"7oDYjo3d9r58EJKYi5x4E8").hexdigest(),
    "alice_api_key_value": hashlib.sha256(b"mUP7PpTHmFAkxcQLWKMY8t").hexdigest()
}

USERS: Dict[str, Dict[str, str]] = {
    hashlib.sha256(b"7oDYjo3d9r58EJKYi5x4E8").hexdigest(): {"name": "Bob"},
    hashlib.sha256(b"mUP7PpTHmFAkxcQLWKMY8t").hexdigest(): {"name": "Alice"}
}

def check_api_key(api_key: str) -> bool:
    """Verify API key with constant-time comparison."""
    if not api_key:
        return False
    return any(hmac.compare_digest(k, api_key) for k in API_KEYS.keys())

def get_user_from_api_key(api_key: str) -> Optional[Dict[str, str]]:
    """Get user from API key securely."""
    if not api_key:
        return None
    user_id = API_KEYS.get(api_key)
    return USERS.get(user_id) if user_id else None
