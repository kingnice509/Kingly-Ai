"""Application Configuration"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings from environment variables"""
    
    # API
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Kingly AI"
    PROJECT_VERSION: str = "3.0.0"
    DEBUG: bool = False
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    ENVIRONMENT: str = "development"
    
    # Database
    DATABASE_URL: str
    DATABASE_ECHO: bool = False
    SQLALCHEMY_POOL_SIZE: int = 20
    SQLALCHEMY_MAX_OVERFLOW: int = 0
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    CACHE_TTL: int = 3600
    
    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # OAuth
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    APPLE_TEAM_ID: str
    APPLE_KEY_ID: str
    APPLE_CLIENT_ID: str
    
    # File Storage
    STORAGE_TYPE: str = "s3"  # s3 or gcs
    AWS_ACCESS_KEY_ID: Optional[str] = None
    AWS_SECRET_ACCESS_KEY: Optional[str] = None
    AWS_BUCKET_NAME: Optional[str] = None
    AWS_REGION: str = "us-east-1"
    GCS_PROJECT_ID: Optional[str] = None
    GCS_BUCKET_NAME: Optional[str] = None
    
    # Email
    SENDGRID_API_KEY: str
    SENDGRID_FROM_EMAIL: str = "noreply@kingly.com"
    
    # SMS
    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str
    TWILIO_PHONE_NUMBER: str
    
    # Payments
    PAYSTACK_PUBLIC_KEY: str
    PAYSTACK_SECRET_KEY: str
    FLUTTERWAVE_PUBLIC_KEY: str
    FLUTTERWAVE_SECRET_KEY: str
    STRIPE_PUBLIC_KEY: str
    STRIPE_SECRET_KEY: str
    STRIPE_WEBHOOK_SECRET: str
    
    # AI Services
    OPENAI_API_KEY: str
    OPENAI_ORG_ID: Optional[str] = None
    REPLICATE_API_TOKEN: str
    
    # Celery
    CELERY_BROKER_URL: str = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/2"
    
    # Monitoring
    SENTRY_DSN: Optional[str] = None
    SENTRY_TRACES_SAMPLE_RATE: float = 0.1
    
    # CORS
    CORS_ORIGINS: list = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: list = ["*"]
    CORS_ALLOW_HEADERS: list = ["*"]
    
    # Rate Limiting
    RATE_LIMIT_ENABLED: bool = True
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_PERIOD: int = 60
    
    # Email Templates
    EMAIL_VERIFICATION_TEMPLATE_ID: str = "d-verification-template"
    PASSWORD_RESET_TEMPLATE_ID: str = "d-password-reset-template"
    
    # Features
    ENABLE_AI_FEATURES: bool = True
    ENABLE_PAYMENTS: bool = True
    ENABLE_MARKETPLACE: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
