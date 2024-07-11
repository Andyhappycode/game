# 定义图书信息字典，key为书籍ID，value为书籍信息字典
books = {1:上海寻宝记,2:北京寻宝记,3:天津寻宝记,4:重庆寻宝记,5:山东寻宝记,6:四川寻宝记,7:湖北寻宝记,8:浙江寻宝记,9:甘肃寻宝记,10:陕西寻宝记,11:江西寻宝记,12:江苏寻宝记,13:云南寻宝记,14:河南寻宝记,15:安徽寻宝记,16:湖南寻宝记,17:广东寻宝记,18:辽宁寻宝记,19香港寻宝记,20:贵州寻宝记,21:青海寻宝记,22:澳门寻宝记,23:广西寻宝记,24福建寻宝记,25:河北寻宝记,26:新疆寻宝记,27:海南寻宝记,28黑龙江寻宝记,29:秦朝寻宝记

}

#\
def borrow_book(user, book_id):
    """用户借书函数"""
    if book_id in books and books[book_id]['available']:
        books[book_id]['available'] = False
        borrow_records.setdefault(user, []).append({'book_id': book_id, 'borrow_date': get_current_date()})
        return f"{user} 成功借阅了《{books[book_id]['title']}》。"
    else:
        return "这本书不可借阅或不存在。"

def return_book(user, book_id):
    """用户还书函数"""
    if any(record['book_id'] == book_id for record in borrow_records.get(user, [])):
        books[book_id]['available'] = True
        borrow_records[user] = [record for record in borrow_records[user] if record['book_id'] != book_id]
        return f"{user} 成功归还了《{books[book_id]['title']}》。"
    else:
        return "这本书没有被该用户借阅，无法归还。"

# 示例操作
print(borrow_book(3))
print(return_book(2))