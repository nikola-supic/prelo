def download_playlist(user_id, playlist, network, temporary = False):
    for song in playlist:
        download(user_id, song, network, temporary)

def download_single(user_id, song, network, temporary = False):
    download(user_id, song, network, temporary)

def download(user_id, song, network, temporary):
    try:
        file_path, song_size = network.download_song(user_id, song.song_id, song.path, temporary)

    except Exception as e:
        print('=' * 20)
        print('Error while downloading song.')
        print(str(e))
        print()
        print('=' * 20)