NOTIFICATIONS_DB_PATH = '/var/cache/yunohost/notification/notification.json'


def notification_add(title, message, category):
    pass


def notification_read(notification_id):
    pass


def notification_unread(notification_id):
    pass


def notification_remove(notification_id):
    pass


def notification_list(all=False, unread=False, read=False, limit=10, offset=0):
    pass


def notification_send_batch(since, read=False):
    pass
