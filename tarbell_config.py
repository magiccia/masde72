# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""

# Google spreadsheet key
SPREADSHEET_KEY = "1HEyueJ3M7IyDPOj-HZdNhsgHDqrQEqCr87Hmq30XX_Y"

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt"]

# Spreadsheet cache lifetime in seconds. (Default: 4)
# SPREADSHEET_CACHE_TTL = 4

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# Get context from a local file or URL. This file can be a CSV or Excel
# spreadsheet file. Relative, absolute, and remote (http/https) paths can be 
# used.
# CONTEXT_SOURCE_FILE = ""

# EXPERIMENTAL: Path to a credentials file to authenticate with Google Drive.
# This is useful for for automated deployment. This option may be replaced by
# command line flag or environment variable. Take care not to commit or publish
# your credentials file.
# CREDENTIALS_PATH = ""

# S3 bucket configuration
S3_BUCKETS = {
    'staging': 'masde72.recoveredfactory.net',
    'production': 'masde72.recoveredfactory.net',
}

# Default template variables
DEFAULT_CONTEXT = {
    'name': 'masde72',
    'title': 'Mas de 72',
    'la_matanza_versions': [
        (u'Oficial', 'oficial', '_textos/cap1-a-oficial.md'),
        (u'Embajada EUA', 'eua', '_textos/cap1-a-eua.md'),
        (u'Tesis', 'tesis', '_textos/cap1-a-tesis.md'),
        (u'CNDH', 'cndh', '_textos/cap1-a-cndh.md'),
    ],
    'los_sobrevivientes_versions': [
        (u'Oficial', 'oficial', '_textos/cap1-b-oficial.md'),
        (u'Embajada EUA', 'eua', '_textos/cap1-b-eua.md'),
        (u'Tesis', 'tesis', '_textos/cap1-b-tesis.md'),
        (u'CNDH', 'cndh', '_textos/cap1-b-cndh.md'),
        (u'Moore', 'moore', '_textos/cap1-b-moore.md'),
        (u'El Faro', 'faro', '_textos/cap1-b-faro.md'),
        (u'Freddy Lala', 'lala', '_textos/cap1-b-lala.md'),
    ],
    'el_hallazgo_versions': [
        (u'Oficial', 'oficial', '_textos/cap1-c-oficial.md'),
        (u'Tesis', 'tesis', '_textos/cap1-c-tesis.md'),
        (u'Insight Crime', 'incrime', '_textos/cap1-c-incrime.md'),
    ],
    'la_hipotesis_versions': [
        (u'Averiguación Previa', 'previa', '_textos/cap1-d-previa.md'),
        (u'Embajada EUA', 'eua', '_textos/cap1-d-eua.md'),        
        (u'Moore', 'moore', '_textos/cap1-d-moore.md'),
        (u'El Faro', 'oficial', '_textos/cap1-d-faro.md'),
        (u'Insight Crime', 'incrime', '_textos/cap1-d-incrime.md'),
    ],


}
