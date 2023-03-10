import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    START_TXT = """<b>๐๐๐๐ฒ {}, I'm <a href=https://telegram.me/{}>{}</a> 
    
๐๐ ๐๐ฆ ๐๐ฎ๐ญ๐จ๐๐ข๐ฅ๐ญ๐๐ซ ๐๐ง๐ ๐ฆ๐๐ง๐ฎ๐๐ฅ๐ฅ ๐๐ข๐ฅ๐ญ๐๐ซ ๐๐จ๐ญ ๐ฐ๐ข๐ญ๐ก ๐๐ฎ๐ญ๐จ ๐๐๐ฅ๐๐ญ๐ ๐๐๐๐ญ๐ฎ๐ซ๐ ๐๐จ๐ญ๐ก ๐๐ข๐ฅ๐ญ๐๐ซ๐ฌ ๐ญ๐จ ๐๐ฏ๐จ๐ข๐ ๐ฏ๐ข๐จ๐ฅ๐๐ง๐๐๐</b>"""
    HELP_TXT = """๐๐๐๐ฒ {}
๐ท๐ด๐๐ด ๐ธ๐ ๐๐ท๐ด ๐ท๐ด๐ป๐ฟ ๐ต๐พ๐ ๐ผ๐ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐."""
    ABOUT_TXT = """<i><b><u>AutoFilter + UrlShortner Bot</u></b>

๐ Want An </i><i><b>'AutoFilter + UrlShortner Bot'</b> Like Me For Your Group &amp; Earn Money Using It?

๐ฒ </i><i><b>๐๐ฒ ๐๐ซ๐๐๐ญ๐๐ซ ยป</b> </i><i>@Beastonejnanesh</i>"""    
    SOURCE_TXT = """<i><b><u>AutoFilter + UrlShortner Bot</u></b>

๐ Want An </i><i><b>'AutoFilter + UrlShortner Bot'</b> Like Me For Your Group &amp; Earn Money Using It?

๐ฒ </i><i><b>๐๐ฒ ๐๐ซ๐๐๐ญ๐๐ซ ยป</b> </i><i>@Beastonejnanesh</i>"""    
    MANUELFILTER_TXT = """Help: <b>FILTERS ยป</b>

ยป <b>Filter is A Feature Where Users can Set Automated Reply to a Specific Word</b>

<b>Important Notes:</b>
1.<i> I Have To Be Admin </i>
2.<i> Only admins can add Filters in Chat</i>
3.<i> Buttons have a limit of 64 Characters</i>

<b>Commands and Usage:</b>
โข <i> /filter - Add a Filter</i>
โข <i> /filters - List of All Filters</i>
โข <i> /del - Delete a Filter</i>
โข <i> /delall - Delete All Filters</i> """
    BUTTON_TXT = """Help: <b>BUTTONS ยป</b>

ยป Supports both url and alert inline buttons.

<b>NOTE:</b>
1. <i>Telegram will not allows you to send buttons without any content, so content is mandatory.</i>
2. <i>Supports buttons with any telegram media type</i>
3. <i>Buttons should be properly parsed as markdown format</i>

<b>URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/thunderboltfilterbot)</code>

<b>Alert Buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>AUTO FILTER ยป</b>

Add Me In Your Group as Admin & I Will Provide Any Movie, Series, Animation etc.,"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. <i>Only Admins Can Add Connection</i>
2. <i>Send <code>/connect</code> To Connect Me to Your PM</i>

<b>Commands and Usage:</b>
โข<i> /connect  - Connect a Chat to your PM</i>
โข<i> /disconnect  - Disconnect from a Chat</i>
โข<i> /connections - List Of All Connections</i>"""
    EXTRAMOD_TXT = """Help: <b>Extra Features of Me ยป</b>

<b>Commands and Usage:</b>
โข<i> /id - Get ID Of A User</i>
โข<i> /info  - Get Info About a User</i>
โข<i> /imdb  - Get Movie/Series Info from IMDb</i>"""
    ADMIN_TXT = """Help: <b>ADMIN MODS ยป</b>

<b>NOTE:</b>
This Works Only For Admins!

<b>Commands and Usage:</b>
โข<i> /stats - Get Status of DataBase</i>
โข<i> /delete - Delete A File</i>
โข<i> /users - List of My Users </i>
โข<i> /chats - Get List Of My Chats </i>
โข<i> /leave  - Leave from a chat</i>
โข<i> /disable  - Disable a Chat</i>
โข<i> /ban  - Ban a User</i>
โข<i> /unban  - Unban a User</i>
โข<i> /channel - List of All Connected Channels</i>
โข<i> /broadcast - Broadcast a Message to All Users</i>"""
    STATUS_TXT = """โ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: {}
โ ๐๐พ๐๐ฐ๐ป ๐๐๐ด๐๐: {}
โ ๐๐พ๐๐ฐ๐ป ๐ฒ๐ท๐ฐ๐๐: {}
โ ๐๐๐ด๐ณ ๐๐๐พ๐๐ฐ๐ถ๐ด: {} ๐ผ๐๐ฑ
โ ๐ต๐๐ด๐ด ๐๐๐พ๐๐ฐ๐ถ๐ด: {} ๐ผ๐๐ฑ"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
