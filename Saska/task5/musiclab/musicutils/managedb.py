import datetime
from .models import User, Album, Track, UserPlaylist


def insert_data():
    data = {
        'user': {
            1: (1, 'Alex', 'Shirko', 12),
            2: (2, 'Semen', 'Mahalin', 5),
            3: (3, 'Ivan', 'Pozdnyakov', 4),
            4: (4, 'Kirill', 'Kuzmin', 1),
            5: (5, 'Ilya', 'Molchanov', 4)
        },
        'album': {
            0: (1, 'Single', 'Single', datetime.date(2016, 1, 1)),
            1: (2, 'Elevation', 'alternative metal', datetime.date(2016, 1, 1)),
            3: (3, 'Monuments', 'alternative metal', datetime.date(2016, 10, 11)),
            4: (4, 'Ephemeral', 'alternative metal', datetime.date(2019, 1, 1))
        },
        'track': {
            1: (1, 2, 'Delusion', 'We Are The Catalyst', f'{datetime.time(0, 3, 50)}'),
            2: (2, 2, 'Open Door', 'We Are The Catalyst', f'{datetime.time(0, 3, 34)}'),
            3: (3, 2, 'One More Day', 'We Are The Catalyst', f'{datetime.time(0, 3, 28)}'),
            4: (4, 2, 'Askja', 'We Are The Catalyst', f'{datetime.time(0, 4, 2)}'),
            5: (5, 3, 'Our Way to the Sun', 'We Are The Catalyst', f'{datetime.time(0, 4, 3)}'),
            6: (6, 3, 'Not Alone', 'We Are The Catalyst', f'{datetime.time(0, 5, 8)}'),
            7: (7, 3, 'Don’t You Worry Child', 'We Are The Catalyst', f'{datetime.time(0, 4, 27)}'),
            8: (8, 4, 'The Code', 'We Are The Catalyst', f'{datetime.time(0, 3, 9)}'),
            9: (9, 4, 'In Shadows', 'We Are The Catalyst', f'{datetime.time(0, 3, 30)}'),
            10: (10, 4, 'Dust', 'We Are The Catalyst', f'{datetime.time(0, 3, 48)}'),
            11: (11, 1, 'Losing My Mind', 'We Are The Catalyst', f'{datetime.time(0, 3, 15)}'),
            12: (12, 1, 'Blinding Lights', 'We Are The Catalyst', f'{datetime.time(0, 3, 17)}')
        },
        'user_playlist': {
            1: (1, 1, 1),
            2: (2, 1, 2),
            3: (3, 1, 3),
            4: (4, 1, 4),
            5: (5, 1, 5),
            7: (6, 1, 6),
            8: (7, 1, 7),
            9: (8, 1, 8),
            10: (9, 1, 9),
            11: (10, 1, 10),
            12: (11, 1, 11),
            13: (12, 1, 12),
            14: (13, 2, 11),
            15: (14, 2, 1),
            16: (15, 2, 3),
            17: (16, 2, 5),
            18: (17, 2, 7),
            19: (18, 3, 9),
            20: (19, 3, 11),
            21: (20, 3, 1),
            22: (21, 3, 2),
            23: (22, 4, 3),
            24: (23, 5, 5),
            25: (24, 5, 6),
            26: (25, 5, 12),
            27: (26, 5, 4),
        }
    }

    try:
        for du in data['user'].values():
            user = User(id=du[0], first_name=du[1], last_name=du[2], playlist_size=du[3])
            user.save()

        for da in data['album'].values():
            album = Album(id=da[0], title=da[1], description=da[2], pab_date=da[3])
            album.save()

        for dt in data['track'].values():
            track = Track(id=dt[0], title=dt[2], singer=dt[3], duration=dt[4], album=Album.objects.get(pk=dt[1]))
            track.save()

        for dup in data['user_playlist'].values():
            user_playlist = UserPlaylist(id=dup[0], user=User.objects.get(pk=dup[1]), track=Track.objects.get(pk=dup[2]))
            user_playlist.save()
    except ValueError:
        print('Pizdec')
        clear_db()


def select_all_from(model):
    return model.objects.all().values()


def clear_db():
    User.objects.all().delete()
    Album.objects.all().delete()
    Track.objects.all().delete()
    UserPlaylist.objects.all().delete()


def add_record(model, params):
    record = model(*params)
    record.save()


def delete_record(model, row_id):
    record = model.objects.get(pk=row_id)
    record.delete()