import database as db

def download_playlist(user_id, playlist, network):
    for song_id in playlist:
        download(user_id, song_id[0], network)

def download_single(user_id, song_id, network):
    download(user_id, song_id, network)

def download(user_id, song_id, network):
    try:
        song = db.Song(song_id)
        file_path, song_size = network.download_song(user_id, song.song_id, song.path)

    except Exception as e:
        print(str(e))
        print('Error')