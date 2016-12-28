import logging

LOG_FILENAME = 'niza.log'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    format='%(asctime)s %(name)-2s; %(levelname)-2s; %(message)s',
                    datefmt='%Y-%m-%d; %H:%M;',
                    )

logging.error('This message should go to the log file')

f = open(LOG_FILENAME, 'rt')
try:
    body = f.read()
finally:
    f.close()

print('FILE:')
print(body)