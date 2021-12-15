from typing import List


Lang = {
    "🔎Определить👅": "auto",
    "🇷🇺Русский🇷🇺": "ru",
    "🇬🇧Английский🇬🇧": "en",
    "🇩🇪Немецкий🇩🇪": "de",
    "🇪🇸Испанский🇪🇸": "es",
    "🇮🇹Итальянский🇮🇹": "it",
    "🇫🇷Французский🇫🇷": "fr",
    "🇵🇹Португальский🇵🇹": "pt",
    "🇯🇵Японский🇯🇵": "ja",
    "🇨🇳Китайский🇨🇳": "zh-tw",
    "🇦🇪Арабский🇦🇪": "ar",
    "🇹🇷Турецкий🇹🇷": "tr",
}
listLangKeys = list(Lang.keys())


def get_key(_dict, value):
    for k, v in _dict.items():
        if v == value:
            return k