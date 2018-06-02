from common.database import Database

class Video(object):
    def __init__(self, account, title, link, img):
        self.account = account
        self.title = title
        self.link = link
        self.img = img

    def save_to_db(self):
        Database.insert(collection='videos', data=self.json())

    def json(self):
        return {
            "Account": self.account,
            "Title": self.title,
            "Link": self.link,
            "Img": self.img
        }

    @staticmethod
    def find_video(account):
        user_video = Database.find(collection='videos', query={"Account": account})
        return user_video

    @staticmethod
    def delete_video(account, link):
        Database.remove(collection='videos', query={"Account": account, "Link": link})
