filename = 'student.txt'
import os


def main():
    while True:
        menu()
        choice = int(input('请选择：'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定要退出系统吗？(y/n)：')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用！')
                    break  # 退出循环
                else:
                    continue
            elif choice == 1:
                insert()  # 录入学生信息
            elif choice == 2:
                search()  # 查找学生信息
            elif choice == 3:
                delete()  # 删除学生信息
            elif choice == 4:
                modify()  # 修改学生信息
            elif choice == 5:
                sort()  # 排序
            elif choice == 6:
                total()  # 统计学生总人数
            elif choice == 7:
                show()  # 显示所有学生信息
        else:
            print('你输入的序号有误！')
            continue


def menu():  # 主界面
    print('====================学生信息管理系统=====================')
    print('-----------------------功能菜单-------------------------')
    print('\t\t\t\t\t\t0.退出系统')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('------------------------------------------------------')


def insert():  # 插入学生信息
    student_list = []
    while True:
        id = input('请输入ID(如1001):')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入Python成绩：'))
            java = int(input('请输入Java成绩：'))
        except:
            print('输入无效，不是整数类型，请重新输入！')
            continue
        # 将录入的学上信息保存到字典中
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        # 将字学生信息添加到列表中
        student_list.append(student)
        answer = input('是否继续添加(y/n):')
        if answer == 'y' or answer == 'Y':
            continue  # 继续添加学生信息
        else:
            break  # 退出
    # 调用save()将输入的学生信息保存到文件中
    save(student_list)
    print('学生信息录入完毕！')


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')  # 如果没有就以写入的方式打开 可以新创建
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()  # 最后别忘记关闭


def search():  # 查找学生信息
    student_query = []  # 用于存放学生
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按ID查找请输入1，按姓名查找请输入2：')
            if mode == '1':
                id = input('请输入要查找的学生的ID:')
            elif mode == '2':
                name = input('请输入要查找的学生的姓名：')
            else:
                print('您的输入有误！请重新输入！')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
            # 进行显示查询
            show_student(student_query)
            # 清空列表
            student_query.clear()
            answer = input('是否要继续查询？(y/n)')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break
        else:
            print('暂未保存学生信息！')


def show_student(lst):
    if len(lst) == 0:
        print('没有查询到学生信息！')
        return
    # 定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'  # id name english python java sum
    print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
    # 定义内容的显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english')) + int(item.get('python')) + int(item.get('java'))
                                 ))


def delete():  # 删除学生信息
    while True:
        student_id = input('请输入要删除的学生的id：')
        if student_id != '':
            if os.path.exists(filename):  # 判断文件是否存在
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()  # 读取到student_old列表中存储
            else:
                student_old = []  # 若没读到数据就是一个空列表
            flag = False  # 标记是否删除 # False为还未删除
            if student_old:  # 列表当中有数据的情况
                with open(filename, 'w', encoding='utf-8') as wfile:  # w方式打开不存在会创建 存在会覆盖
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # 将字符串转成字典 eval函数为去掉字符串外边的引号 用dict函数生成字典键不需要加引号 键会自动与其之前的值进行匹配
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print('id为{0}的学生信息已被删除！'.format(student_id))
                    else:
                        print('没有找到id为{0}的学生信息。'.format(student_id))
            else:  # 列表当中没数据的情况
                print('无学生信息！')
                break
            show()  # 删除之后重新显示学生信息
            answer = input('是否继续删除(y/n):')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break


def modify():  # 修改学生信息
    show()
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()  # 把原来的学生信息放到列表当中
    else:
        return  # 文件不存在的情况下直接结束了
    student_id = input('请输入要修改的学生的ID：')
    if student_id != '':
        with open(filename, 'w', encoding='utf-8') as wfile:
            for item in student_old:
                d = dict(eval(item))  # 通过eval函数进行转换
                if d['id'] == student_id:
                    print('找到学生信息可以修改！')
                    while True:
                        try:
                            d['name'] = input('请输入姓名：')
                            d['english'] = int(input('请输入英语成绩：'))
                            d['python'] = int(input('请输入python成绩：'))
                            d['java'] = int(input('请输入Java成绩：'))
                        except:
                            print("您的输入有误，请重新输入！")
                        else:
                            break  # 没有出现问题 会执行到else 然后退出循环
                    wfile.write(str(d) + '\n')
                    print('修改成功！')
                else:  # 要不是你要修改的信息则需要写回去
                    wfile.write(str(d) + '\n')
            answer = input('是否要继续修改其他学生信息(y/n):')
            if answer == 'y' or answer == 'Y':
                modify()  # 调用自身进行重复


def sort():  # 排序学生信息
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list = rfile.readlines()
            # 将字符串转化为字典类型
        student_new = []
        for item in student_list:
            d = dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc = input('请选择排序方式:0表示升序，1表示降序')
    if asc_or_desc == '0':  # 升序
        asc_or_desc_bool = False  # 标记
    elif asc_or_desc == '1':  # 降序
        asc_or_desc_bool = True
    else:
        print('您的输入有误，请重新输入！')
        sort()
    mode = input('请选择排序方式(1按英语成绩排序，2按python成绩排序，3按Java成绩排序，0按照总成绩排序)：')
    if mode == '1':
        student_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)  # False为升序
    elif mode == '2':
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode == '3':
        student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
    elif mode == '0':
        student_new.sort(key=lambda x: int(x['english']) + int(x['python']) + int(x['java']), reverse=asc_or_desc_bool)
    else:
        print("您的输入有误，请重新输入")
        sort()
    show_student(student_new)


def total():  # 统计总人数
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('还没有录入学生信息')
    else:
        print('暂未保存数据信息。。。。')


def show():  # 显示所有学生信息
    student_list = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            for item in students:
                student_list.append(dict(eval(item)))
            if student_list:  # 如果存储学生信息的列表不为空 则打印所有学生信息
                show_student(student_list)
    else:
        print('暂未保存过数据。。。。')


if __name__ == '__main__':  # 只在这个模块中才运行的语句 被别的模块调用了不会执行
    main()
