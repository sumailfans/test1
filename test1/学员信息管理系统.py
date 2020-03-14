def print_info():
    '''显示输入提示界面'''
    print('_' * 20)
    print('欢迎登陆学员管理系统')
    print('1:添加学员')
    print('2:删除学员')
    print('3:修改学员信息')
    print('4:查询学员信息')
    print('5:显示所有学员信息')
    print('6:退出系统')
    print('_' * 20)

def add_info():
    '''添加学员'''
    #接受用户输入学员信息
    new_id = input('请输入学号：')
    new_name = input('请输入姓名：')
    new_tel = input('请输入手机号：')
    #声明info是全局变量
    global info
    #检测用户输入的姓名是否存在，存在则报错提示
    for i in info:
        if new_name == i['name']:
            print('该用户已经存在！')
            return
    #如果用户输入的姓名不存在，则添加该学员信息
    info_dict = {}
    #将用户输入的数据追加到字典
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel
    #将这个学员信息数据追加到列表
    info.append(info_dict)

    print(info)


def del_info():
    '''删除学员'''
    while True:
        del_id = int(input('请输入要删除的学员学号：'))
        global info
        #检查学员是否存在
        #如果存在则删除列表指定的下标的数据
        if 0 <= del_id <= len(info):
            del_flag = input('确定要删除吗？ yes or no')
            if del_flag == 'yes':
                del info[del_id]
                print(info)
                #删除了目标学员的信息后退出循环
                break
            else:
                print('输入学员有误，请重新输入：')




def modify_info():
    '''修改学员信息'''
    while True:
        # 用户输入要修改的学员信息
        modify_num = int(input('请输入要修改的学员学号：'))
        global info
        #检查这个学员是否存在，存在则打印学员信息，并按用户输入修改
        if 0 <= modify_num < len(info):
            print(f'该学员学号是{info[modify_num]["id"]},姓名是{info[modify_num]["name"]}'
                  f'手机号是{info[modify_num]["tel"]}')
            info[modify_num]["id"] = input('请输入学号：')
            info[modify_num]["name"] = input('请输入姓名：')
            info[modify_num]["tel"] = input('请输入手机号：')
            print(info)
            break
        else:
            print('输入学员有误，请重新输入：')


def search_info():
    '''查询学员信息'''
    search_name = input('请输入要查找的学员姓名：')
    global info
    for i in info:
        if search_name == i['name']:
            print('*** 查询结果如下 ***')
            print(f'该学员学号是{i["id"]},姓名是{i["name"]},手机号是{i["tel"]}')
            break
        else:
            print('查无此人.....')


def print_all():
    '''显示所有学员信息'''
    print('学号\t姓名\t手机号')
    global info
    for i in info:
        print(f'{i["id"]}\t{i["name"]}\t{i["tel"]}')



info = []
while True:
    print_info()
    user_num = input('输入功能序号：')
    if user_num == '1':
        print('添加学员')
        add_info()
    elif user_num == '2':
        print('删除学员')
        del_info()
    elif user_num == '3':
        print('修改学员信息')
        modify_info()
    elif user_num == '4':
        print('查询学员信息')
        search_info()
    elif user_num == '5':
        print('显示所有学员信息')
        print_all()
    elif user_num == '6':
        print('退出系统')
        break
    else:
        print('输入错误，请重新输入！！！')