"""Application Constants"""

# Music Genres
MUSIC_GENRES = [
    "Afrobeat", "Hip Hop", "Trap", "R&B", "Pop", "Soul",
    "Reggae", "Dancehall", "Amapiano", "Fuji", "Gospel",
    "Jazz", "Rock", "Country", "Electronic", "Classical",
    "House", "Techno", "Drill", "Grime", "Punk"
]

# Moods
MUSIC_MOODS = [
    "Happy", "Sad", "Energetic", "Calm", "Romantic",
    "Angry", "Melancholic", "Uplifting", "Dark", "Playful",
    "Motivational", "Peaceful", "Intense", "Dreamy", "Epic"
]

# Languages
SUPPORTED_LANGUAGES = {
    "en": "English",
    "ha": "Hausa",
    "ar": "Arabic",
    "fr": "French",
    "yo": "Yoruba",
    "ig": "Igbo",
    "es": "Spanish",
    "pt": "Portuguese",
    "sw": "Swahili",
}

# Countries
COUNTRIES = [
    "Nigeria", "Ghana", "Kenya", "South Africa", "Uganda",
    "Ethiopia", "Egypt", "Morocco", "Cameroon", "Senegal",
    "USA", "UK", "Canada", "Australia", "India",
]

# File Upload Constraints
MAX_FILE_SIZE = 500 * 1024 * 1024  # 500 MB
MAX_IMAGE_SIZE = 50 * 1024 * 1024  # 50 MB
ALLOWED_AUDIO_FORMATS = ["mp3", "wav", "flac", "m4a", "ogg"]
ALLOWED_IMAGE_FORMATS = ["jpg", "jpeg", "png", "webp", "gif"]

# API Pagination
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# Cache Keys
CACHE_USER_PREFIX = "user:"
CACHE_MUSIC_PREFIX = "music:"
CACHE_PLAYLIST_PREFIX = "playlist:"
CACHE_TRENDING_PREFIX = "trending:"
CACHE_TTL_SHORT = 300  # 5 minutes
CACHE_TTL_MEDIUM = 3600  # 1 hour
CACHE_TTL_LONG = 86400  # 24 hours

# Rate Limiting
RATE_LIMIT_AUTH_ATTEMPTS = 5
RATE_LIMIT_AUTH_WINDOW = 900  # 15 minutes
RATE_LIMIT_API_CALLS = 100
RATE_LIMIT_API_WINDOW = 3600  # 1 hour

# Payment
PAYMENT_STATUS_PENDING = "pending"
PAYMENT_STATUS_COMPLETED = "completed"
PAYMENT_STATUS_FAILED = "failed"
PAYMENT_STATUS_REFUNDED = "refunded"

# Roles
ROLE_USER = "user"
ROLE_CREATOR = "creator"
ROLE_ADMIN = "admin"
ROLE_MODERATOR = "moderator"

# Music Visibility
VISIBILITY_PUBLIC = "public"
VISIBILITY_PRIVATE = "private"
VISIBILITY_UNLISTED = "unlisted"

# Transaction Types
TRANSACTION_TYPE_DEPOSIT = "deposit"
TRANSACTION_TYPE_WITHDRAWAL = "withdrawal"
TRANSACTION_TYPE_PURCHASE = "purchase"
TRANSACTION_TYPE_EARNING = "earning"
TRANSACTION_TYPE_REFUND = "refund"

# Verification Status
VERIFICATION_STATUS_PENDING = "pending"
VERIFICATION_STATUS_VERIFIED = "verified"
VERIFICATION_STATUS_REJECTED = "rejected"
