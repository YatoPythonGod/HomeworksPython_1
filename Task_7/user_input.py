from easygui import enterbox


def get_data(title_txt, msg_txt):
    data = enterbox(msg=msg_txt, title=title_txt)
    title = title_txt
    msg = msg_txt
    return data if data else get_data(title, msg)