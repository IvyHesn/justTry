#!/usr/bin/env python
# -*- coding: gbk -*-
from lxml import etree


def create_tree(file_path):
    tree = etree.parse(file_path)
    return tree

tree = create_tree('items.xml')
root = tree.getroot()


def find_nodelist(tree, Xpath):
    '''
    返回的是符合条件的列表
    '''
    root = tree.getroot()
    nodelist = root.findall(Xpath)
    return nodelist


def find_attrib_value(node, name):
    '''使用find_nodelist()后，索引需要的一项，查找指定的属性的值'''
    value = node.attrib[name]
    return value

# nodelist=find_nodelist(tree,'./levels[@id="0"]/level[@id="0"]/createItems/createElement[@elementId="0"]')
nodelist = find_nodelist(tree, './item[@id="1"]/award')
node = nodelist[0]
node.set('step', '5')
value = find_attrib_value(nodelist[0], 'step')
print(value)


def change_attrib_value(node, key, value):
    '''
    修改属性的值
    '''
    node.set(key, value)


def write_xml(tree, out_path):
    '''将xml文件写出
            tree: xml树
            out_path: 写出路径'''
    tree.write(out_path, encoding="utf-8", xml_declaration=True)

#child2= etree.SubElement(root, "child2")
#child3 = etree.SubElement(child2, "child3")

#print (etree.tostring(root,pretty_print=True))


write_xml(tree, 'items2.xml')
