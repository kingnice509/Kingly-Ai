"""Music and Streaming Database Models"""
from sqlalchemy import Column, String, Boolean, DateTime, Text, Integer, Float, Enum, LargeBinary, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB, ARRAY
from datetime import datetime, timezone
import uuid
import enum

from app.database import Base


class MusicType(str, enum.Enum):
    """Music creation type"""
    ORIGINAL = "original"
    AI_GENERATED = "ai_generated"
    UPLOADED = "uploaded"
    REMIX = "remix"


class Visibility(str, enum.Enum):
    """Content visibility"""
    PUBLIC = "public"
    PRIVATE = "private"
    UNLISTED = "unlisted"


class Music(Base):
    """Music/Song Model"""
    __tablename__ = "music"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    creator_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    genre = Column(String(100), nullable=True, index=True)
    mood = Column(String(100), nullable=True)
    language = Column(String(10), default="en")
    
    # Audio Properties
    audio_url = Column(String(500), nullable=False)
    audio_duration = Column(Integer, nullable=True)  # in seconds
    audio_bitrate = Column(Integer, nullable=True)  # in kbps
    audio_format = Column(String(20), nullable=True)  # mp3, wav, flac
    waveform_data = Column(JSONB, nullable=True)
    
    # Metadata
    cover_art_url = Column(String(500), nullable=True)
    lyrics = Column(Text, nullable=True)
    bpm = Column(Integer, nullable=True)
    key = Column(String(10), nullable=True)  # C, C#, D, etc.
    
    # Publishing
    music_type = Column(Enum(MusicType), default=MusicType.UPLOADED)
    visibility = Column(Enum(Visibility), default=Visibility.PUBLIC)
    is_explicit = Column(Boolean, default=False)
    
    # Streaming Stats
    stream_count = Column(Integer, default=0)
    download_count = Column(Integer, default=0)
    like_count = Column(Integer, default=0)
    comment_count = Column(Integer, default=0)
    share_count = Column(Integer, default=0)
    
    # Engagement
    rating = Column(Float, default=0.0)
    review_count = Column(Integer, default=0)
    
    # Metadata
    tags = Column(ARRAY(String), nullable=True)
    collaborators = Column(JSONB, nullable=True)  # [{"user_id": "", "role": "producer"}]
    
    # Release Info
    release_date = Column(DateTime(timezone=True), nullable=True)
    album_name = Column(String(255), nullable=True)
    track_number = Column(Integer, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"<Music {self.title}>"


class Playlist(Base):
    """Playlist Model"""
    __tablename__ = "playlists"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    creator_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    cover_image_url = Column(String(500), nullable=True)
    
    visibility = Column(Enum(Visibility), default=Visibility.PUBLIC)
    is_collaborative = Column(Boolean, default=False)
    
    # Stats
    music_count = Column(Integer, default=0)
    like_count = Column(Integer, default=0)
    play_count = Column(Integer, default=0)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"<Playlist {self.title}>"


class PlaylistItem(Base):
    """Playlist Item (Music in Playlist)"""
    __tablename__ = "playlist_items"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    playlist_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    music_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    
    order_index = Column(Integer, nullable=False)
    added_by = Column(UUID(as_uuid=True), nullable=True)
    
    added_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"<PlaylistItem playlist:{self.playlist_id}>"


class StreamingHistory(Base):
    """User Streaming History"""
    __tablename__ = "streaming_history"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    music_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    
    played_duration = Column(Integer, nullable=True)  # in seconds
    listened_percentage = Column(Float, default=0.0)
    device_type = Column(String(50), nullable=True)
    
    played_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), index=True)
    
    def __repr__(self):
        return f"<StreamingHistory user:{self.user_id}>"


class Download(Base):
    """Music Download Record"""
    __tablename__ = "downloads"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    music_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    
    quality = Column(String(50), nullable=True)  # high, medium, low
    file_format = Column(String(20), nullable=True)  # mp3, wav, flac
    file_size = Column(Integer, nullable=True)  # in bytes
    
    downloaded_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"<Download user:{self.user_id}>"


class Like(Base):
    """Like/Favorite Record"""
    __tablename__ = "likes"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    music_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"<Like user:{self.user_id} music:{self.music_id}>"


class Comment(Base):
    """Music Comment"""
    __tablename__ = "comments"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    music_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    user_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    
    content = Column(Text, nullable=False)
    like_count = Column(Integer, default=0)
    
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"<Comment music:{self.music_id}>"
