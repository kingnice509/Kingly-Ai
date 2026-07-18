"""User Database Models"""
from sqlalchemy import Column, String, Boolean, DateTime, Text, Integer, Enum, LargeBinary
from sqlalchemy.dialects.postgresql import UUID, JSONB
from datetime import datetime, timezone
import uuid
import enum

from app.database import Base


class UserRole(str, enum.Enum):
    """User roles"""
    USER = "user"
    CREATOR = "creator"
    ADMIN = "admin"
    MODERATOR = "moderator"


class AccountStatus(str, enum.Enum):
    """Account status"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    DELETED = "deleted"


class User(Base):
    """User Model"""
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=True)
    display_name = Column(String(100), nullable=True)
    bio = Column(Text, nullable=True)
    profile_photo_url = Column(String(500), nullable=True)
    cover_image_url = Column(String(500), nullable=True)
    country = Column(String(100), nullable=True)
    language = Column(String(10), default="en")
    phone_number = Column(String(20), nullable=True, unique=True, index=True)
    phone_verified = Column(Boolean, default=False)
    email_verified = Column(Boolean, default=False)
    verification_badge = Column(Boolean, default=False)
    two_factor_enabled = Column(Boolean, default=False)
    two_factor_method = Column(String(50), nullable=True)  # authenticator, sms, email
    
    role = Column(Enum(UserRole), default=UserRole.USER)
    account_status = Column(Enum(AccountStatus), default=AccountStatus.ACTIVE)
    
    followers_count = Column(Integer, default=0)
    following_count = Column(Integer, default=0)
    total_earnings = Column(String(20), default="0")  # Store as string for precision
    
    social_links = Column(JSONB, nullable=True)  # {"twitter": "...", "instagram": "..."}
    preferences = Column(JSONB, nullable=True)  # {"theme": "dark", "notifications": true}
    
    last_login = Column(DateTime(timezone=True), nullable=True)
    last_password_change = Column(DateTime(timezone=True), nullable=True)
    
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    deleted_at = Column(DateTime(timezone=True), nullable=True)
    
    def __repr__(self):
        return f"<User {self.username}>"
    
    def is_active(self) -> bool:
        return self.account_status == AccountStatus.ACTIVE
    
    def is_admin(self) -> bool:
        return self.role in [UserRole.ADMIN, UserRole.MODERATOR]
    
    def is_creator(self) -> bool:
        return self.role in [UserRole.CREATOR, UserRole.ADMIN]


class OAuthAccount(Base):
    """OAuth Account Linking"""
    __tablename__ = "oauth_accounts"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    provider = Column(String(50), nullable=False)  # google, apple, facebook
    provider_user_id = Column(String(255), nullable=False)
    provider_email = Column(String(255), nullable=True)
    access_token = Column(Text, nullable=True)
    refresh_token = Column(Text, nullable=True)
    token_expires_at = Column(DateTime(timezone=True), nullable=True)
    
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"<OAuthAccount {self.provider}:{self.user_id}>"


class DeviceSession(Base):
    """Device Session Management"""
    __tablename__ = "device_sessions"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    device_name = Column(String(255), nullable=True)
    device_type = Column(String(50), nullable=True)  # mobile, web, tablet
    device_os = Column(String(50), nullable=True)  # iOS, Android, Windows, Linux, macOS
    device_fingerprint = Column(String(255), nullable=True, unique=True)
    ip_address = Column(String(45), nullable=True)
    user_agent = Column(Text, nullable=True)
    
    access_token = Column(Text, nullable=True)
    refresh_token = Column(Text, nullable=True)
    token_expires_at = Column(DateTime(timezone=True), nullable=True)
    
    last_activity = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    is_active = Column(Boolean, default=True)
    
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"<DeviceSession {self.device_name}>"
