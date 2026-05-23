from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum
import json


class Platform(str, Enum):
    TWITCH = "twitch"
    YOUTUBE = "youtube"
    DISCORD = "discord"


class EventType(str, Enum):
    CHAT_MESSAGE = "chat_message"
    DONATION = "donation"
    SUBSCRIPTION = "subscription"
    RAID = "raid"
    MILESTONE = "milestone"
    MODERATION_FLAG = "moderation_flag"
    SCREEN_FRAME = "screen_frame"
    AUDIO_TRANSCRIPT = "audio_transcript"
    METRIC_UPDATE = "metric_update"


@dataclass
class StreamEvent:
    platform: str
    event_type: str
    session_id: str
    payload: dict
    timestamp: str  # ISO 8601

    def to_bytes(self) -> bytes:
        return json.dumps(asdict(self)).encode("utf-8")

    @classmethod
    def from_bytes(cls, data: bytes) -> "StreamEvent":
        return cls(**json.loads(data.decode("utf-8")))
