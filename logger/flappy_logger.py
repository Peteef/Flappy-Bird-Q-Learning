import logging
import datetime
from shutil import copy2


class FlappyLogger:
    def __init__(self):
        self.date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.baseLogPath = 'var/log/game.log'
        self.historyLogPath = 'var/log/game_history/' + str(self.date) + '_game.log'

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.clear_logfile()
        handler = logging.FileHandler(self.baseLogPath)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def game_start(self):
        self.logger.info('[Game starting]')

    def game_stop(self):
        self.logger.info('Game stopping')

    def turn_start(self, turn):
        self.logger.info('Starting turn ' + str(turn))

    def log_result(self, turn, score):
        self.logger.info('Finished turn ' + str(turn) + ' with score: ' + str(score))
        copy2(self.baseLogPath, self.historyLogPath)

    def clear_logfile(self):
        open('var/log/game.log', 'w').close()


