import json
import logging
import os
import sys

from game.attack import AttackCache


class VillageManager:
    @staticmethod
    def farm_manager(verbose=False, clean_reports=False):
        logger = logging.getLogger("Mened\u017cer farmy")
        config = {}
        try:
            with open("config.json", "r") as f:
                config = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            try:
                with open("config.example.json", "r") as f:
                    config = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                config = {}

        if verbose:
            logger.info("Wsie: %d", len(config.get("villages", {})))
        attacks = AttackCache.cache_grab()

        if verbose:
            logger.info("Farmy: %d", len(attacks))

        # Report scanning is disabled. No report cache is consulted.
        return


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, format="%(asctime)s - %(levelname)s - %(message)s")
    VillageManager.farm_manager(verbose=True)
