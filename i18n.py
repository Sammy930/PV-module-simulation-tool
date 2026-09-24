import gettext
from pathlib import Path
from config_loader import LANG

#Locate locale directory
script_dir = Path(__file__).resolve().parent
locales = script_dir / "./locales"

#i18n localization
fr_i18n = gettext.translation('simulation_script', locales, fallback=True, languages=[LANG])
fr_i18n.install()
_ = fr_i18n.gettext