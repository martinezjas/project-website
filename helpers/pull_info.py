from helpers.determine_themes import determine_themes
import json


def pull_data(hymn_option, json_data, hymn_number):
    audio_url = None
    if hymn_option == 'instrumental':
        audio_url = 'https://archive.org/download/HimnarioPistas/' + \
            str(hymn_number).zfill(3) + \
            '.mp3'  # json_data['hymn']['mp3UrlInstr']
    else:
        audio_url = 'https://archive.org/download/HimnarioAdventista/' + \
            str(hymn_number).zfill(3) + '.mp3'  # json_data['hymn']['mp3Url']
    title = json_data['hymn']['title']
    number = json_data['hymn']['number']
    icon, bg_url = determine_themes(hymn_number)
    lyrics = json.dumps(json_data['history'])
    print(lyrics)
    return audio_url, title, number, lyrics, bg_url, icon
