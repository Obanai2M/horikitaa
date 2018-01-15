from telegram.ext import BaseFilter

from xenian_bot.utils import data


class DownloadModeFilter(BaseFilter):
    data_set_name = 'download_mode'

    def filter(self, message):
        return self.is_mode_on(message.from_user.username)

    def is_mode_on(self, telegram_user: str):
        """Check if mode is on

        Args:
            telegram_user (:obj:`str`): The telegram users username
        """
        mode_list = data.get(self.data_set_name)
        return mode_list.get(telegram_user, False)

    def turn_on(self, telegram_user: str):
        """Turn download mode on

        Args:
            telegram_user (:obj:`str`): The telegram users username
        """
        mode_dict = data.get(self.data_set_name)
        mode_dict[telegram_user] = True
        data.save(self.data_set_name, mode_dict)

    def turn_off(self, telegram_user: str):
        """Turn download mode off

        Args:
            telegram_user (:obj:`str`): The telegram users username
        """
        mode_dict = data.get(self.data_set_name)
        mode_dict[telegram_user] = False
        data.save(self.data_set_name, mode_dict)

    def toggle_mode(self, telegram_user: str):
        """Toggle download mode

        Args:
            telegram_user (:obj:`str`): The telegram users username

        Returns:
                (:obj:`bool`): True if the mode is now on False if off
        """
        if self.is_mode_on(telegram_user):
            self.turn_off(telegram_user)
            return False
        self.turn_on(telegram_user)
        return True


download_mode_filter = DownloadModeFilter()