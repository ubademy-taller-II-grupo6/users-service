from dao.user_dao import UserDao

if __name__=='__main__':
    dao = UserDao()
    dao.insert_user("test", "test", "test", "test")