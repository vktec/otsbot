from enum import Enum

class DiscordPerm(Enum):
    CREATE_INSTANT_INVITE = "create_instant_invite"
    KICK_MEMBERS = "kick_members"
    BAN_MEMBERS = "ban_members"
    ADMINISTRATOR = "administrator"
    MANAGE_CHANNELS = "manage_channels"
    MANAGE_SERVER = "manage_server"
    ADD_REACTIONS = "add_reactions"
    VIEW_AUDIT_LOGS = "view_audit_logs"
    READ_MESSAGES = "read_messages"
    SEND_MESSAGES = "send_messages"
    SEND_TTS_MESSAGES = "send_tts_messages"
    MANAGE_MESSAGES = "manage_messages"
    EMBED_LINKS = "embed_links"
    ATTACH_FILES = "attach_files"
    READ_MESSAGE_HISTORY = "read_message_history"
    MENTION_EVERYONE = "mention_everyone"
    EXTERNAL_EMOJIS = "external_emojis"
    CONNECT = "connect"
    SPEAK = "speak"
    MUTE_MEMBERS = "mute_members"
    DEAFEN_MEMBERS = "deafen_members"
    MOVE_MEMBERS = "move_members"
    USE_VOICE_ACTIVATION = "use_voice_activation"
    CHANGE_NICKNAME = "change_nickname"
    MANAGE_NICKNAMES = "manage_nicknames"
    MANAGE_ROLES = "manage_roles"
    MANAGE_WEBHOOKS = "manage_webhooks"
    MANAGE_EMOJIS = "manage_emojis"
