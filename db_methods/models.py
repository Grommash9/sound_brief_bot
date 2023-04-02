from dataclasses import dataclass


@dataclass
class VoiceFile:
    record_id: int
    chat_id: int
    message_id: int
    short_text: str
    text: str
