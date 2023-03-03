from helpers.determine_themes import determine_themes
import json


def pull_data(hymn_option, json_data, hymn_number):
    audio_url = None
    if hymn_option == 'instrumental':
        audio_url = json_data['hymn']['mp3UrlInstr']
    else:
        audio_url = json_data['hymn']['mp3Url']
    title = json_data['hymn']['title']
    number = json_data['hymn']['number']
    supertheme, subtheme = determine_themes(hymn_number)
    lyrics = json.dumps(json_data['history'])
    return audio_url, title, number, supertheme, subtheme, lyrics
