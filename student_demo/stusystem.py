#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 22:37
# @Author  : zengxt
# @File    : stusystem.py

import os

# 保存学生信息的文件名
filename = 'student.dat'

def main():
    while True:
        menum()
        try:
            num = int(input('请选择：'))
            if num in [0, 1, 2, 3, 4, 5, 6, 7]:
                if num == 0:
                    answer = input('您确定要退出系统吗？ y/n：')
                    if answer == 'y' or answer == 'Y' or answer == 'yes' or answer == 'YES':
                        print('谢谢您的使用！！！')
                        break
                elif num == 1:
                    insert()
                elif num == 2:
                    search()
                elif num == 3:
                    delete()
                elif num == 4:
                    modify()
                elif num == 5:
                    sort()
                elif num == 6:
                    total()
                elif num == 7:
                    show()
        except ValueError:
            print('请选择有效的菜单！')


def menum():
    print('学生信息管理系统')
    print('---功能菜单---')
    print('1，录入学生信息')
    print('2，查找学生信息')
    print('3，删除学生信息')
    print('4，修改学生信息')
    print('5，排序')
    print('6，统计学生总共人数')
    print('7，显示所有学生信息')
    print('0，退出')


def insert():
    student_list = []
    while True:
        id = input('请输入学生ID（如1001）：')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break

        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入python成绩：'))
            java = int(input('请输入java成绩：'))
        except:
            print('输入的信息不是整数类型，请重新输入！')
            continue
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        student_list.append(student)
        answer = input('是否继续添加 y/n？：')
        if answer == 'n' or answer == 'N' or answer == 'no' or answer == 'NO':
            break

    save(student_list)
    print('学生信息录入完成！')


def save(student_list):
    try:
        file = open(filename, 'a', encoding='utf-8')
    except:
        file = open(filename, 'w', encoding='utf-8')

    for item in student_list:
        file.write(str(item) + '\n')
    file.close()


def search():
    if not os.path.exists(filename):
        print('暂无学生记录！！')
        return

    while True:
        mode = input('1：按ID查找，2：按姓名查找：')
        if mode == '1':
            student_id = input('请输入要查找的学生的ID：')
            search_query = search_by_id(student_id)
        elif mode == '2':
            student_name = input('请输入要查找的学生的姓名：')
            search_query = search_by_name(student_name)
        else:
            print('选择有误，请重新输入')
            continue
        show_search_query(search_query)

        answer = input('是否继续查找 y/n？：')
        if answer == 'n' or answer == 'N' or answer == 'no' or answer == 'NO':
            break


def show_search_query(search_query):
    if len(search_query) == 0:
        print('没有找到学生记录!!!')
        return

    format_data = '{:^8}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_data.format('学生ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
    for item in search_query:
        print(format_data.format(item['id'], item['name'], item['english'], item['python'], item['java'],
                                 int(item['english']) + int(item['python']) + int(item['java'])))


def search_by_id(student_id):
    search_query = []
    with open(filename, 'r',  encoding='utf-8') as file:
        student_list = file.readlines()
        for stu in student_list:
            stu = dict(eval(stu))
            if stu['id'] == student_id:
                search_query.append(stu)
    return search_query


def search_by_name(student_name):
    search_query = []
    with open(filename, 'r',  encoding='utf-8') as file:
        student_list = file.readlines()
        for stu in student_list:
            stu = dict(eval(stu))
            if stu['name'] == student_name:
                search_query.append(stu)
    return search_query


def delete():
    while True:
        student_id = input('请输入要删除的学生的ID：')
        if not student_id:
            break

        if os.path.exists(filename):
            with open(filename, 'r',  encoding='utf-8') as file:
                student_list = file.readlines()
        else:
            student_list = []

        if student_list:
            flag = False
            with open(filename, 'w', encoding='utf-8') as file:
                for stu in student_list:
                    # eval() 函数用来执行一个字符串表达式，并返回表达式的值。
                    stu = dict(eval(stu))
                    if stu['id'] != student_id:
                        file.write(str(stu) + '\n')
                    else:
                        flag = True

                if flag:
                    print(f'ID为{student_id}的学生已删除。')
                else:
                    print(f'没有找到ID为{student_id}的学生。')
        else:
            print('没有学生记录！')
            break

        print('==============================')
        show()
        answer = input('是否继续删除 y/n？：')
        if answer == 'n' or answer == 'N' or answer == 'no' or answer == 'NO':
            break


def modify():
    if not os.path.exists(filename):
        print('暂无学生记录！！')
        return

    with open(filename, 'r',  encoding='utf-8') as file:
        student_list = file.readlines()

    student_id = input('请输入要修改的学生的ID：')
    with open(filename, 'w',  encoding='utf-8') as file:
        flag = False
        for stu in student_list:
            stu = dict(eval(stu))
            if stu['id'] == student_id:
                print(f'找到了ID为{student_id}的学生，可以修改')
                while True:
                    try:
                        stu['name'] = input('请输入新的学生姓名：')
                        stu['english'] = int(input('请输入新的英语成绩：'))
                        stu['python'] = int(input('请输入新的python成绩：'))
                        stu['java'] = int(input('请输入新的java成绩：'))
                    except:
                        print('您的输入有误，请输入正确的值！')
                    else:
                        break
                flag = True
                print('修改成功！！')
            file.write(str(stu) + '\n')
        if not flag:
            print(f'没有找到ID为{student_id}的学生！！')

    show()
    answer = input('是否继续修改 y/n？：')
    if answer == 'y' or answer == 'Y' or answer == 'yes' or answer == 'YES':
        modify()


def sort():
    if not os.path.exists(filename):
        print('暂无学生记录！！')
        return

    student_list = []
    with open(filename, 'r',  encoding='utf-8') as file:
        for stu in file.readlines():
            student_list.append(dict(eval(stu)))

    asc_or_desc = input('请选择(0,升序 1,降序)：')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('选择有误，请重新输入！！')
        sort()

    mode = input('请选择排序方式（1，按英语成绩；2，按python成绩；3，按java成绩；4，按总成绩）：')
    if mode == '1':
        student_list.sort(key=lambda stu_list: int(stu_list['english']), reverse=asc_or_desc_bool)
    elif mode == '2':
        student_list.sort(key=lambda stu_list: int(stu_list['python']), reverse=asc_or_desc_bool)
    elif mode == '3':
        student_list.sort(key=lambda stu_list: int(stu_list['java']), reverse=asc_or_desc_bool)
    elif mode == '4':
        student_list.sort(key=lambda stu_list: int(stu_list['english']) + int(stu_list['python']) + int(stu_list['java']), reverse=asc_or_desc_bool)
    else:
        print('选择有误，请重新输入！！')
        sort()
    show_search_query(student_list)


def total():
    if not os.path.exists(filename):
        print('暂无学生记录！！')
        return

    with open(filename, 'r',  encoding='utf-8') as file:
        student_list = file.readlines()
        if student_list:
            print(f'一共有{len(student_list)}名学生信息！')
        else:
            print('暂未录入学生信息！')


def show():
    if os.path.exists(filename):
        print('学号\t姓名\t英语成绩\tpython成绩\tjava成绩')
        with open(filename, 'r', encoding='utf-8') as file:
            for item in file.readlines():
                item = dict(eval(item))
                print(item['id'] + '\t' + item['name'] + '\t' + str(item['english']) + '\t\t' + str(item['python']) + '\t\t\t' + str(item['java']))
    else:
        print('暂无学生信息！')


if __name__ == '__main__':
    main()
