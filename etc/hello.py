CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web',
    'args': (
        '--bind=0.0.0.0:8080',
        '--deamon',
        '--workers=16',
        '--timeout=60',
        'hello:app',
    ),
}