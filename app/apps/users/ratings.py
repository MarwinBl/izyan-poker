from django.utils.translation import gettext_lazy as _

MAX_USER_RATING = 2000
USER_RATINGS = {
    0: _('Неизвестный 💩'),
    100: _('Новичок 👶'),
    200: _('Скромняга 🤔'),
    300: _('Голосователь ☑️'),
    400: _('Бывалый 🤸'),
    500: _('Опытный 👍'),
    600: _('Прошаренный 🎸'),
    700: _('Ветеран 🏆'),
    800: _('Гроссмейстер 💎'),
    900: _('Мастер 💣'),
    1000: _('Мастер-джейдай ⭐'),
    1100: _('Мастер-джейдай ⭐'),
    1200: _('Мастер-джейдай ⭐'),
    1300: _('Мега босс 💰'),
    1400: _('Мега босс 💰'),
    1500: _('Мега босс 💰'),
    1600: _('Бесподобный 💯'),
    1700: _('Бесподобный 💯'),
    1800: _('Бесподобный 💯'),
    1900: _('Оракул ☯'),
    MAX_USER_RATING: _('Бог голосований 🥇'),
}
